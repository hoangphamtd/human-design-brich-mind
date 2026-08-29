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
"""transit_thang.py — Tầng tháng: chia tháng thành các cửa sổ Mặt Trời.

Khung lấy theo cách omapadotesouro.com làm — bài dự báo tháng có cấu trúc
chặt nhất trong số các nguồn đã khảo sát:

  · Mặt Trời và Trái Đất luôn đi thành CẶP ĐỐI CỰC. Mặt Trời là chủ đề
    người ta ý thức được, Trái Đất là nền giữ chân. Đây là cơ học Human
    Design chứ không phải chỉ liệt kê cổng.
  · Mỗi cửa sổ có NGÀY CỤ THỂ, khoảng 5-6 ngày.
  · Mỗi cửa sổ có lời khuyên NÊN LÀM GÌ và TRÁNH GÌ.
  · Cuối bài có mục riêng cho từng Type.

Phần họ KHÔNG có mà mình có: cá nhân hoá theo bản đồ từng người — biết
cổng nào của khách được bật, kênh nào tạm đóng trong cửa sổ đó.
"""
from __future__ import annotations
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
import swisseph as swe

import hd_engine as E


def _mat_troi(jd: float) -> float:
    return swe.calc_ut(jd, swe.SUN, E.FLAGS)[0][0] % 360.0


def _jd(dt: datetime) -> float:
    u = dt.astimezone(ZoneInfo("UTC"))
    return swe.julday(u.year, u.month, u.day,
                      u.hour + u.minute / 60, swe.GREG_CAL)


def _tim_doi_cong(jd_tu: float, jd_den: float) -> list[float]:
    """Tìm chính xác thời điểm Mặt Trời sang cổng mới."""
    ra, jd = [], jd_tu
    truoc = E.wheel_position(_mat_troi(jd))["gate"]
    while jd < jd_den:
        jd += 0.25
        nay = E.wheel_position(_mat_troi(jd))["gate"]
        if nay != truoc:
            lo, hi = jd - 0.25, jd
            for _ in range(40):                       # chia đôi tới dưới 1 phút
                giua = (lo + hi) / 2
                if E.wheel_position(_mat_troi(lo))["gate"] == \
                   E.wheel_position(_mat_troi(giua))["gate"]:
                    lo = giua
                else:
                    hi = giua
            ra.append(hi)
            truoc = nay
    return ra


def cua_so_thang(nam: int, thang: int, tz: str = "Asia/Ho_Chi_Minh") -> list[dict]:
    """Chia một tháng thành các cửa sổ Mặt Trời, mỗi cửa sổ khoảng 5-6 ngày."""
    Z = ZoneInfo(tz)
    dau = datetime(nam, thang, 1, tzinfo=Z)
    cuoi = (datetime(nam + (thang == 12), thang % 12 + 1, 1, tzinfo=Z))

    moc = [_jd(dau)] + _tim_doi_cong(_jd(dau), _jd(cuoi)) + [_jd(cuoi)]
    ra = []
    for i in range(len(moc) - 1):
        giua = (moc[i] + moc[i + 1]) / 2
        lon = _mat_troi(giua)
        mt = E.wheel_position(lon)
        td = E.wheel_position((lon + 180.0) % 360.0)
        b = datetime.fromtimestamp(
            (moc[i] - 2440587.5) * 86400, ZoneInfo("UTC")).astimezone(Z)
        k = datetime.fromtimestamp(
            (moc[i + 1] - 2440587.5) * 86400, ZoneInfo("UTC")).astimezone(Z)
        ra.append({
            "tu": b, "den": k,
            "so_ngay": round((moc[i + 1] - moc[i]), 1),
            "mat_troi": mt["gate"], "mt_hao": mt["line"],
            "trai_dat": td["gate"], "td_hao": td["line"],
        })
    return ra


def ca_nhan_hoa(cua_so: dict, chart: dict) -> dict:
    """Cửa sổ này chạm gì vào bản đồ RIÊNG của người này?

    Đây là phần các trang dự báo tháng không làm được, vì họ viết chung
    cho cả thế giới. Mình biết cổng nào của khách đang treo.
    """
    cong_sinh = set(chart["cong_hoat_hoa"])
    tt_sinh = set(chart["trung_tam_dinh_nghia"])
    troi = {cua_so["mat_troi"], cua_so["trai_dat"]}

    kenh_tam, tt_tam = [], set()
    for a, b in E.CHANNELS:
        co_a = a in cong_sinh or a in troi
        co_b = b in cong_sinh or b in troi
        # chỉ tính kênh MỚI đóng nhờ transit, không tính kênh vốn đã có
        if co_a and co_b and not (a in cong_sinh and b in cong_sinh):
            kenh_tam.append(f"{min(a,b)}-{max(a,b)}")
            tt_tam |= {E.GATE_CENTER[a], E.GATE_CENTER[b]}

    return {
        "co_san": sorted(troi & cong_sinh),          # cổng khách vốn có
        "muon_them": sorted(troi - cong_sinh),       # cổng khách được mượn
        "kenh_tam": sorted(set(kenh_tam)),
        "trung_tam_tam": sorted(tt_tam - tt_sinh),   # trung tâm tạm sáng lên
    }


if __name__ == "__main__":
    print("CÁC CỬA SỔ MẶT TRỜI — tháng 9/2026\n")
    print(f"{'Từ ngày':<12}{'Đến':<12}{'Dài':<7}{'Mặt Trời':<12}Trái Đất")
    print("-" * 58)
    for c in cua_so_thang(2026, 9):
        print(f"{c['tu'].strftime('%d/%m %H:%M'):<12}"
              f"{c['den'].strftime('%d/%m %H:%M'):<12}"
              f"{c['so_ngay']:<7}"
              f"cổng {c['mat_troi']}.{c['mt_hao']:<6}"
              f"cổng {c['trai_dat']}.{c['td_hao']}")

    print("\n\nRIÊNG CHO MỘT NGƯỜI — TK-06, Projector 2/4\n")
    ca = E.build_chart(1985, 3, 15, 7, 30, noi_sinh="Cần Thơ")
    for c in cua_so_thang(2026, 9):
        r = ca_nhan_hoa(c, ca)
        if r["kenh_tam"] or r["muon_them"]:
            print(f"  {c['tu'].strftime('%d/%m')}–{c['den'].strftime('%d/%m')}  "
                  f"MT {c['mat_troi']} · TĐ {c['trai_dat']}")
            if r["co_san"]:
                print(f"      cổng vốn có được nhấn: {r['co_san']}")
            if r["kenh_tam"]:
                print(f"      kênh tạm đóng: {', '.join(r['kenh_tam'])}")
            if r["trung_tam_tam"]:
                print(f"      trung tâm tạm sáng: {', '.join(r['trung_tam_tam'])}")
