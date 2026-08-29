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
"""luan_moc_doi.py — Dựng bản luận mốc đời cho một người.

Công thức ba tầng, theo đúng chốt của Thầy Hoàng ngày 28/08/2026:

    1. DỮ KIỆN   — thiên văn tính được, cụ thể tới từng tháng
    2. NỐI VÀO ĐỜI — mốc rơi vào cổng nào thì nghiêng về lĩnh vực đó
    3. VIỆC LÀM  — khách rời đi với một việc cụ thể

Tầng 2 là chỗ khách hiểu và dùng được. Không có nó thì tầng 1 vô dụng.
"""
from __future__ import annotations
from datetime import datetime
from zoneinfo import ZoneInfo

import hd_engine as E
import moc_doi as M
from content_moc_doi import MOC_DOI, LINH_VUC_THEO_TRUNG_TAM

CENTER_VI = {"head": "Đầu", "ajna": "Ajna", "throat": "Cổ họng", "g": "Trung tâm G",
             "heart": "Tim", "spleen": "Lá lách", "solar_plexus": "Đám rối mặt trời",
             "sacral": "Xương cùng", "root": "Gốc"}


def _khoang(m: dict) -> str:
    if m["so_lan_cham"] == 1:
        return f"tháng {m['bat_dau'].strftime('%m/%Y')}"
    return (f"từ tháng {m['bat_dau'].strftime('%m/%Y')} tới "
            f"tháng {m['ket_thuc'].strftime('%m/%Y')}")


def luan_mot_moc(m: dict, ten_cong: str) -> dict:
    """Ba tầng cho một mốc. Trả về dict để dễ đưa lên web hoặc in ra."""
    d = MOC_DOI[m["khoa"]]
    tt = E.GATE_CENTER[m["cong"]]
    linh_vuc, chi_tiet = LINH_VUC_THEO_TRUNG_TAM[tt]

    lan = ("chạm một lần" if m["so_lan_cham"] == 1
           else f"chạm {m['so_lan_cham']} lần, kéo dài {m['keo_dai_thang']} tháng")

    du_kien = (
        f"{d['ten_vi']} của bạn rơi vào {_khoang(m)}, lúc bạn {m['tuoi_bat_dau']} tuổi — "
        f"{lan}. Đây là dữ kiện thiên văn, tính trước được và không đổi.")

    noi_vao_doi = (
        f"Mốc này của bạn chạm đúng cổng {m['cong']}.{m['hao']} — {ten_cong}, "
        f"nằm ở trung tâm {CENTER_VI[tt]}. Nên câu hỏi của giai đoạn này với bạn "
        f"nghiêng về **{linh_vuc}**: {chi_tiet}. "
        f"Cùng một mốc tuổi, người khác cổng thì câu hỏi sẽ khác.")

    return {
        "khoa": m["khoa"], "ten": d["ten_vi"], "tagline": d["tagline"],
        "tuoi": f"{m['tuoi_bat_dau']}" if m["so_lan_cham"] == 1
                else f"{m['tuoi_bat_dau']}–{m['tuoi_ket_thuc']}",
        "thoi_gian": _khoang(m),
        "cong": f"{m['cong']}.{m['hao']}", "ten_cong": ten_cong,
        "trung_tam": CENTER_VI[tt], "linh_vuc": linh_vuc,
        "du_kien": du_kien,
        "noi_vao_doi": noi_vao_doi,
        "co_hoc": d["co_hoc"],
        "thuong_thay": d["thuong_thay"],
        "thuan": d["di_qua_thuan"],
        "lech": d["di_qua_lech"],
        "cau_hoi": d["cau_hoi"],
    }


def luan_moc_doi(chart: dict, kho_cong: dict, tz: str = "Asia/Ho_Chi_Minh") -> dict:
    """Chia mốc thành đã qua / đang trong / sắp tới, kèm bản luận đầy đủ."""
    hn = datetime.now(ZoneInfo(tz))
    qua, dang, sap = [], [], []
    for m in M.moc_doi(chart, tz):
        ten_cong = kho_cong.get(str(m["cong"]), {}).get("name_vi", f"cổng {m['cong']}")
        b = luan_mot_moc(m, ten_cong)
        b["_bat_dau"] = m["bat_dau"]
        if m["bat_dau"] <= hn <= m["ket_thuc"]:
            dang.append(b)
        elif m["bat_dau"] > hn:
            b["con_bao_lau"] = _con(m["bat_dau"], hn)
            sap.append(b)
        else:
            qua.append(b)
    return {"dang_o_trong": dang, "sap_toi": sap[:2], "da_qua": qua}


def _con(moc: datetime, hn: datetime) -> str:
    ngay = (moc - hn).days
    nam, thang = ngay // 365, (ngay % 365) // 30
    if nam and thang:
        return f"còn {nam} năm {thang} tháng"
    if nam:
        return f"còn {nam} năm"
    return f"còn {thang} tháng"


if __name__ == "__main__":
    import json
    from pathlib import Path
    kho = json.loads(Path("hd-content-public.json").read_text(encoding="utf-8"))["gates"]

    for ten, args in [("TK-04", dict(nam=1968, thang=12, ngay=25, gio=4, phut=20, mien="nam")),
                      ("TK-06", dict(nam=1985, thang=3, ngay=15, gio=7, phut=30))]:
        c = E.build_chart(**args)
        r = luan_moc_doi(c, kho)
        print("═" * 76)
        print(f"{ten} — {c['type']} · {c['authority']} · Profile {c['profile']}")
        print("═" * 76)
        for nhan, ds in [("ĐANG Ở TRONG", r["dang_o_trong"]), ("MỐC TỚI", r["sap_toi"][:1])]:
            for b in ds:
                print(f"\n◈ {nhan}: {b['ten']}"
                      + (f"  ({b.get('con_bao_lau','')})" if b.get("con_bao_lau") else ""))
                print(f"  {b['tagline']}\n")
                print(f"  [1] {b['du_kien']}\n")
                print(f"  [2] {b['noi_vao_doi']}\n")
                print(f"  [3] {b['thuong_thay'][:190]}…\n")
                print(f"  Câu hỏi: {b['cau_hoi'][0]}")
        print()
