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
"""moc_doi.py — Tầng năm: các mốc chuyển đời tính từ chu kỳ hành tinh.

Đây là tầng CHẮC CHẮN NHẤT trong ba tầng thời gian, vì nó chỉ phụ thuộc
chu kỳ quỹ đạo — tính trước được hàng chục năm, sai số dưới một ngày.

KHÔNG dùng Chiron: Moshier ephemeris không có, phải tải file dữ liệu Swiss
Ephemeris riêng và vướng giấy phép. Bốn mốc dưới đây đã đủ phủ cả đời người.

Ranh giới ngôn ngữ (§7.3 Instructions):
  ✅ được  — "giai đoạn này thường là lúc người ta xét lại cam kết lớn"
  ❌ cấm   — "tháng 3 năm sau anh sẽ mất việc"
Nói mạnh, nói cụ thể, nhưng nói THIÊN HƯỚNG chứ không phán SỰ KIỆN.
"""
from __future__ import annotations
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
import swisseph as swe

import hd_engine as E

# (khoá, tên, thiên thể, góc lệch so với vị trí lúc sinh, tuổi ước chừng)
MOC = [
    ("saturn_1",  "Saturn Return lần một",   swe.SATURN,   0.0,   29),
    ("uranus_op", "Uranus đối đỉnh",         swe.URANUS, 180.0,   41),
    ("saturn_2",  "Saturn Return lần hai",   swe.SATURN,   0.0,   59),
]
CHU_KY_MOC = 12  # Jupiter Return lặp mỗi ~12 năm


def _lon(jd: float, pl: int) -> float:
    return swe.calc_ut(jd, pl, E.FLAGS)[0][0] % 360.0


def _lech(jd: float, pl: int, dich: float) -> float:
    """Hiệu góc có dấu, trong khoảng -180..180."""
    return (_lon(jd, pl) - dich + 180.0) % 360.0 - 180.0


def tim_cham(jd_sinh: float, pl: int, goc: float,
             tu_tuoi: float, den_tuoi: float) -> list[float]:
    """Tìm MỌI lần thiên thể chạm đúng điểm đó trong khoảng tuổi cho trước.

    Hành tinh ngoài có nghịch hành nên thường chạm 3 lần chứ không phải 1 —
    và đó là chi tiết có ý nghĩa, nghĩa là giai đoạn kéo dài chứ không phải
    một ngày. Nên phải tìm hết, không dừng ở lần đầu.
    """
    dich = (_lon(jd_sinh, pl) + goc) % 360.0
    b, k = jd_sinh + tu_tuoi * 365.2422, jd_sinh + den_tuoi * 365.2422
    ra, jd, truoc = [], b, _lech(b, pl, dich)
    while jd < k:
        jd += 3.0
        nay = _lech(jd, pl, dich)
        if truoc * nay < 0 and abs(nay - truoc) < 180:
            lo, hi = jd - 3.0, jd
            for _ in range(60):                      # chia đôi cho tới dưới 1 phút
                giua = (lo + hi) / 2
                if _lech(lo, pl, dich) * _lech(giua, pl, dich) < 0:
                    hi = giua
                else:
                    lo = giua
            ra.append((lo + hi) / 2)
        truoc = nay
    return ra


def gop_cum(cham: list[float], khoang_ngay: float = 900.0) -> list[list[float]]:
    """Gộp các lần chạm gần nhau thành MỘT giai đoạn.

    Hành tinh nghịch hành thì đi qua cùng một điểm ba lần trong vòng vài tháng.
    Đó là một mốc kéo dài, không phải ba mốc riêng. Không gộp thì bảng kết quả
    hiện ba dòng cùng tên, khách đọc không hiểu.
    """
    if not cham:
        return []
    cum, hien = [], [cham[0]]
    for c in cham[1:]:
        if c - hien[-1] <= khoang_ngay:
            hien.append(c)
        else:
            cum.append(hien)
            hien = [c]
    cum.append(hien)
    return cum


def _ngay(jd: float, tz: str) -> datetime:
    y, m, d, h = swe.revjul(jd, swe.GREG_CAL)
    return (datetime(int(y), int(m), int(d)) + timedelta(hours=h)) \
        .replace(tzinfo=ZoneInfo("UTC")).astimezone(ZoneInfo(tz))


def moc_doi(chart: dict, tz: str = "Asia/Ho_Chi_Minh") -> list[dict]:
    """Trả về các mốc chuyển đời của một người, kèm cổng mà hành tinh chiếm."""
    jd = chart["thoi_diem"]["jd_ca_tinh"]
    ra = []

    def them(khoa, ten, pl, cum):
        p = E.wheel_position(_lon(cum[0], pl))
        ra.append({
            "khoa": khoa, "ten": ten, "so_lan_cham": len(cum),
            "bat_dau": _ngay(cum[0], tz), "ket_thuc": _ngay(cum[-1], tz),
            "tuoi_bat_dau": round((cum[0] - jd) / 365.2422, 1),
            "tuoi_ket_thuc": round((cum[-1] - jd) / 365.2422, 1),
            "keo_dai_thang": round((cum[-1] - cum[0]) / 30.44),
            "cong": p["gate"], "hao": p["line"],
        })

    for khoa, ten, pl, goc, tuoi in MOC:
        for cum in gop_cum(tim_cham(jd, pl, goc, tuoi - 10, tuoi + 10)):
            them(khoa, ten, pl, cum)

    # Jupiter Return lặp mỗi ~12 năm
    for cum in gop_cum(tim_cham(jd, swe.JUPITER, 0.0, 10, 85)):
        them("jupiter", "Jupiter Return", swe.JUPITER, cum)

    return sorted(ra, key=lambda x: x["tuoi_bat_dau"])


if __name__ == "__main__":
    c = E.build_chart(1985, 3, 15, 7, 30, noi_sinh="Cần Thơ")
    print(f"Người sinh 15/03/1985 07:30 — {c['type']} · {c['profile']}\n")
    print(f"{'Mốc':<26}{'Tuổi':<14}{'Thời gian':<26}{'Kéo dài':<12}Cổng")
    print("-" * 88)
    for m in moc_doi(c):
        tuoi = (f"{m['tuoi_bat_dau']}" if m["so_lan_cham"] == 1
                else f"{m['tuoi_bat_dau']}–{m['tuoi_ket_thuc']}")
        tg = (m["bat_dau"].strftime("%m/%Y") if m["so_lan_cham"] == 1
              else f"{m['bat_dau'].strftime('%m/%Y')} → {m['ket_thuc'].strftime('%m/%Y')}")
        keo = f"{m['keo_dai_thang']} tháng" if m["keo_dai_thang"] else "một lần"
        print(f"{m['ten']:<26}{tuoi:<14}{tg:<26}{keo:<12}{m['cong']}.{m['hao']}")
