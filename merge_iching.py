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
"""Nhập bảng Kinh Dịch vào hd-core-data.json."""
import json
from iching_map import ICHING, GHI_CHU_LECH

d = json.load(open("hd-core-data.json", encoding="utf-8"))
m = {r[0]: r for r in ICHING}
for g in d["gates"]:
    n, hv, han, ngh, hd, k = m[g["gate"]]
    g["iching"] = {"que_so": n, "ten_han_viet": hv,
                   "nghia_goc": ngh, "muc_khop": k,
                   "ghi_chu": GHI_CHU_LECH.get(n)}
d["meta"]["iching"] = ("Human Design dùng thẳng số hiệu quẻ King Wen làm số hiệu cổng: "
                       "cổng N = quẻ N. Trường muc_khop cho biết tên cổng HD bám sát "
                       "nghĩa quẻ tới đâu (cao / vua / lech).")
json.dump(d, open("hd-core-data.json","w",encoding="utf-8"), ensure_ascii=False, indent=2)
print("✅ đã gắn 64 quẻ vào hd-core-data.json")
print("   ví dụ cổng 48:", d["gates"][[g["gate"] for g in d["gates"]].index(48)]["iching"])
