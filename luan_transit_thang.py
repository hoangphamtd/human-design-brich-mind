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
"""luan_transit_thang.py — Dựng bài dự báo tháng RIÊNG cho một người.

Khung theo omapadotesouro.com, thêm phần cá nhân hoá mà họ không có:
biết cổng nào của khách vốn có, cổng nào được mượn, kênh nào tạm đóng.

Mỗi cửa sổ có bốn phần:
    1. NGÀY       — từ ngày nào tới ngày nào, dài mấy ngày
    2. CHỦ ĐỀ     — Mặt Trời làm gì, Trái Đất giữ chân bằng gì
    3. RIÊNG BẠN  — cửa sổ này chạm gì vào bản đồ của chính bạn
    4. NÊN / TRÁNH — hai câu cụ thể
"""
from __future__ import annotations
import json
from pathlib import Path

import hd_engine as E
import transit_thang as T
from content_transit import NEN_TRANH

CENTER_VI = {"head": "Đầu", "ajna": "Ajna", "throat": "Cổ họng", "g": "Trung tâm G",
             "heart": "Tim", "spleen": "Lá lách", "solar_plexus": "Đám rối mặt trời",
             "sacral": "Xương cùng", "root": "Gốc"}

# Lời nhắc theo Type — mỗi loại năng lượng dùng cửa sổ transit khác nhau
THEO_TYPE = {
    "generator": "Tháng này việc gì cũng chờ có người hỏi rồi để bụng trả lời. "
                 "Cửa sổ nào bụng không gật thì để yên, đừng vì thấy hợp lý mà nhận.",
    "manifesting_generator": "Bạn sẽ muốn nhảy vào ngay khi thấy cửa sổ hợp. "
                             "Nhảy được, nhưng báo trước cho người bị ảnh hưởng một câu.",
    "manifestor": "Cửa sổ nào thấy đúng thì khởi động, nhưng nói trước cho người "
                  "liên quan. Không báo trước là gặp sức cản, rồi sinh bực.",
    "projector": "Đừng dùng lịch này để tự lao vào việc. Dùng nó để biết tuần nào "
                 "mình dễ được nhìn thấy, rồi chờ lời mời đúng.",
    "reflector": "Cả tháng này với bạn là một chu kỳ để quan sát, không phải để "
                 "quyết. Ghi lại mỗi cửa sổ bạn thấy thế nào, cuối tháng đọc lại.",
}


def bai_thang(chart: dict, nam: int, thang: int,
              kho_cong: dict, tz: str = "Asia/Ho_Chi_Minh") -> dict:
    cua_so = []
    for c in T.cua_so_thang(nam, thang, tz):
        r = T.ca_nhan_hoa(c, chart)
        mt, td = c["mat_troi"], c["trai_dat"]
        cd_mt, nen, tranh = NEN_TRANH[mt]
        cd_td = NEN_TRANH[td][0]

        # phần riêng cho người này
        rieng = []
        if r["co_san"]:
            ds = ", ".join(f"cổng {g}" for g in r["co_san"])
            rieng.append(f"{ds} là cổng bạn vốn có — tuần này nó được nhấn mạnh hơn thường lệ.")
        if r["kenh_tam"]:
            ds = ", ".join(r["kenh_tam"])
            tt = ", ".join(CENTER_VI[x] for x in r["trung_tam_tam"]) if r["trung_tam_tam"] else ""
            cau = f"Kênh {ds} của bạn tạm đóng trong mấy ngày này"
            cau += f", nên trung tâm {tt} tạm sáng lên — bạn sẽ thấy mình có thứ năng lượng vốn không phải của mình." if tt else "."
            rieng.append(cau)
        if not rieng:
            rieng.append("Cửa sổ này không chạm vào cổng nào của bạn. "
                         "Bạn vẫn cảm được không khí chung, nhưng nhẹ hơn người có cổng đó.")

        cua_so.append({
            "tu": c["tu"], "den": c["den"], "so_ngay": c["so_ngay"],
            "mat_troi": f"{mt}.{c['mt_hao']}", "trai_dat": f"{td}.{c['td_hao']}",
            "ten_mt": kho_cong.get(str(mt), {}).get("name_vi", ""),
            "ten_td": kho_cong.get(str(td), {}).get("name_vi", ""),
            "chu_de": cd_mt, "chu_de_nen": cd_td,
            "rieng_ban": " ".join(rieng),
            "nen": nen, "tranh": tranh,
        })

    return {"thang": f"{thang:02d}/{nam}", "cua_so": cua_so,
            "loi_theo_type": THEO_TYPE[chart["type"]]}


def in_ra(b: dict, chart: dict, ten: str):
    print("═" * 74)
    print(f"THÁNG {b['thang']} — {ten}")
    print(f"{chart['type']} · {chart['authority']} · Profile {chart['profile']}")
    print("═" * 74)
    for c in b["cua_so"]:
        print(f"\n◈ {c['tu'].strftime('%d/%m')} – {c['den'].strftime('%d/%m')}"
              f"  ({c['so_ngay']} ngày)   Mặt Trời {c['mat_troi']} · Trái Đất {c['trai_dat']}")
        print(f"  {c['chu_de'].upper()}")
        print(f"  Mặt Trời ở cổng {c['mat_troi'].split('.')[0]} — {c['ten_mt']}. "
              f"Trái Đất giữ chân ở cổng {c['trai_dat'].split('.')[0]} — {c['ten_td']}.")
        print(f"\n  Riêng bạn: {c['rieng_ban']}")
        print(f"\n  ✔ NÊN:   {c['nen']}")
        print(f"  ✘ TRÁNH: {c['tranh']}")
    print(f"\n{'─' * 74}")
    print(f"Với {chart['type']}: {b['loi_theo_type']}")


if __name__ == "__main__":
    kho = json.loads(Path("hd-content-public.json").read_text(encoding="utf-8"))["gates"]
    ca = E.build_chart(1985, 3, 15, 7, 30, noi_sinh="Cần Thơ")
    in_ra(bai_thang(ca, 2026, 9, kho), ca, "TK-06")
