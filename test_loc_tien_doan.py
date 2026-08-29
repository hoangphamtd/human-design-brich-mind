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
"""test_loc_tien_doan.py — Tự kiểm bộ lọc tầng tiên đoán.

Lý do có file này (HD-11 §7): dự án đã hai lần mắc lỗi "phép kiểm không phủ
hết thứ nó định phủ". HD-10 §6 báo đã rà 200 cửa sổ tháng và 214 bản luận
mốc đời, sạch cả hai — nhưng "sạch" mới chỉ nghĩa là mấy cái regex không bắt
được gì. Chưa ai kiểm xem regex đó có bắt nổi câu hỏng hay không.

File này nhét mẫu hỏng vào xem bộ lọc có bắt được không, và nhét mẫu tốt vào
xem nó có bắt nhầm không. Hai chiều, không thiếu chiều nào.

Chạy:
    .venv\\Scripts\\python -m unittest test_loc_tien_doan      → chạy bài kiểm
    .venv\\Scripts\\python test_loc_tien_doan.py --bao-cao     → in bảng kết quả
"""
from __future__ import annotations
import re
import sys
import unittest

import loc_nd38 as L

# ---------------------------------------------------------------------------
# Bộ lọc tầng tiên đoán theo HD-10 §6, chép nguyên văn.
#
# LƯU Ý: tới ngày viết file này, dict `CAM` KHÔNG tồn tại trong loc_nd38.py
# (grep toàn dự án không thấy). Nghĩa là năm mẫu dưới đây chỉ nằm trên tài
# liệu, chưa bao giờ được nối vào bộ lọc đang chạy. Giữ nguyên văn ở đây để
# đo đúng "bộ lọc hiện tại" ở lần chạy đầu.
# ---------------------------------------------------------------------------
BASELINE_HD10 = {
    "phán biến cố": r"(bạn|anh|chị)\s+sẽ\s+(mất|gặp|bị|cãi|ly\s+hôn|phá\s+sản)",
    "hẹn ngày xấu": r"ngày\s+\d{1,2}\s+(bạn|anh|chị)\s+(sẽ|bị)",
    "gặp hạn":      r"(gặp\s+hạn|vận\s+hạn|đại\s+hạn|xui|tai\s+ương)",
    "ngày tốt xấu": r"ngày\s+(tốt|xấu|đẹp|kỵ)",
    "chắc chắn":    r"(chắc\s+chắn|nhất\s+định)\s+(bạn|anh|chị)?\s*sẽ",
}

CAM_DA_NOI = hasattr(L, "CAM")          # bộ lọc tiên đoán đã nối vào code chưa
CAM_DANG_DUNG = getattr(L, "CAM", BASELINE_HD10)


# ---------------------------------------------------------------------------
# 2.1 — MẪU HỎNG: bộ lọc PHẢI bắt được cả 14 câu
#       Câu vi phạm bốn điều cấm của HD-10 §4, viết như người thật sẽ viết.
# ---------------------------------------------------------------------------
MAU_HONG = [
    (1,  "Cuối tháng này anh sẽ mất một khoản tiền lớn.",       "phán biến cố"),
    (2,  "Ngày 11 chị sẽ bị người ta lừa hợp đồng.",            "hẹn ngày cho biến cố"),
    (3,  "Tháng ba năm sau bạn gặp hạn công việc.",             "chữ hạn"),
    (4,  "Ngày 20 là ngày xấu, đừng khởi sự gì.",               "ngôn ngữ xem ngày"),
    (5,  "Chắc chắn bạn sẽ chia tay trong quý này.",            "chắc chắn + biến cố"),
    (6,  "Tháng này dễ mất việc, nên chuẩn bị trước.",          "phán mất mát, không chủ ngữ"),
    (7,  "Quanh ngày 11 nên kiêng ký giấy tờ.",                 "xem ngày, chữ kiêng"),
    (8,  "Giai đoạn này sao xấu chiếu, làm gì cũng khó.",       "ngôn ngữ tử vi"),
    (9,  "Coi chừng tai nạn quanh ngày 20.",                    "hẹn ngày cho tai hoạ"),
    (10, "Vợ chồng anh chị sẽ cãi nhau trong tuần đầu.",        "phán biến cố quan hệ"),
    (11, "Cấu hình này khiến bạn ly dị sớm.",                   "phán mất mát, biến thể ly dị"),
    (12, "Tháng sau khó tránh khỏi mất mát về tiền bạc.",       "phán mất mát, không chủ ngữ"),
    (13, "Nên đi cúng giải trước rằm cho nhẹ vận.",             "nghi lễ đổi vận"),
    (14, "Ngày này hung, ngày kia cát, nhớ chọn cho kỹ.",       "xem ngày hung/cát"),
]

# ---------------------------------------------------------------------------
# 2.2 — MẪU TỐT: bộ lọc PHẢI KHÔNG bắt câu nào
#       Câu đúng chuẩn HD-10, hoặc câu trung tính dễ bị regex bắt nhầm.
# ---------------------------------------------------------------------------
MAU_TOT = [
    (1,  "Cửa sổ này thường đi kèm cảm giác bực bội; nếu thấy vậy, dừng lại trước khi phản ứng.", "—"),
    (2,  "Quanh giữa tháng, nên xem kỹ giấy tờ trước khi ký.",                                    "—"),
    (3,  "Nhiều người có cấu hình này thấy rằng tuần đầu tháng khá căng.",                        "—"),
    (4,  "Hôm nào trời đẹp, ngày đẹp thì ra ngoài đi bộ một vòng.",                               "chứa 'ngày đẹp'"),
    (5,  "Trong tuần này anh chị sẽ gặp nhiều người mới hơn bình thường.",                        "chứa 'chị sẽ gặp'"),
    (6,  "Cảm giác xui xẻo mà nhiều người mô tả thường chỉ là mệt tích tụ.",                      "chứa 'xui'"),
    (7,  "Mốc này kéo dài từ tháng 1 năm 2027 tới tháng 10 năm 2027.",                            "có số ngày tháng"),
    (8,  "Nếu bạn sẽ đi xa trong tháng này, thu xếp lịch nghỉ cho đủ.",                           "chứa 'bạn sẽ đi'"),
    (9,  "Đây là tham chiếu để anh/chị tự kiểm nghiệm, không phải lời phán.",                     "—"),
    (10, "Ngày 15 là ngày Mặt Trời chuyển sang cổng 12.",                                         "khớp mẫu 'ngày N'"),
]


def bat(cau: str) -> list[str]:
    """Trả về danh sách tên luật bắt được câu này. Rỗng nghĩa là lọt lưới.

    Gọi THẲNG loc_nd38.vi_pham() — đúng hàm mà bản rà hàng thật dùng. Không
    chép lại luật vào đây, để không tái diễn cảnh bài kiểm xanh mà hàng thật
    chạy bộ luật khác (đúng lỗi HD-10 §6 đã mắc).

    Xét cả Tầng A lẫn tầng tiên đoán. Tầng B không tính — đó là danh sách gỡ
    ở bản public, không phải vi phạm.
    """
    if not CAM_DA_NOI:                                   # trước khi sửa: đo bản HD-10 §6
        return bat_theo_baseline(cau)
    return [f"{nhan}:{ten}" for nhan, ten, _ in L.vi_pham(cau)]


def bat_theo_baseline(cau: str) -> list[str]:
    """Chạy lại đúng bộ lọc CŨ (Tầng A + 5 mẫu HD-10 §6) để tái hiện lần chạy đầu."""
    low = cau.lower()
    ra = []
    for nhan, nhom in (("A", L.TANG_A), ("tiên đoán", BASELINE_HD10)):
        for ten, pat in nhom.items():
            for m in re.finditer(pat, low):
                if L._la_phu_dinh(low, m.start()):
                    continue
                ra.append(f"{nhan}:{ten}")
                break
    return ra


class KiemMauHong(unittest.TestCase):
    """Chiều thứ nhất: bộ lọc có bắt nổi câu hỏng không."""

    def test_bat_du_14_cau_hong(self):
        lot = [(i, c, v) for i, c, v in MAU_HONG if not bat(c)]
        self.assertEqual(
            [], lot,
            "\n\nCÂU HỎNG LỌT LƯỚI:\n" + "\n".join(f"  #{i} [{v}] {c}" for i, c, v in lot))


class KiemMauTot(unittest.TestCase):
    """Chiều thứ hai: bộ lọc có bắt nhầm câu tốt không."""

    def test_khong_bat_nham_cau_nao(self):
        nham = [(i, c, bat(c)) for i, c, _ in MAU_TOT if bat(c)]
        self.assertEqual(
            [], nham,
            "\n\nCÂU TỐT BỊ BẮT NHẦM:\n" + "\n".join(f"  #{i} {c}\n      -> {r}" for i, c, r in nham))


class KiemChinhBaiKiem(unittest.TestCase):
    """Tự kiểm phép kiểm: hàm bat() phải thật sự phân biệt được hai chiều.

    Nếu bat() hỏng thành 'luôn trả rỗng' thì bài kiểm mẫu tốt vẫn xanh mà
    không ai biết. Chốt hai mỏ neo để bắt đúng trường hợp đó.
    """

    def test_bat_duoc_cau_hong_khong_the_choi_cai(self):
        self.assertTrue(bat("Chắc chắn bạn sẽ phá sản vào ngày 3."))

    def test_khong_bat_cau_trung_tinh_hoan_toan(self):
        self.assertEqual([], bat("Mặt Trời đi qua cổng 12 trong tuần tới."))


class KiemKhongBatNhamKhoThat(unittest.TestCase):
    """Mười câu mẫu là bẫy do người nghĩ ra. Kho thật 133 khối là bẫy do đời
    nghĩ ra — và nó đã bắt được hai lỗi regex mà mười câu kia không bắt nổi:
    'tai nạn' trong nghĩa bóng, và 'là' khớp vào hai chữ đầu của 'làm'.
    """

    # Bản nội bộ đầy đủ trước, bản public sau. Kho GitHub cố ý KHÔNG có
    # hd-content-v1.json (Tầng B), nên ở đó bài này lùi về bản public.
    #
    # KHÔNG dùng skipTest: bỏ qua âm thầm là mất phủ mà bộ kiểm vẫn xanh —
    # đúng dạng lỗi §7. Người tải kho về sẽ thấy 7/7 mà thật ra chạy 6 bài.
    #
    # Nhánh lùi vẫn giữ được phủ thật: ba chỗ bắt nhầm từng tìm ra — "là"
    # khớp vào "làm" ở Profile 3/5, và "tai nạn" nghĩa bóng ở Cổng 63 với
    # Kênh 4-63 — đều nằm trong nội dung public.
    KHO = ["hd-content-v1.json", "hd-content-public.json"]

    def test_bo_loc_tien_doan_khong_bat_nham_kho_ban_do_sinh(self):
        import json
        import os
        dung = next((f for f in self.KHO if os.path.isfile(f)), None)
        self.assertIsNotNone(
            dung, f"Không thấy kho nội dung nào trong {self.KHO} — không rà được gì.")
        with open(dung, encoding="utf-8") as f:
            C = json.load(f)

        so_khoi = sum(len(C.get(k, {})) for k in
                      ("types", "authorities", "profiles", "centers", "gates", "channels"))
        nhan = f"{dung} · {so_khoi} khối"
        if dung != self.KHO[0]:
            nhan += "  (bản nội bộ không có ở đây — đã lùi về bản public)"
        print(f"\n  [rà kho] {nhan}")

        nham = [(khoi, ten, trich.strip())
                for khoi, _, van in L.duyet(C)
                for tang, ten, trich in L.vi_pham(van) if tang == "tiên đoán"]
        self.assertEqual(
            [], nham,
            f"\n\nBỘ LỌC TIÊN ĐOÁN BẮT NHẦM — đang rà {nhan}:\n"
            + "\n".join(f"  [{t}] {k}: …{x}…" for k, t, x in nham))


class KiemContentSachTangB(unittest.TestCase):
    """Canh cổng cho việc công bố mã nguồn theo AGPL.

    Tầng B — phần cơ thể theo hệ thống gốc — được dùng khi tư vấn riêng, CẤM
    trong nội dung công khai (§7.3 / HD-02 §9.3). Ngày 29/08/2026 nó đã được
    tách khỏi `content_*.py` sang `noi_dung_tang_b.py`, để `content_*.py` đẩy
    lên GitHub mà không mang theo.

    Bài này canh việc đó: ai vô tình viết một câu Tầng B trở lại vào
    `content_*.py` thì bộ kiểm đỏ NGAY, chứ không phải phát hiện sau khi mã
    đã lên mạng. Công bố mã nguồn là việc không lùi được.
    """

    MODULE = [
        ("content_types", "TYPES"), ("content_authorities", "AUTHORITIES"),
        ("content_profiles", "PROFILES"), ("content_centers", "CENTERS"),
        ("content_channels", "CHANNELS"),
        ("content_gates_p1", "GATES_P1"), ("content_gates_p2", "GATES_P2"),
        ("content_gates_p3", "GATES_P3"), ("content_gates_p4", "GATES_P4"),
        ("iching_map", "ICHING"),
    ]

    def test_content_py_khong_con_tang_b(self):
        import importlib
        dinh = []
        for ten_mod, ten_bien in self.MODULE:
            mod = importlib.reload(importlib.import_module(ten_mod))
            kho = getattr(mod, ten_bien)
            for _, duong, van in L._di(ten_mod, f"{ten_mod}.{ten_bien}", kho):
                low = van.lower()
                for ten_luat, pat in L.TANG_B.items():
                    for m in re.finditer(pat, low):
                        dinh.append((ten_luat, duong,
                                     van[max(0, m.start() - 40):m.end() + 40].strip()))
        self.assertEqual(
            [], dinh,
            f"\n\nTẦNG B QUAY LẠI content_*.py — {len(dinh)} chỗ.\n"
            "Đây là mã nguồn công khai theo AGPL: đẩy lên là công khai Tầng B,\n"
            "và không lùi được. Chuyển nội dung này sang noi_dung_tang_b.py.\n"
            + "\n".join(f"  [{t}] {d}\n      …{x}…" for t, d, x in dinh[:8]))


class KiemChinhBanRaTangThoiGian(unittest.TestCase):
    """Tự kiểm bản rà tầng thời gian — mấu chốt của cả lệnh này.

    ra_tang_thoi_gian() báo 'sạch'. Câu đó chỉ có giá trị nếu nó BIẾT KÊU khi
    có câu hỏng. Nên nhét một câu hỏng vào kho rồi xem nó có kêu không —
    đúng cách Claude Code đã bắt lỗi biên hào ở HD-11 §7.
    """

    def _chay_gon(self):
        """Chạy bản rà trên panel rút gọn cho nhanh, nuốt phần in ra."""
        import contextlib, io as _io
        with contextlib.redirect_stdout(_io.StringIO()):
            return L.ra_tang_thoi_gian()

    def test_ban_ra_biet_keu_khi_kho_bi_nhiem(self):
        import content_transit as CT
        import content_moc_doi as CM

        goc_nguoi, goc_moc, goc_thang = L.NGUOI_MAU, L.NGUOI_MAU_MOC, L.THANG_MAU
        goc_nen_tranh = CT.NEN_TRANH[1]
        goc_saturn = CM.MOC_DOI["saturn_1"]["thuong_thay"]
        try:
            L.NGUOI_MAU, L.NGUOI_MAU_MOC = goc_nguoi[:1], []
            L.THANG_MAU = goc_thang[:1]

            sach = self._chay_gon()
            self.assertEqual(0, sach, "Kho đang sạch thì bản rà phải báo 0")

            # nhiễm kho tháng
            CT.NEN_TRANH[1] = ("Chủ đề", "Ngày 11 chị sẽ bị lừa hợp đồng.", "Tránh gì đó")
            self.assertGreater(self._chay_gon(), 0,
                               "Nhét câu hỏng vào kho THÁNG mà bản rà vẫn báo sạch")
            CT.NEN_TRANH[1] = goc_nen_tranh

            # nhiễm kho mốc đời
            CM.MOC_DOI["saturn_1"]["thuong_thay"] = "Giai đoạn này sao xấu chiếu, dễ mất việc."
            self.assertGreater(self._chay_gon(), 0,
                               "Nhét câu hỏng vào kho MỐC ĐỜI mà bản rà vẫn báo sạch")
        finally:
            CT.NEN_TRANH[1] = goc_nen_tranh
            CM.MOC_DOI["saturn_1"]["thuong_thay"] = goc_saturn
            L.NGUOI_MAU, L.NGUOI_MAU_MOC, L.THANG_MAU = goc_nguoi, goc_moc, goc_thang


def bao_cao() -> str:
    """In bảng kết quả cho báo cáo. Không phải bài kiểm, chỉ để đọc."""
    d = []
    d.append("Bộ lọc tiên đoán đã nối vào loc_nd38.py: "
             + ("CÓ (dict CAM)" if CAM_DA_NOI else "CHƯA — dùng bản chép từ HD-10 §6"))
    d.append(f"Số luật đang xét: Tầng A {len(L.TANG_A)} · tiên đoán {len(CAM_DANG_DUNG)}\n")

    d.append("MẪU HỎNG — phải bắt được cả 14\n")
    d.append("| # | Câu | Vi phạm | Bắt? | Luật bắt |")
    d.append("|---|---|---|---|---|")
    lot = 0
    for i, c, v in MAU_HONG:
        r = bat(c)
        if not r:
            lot += 1
        d.append(f"| {i} | {c} | {v} | {'✅' if r else '❌ LỌT'} | {', '.join(r) or '—'} |")

    d.append("\nMẪU TỐT — phải không bắt câu nào\n")
    d.append("| # | Câu | Bẫy | Bắt nhầm? | Luật bắt nhầm |")
    d.append("|---|---|---|---|---|")
    nham = 0
    for i, c, v in MAU_TOT:
        r = bat(c)
        if r:
            nham += 1
        d.append(f"| {i} | {c} | {v} | {'❌ NHẦM' if r else '✅'} | {', '.join(r) or '—'} |")

    d.append(f"\n**TỔNG: bắt {len(MAU_HONG)-lot}/{len(MAU_HONG)} câu hỏng · "
             f"bắt nhầm {nham}/{len(MAU_TOT)} câu tốt**")
    return "\n".join(d)


if __name__ == "__main__":
    if "--bao-cao" in sys.argv:
        if "--baseline" in sys.argv:                      # ép chạy bộ lọc CŨ
            globals()["bat"] = bat_theo_baseline
            globals()["CAM_DA_NOI"] = False
            globals()["CAM_DANG_DUNG"] = BASELINE_HD10
        print(bao_cao())
    else:
        unittest.main()
