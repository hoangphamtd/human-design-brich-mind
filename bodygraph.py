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
"""bodygraph.py — Vẽ BodyGraph dạng SVG từ kết quả chart engine.

Mỗi cổng có một điểm neo cố định trên viền trung tâm, đúng như bản đồ chuẩn.
Kênh là đường thẳng nối hai điểm neo, nên các kênh song song không chồng nhau.

Quy ước màu chuẩn Human Design:
    đen  = cổng đến từ Cá tính (ý thức)
    đỏ   = cổng đến từ Thiết kế (vô thức)
    kênh có cổng đen một đầu, đỏ đầu kia → mỗi nửa một màu
Trung tâm định nghĩa: tô đầy. Trung tâm mở: viền mảnh, để trống.
Cổng treo (hoạt hoá nhưng kênh chưa đủ): nửa đường — thấy ngay còn thiếu cổng nào.
"""
from __future__ import annotations

from functools import lru_cache

LE = 20                 # lề bốn phía quanh hình
INK, SON, VIEN, NEN = "#221E1B", "#C0392B", "#C9CBC0", "#F0F1EA"

# Màu 9 trung tâm là QUY ƯỚC NGÀNH, không phải gu thẩm mỹ.
# Người học Human Design nhìn màu là biết ngay trung tâm nào.
MAU_TT = {
    "head":         "#F2C230",   # vàng
    "ajna":         "#5CB85C",   # xanh lá
    "throat":       "#A9825C",   # nâu
    "g":            "#C7C13A",   # vàng ô liu
    "heart":        "#C1502E",   # đỏ cam
    "spleen":       "#A9825C",   # nâu
    "solar_plexus": "#A9825C",   # nâu
    "sacral":       "#C1502E",   # đỏ cam
    "root":         "#A9825C",   # nâu
}
XANH_CONG = "#1F5FA8"            # nền số cổng đang tạo kênh

POS = {
    "head": (270, 60), "ajna": (270, 143), "throat": (270, 260),
    "g": (270, 379), "heart": (350, 397),
    "spleen": (136, 493), "solar_plexus": (404, 493),
    "sacral": (270, 508), "root": (270, 623),
}
SHAPES = {
    "head": ("tri_up", 93), "ajna": ("tri_down", 93), "throat": ("square", 89),
    "g": ("diamond", 97), "heart": ("tri_left", 60),
    "spleen": ("tri_right", 85), "solar_plexus": ("tri_left", 85),
    "sacral": ("square", 89), "root": ("square", 89),
}

# Điểm neo của từng cổng: (dx, dy) so với tâm trung tâm chứa nó.
ANCHOR = {
    # Đầu — cạnh đáy tam giác, trái→phải
    64: (-27, 29), 61: (0, 29), 63: (27, 29),
    # Ajna — cạnh trên (lên Đầu) và vùng đỉnh dưới (xuống Cổ họng)
    47: (-29, -31), 24: (0, -31), 4: (29, -31),
    17: (-18, 21), 43: (0, 29), 11: (18, 21),
    # Cổ họng — trên lên Ajna · dưới xuống G/Sacral · phải sang Tim & Đám rối · trái sang Lá lách
    62: (-25, -44), 23: (0, -44), 56: (25, -44),
    16: (-44, 16), 20: (-29, 44), 31: (-11, 44), 8: (7, 44), 33: (26, 44),
    # Cạnh phải, trên→dưới: 35 · 12 · 45. Ba kênh này KHÁC BÁN KÍNH cung:
    # 45 vào Tim nằm phía trong, 35 và 12 vòng ra ngoài tới Đám rối. Xếp
    # theo độ cao của đích (45 lên trên) thì 45 phải cắt qua hai cung bên
    # dưới nó — đo được 9 chỗ cắt thay vì 7.
    35: (44, -20), 12: (44, 2), 45: (44, 23),
    # Trung tâm G — tám hướng quanh hình thoi
    1: (0, -48), 13: (25, -25), 25: (48, 0), 46: (25, 25),
    2: (0, 48), 15: (-25, 25), 10: (-48, 0), 7: (-25, -25),
    # Tim — tam giác nhỏ bên phải, đỉnh trỏ về G
    21: (14, -25), 51: (-30, 0), 26: (2, 25), 40: (20, 16),
    # Lá lách — tam giác bên trái, đỉnh trỏ vào trong
    48: (27, -33), 57: (34, -11), 44: (33, 7), 50: (29, 25),
    32: (2, 31), 28: (-14, 27), 18: (-25, 21),
    # Đám rối mặt trời — tam giác bên phải, đỉnh trỏ vào trong
    36: (-29, -33), 22: (-34, -14), 37: (-33, 6), 6: (-29, 25), 49: (-2, 31), 55: (14, 27), 30: (25, 21),
    # Xương cùng
    34: (-37, -44), 5: (-20, -44), 14: (0, -44), 29: (20, -44), 59: (37, -44),
    9: (-29, 44), 3: (-10, 44), 42: (10, 44), 27: (29, 44),
    # Gốc — cạnh trên 52·60·53 thẳng lên Xương cùng (9·3·42);
    # 54 ra cạnh TRÁI (sang Lá lách), 19 ra cạnh PHẢI (sang Đám rối)
    52: (-29, -44), 60: (-10, -44), 53: (10, -44),
    54: (-44, -37), 38: (-44, -20), 58: (-44, 7),
    19: (44, -37), 39: (44, -20), 41: (44, 7),
}
CENTER_GATES = {
    "head": [61, 63, 64], "ajna": [47, 24, 4, 11, 43, 17],
    "throat": [62, 23, 56, 35, 12, 45, 33, 8, 31, 20, 16],
    "g": [1, 13, 25, 46, 2, 15, 10, 7], "heart": [21, 40, 26, 51],
    "spleen": [48, 57, 44, 50, 32, 28, 18],
    "solar_plexus": [36, 22, 37, 6, 49, 55, 30],
    "sacral": [5, 14, 29, 59, 9, 3, 42, 27, 34],
    "root": [53, 60, 52, 19, 39, 41, 58, 38, 54],
}
GATE_CENTER = {g: c for c, gs in CENTER_GATES.items() for g in gs}

CHANNELS = [
    (1, 8), (2, 14), (3, 60), (4, 63), (5, 15), (6, 59), (7, 31), (9, 52),
    (10, 20), (10, 34), (10, 57), (11, 56), (12, 22), (13, 33), (16, 48),
    (17, 62), (18, 58), (19, 49), (20, 34), (20, 57), (21, 45), (23, 43),
    (24, 61), (25, 51), (26, 44), (27, 50), (28, 38), (29, 46), (30, 41),
    (32, 54), (34, 57), (35, 36), (37, 40), (39, 55), (42, 53), (47, 64),
]


def _dinh(center: str) -> list[tuple[float, float]]:
    """Toạ độ các đỉnh của hình trung tâm, tính từ tâm."""
    kind, sz = SHAPES[center]
    h = sz / 2
    if kind == "square":
        return [(-h, -h), (h, -h), (h, h), (-h, h)]
    if kind == "diamond":
        return [(0, -h), (h, 0), (0, h), (-h, 0)]
    if kind == "tri_up":
        return [(0, -h), (h * 0.92, h * 0.62), (-h * 0.92, h * 0.62)]
    if kind == "tri_down":
        return [(0, h), (h * 0.92, -h * 0.62), (-h * 0.92, -h * 0.62)]
    if kind == "tri_left":
        return [(-h * 0.86, 0), (h * 0.62, -h * 0.92), (h * 0.62, h * 0.92)]
    if kind == "tri_right":
        return [(h * 0.86, 0), (-h * 0.62, -h * 0.92), (-h * 0.62, h * 0.92)]
    raise ValueError(kind)


def _chieu_len_bien(center: str, dx: float, dy: float) -> tuple[float, float]:
    """Kéo điểm neo về đúng CẠNH của hình.

    Neo khai bằng tay dễ rơi ra ngoài hình tam giác — khi đó đường kênh bắt đầu
    ở khoảng trống, nhìn như mối nối không dính vào đâu. Hàm này chiếu điểm về
    cạnh gần nhất nên mọi neo luôn nằm trên viền.
    """
    P = _dinh(center)
    tot, best = None, 1e9
    for i in range(len(P)):
        ax, ay = P[i]
        bx, by = P[(i + 1) % len(P)]
        ux, uy = bx - ax, by - ay
        L2 = ux * ux + uy * uy or 1.0
        t = max(0.0, min(1.0, ((dx - ax) * ux + (dy - ay) * uy) / L2))
        px, py = ax + ux * t, ay + uy * t
        d = (px - dx) ** 2 + (py - dy) ** 2
        if d < best:
            best, tot = d, (px, py)
    return tot


def gate_xy(g: int, lun: float = 0.0) -> tuple[float, float]:
    """Toạ độ neo cổng. lun > 0 kéo điểm THỤT VÀO trong trung tâm,
    để đầu đường nằm dưới hình, không bị hở ra một khe trắng."""
    c = GATE_CENTER[g]
    cx, cy = POS[c]
    dx, dy = _chieu_len_bien(c, *ANCHOR[g])
    if lun:
        L = (dx * dx + dy * dy) ** 0.5 or 1.0
        dx -= dx / L * lun
        dy -= dy / L * lun
    return cx + dx, cy + dy


def shape_path(center: str) -> str:
    kind, s = SHAPES[center]
    x, y = POS[center]
    h = s / 2
    if kind == "square":
        return f'<rect x="{x-h}" y="{y-h}" width="{s}" height="{s}" rx="2"'
    if kind == "diamond":
        return f'<polygon points="{x},{y-h} {x+h},{y} {x},{y+h} {x-h},{y}"'
    if kind == "tri_up":
        return f'<polygon points="{x},{y-h} {x+h*0.92},{y+h*0.62} {x-h*0.92},{y+h*0.62}"'
    if kind == "tri_down":
        return f'<polygon points="{x},{y+h} {x+h*0.92},{y-h*0.62} {x-h*0.92},{y-h*0.62}"'
    if kind == "tri_left":
        return f'<polygon points="{x-h*0.86},{y} {x+h*0.62},{y-h*0.92} {x+h*0.62},{y+h*0.92}"'
    if kind == "tri_right":
        return f'<polygon points="{x+h*0.86},{y} {x-h*0.62},{y-h*0.92} {x-h*0.62},{y+h*0.92}"'
    raise ValueError(kind)


TRUC = 270.0                      # trục dọc của cơ thể (POS["g"][0])

# Làn của từng kênh trong bó chạy vòng ngoài. 0 = trong cùng.
# Kênh nối hai trung tâm KỀ NHAU để 0 — nó đi thẳng, không cần vòng.
LAN = {
# Chỉ kênh có CẢ HAI đầu nằm xa tâm mới đi theo vòng đồng tâm. Kênh có một
# đầu sát tâm (10-57 từ G, 34-57 từ Xương cùng) mà ép lên vòng ngoài thì phải
# quặt ra rất xa rồi vòng ngược lại — đúng chỗ rối bên trái. Bản đồ chuẩn vẽ
# hai kênh ấy gần như thẳng, nên để làn 0.
# Bó trên và bó dưới dùng CHUNG thang bán kính, nhờ vậy cung trên nối tiếp
# cung dưới thành một vòng liền như app.
    # trái · Cổ họng → Lá lách
    (20, 57): 4, (16, 48): 5,
    # trái · Lá lách ↔ Gốc
    (32, 54): 3, (28, 38): 4, (18, 58): 5,
    # phải · Cổ họng → Đám rối
    (12, 22): 4, (35, 36): 5,
    # phải · Gốc ↔ Đám rối
    (19, 49): 3, (39, 55): 4, (30, 41): 5,
    # Băng ngang vùng giữa — KHÔNG thuộc hệ vòng đồng tâm (tâm nằm ngay
    # trong khe G↔Xương cùng, vòng tròn qua đó sẽ cắt cả hai).
    #   -1 = uốn ôm SÁT bụng dưới hình thoi G
    #    0 = đi thẳng, chỉ lách khi bị chắn
    (26, 44): -1, (20, 34): 0, (10, 57): 0, (34, 57): 0,
    # hai trung tâm kề nhau — đi thẳng
    (27, 50): 0, (37, 40): 0, (6, 59): 0,
    (21, 45): 0, (25, 51): 0,
    (13, 33): 0, (7, 31): 0, (1, 8): 0, (10, 20): 0,
    (29, 46): 0, (5, 15): 0, (2, 14): 0, (10, 34): 0,
    (9, 52): 0, (3, 60): 0, (42, 53): 0,
    (11, 56): 0, (17, 62): 0, (23, 43): 0,
    (4, 63): 0, (24, 61): 0, (47, 64): 0,
}
# Vòng cung của bản đồ chuẩn là những cung ĐỒNG TÂM: cùng một tâm, chỉ khác
# bán kính. Vì cùng tâm nên chúng song song thật và không thể cắt nhau. Trước
# đây mỗi dây cung được đẩy phình một lượng riêng — mỗi đường một tâm khác
# nhau, nên nhìn thế nào cũng lệch.
BK_DAU = 112.0     # bán kính vòng trong cùng (làn 1)
ONG = 20.0         # khoảng cách giữa hai vòng
BUOC = 3.0         # bước nới bán kính khi vòng bị vướng trung tâm
PHINH_MAX = 220.0


def _tam() -> tuple[float, float]:
    """Tâm chung của mọi vòng cung: giữa Trung tâm G và Xương cùng."""
    return TRUC, (POS["g"][1] + POS["sacral"][1]) / 2


def _ban_kinh(lan: int) -> float:
    return BK_DAU + (lan - 1) * ONG


def _lan(a: int, b: int) -> int:
    return LAN.get((a, b), LAN.get((b, a), 0))


def _sau_trong(c: str, px: float, py: float) -> float:
    """Điểm nằm sâu bao nhiêu trong hình trung tâm c. Số âm nghĩa là ở ngoài."""
    cx, cy = POS[c]
    P = [(cx + dx, cy + dy) for dx, dy in _dinh(c)]
    n = len(P)
    gx = sum(q[0] for q in P) / n
    gy = sum(q[1] for q in P) / n
    sau = 1e9
    for i in range(n):
        ax, ay = P[i]
        bx, by = P[(i + 1) % n]
        ux, uy = bx - ax, by - ay
        L = (ux * ux + uy * uy) ** 0.5 or 1.0
        d = (ux * (py - ay) - uy * (px - ax)) / L
        if (ux * (gy - ay) - uy * (gx - ax)) / L < 0:
            d = -d
        sau = min(sau, d)
    return sau


def _tt_tai(px: float, py: float) -> str:
    """Điểm neo này thuộc trung tâm nào."""
    return max(POS, key=lambda c: _sau_trong(c, px, py))


def _bez(P, t: float) -> tuple[float, float]:
    s = 1 - t
    return (s*s*s*P[0][0] + 3*s*s*t*P[1][0] + 3*s*t*t*P[2][0] + t*t*t*P[3][0],
            s*s*s*P[0][1] + 3*s*s*t*P[1][1] + 3*s*t*t*P[2][1] + t*t*t*P[3][1])


def _diem(x1, y1, x2, y2, ox, oy) -> list[tuple[float, float]]:
    """Bốn điểm điều khiển: hai tay nắm đẩy vuông góc khỏi dây cung."""
    ax, ay = x1 + (x2 - x1) * 0.32, y1 + (y2 - y1) * 0.32
    bx, by = x1 + (x2 - x1) * 0.68, y1 + (y2 - y1) * 0.68
    return [(x1, y1), (ax + ox, ay + oy), (bx + ox, by + oy), (x2, y2)]


def _vuong(P, tru, lui: float = -1.0) -> bool:
    """True khi đường KHÔNG chạm ruột trung tâm nào ngoài hai đầu của nó.
    lui âm = còn chừa một vành đai an toàn quanh mỗi hình."""
    for i in range(1, 120):
        x, y = _bez(P, i / 120)
        for c in tru:
            if _sau_trong(c, x, y) > lui:
                return False
    return True


@lru_cache(maxsize=None)
def _cong(x1, y1, x2, y2, lan):
    """Độ phình của một kênh, đo theo pháp tuyến của dây cung.

    · làn 0 — hai trung tâm kề nhau: đi THẲNG. Chỉ phình khi bị một trung tâm
      thứ ba chắn ngang (trung tâm được vẽ đè lên đường, đường xuyên qua sẽ bị
      cắt thành mảnh mồ côi trông như đoạn lơ lửng).
    · làn ≥ 1 — kênh đi vòng: điểm giữa của kênh được đặt lên đúng VÒNG TRÒN
      bán kính của làn, tâm chung ở giữa G và Xương cùng. Mọi kênh cùng làn
      nằm trên cùng một vòng, nên các vòng cung song song thật.
    """
    ux, uy = x2 - x1, y2 - y1
    L = (ux * ux + uy * uy) ** 0.5 or 1.0
    ux, uy = ux / L, uy / L
    nx, ny = -uy, ux
    dau, cuoi = _tt_tai(x1, y1), _tt_tai(x2, y2)
    tru = [c for c in POS if c not in (dau, cuoi)]

    cx, cy = _tam()
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    dx, dy = mx - cx, my - cy
    if nx * dx + ny * dy < 0:            # pháp tuyến luôn chỉ RA XA tâm
        nx, ny = -nx, -ny
    dn = dx * nx + dy * ny
    dd = dx * dx + dy * dy

    if lan < 0:
        # Ôm sát vật cản phía TRONG: quay pháp tuyến về phía tâm rồi đẩy đến
        # mức xa nhất còn chưa chạm hình nào. Kênh 26-44 nhờ vậy cong ôm sát
        # bụng dưới hình thoi G thay vì kẻ thẳng ngang qua vùng giữa.
        nx, ny = -nx, -ny
        tot, k = None, 0
        while k * BUOC <= PHINH_MAX:
            h = k * BUOC
            if _vuong(_diem(x1, y1, x2, y2, nx * h, ny * h), tru):
                tot = h
            elif tot is not None:
                break
            k += 1
        return (tot if tot is not None else 0.0), nx, ny

    if lan == 0:
        k = 0
        while k * BUOC <= PHINH_MAX:
            h = k * BUOC
            for s in ((1,) if h == 0 else (1, -1)):
                if _vuong(_diem(x1, y1, x2, y2, s * nx * h, s * ny * h), tru):
                    return h, s * nx, s * ny
            k += 1
        return 0.0, nx, ny

    # Điểm giữa Bezier nằm cách dây cung 0.75·h. Cần nó ở đúng bán kính R:
    #     |d + 0.75·h·n| = R   →   0.5625h² + 1.5(d·n)h + (|d|² − R²) = 0
    R0 = _ban_kinh(lan)
    k = 0
    while R0 + k * BUOC <= PHINH_MAX:
        R = R0 + k * BUOC
        det = dn * dn - dd + R * R
        if det >= 0.0:
            h = (4.0 / 3.0) * (-dn + det ** 0.5)
            if h >= 0.0 and _vuong(_diem(x1, y1, x2, y2, nx * h, ny * h), tru):
                return h, nx, ny
        k += 1
    return 0.0, nx, ny


def _ctrl(x1, y1, x2, y2, lan=0) -> list[tuple[float, float]]:
    h, nx, ny = _cong(round(x1, 1), round(y1, 1), round(x2, 1), round(y2, 1), lan)
    return _diem(x1, y1, x2, y2, nx * h, ny * h)


def _phinh(x1, y1, x2, y2, lan) -> float:
    """Độ đẩy ra ngoài, đo theo pháp tuyến của dây cung."""
    return _cong(round(x1, 1), round(y1, 1), round(x2, 1), round(y2, 1), lan)[0]


def _d(x1, y1, x2, y2, lan=0) -> str:
    P = _ctrl(x1, y1, x2, y2, lan)
    return (f"M{P[0][0]:.1f},{P[0][1]:.1f} C{P[1][0]:.1f},{P[1][1]:.1f} "
            f"{P[2][0]:.1f},{P[2][1]:.1f} {P[3][0]:.1f},{P[3][1]:.1f}")


def _nua(x1, y1, x2, y2, lan=0) -> tuple[float, float]:
    """Điểm t=0.5 của đường — chỗ chia hai màu."""
    return _bez(_ctrl(x1, y1, x2, y2, lan), 0.5)


def _mot_phan(x1, y1, x2, y2, lan, dau: bool, ti: float = 0.5) -> str:
    """Cắt lấy phần đầu (dau=True) hoặc phần cuối (dau=False) theo tỉ lệ ti.

    de Casteljau cắt từ đầu nào thì giữ nguyên đầu ấy, nên nửa đường LUÔN
    bắt đầu đúng tại điểm neo của cổng mà nó mang màu.
    """
    P = _ctrl(x1, y1, x2, y2, lan)
    if not dau:
        P = P[::-1]
    t = ti
    lerp = lambda a, b: (a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t)
    a1, b1, c1 = lerp(P[0], P[1]), lerp(P[1], P[2]), lerp(P[2], P[3])
    d1, e1 = lerp(a1, b1), lerp(b1, c1)
    f1 = lerp(d1, e1)
    return (f"M{P[0][0]:.1f},{P[0][1]:.1f} C{a1[0]:.1f},{a1[1]:.1f} "
            f"{d1[0]:.1f},{d1[1]:.1f} {f1[0]:.1f},{f1[1]:.1f}")


def _nua_path(x1, y1, x2, y2, lan, dau: bool) -> str:
    """Nửa đường, giữ nguyên hình cong."""
    return _mot_phan(x1, y1, x2, y2, lan, dau, 0.5)


def _ve(p: str, color, w=4.4):
    if color == "both":
        return (f'<path d="{p}" fill="none" stroke="{INK}" stroke-width="{w}"/>'
                f'<path d="{p}" fill="none" stroke="{SON}" stroke-width="{w}" '
                f'stroke-dasharray="5 5"/>')
    return (f'<path d="{p}" fill="none" stroke="{color}" stroke-width="{w}" '
            f'stroke-linecap="round"/>')


KY_HIEU = {"sun": "\u2609", "earth": "\u2295", "north_node": "\u260A",
           "south_node": "\u260B", "moon": "\u263D", "mercury": "\u263F",
           "venus": "\u2640", "mars": "\u2642", "jupiter": "\u2643",
           "saturn": "\u2644", "uranus": "\u2645", "neptune": "\u2646",
           "pluto": "\u2647"}
THU_TU = ["sun", "earth", "north_node", "south_node", "moon", "mercury", "venus",
          "mars", "jupiter", "saturn", "uranus", "neptune", "pluto"]


def bang_kich_hoat(chart: dict) -> str:
    """Bảng 26 kích hoạt — Thiết kế (đỏ) bên trái, Cá tính (đen) bên phải,
    ký hiệu hành tinh ở giữa, đúng kiểu bản đồ chuẩn."""
    hang = []
    for k in THU_TU:
        d, p = chart["thiet_ke"][k], chart["ca_tinh"][k]
        hang.append(
            f'<tr><td class="tk">{d["gate"]}.{d["line"]}</td>'
            f'<td class="kh">{KY_HIEU[k]}</td>'
            f'<td class="ct">{p["gate"]}.{p["line"]}</td></tr>')
    return ('<table class="bangkh"><thead><tr>'
            '<th class="tk">Thiết kế</th><th></th><th class="ct">Cá tính</th>'
            '</tr></thead><tbody>' + "".join(hang) + "</tbody></table>")


def css_bang() -> str:
    return """
.bangkh{border-collapse:collapse;background:#EFE3C8;border:1px solid #C4A97B;
  border-radius:8px;overflow:hidden;font-family:"JetBrains Mono",monospace;font-size:.82rem}
.bangkh th{font-size:9px;letter-spacing:.12em;text-transform:uppercase;
  padding:7px 12px 5px;font-weight:500;border-bottom:1px solid #D6BE95}
.bangkh td{padding:2.5px 12px;line-height:1.35}
.bangkh .tk{color:#C0392B;text-align:right}
.bangkh .ct{color:#1A1A1A;text-align:left}
.bangkh .kh{font-size:1rem;text-align:center;color:#4A4238;padding:0 4px}
"""


def _do_khung() -> tuple[float, float, float, float]:
    """Đo hộp bao của TOÀN BỘ nét vẽ: 36 đường kênh (kể cả độ phình),
    chín hình trung tâm, và vòng tròn số cổng. Nhờ vậy khung ảnh ôm sát
    hình — không còn dải trống hai bên, và chóp Đầu không bị cắt."""
    xs, ys = [], []
    for a, b in CHANNELS:
        P = _ctrl(*gate_xy(a, 4), *gate_xy(b, 4), _lan(a, b))
        for i in range(41):
            x, y = _bez(P, i / 40)
            xs.append(x); ys.append(y)
    for c in POS:
        cx, cy = POS[c]
        for dx, dy in _dinh(c):
            xs.append(cx + dx); ys.append(cy + dy)
    for g in GATE_CENTER:
        x, y = gate_xy(g)
        xs.append(x); ys.append(y)
    r = 8.0                       # nửa bề rộng nét + vòng tròn số cổng
    return min(xs) - r, min(ys) - r, max(xs) + r, max(ys) + r


_x0, _y0, _x1, _y1 = _do_khung()
W = round(_x1 - _x0 + 2 * LE)
H = round(_y1 - _y0 + 2 * LE)
DOI_X = LE - _x0
DOI_Y = LE - _y0


def render(chart: dict, size: int = 400) -> str:
    p = {v["gate"] for v in chart["ca_tinh"].values()}
    d = {v["gate"] for v in chart["thiet_ke"].values()}
    active = p | d
    defined = set(chart["trung_tam_dinh_nghia"])

    def mau(g):
        return "both" if (g in p and g in d) else (INK if g in p else SON)

    out = [f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" '
           f'width="{size}" role="img" aria-label="BodyGraph">',
           '<defs><linearGradient id="troi" x1="0" y1="0" x2="0" y2="1">'
           '<stop offset="0%" stop-color="#BBD8E8"/>'
           '<stop offset="55%" stop-color="#DCE9EC"/>'
           '<stop offset="100%" stop-color="#EFE6D2"/></linearGradient></defs>',
           f'<rect width="{W}" height="{H}" fill="url(#troi)"/>',
           f'<g transform="translate({DOI_X:.1f},{DOI_Y:.1f})">',
           '<defs><style>.c-def{fill:#221E1B}.c-open{fill:#F0F1EA;stroke:#B9BCB0;stroke-width:1.5}'
           '.gn{font:400 8.5px "JetBrains Mono",monospace;fill:#8C8578}'
           '.gn-on{font:500 8.5px "JetBrains Mono",monospace;fill:#221E1B}</style></defs>']

    # 1. khung 36 kênh, rất nhạt
    for a, b in CHANNELS:
        x1, y1 = gate_xy(a, 4); x2, y2 = gate_xy(b, 4)
        out.append(f'<path d="{_d(x1, y1, x2, y2, _lan(a, b))}" fill="none" '
                   f'stroke="{VIEN}" stroke-width="2" opacity=".55"/>')

    # 2. cổng treo — nửa đường
    for a, b in CHANNELS:
        ha, hb = a in active, b in active
        if ha == hb:
            continue
        g = a if ha else b
        xa, ya = gate_xy(a, 4); xb, yb = gate_xy(b, 4)
        out.append(_ve(_mot_phan(xa, ya, xb, yb, _lan(a, b), g == a, 0.30),
                       mau(g), 4.0))

    # 3. kênh định nghĩa — mỗi nửa mang màu cổng đầu đó
    for a, b in CHANNELS:
        if a not in active or b not in active:
            continue
        x1, y1 = gate_xy(a, 4); x2, y2 = gate_xy(b, 4)
        lan = _lan(a, b)
        out.append(_ve(_mot_phan(x1, y1, x2, y2, lan, True), mau(a)))
        out.append(_ve(_mot_phan(x1, y1, x2, y2, lan, False), mau(b)))

    # 4. chín trung tâm vẽ đè lên đường — màu theo quy ước ngành
    for c in POS:
        if c in defined:
            out.append(f'{shape_path(c)} fill="{MAU_TT[c]}" stroke="#6B5A45" stroke-width="1"/>')
        else:
            out.append(f'{shape_path(c)} fill="{NEN}" stroke="{VIEN}" stroke-width="1.5"/>')

    # 5. số cổng. Cổng đang tạo kênh: nền tròn xanh, chữ trắng — như app chuẩn.
    trong_kenh = {g for a, b in CHANNELS if a in active and b in active for g in (a, b)}
    for g in sorted(GATE_CENTER):
        x, y = gate_xy(g)
        if g in trong_kenh:
            out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="6.4" fill="{XANH_CONG}"/>')
            fill, dam = "#FFFFFF", 600
        elif g in active:
            fill, dam = "#141210", 700      # cổng treo
        else:
            # chưa hoạt hoá: chữ nhạt, nhưng phải đọc được trên nền màu trung tâm
            fill, dam = ("#F4EFE6" if GATE_CENTER[g] in defined else "#8A857C"), 400
        out.append(f'<text x="{x:.1f}" y="{y+3:.1f}" text-anchor="middle" '
                   f'font-family="Helvetica,Arial,sans-serif" font-size="7.6" '
                   f'font-weight="{dam}" fill="{fill}">{g}</text>')

    out.append("</g></svg>")
    return "".join(out)


if __name__ == "__main__":
    import hd_engine as E
    open("bodygraph-demo.svg", "w", encoding="utf-8").write(
        render(E.build_chart(1970, 5, 1, 14, 20)))
    print("✅ bodygraph-demo.svg")
