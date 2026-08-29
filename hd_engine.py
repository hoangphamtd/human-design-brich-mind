# -*- coding: utf-8 -*-
# Human Design B-RICH MIND
# Copyright (C) 2026 B-RICH MIND
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
#
# This program uses the Swiss Ephemeris library, Copyright (C) 1997-2021
# Astrodienst AG, Switzerland, under the AGPL option of its dual license.
"""hd_engine.py — Chart engine Human Design cho B-RICH MIND.

Vào:  ngày · giờ địa phương · múi giờ · toạ độ nơi sinh
Ra:   26 kích hoạt · kênh · trung tâm · Type · Authority · Profile ·
      Definition · Incarnation Cross · 4 mũi tên Variable

Nguyên tắc (HD-01):
  - luôn floor(), không bao giờ round()
  - Design = 88°00' cung mặt trời TRƯỚC lúc sinh, giải bằng lặp — không phải 88 ngày
  - "motor nối Cổ họng" = liên thông ĐỒ THỊ, không phải kênh trực tiếp
  - neo bánh xe: cổng 41 tại 302.0°, hoàng đạo nhiệt đới

Ephemeris: Moshier (dựng sẵn trong pyswisseph, không cần file dữ liệu ngoài,
không vướng ràng buộc giấy phép Swiss Ephemeris).
"""

from __future__ import annotations
from collections import deque
from dataclasses import dataclass, asdict, field
from datetime import datetime
from zoneinfo import ZoneInfo
import json
import swisseph as swe

# ─────────────────────────── hằng số ───────────────────────────

START_DEG = 302.0                 # cổng 41 bắt đầu tại 2°00' Bảo Bình
GATE_ARC = 360.0 / 64             # 5.625°
LINE_ARC = GATE_ARC / 6           # 0.9375°
COLOR_ARC = LINE_ARC / 6
TONE_ARC = COLOR_ARC / 6
BASE_ARC = TONE_ARC / 5
DESIGN_ARC = 88.0                 # cung mặt trời
EPS = 1e-9

WHEEL = [41, 19, 13, 49, 30, 55, 37, 63, 22, 36, 25, 17, 21, 51, 42, 3,
         27, 24, 2, 23, 8, 20, 16, 35, 45, 12, 15, 52, 39, 53, 62, 56,
         31, 33, 7, 4, 29, 59, 40, 64, 47, 6, 46, 18, 48, 57, 32, 50,
         28, 44, 1, 43, 14, 34, 9, 5, 26, 11, 10, 58, 38, 54, 61, 60]

FLAGS = swe.FLG_MOSEPH | swe.FLG_SPEED

# True Node là chuẩn Human Design. Đây là một trong hai điểm còn treo ở Giai đoạn 0.
NODE_MODE = "true"       # "true" | "mean"

BODIES = [
    ("sun", swe.SUN), ("earth", None), ("north_node", None), ("south_node", None),
    ("moon", swe.MOON), ("mercury", swe.MERCURY), ("venus", swe.VENUS),
    ("mars", swe.MARS), ("jupiter", swe.JUPITER), ("saturn", swe.SATURN),
    ("uranus", swe.URANUS), ("neptune", swe.NEPTUNE), ("pluto", swe.PLUTO),
]

CENTER_GATES = {
    "head": [61, 63, 64],
    "ajna": [47, 24, 4, 11, 43, 17],
    "throat": [62, 23, 56, 35, 12, 45, 33, 8, 31, 20, 16],
    "g": [1, 13, 25, 46, 2, 15, 10, 7],
    "heart": [21, 40, 26, 51],
    "spleen": [48, 57, 44, 50, 32, 28, 18],
    "solar_plexus": [36, 22, 37, 6, 49, 55, 30],
    "sacral": [5, 14, 29, 59, 9, 3, 42, 27, 34],
    "root": [53, 60, 52, 19, 39, 41, 58, 38, 54],
}
GATE_CENTER = {g: c for c, gs in CENTER_GATES.items() for g in gs}
MOTORS = {"heart", "root", "solar_plexus", "sacral"}

CHANNELS = [
    (1, 8), (2, 14), (3, 60), (4, 63), (5, 15), (6, 59), (7, 31), (9, 52),
    (10, 20), (10, 34), (10, 57), (11, 56), (12, 22), (13, 33), (16, 48),
    (17, 62), (18, 58), (19, 49), (20, 34), (20, 57), (21, 45), (23, 43),
    (24, 61), (25, 51), (26, 44), (27, 50), (28, 38), (29, 46), (30, 41),
    (32, 54), (34, 57), (35, 36), (37, 40), (39, 55), (42, 53), (47, 64),
]

PROFILE_ANGLE = {
    "1/3": "Right Angle", "1/4": "Right Angle", "2/4": "Right Angle",
    "2/5": "Right Angle", "3/5": "Right Angle", "3/6": "Right Angle",
    "4/6": "Right Angle", "4/1": "Juxtaposition",
    "5/1": "Left Angle", "5/2": "Left Angle",
    "6/2": "Left Angle", "6/3": "Left Angle",
}

DEFINITION_NAME = {0: "Không định nghĩa", 1: "Định nghĩa đơn", 2: "Định nghĩa tách đôi",
                   3: "Tách ba", 4: "Tách bốn"}


# ─────────────────── bánh xe: độ → cổng/hào/màu/tông/nền ───────────────────

def wheel_position(lon: float) -> dict:
    """Đổi kinh độ hoàng đạo sang cổng, hào, màu, tông, nền. Chỉ dùng floor()."""
    off = (lon - START_DEG) % 360.0
    idx = int(off / GATE_ARC + EPS)
    idx = min(idx, 63)
    rem = off - idx * GATE_ARC

    line = int(rem / LINE_ARC + EPS) + 1
    r2 = rem - (line - 1) * LINE_ARC
    color = int(r2 / COLOR_ARC + EPS) + 1
    r3 = r2 - (color - 1) * COLOR_ARC
    tone = int(r3 / TONE_ARC + EPS) + 1
    r4 = r3 - (tone - 1) * TONE_ARC
    base = int(r4 / BASE_ARC + EPS) + 1

    return {"gate": WHEEL[idx], "line": min(line, 6), "color": min(color, 6),
            "tone": min(tone, 6), "base": min(base, 5), "lon": lon}


# ───────────────────── múi giờ hai miền (HD-09) ─────────────────────
# Việt Nam dùng HAI múi giờ khác nhau từ 1/1/1960 đến 13/6/1975.
#   Miền Nam: UTC+8 (sắc lệnh 362-TTP ngày 30/12/1959)
#   Miền Bắc: UTC+7 (giờ pháp định, QĐ 121/QĐ-CP ngày 8/8/1967)
# tzdata Asia/Ho_Chi_Minh CHỈ ghi lịch sử miền Nam — dùng cho người sinh
# miền Bắc giai đoạn này sẽ lệch đúng 1 giờ → lệch hào → sai Profile.
TZ_NAM = "Asia/Ho_Chi_Minh"
TZ_BAC = "Asia/Bangkok"          # luôn UTC+7 từ 1920, khớp giờ pháp định miền Bắc
MOC_THONG_NHAT = (1975, 6, 14)   # từ ngày này cả nước cùng UTC+7
MOC_RO_RANG = (1955, 1, 1)       # trước mốc này lịch sử hai miền chưa thống nhất


def vung_theo_mien(mien: str, nam: int, thang: int, ngay: int) -> str:
    """Chọn vùng múi giờ theo miền sinh. mien: 'bac' | 'nam'."""
    if mien not in ("bac", "nam"):
        raise ValueError(f"mien phải là 'bac' hoặc 'nam', không phải {mien!r}")
    if (nam, thang, ngay) >= MOC_THONG_NHAT:
        return TZ_NAM                     # sau thống nhất, hai miền như nhau
    return TZ_BAC if mien == "bac" else TZ_NAM


# ─────────────────────────── thời gian ───────────────────────────

def gio_khong_ton_tai(dt_local: datetime) -> datetime | None:
    """Giờ khách khai có thật sự tồn tại trên đồng hồ không?

    Đêm nhảy giờ mùa hè, đồng hồ nhảy thẳng qua một khoảng — ví dụ Pháp
    25/3/1990 nhảy từ 02:00 lên 03:00, nên 02:00–02:59 CHƯA TỪNG CÓ.
    Trả về giờ đã dịch lên nếu giờ khai không tồn tại, ngược lại trả None.

    Cách nhận biết: đổi sang UTC rồi đổi ngược lại. Giờ có thật thì về đúng
    chỗ cũ; giờ không có thật thì rơi sang một giờ khác.
    """
    if dt_local.tzinfo is None:
        return None
    quay_ve = dt_local.astimezone(ZoneInfo("UTC")).astimezone(dt_local.tzinfo)
    return quay_ve if quay_ve != dt_local else None


def to_julian(dt_local: datetime, tz_name: str) -> float:
    """Giờ địa phương + tên múi giờ → Julian Day (UT).

    tzdata xử lý mốc Việt Nam đổi UTC+8 → UTC+7 ngày 13/6/1975.
    """
    if dt_local.tzinfo is None:
        dt_local = dt_local.replace(tzinfo=ZoneInfo(tz_name))
    u = dt_local.astimezone(ZoneInfo("UTC"))
    hour = u.hour + u.minute / 60 + u.second / 3600
    return swe.julday(u.year, u.month, u.day, hour, swe.GREG_CAL)


# ─────────────────────────── ephemeris ───────────────────────────

def _calc(jd: float, planet: int) -> tuple[float, float]:
    """Trả về (kinh độ, tốc độ độ/ngày)."""
    res, _ = swe.calc_ut(jd, planet, FLAGS)
    return res[0] % 360.0, res[3]


def sun_lon(jd: float) -> float:
    return _calc(jd, swe.SUN)[0]


def design_jd(jd_birth: float) -> float:
    """Thời điểm Mặt Trời ở đúng 88°00' cung TRƯỚC vị trí lúc sinh.

    Giải bằng Newton. KHÔNG phải 'lùi 88 ngày'.
    """
    target = (sun_lon(jd_birth) - DESIGN_ARC) % 360.0
    jd = jd_birth - 88.0
    for _ in range(60):
        lon, speed = _calc(jd, swe.SUN)
        delta = (lon - target + 180.0) % 360.0 - 180.0
        if abs(delta) < 1e-10:
            break
        jd -= delta / (speed if abs(speed) > 1e-9 else 1.0)
    return jd


def activations(jd: float) -> dict:
    """13 thiên thể tại một thời điểm. Trái Đất = Mặt Trời + 180°, Nút Nam = Nút Bắc + 180°."""
    node_pl = swe.TRUE_NODE if NODE_MODE == "true" else swe.MEAN_NODE
    s = sun_lon(jd)
    n = _calc(jd, node_pl)[0]
    out = {"sun": s, "earth": (s + 180.0) % 360.0,
           "north_node": n, "south_node": (n + 180.0) % 360.0}
    for name, pl in BODIES:
        if pl is not None and name != "sun":
            out[name] = _calc(jd, pl)[0]
    return {k: wheel_position(v) for k, v in out.items()}


# ─────────────────────── suy luận BodyGraph ───────────────────────

def defined_channels(gates: set[int]) -> list[tuple[int, int]]:
    return [c for c in CHANNELS if c[0] in gates and c[1] in gates]


def defined_centers(chans: list[tuple[int, int]]) -> set[str]:
    out = set()
    for a, b in chans:
        out.add(GATE_CENTER[a])
        out.add(GATE_CENTER[b])
    return out


def center_graph(chans: list[tuple[int, int]]) -> dict[str, set[str]]:
    g: dict[str, set[str]] = {}
    for a, b in chans:
        ca, cb = GATE_CENTER[a], GATE_CENTER[b]
        if ca == cb:
            continue
        g.setdefault(ca, set()).add(cb)
        g.setdefault(cb, set()).add(ca)
    return g


def connected_to(graph: dict[str, set[str]], start: str, target: str) -> bool:
    """Liên thông đồ thị (BFS) — KHÔNG phải kênh trực tiếp. Đây là chỗ hay code sai nhất."""
    if start not in graph:
        return False
    seen, q = {start}, deque([start])
    while q:
        cur = q.popleft()
        if cur == target:
            return True
        for nxt in graph.get(cur, ()):
            if nxt not in seen:
                seen.add(nxt)
                q.append(nxt)
    return False


def components(graph: dict[str, set[str]], nodes: set[str]) -> int:
    seen, n = set(), 0
    for node in nodes:
        if node in seen:
            continue
        n += 1
        q = deque([node])
        seen.add(node)
        while q:
            cur = q.popleft()
            for nxt in graph.get(cur, ()):
                if nxt not in seen:
                    seen.add(nxt)
                    q.append(nxt)
    return n


def motor_to_throat(graph: dict[str, set[str]], centers: set[str]) -> bool:
    if "throat" not in centers:
        return False
    return any(m in centers and connected_to(graph, m, "throat") for m in MOTORS)


def energy_type(centers: set[str], graph: dict[str, set[str]]) -> str:
    if not centers:
        return "reflector"
    if "sacral" in centers:
        return "manifesting_generator" if motor_to_throat(graph, centers) else "generator"
    return "manifestor" if motor_to_throat(graph, centers) else "projector"


def authority(centers: set[str], graph: dict[str, set[str]]) -> str:
    """Dừng ở mục đầu tiên khớp — thứ tự ưu tiên là bắt buộc."""
    if "solar_plexus" in centers:
        return "emotional"
    if "sacral" in centers:
        return "sacral"
    if "spleen" in centers:
        return "splenic"
    if "heart" in centers:
        return "ego"
    if "g" in centers and connected_to(graph, "g", "throat"):
        return "self_projected"
    if not centers:
        return "lunar"
    return "mental_projected"


def variables(p: dict, d: dict) -> dict:
    """4 mũi tên. Tông 1–3 → trái, tông 4–6 → phải."""
    def arrow(t):
        return "trái" if t <= 3 else "phải"
    return {
        "determination": {"nguon": "Tông MT/TĐ Thiết kế", "tone": d["sun"]["tone"],
                          "huong": arrow(d["sun"]["tone"]), "nghia": "Tiêu hoá"},
        "environment": {"nguon": "Tông Nút Thiết kế", "tone": d["north_node"]["tone"],
                        "huong": arrow(d["north_node"]["tone"]), "nghia": "Môi trường"},
        "perspective": {"nguon": "Tông MT/TĐ Cá tính", "tone": p["sun"]["tone"],
                        "huong": arrow(p["sun"]["tone"]), "nghia": "Góc nhìn"},
        "motivation": {"nguon": "Tông Nút Cá tính", "tone": p["north_node"]["tone"],
                       "huong": arrow(p["north_node"]["tone"]), "nghia": "Động lực"},
    }


# ─────────────────────────── API chính ───────────────────────────

def build_chart(nam, thang, ngay, gio, phut, tz="Asia/Ho_Chi_Minh",
                lat=10.8231, lon=106.6297, noi_sinh="TP. Hồ Chí Minh, Việt Nam",
                gio_chac_chan=True, mien=None) -> dict:
    # mien chỉ áp dụng cho người sinh tại Việt Nam
    if mien:
        tz = vung_theo_mien(mien, nam, thang, ngay)
    dt = datetime(nam, thang, ngay, gio, phut, tzinfo=ZoneInfo(tz))

    # Giờ khách khai có thể không tồn tại (đêm nhảy giờ). Dịch lên như bản đồ
    # chuẩn làm, và báo cho khách biết — bản đồ không đổi vì cùng một thời
    # điểm UTC, nhưng in ra giờ chưa từng có trên đồng hồ thì sai.
    gio_da_dich = gio_khong_ton_tai(dt)
    if gio_da_dich is not None:
        gio_khai = dt.strftime("%H:%M")
        dt = gio_da_dich

    jd_p = to_julian(dt, tz)
    jd_d = design_jd(jd_p)

    P = activations(jd_p)
    D = activations(jd_d)

    gates = {v["gate"] for v in P.values()} | {v["gate"] for v in D.values()}
    chans = defined_channels(gates)
    centers = defined_centers(chans)
    graph = center_graph(chans)

    profile = f"{P['sun']['line']}/{D['sun']['line']}"
    y, m, d_, h = swe.revjul(jd_d, swe.GREG_CAL)

    canh_bao = []
    if gio_da_dich is not None:
        canh_bao.append(
            f"Giờ {gio_khai} ngày {ngay:02d}/{thang:02d}/{nam} KHÔNG TỒN TẠI tại nơi này "
            f"— đêm đó đồng hồ nhảy giờ mùa hè, bỏ qua cả khoảng ấy. Hệ thống đã dịch "
            f"lên {dt.strftime('%H:%M')} theo đúng cách bản đồ chuẩn xử lý. Bản đồ không "
            f"đổi, nhưng nên hỏi lại khách giờ sinh cho chắc.")
    if not gio_chac_chan:
        canh_bao.append("Giờ sinh chưa chắc chắn → Profile và Authority có thể lệch. "
                        "Cần bản đối chiếu theo khoảng giờ trước khi luận.")
    truoc_thong_nhat = (nam, thang, ngay) < MOC_THONG_NHAT
    if truoc_thong_nhat and tz in (TZ_NAM, TZ_BAC):
        if mien == "bac":
            canh_bao.append("Sinh MIỀN BẮC trước 14/6/1975 → đã dùng UTC+7 theo giờ pháp định "
                            "miền Bắc, không dùng UTC+8 của miền Nam. Nếu khách thực ra sinh "
                            "miền Nam thì phải dựng lại, kết quả sẽ khác.")
        elif mien == "nam":
            canh_bao.append("Sinh MIỀN NAM trước 14/6/1975 → đã dùng lịch sử múi giờ miền Nam. "
                            "Nếu khách thực ra sinh miền Bắc thì phải dựng lại, kết quả sẽ khác.")
        else:
            canh_bao.append("Sinh trước 14/6/1975 mà CHƯA CHỌN MIỀN. Hai miền khi đó lệch nhau "
                            "1 giờ → có thể lệch hào và sai Profile. Cần hỏi khách sinh miền nào.")
    if (nam, thang, ngay) < MOC_RO_RANG:
        canh_bao.append("Sinh trước 1955 — giai đoạn múi giờ hai miền chưa thống nhất, các nguồn "
                        "không khớp hoàn toàn. Nên dựng cả hai phương án miền để đối chiếu.")
    canh_bao.append(f"Nút Bắc đang dùng chế độ {NODE_MODE.upper()} NODE — điểm còn treo, chưa đối chiếu nguồn ngoài.")

    return {
        "dau_vao": {"ngay_sinh": dt.strftime("%d/%m/%Y %H:%M"),
                    "gio_khai_ban_dau": gio_khai if gio_da_dich is not None else None, "mui_gio": tz,
                    "utc_offset": str(dt.utcoffset()), "noi_sinh": noi_sinh, "mien": mien,
                    "lat": lat, "lon": lon, "gio_chac_chan": gio_chac_chan},
        "thoi_diem": {"jd_ca_tinh": jd_p, "jd_thiet_ke": jd_d,
                      "thiet_ke_utc": f"{int(d_):02d}/{int(m):02d}/{int(y)} "
                                      f"{int(h):02d}:{int((h % 1) * 60):02d}",
                      "so_ngay_lui": round(jd_p - jd_d, 4)},
        "ca_tinh": P, "thiet_ke": D,
        "cong_hoat_hoa": sorted(gates),
        "kenh": [f"{a}-{b}" for a, b in chans],
        "trung_tam_dinh_nghia": sorted(centers),
        "trung_tam_mo": sorted(set(CENTER_GATES) - centers),
        "type": energy_type(centers, graph),
        "authority": authority(centers, graph),
        "profile": profile,
        "definition": DEFINITION_NAME[components(graph, centers)],
        "incarnation_cross": {
            "cong": [P["sun"]["gate"], P["earth"]["gate"],
                     D["sun"]["gate"], D["earth"]["gate"]],
            "goc": PROFILE_ANGLE[profile],
        },
        "variables": variables(P, D),
        "canh_bao": canh_bao,
    }


if __name__ == "__main__":
    import sys
    c = build_chart(1985, 3, 15, 7, 30)
    print(json.dumps(c, ensure_ascii=False, indent=2, default=str))
