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
"""loc_nd38.py — Rà 142 khối nội dung theo bộ lọc hai tầng §7.3.

Tầng A: cấm mọi nơi → phải sửa, kể cả bản nội bộ.
Tầng B: được trong tư vấn riêng, cấm trong nội dung công khai
        → giữ ở bản nội bộ, gỡ ở bản public.

Script CHỈ BÁO CÁO, không tự sửa. Sửa là việc của người.
"""
import json, re, sys
from collections import defaultdict

# ── Tầng A — cấm mọi nơi
TANG_A = {
    "chữa bệnh": r"chữa\s+(bệnh|khỏi)",
    "trị bệnh": r"\btrị\s+(bệnh|liệu|dứt)",
    "điều trị": r"điều\s+trị",
    "khỏi bệnh": r"khỏi\s+(bệnh|hẳn)",
    "thay thế bác sĩ": r"thay\s+(thế\s+)?(bác\s*sĩ|thuốc)",
    "bỏ thuốc": r"\bbỏ\s+thuốc\b",
    "chẩn đoán": r"chẩn\s+đoán",
    "GÂY RA bệnh": r"gây\s+(ra\s+)?(bệnh|ung thư|suy)",
    "tiên đoán tương lai": r"tiên\s+đoán",
    "số mệnh đã định": r"số\s+mệnh\s+đã\s+định",
    "chắc chắn bạn sẽ": r"chắc\s+chắn\s+(bạn|anh|chị)\s+sẽ",
    "100% chính xác": r"(100%|đúng\s+tuyệt\s+đối)",
    # "ấm cúng" KHÔNG phải cúng bái — phải bắt cụm, không bắt tiếng lẻ
    "cúng giải hạn": r"(cúng\s*(bái|sao|lễ)|đi\s+cúng|lễ\s+cúng|đeo\s+bùa|bùa\s*(chú|hộ)|giải\s+hạn|vật\s+phẩm\s+đổi\s+vận)",
    "chỉ số cơ thể": r"(huyết\s+áp|đường\s+huyết|cân\s+nặng\s+giảm)",
}

# ── Tầng B — chỉ gỡ ở bản public
TANG_B = {
    "hoá giải": r"ho[áa]\s+giải",
    "bệnh / bệnh tật": r"\bbệnh\b",
    "miễn dịch": r"miễn\s+dịch",
    "triệu chứng": r"triệu\s+chứng",
    # nghĩa bóng "sức khoẻ của tập thể" không phải claim y tế → cần người xét
    "sức khoẻ (cần người xét)": r"sức\s+kho[ẻe]",
    "tuyến nội tiết": r"tuyến\s+(yên|giáp|tùng|thượng\s+thận|tuỵ|ức)",
    # "cẩn thận" chứa "thận", "buồng gan" hiếm — phải loại từ ghép
    "cơ quan cơ thể": r"(?<!cẩn )(?<!thân )\b(quả\s+thận|lá\s+gan|dạ\s+dày|túi\s+mật|chức\s+năng\s+(gan|thận))\b",
}

# ── Tầng tiên đoán — bốn điều cấm của HD-10 §4, áp cho tầng năm/tháng/ngày
#
# Năm mẫu cũ chỉ nằm trên giấy trong HD-10 §6, chưa bao giờ nối vào code.
# Bài kiểm test_loc_tien_doan.py cho thấy chúng bắt 7/14 câu hỏng và bắt
# nhầm 3/10 câu tốt. Bộ dưới đây thay chúng, bắt theo MẪU chứ không theo
# nguyên văn câu, nên bắt được cả biến thể chưa có trong bài kiểm.
CAM = {
    # HD-10 §4.1 — A person + will + a verb of misfortune. Bare "gặp" is
    # innocent ("anh chị sẽ gặp nhiều người mới"), so it counts only when a
    # misfortune noun follows it. This is what the old pattern got wrong.
    "phán biến cố":
        r"(?:bạn|anh|chị|em|con|cháu|vợ|chồng|cô|chú|bác)\s+"
        r"(?:sẽ|sắp|rồi\s+sẽ|thể\s+nào\s+cũng)\s+"
        r"(?:bị\b|mất\b|cãi\b|đổ\s+vỡ|chia\s+tay|ly\s+(?:hôn|dị|thân)|phá\s+sản|"
        r"vỡ\s+nợ|thất\s+nghiệp|đổ\s+bệnh|ốm\b|"
        r"gặp\s+(?:hạn|nạn|xui|rắc\s+rối|tai|chuyện|biến|hoạ|họa))",

    # HD-10 §4.4 — Vocabulary of loss is banned outright, subject or not:
    # "Tháng này dễ mất việc" names no one yet still pronounces a verdict.
    # Variants matter: ly hôn / ly dị / ly thân are the same claim.
    # NAMING a hazard is fine ("phát hiện lỗ hổng trước khi nó thành tai nạn");
    # PREDICTING one for the reader is not. So tai nạn / tai hoạ / hoạn nạn
    # count only behind a word that turns them into a forecast or a warning.
    "phán mất mát":
        r"(?:mất\s+(?:việc|nghề|nhà|của|mạng|người)|mất\s+mát|thất\s+nghiệp|"
        r"phá\s+sản|vỡ\s+nợ|ly\s+(?:hôn|dị|thân)|chia\s+tay|tan\s+vỡ|bệnh\s+tật|"
        r"(?:coi\s+chừng|cẩn\s+thận|đề\s+phòng|dễ|khó\s+tránh|sẽ|gặp|bị|gặp\s+phải)"
        r"[^.;!?]{0,20}?(?:tai\s+nạn|tai\s+ho[aạ]|tai\s+ương|hoạn\s+nạn))",

    # HD-10 §4.1 — A calendar date pinned to a misfortune, in EITHER order,
    # inside one clause. "Coi chừng tai nạn quanh ngày 20" puts the event
    # first; the old pattern only looked for date-then-event.
    # Clause is bounded by . ; ! ? so the two halves must really belong together.
    "hẹn ngày cho biến cố":
        r"(?:(?:ngày|hôm|mùng|mồng)\s+\d{1,2}\b[^.;!?]{0,45}?"
        r"(?:\bbị\b|\bmất\b|\bhạn\b|\bnạn\b|\bxui\b|\bkỵ\b|\bhung\b|lừa|rắc\s+rối|kiện\s+tụng)"
        r"|(?:\bbị\b|\bmất\b|\bhạn\b|\bnạn\b|\bxui\b|\bkỵ\b|tai\s+nạn|lừa|rắc\s+rối|kiện\s+tụng)"
        r"[^.;!?]{0,45}?(?:ngày|hôm|mùng|mồng)\s+\d{1,2}\b)",

    # HD-10 §4.3 — Day-picking language. "ngày đẹp" alone is ordinary Vietnamese
    # ("hôm nào trời đẹp, ngày đẹp thì đi bộ"), so it is caught only when a
    # verb of CHOOSING a day precedes it. "xấu / kỵ / hung / cát / lành" after
    # "ngày" is always day-picking, whatever word sits between.
    "ngôn ngữ xem ngày":
        r"(?:ngày\s+(?:\S+\s+)?(?:xấu|kỵ|hung|cát|lành)\b|"
        r"(?:chọn|xem|coi|kén|tìm|nhờ\s+xem)\s+(?:được\s+)?ngày\s+(?:đẹp|tốt|lành)|"
        r"ngày\s+lành\s+tháng\s+tốt|"
        r"kiêng\s+(?:kỵ|kị|cữ|ký|làm|khởi|động|xuất|đi|ăn\s+nói)|\bđại\s+kỵ\b)",

    # HD-10 §4.2 — The vocabulary of fate: hạn, xui, tam tai, sao chiếu.
    # Guarded by _la_noi_ve_chu() so that TALKING ABOUT the word ("cảm giác
    # xui xẻo mà nhiều người mô tả") is not read as ASSERTING it.
    "chữ hạn / xui":
        r"(?:gặp\s+hạn|vận\s+hạn|đại\s+hạn|năm\s+hạn|tháng\s+hạn|hạn\s+nặng|"
        r"tam\s+tai|tai\s+ương|\bxui\b|đen\s+đủi|vận\s+đen)",

    # HD-10 §4.3 + §4.2 — Astrology-of-fate register borrowed from tử vi:
    # a star "shining on" someone, or a ritual that changes one's luck.
    "ngôn ngữ tử vi":
        r"(?:sao\s+(?:xấu|tốt|hạn|chiếu)|sao\s+\S+\s+chiếu|chiếu\s+mệnh|"
        r"thái\s+bạch|kim\s+lâu|la\s+hầu|ngũ\s+quỷ|"
        r"nhẹ\s+vận|đổi\s+vận|giải\s+vận|cải\s+vận|nặng\s+vía|động\s+thổ)",

    # HD-10 §3 — Certainty about the future. Keeps the old rule but adds the
    # everyday Vietnamese equivalents of "chắc chắn".
    # \b after the alternation is load-bearing: without it "là" matched the
    # first two letters of "làm", flagging "cái mình chắc chắn làm được".
    "chắc chắn sẽ":
        r"(?:chắc\s+chắn|nhất\s+định|thế\s+nào\s+cũng|kiểu\s+gì\s+cũng|không\s+thể\s+tránh)"
        r"\s+(?:bạn|anh|chị|em)?\s*(?:sẽ|cũng|là)\b",
}

# ── Lộ trạng thái nội bộ — cấm trên trang khách
#
# Ngày 29/08/2026 phát hiện câu "Nút Bắc đang dùng chế độ TRUE NODE — điểm còn
# treo, chưa đối chiếu nguồn ngoài" hiện trên trang kết quả của khách, dưới
# tiêu đề "Ghi chú kỹ thuật cho người luận". Câu đó vừa sai (đối chiếu đã xong
# từ 28/08) vừa gieo nghi ngờ vào chính bản đồ khách vừa nhận.
#
# Bộ lọc Tầng A và tầng tiên đoán không bắt được nó: nó không phải claim y tế,
# cũng không phải lời phán. Nó là một loại rò rỉ khác — phòng máy nói vọng ra
# phòng khách. Nên cần nhóm luật riêng.
LO_NOI_BO = {
    # Project status leaking into customer-facing copy.
    #
    # "chưa" phải đi với một việc KIỂM CHỨNG mới tính. Kho nội dung có đầy câu
    # như "bạn nói khi chưa ai sẵn sàng nghe" hay "người có tài mà chưa ai
    # biết" — đó là văn cho khách, không phải trạng thái dự án.
    # KHÔNG bắt "chưa hoàn thiện": Cổng 18 vốn là "bản năng phát hiện chỗ chưa
    # hoàn thiện" — văn cho khách, không phải trạng thái dự án.
    "còn treo / chưa kiểm chứng":
        r"(còn\s+treo|điểm\s+(còn\s+)?treo|"
        r"chưa\s+(ai\s+)?(kiểm\s*(chứng|tra)?|rà\b|đối\s+chiếu|xác\s+minh|thẩm\s+định)|"
        r"\bchưa\s+xong\b|"
        r"đang\s+thử\s+nghiệm|bản\s+thử\b|bản\s+nháp|\bTODO\b|\bFIXME\b)",

    # Internal document numbering and phase names: HD-07, "Giai đoạn 0".
    "số hiệu tài liệu / giai đoạn":
        r"(\bHD-\d{2}\b|[Gg]iai\s+đoạn\s+\d)",

    # Source file and identifier names have no business on a customer page.
    "tên file mã / hằng số":
        r"([a-z_]{3,}\.(?:py|json|sh|conf|service)\b|\b(?:NODE_MODE|CONTENT|CONG_TY|TANG_[AB])\b)",

    # Copy addressed to the practitioner or to Thầy, not to the reader.
    "viết cho người trong nhà":
        r"(người\s+luận|bản\s+nội\s+bộ|\bThầy\b|ghi\s+chú\s+kỹ\s+thuật)",
}


# Luật nào cần xét "đang NÓI VỀ chữ đó" hay "đang KHẲNG ĐỊNH điều đó".
# Chỉ áp cho luật từ vựng thuần, KHÔNG áp cho luật phán biến cố — nếu áp
# rộng thì "nhiều người nói tháng này bạn sẽ mất việc" sẽ lọt.
CAN_XET_META = {"chữ hạn / xui"}


def _di(nhan, duong, val):
    """Đi đệ quy qua mọi trường, không bỏ sót trường mới thêm vào sau này."""
    if isinstance(val, str):
        yield nhan, duong, val
    elif isinstance(val, dict):
        for k, v in val.items():
            yield from _di(nhan, f"{duong}.{k}", v)
    # TUPLE phải có ở đây: content_transit.NEN_TRANH lưu bằng tuple, thiếu
    # nhánh này thì cả kho tầng tháng bị bỏ qua im lặng mà vẫn báo "sạch".
    elif isinstance(val, (list, tuple)):
        for i, v in enumerate(val):
            yield from _di(nhan, f"{duong}[{i}]", v)


def duyet(C):
    """Quét TOÀN BỘ cây nội dung. Bỏ qua trường thuần dữ liệu, không phải văn."""
    BO_QUA = {"name_en", "chu_han", "muc_khop", "que_so", "gates", "centers",
              "mach", "priority", "lines", "id"}
    nhan_phan = {"types": "Type", "authorities": "Authority", "profiles": "Profile",
                 "centers": "Trung tâm", "gates": "Cổng", "channels": "Kênh"}
    for phan, nhan in nhan_phan.items():
        for k, v in C.get(phan, {}).items():
            for truong, val in v.items():
                if truong in BO_QUA:
                    continue
                yield from _di(f"{nhan} {k}", f"{phan}.{k}.{truong}", val)


# Câu khuyên đi khám cũng chứa chữ "thay bác sĩ" — không được tính là vi phạm.
PHU_DINH = re.compile(r"(đừng|không|chớ|chẳng|kh\u00f4ng\s+thay\s+thế)")


def _la_phu_dinh(low: str, vi_tri: int) -> bool:
    """Nhìn lui 45 ký tự: nếu có từ phủ định thì đây là câu cảnh báo, không phải claim."""
    return bool(PHU_DINH.search(low[max(0, vi_tri - 45):vi_tri]))


# Nói VỀ một chữ khác với KHẲNG ĐỊNH chữ đó. "Cảm giác xui xẻo mà nhiều
# người mô tả thường chỉ là mệt tích tụ" là câu giải thích, không phải câu
# phán. Chỉ dùng cho các luật trong CAN_XET_META.
NOI_VE_CHU = re.compile(
    r"(cảm\s+giác|cảm\s+tưởng|gọi\s+là|cái\s+gọi\s+là|khái\s+niệm|quan\s+niệm|"
    r"dân\s+gian|chữ\s|nhiều\s+người\s+(nói|gọi|mô\s+tả|tin|hay)|"
    r"người\s+ta\s+(hay\s+)?(nói|gọi|bảo|tin)|thường\s+(nói|gọi))")


def _la_noi_ve_chu(low: str, vi_tri: int) -> bool:
    """Nhìn lui 30 ký tự: có dấu hiệu đang bàn về chữ đó thì không tính vi phạm."""
    return bool(NOI_VE_CHU.search(low[max(0, vi_tri - 30):vi_tri]))


def vi_pham(van: str) -> list[tuple[str, str, str]]:
    """Rà MỘT đoạn văn. Trả về [(tầng, tên luật, đoạn trích)].

    Đây là đường chạy duy nhất cho cả ba nơi dùng: kho nội dung bản đồ sinh,
    tầng năm/tầng tháng, và bài kiểm test_loc_tien_doan.py. Một đường thôi —
    để không tái diễn cảnh bài kiểm kiểm một bộ luật, hàng thật chạy bộ khác.
    """
    low = van.lower()
    ra = []
    for nhan, nhom in (("A", TANG_A), ("tiên đoán", CAM)):
        for ten, pat in nhom.items():
            for m in re.finditer(pat, low):
                if _la_phu_dinh(low, m.start()):
                    continue
                if ten in CAN_XET_META and _la_noi_ve_chu(low, m.start()):
                    continue
                ra.append((nhan, ten, van[max(0, m.start() - 45):m.end() + 45]))
                break
    return ra


def quet(C):
    a, b = defaultdict(list), defaultdict(list)
    for khoi, duong, van in duyet(C):
        low = van.lower()
        for ten, pat in TANG_A.items():
            for m in re.finditer(pat, low):
                if _la_phu_dinh(low, m.start()):
                    continue
                a[ten].append((khoi, duong, van[max(0, m.start()-45):m.end()+45]))
        for ten, pat in TANG_B.items():
            for m in re.finditer(pat, low):
                b[ten].append((khoi, duong, van[max(0, m.start()-45):m.end()+45]))
    return a, b


# ── Tầng thời gian — văn SINH RA LÚC CHẠY, không nằm trong hd-content-v1.json
#
# Kho nội dung bản đồ sinh nằm sẵn trong JSON nên rà thẳng được. Tầng năm và
# tầng tháng thì khác: câu chữ được ghép lúc chạy từ khuôn trong luan_*.py
# cộng với kho trong content_*.py. Muốn rà thì phải DỰNG BÀI THẬT rồi rà văn
# đã ghép — rà riêng kho tĩnh sẽ bỏ sót đúng những câu do khuôn sinh ra.

# Tám ca dựng, đủ năm loại năng lượng, trải từ 1958 tới 1998, cả hai miền.
#
# Nhãn chứ không phải tên người: đây là mã nguồn công khai theo AGPL, mà ngày
# giờ nơi sinh của một người có thật là dữ liệu cá nhân theo NĐ 13/2023. Hai ca
# trùng bộ 50 thì dùng luôn nhãn của bo_50_chart.py để đối chiếu chéo được.
NGUOI_MAU = [
    ("TK-06", dict(nam=1985, thang=3,  ngay=15, gio=7,  phut=30)),          # = bo_50 TK-06
    ("TK-04", dict(nam=1968, thang=12, ngay=25, gio=4,  phut=20, mien="nam")),  # = bo_50 TK-04
    ("CA-01", dict(nam=1972, thang=7,  ngay=4,  gio=19, phut=5,  mien="bac")),
    ("CA-02", dict(nam=1990, thang=11, ngay=9,  gio=13, phut=45)),
    ("CA-03", dict(nam=1998, thang=2,  ngay=28, gio=23, phut=10)),
    ("CA-04", dict(nam=1958, thang=9,  ngay=17, gio=6,  phut=0,  mien="bac")),
    ("CA-05", dict(nam=1979, thang=5,  ngay=22, gio=11, phut=15, mien="nam")),
    ("CA-06", dict(nam=1993, thang=8,  ngay=1,  gio=2,  phut=50)),
]
THANG_MAU = [(2026, 9), (2026, 10), (2026, 11), (2026, 12)]

# Mốc đời phụ thuộc năm sinh, nên tám người trên chỉ ra 80 bản luận — chưa
# phủ nổi con số 214 mà HD-10 §6 khai. Thêm người sinh rải đều 1952–2002 để
# vượt 214, và để chạm đủ 4 khoá mốc × 9 trung tâm.
NGUOI_MAU_MOC = [
    (f"MOC-{i+1:02d}", dict(nam=n, thang=(i % 12) + 1, ngay=(i * 7 % 27) + 1,
                              gio=(i * 5) % 24, phut=(i * 13) % 60,
                              mien="bac" if i % 2 else "nam"))
    for i, n in enumerate(range(1952, 2003, 3))
]


PHU_MOC = set()   # (khoá mốc, trung tâm) đã chạm — để biết panel phủ tới đâu


def van_tang_thoi_gian():
    """Sinh (nhãn, đường, văn) cho mọi câu của tầng năm và tầng tháng.

    Đi đệ quy qua dict trả về, không liệt kê tên trường — đúng bài học lỗi
    thứ sáu ở HD-11 §7: bộ lọc bỏ sót trường mới thêm rồi báo 'sạch'.
    """
    import hd_engine as E
    import moc_doi as M
    import luan_moc_doi as LM
    import luan_transit_thang as LT
    from content_transit import NEN_TRANH
    from content_moc_doi import MOC_DOI, LINH_VUC_THEO_TRUNG_TAM

    with open("hd-content-public.json", encoding="utf-8") as f:
        kho = json.load(f)["gates"]

    # 1. Kho tĩnh của hai tầng
    yield from _di("content_transit.NEN_TRANH", "NEN_TRANH", NEN_TRANH)
    yield from _di("content_moc_doi.MOC_DOI", "MOC_DOI", MOC_DOI)
    yield from _di("content_moc_doi.LINH_VUC", "LINH_VUC", LINH_VUC_THEO_TRUNG_TAM)
    yield from _di("luan_transit_thang.THEO_TYPE", "THEO_TYPE", LT.THEO_TYPE)

    # 2. Bài tháng thật, ghép xong — 8 người × 4 tháng
    for ten, args in NGUOI_MAU:
        c = E.build_chart(**args)
        for nam, thang in THANG_MAU:
            b = LT.bai_thang(c, nam, thang, kho)
            yield from _di(f"lời theo Type {ten} {thang:02d}/{nam}",
                           f"transit.{ten}.{thang:02d}{nam}.type", b["loi_theo_type"])
            for i, cs in enumerate(b["cua_so"]):
                yield from _di(f"cửa sổ {ten} {thang:02d}/{nam} #{i+1}",
                               f"transit.{ten}.{thang:02d}{nam}.{i}", cs)

    # 3. Ghép đủ 4 khoá mốc × 9 trung tâm bằng mốc dựng tay.
    #    Người sinh thật hiếm khi có mốc rơi vào trung tâm Đầu (chỉ 3 cổng),
    #    nên lấy mẫu bao nhiêu người cũng hụt vài tổ hợp. Dựng thẳng cho đủ.
    from datetime import datetime
    cong_theo_tt = {}
    for g, tt in E.GATE_CENTER.items():
        cong_theo_tt.setdefault(tt, g)
    for khoa in MOC_DOI:
        for tt, g in cong_theo_tt.items():
            m = {"khoa": khoa, "cong": g, "hao": 3, "so_lan_cham": 3,
                 "bat_dau": datetime(2027, 1, 1), "ket_thuc": datetime(2027, 10, 1),
                 "tuoi_bat_dau": 42, "tuoi_ket_thuc": 43, "keo_dai_thang": 9}
            b = LM.luan_mot_moc(m, kho.get(str(g), {}).get("name_vi", f"cổng {g}"))
            PHU_MOC.add((khoa, b["trung_tam"]))
            yield from _di(f"mốc dựng tay · {khoa} × {b['trung_tam']}",
                           f"moc_doi.ghep.{khoa}.{tt}", b)

    # 4. Bản luận mốc đời thật — panel rộng hơn để vượt 214 bản
    for ten, args in NGUOI_MAU + NGUOI_MAU_MOC:
        c = E.build_chart(**args)
        for m in M.moc_doi(c):
            ten_cong = kho.get(str(m["cong"]), {}).get("name_vi", f"cổng {m['cong']}")
            b = LM.luan_mot_moc(m, ten_cong)
            PHU_MOC.add((m["khoa"], b["trung_tam"]))
            yield from _di(f"mốc đời {ten} · {m['khoa']}",
                           f"moc_doi.{ten}.{m['khoa']}.{m['tuoi_bat_dau']}", b)


def van_trang_khach():
    """Sinh (nhãn, đường, văn) cho CHỮ KHÁCH THẬT SỰ ĐỌC trên từng trang.

    Rà mã nguồn không đủ: chữ trên trang được ghép lúc chạy từ nhiều nguồn —
    chuỗi viết cứng trong `app.py`/`render_chart.py`, kho JSON, và
    `noi_dung_phap_ly.py`. Nên dựng trang thật rồi bóc chữ ra khỏi thẻ HTML.

    Chạy ở chế độ BAN=public, đúng như bản đang phục vụ khách.
    """
    import os
    os.environ["BAN"] = "public"
    os.environ["GOC"] = "/human-design"
    import hd_engine as E
    import app as A
    import render_chart as RC

    with open("hd-content-public.json", encoding="utf-8") as f:
        kho = json.load(f)

    trang = [
        ("trang chủ / form", A.form_html()),
        ("/rieng-tu", A.trang_rieng_tu()),
        ("/ve-human-design", A.trang_gioi_thieu()),
        ("/ma-nguon", A.trang_ma_nguon()),
    ]
    # Trang kết quả — cả ca không cảnh báo lẫn ba ca có cảnh báo thật
    CA = [
        ("kết quả · bình thường", dict(nam=1985, thang=3, ngay=15, gio=7, phut=30)),
        ("kết quả · giờ chưa chắc", dict(nam=1985, thang=3, ngay=15, gio=7, phut=30,
                                        gio_chac_chan=False)),
        ("kết quả · trước 1975 chưa chọn miền", dict(nam=1970, thang=5, ngay=1, gio=12, phut=0)),
        ("kết quả · trước 1955", dict(nam=1950, thang=5, ngay=5, gio=12, phut=0, mien="bac")),
    ]
    for nhan, kw in CA:
        trang.append((nhan, RC.render(E.build_chart(**kw), "TK-06", kho)))

    for nhan, html in trang:
        yield nhan, f"trang.{nhan}", _chu_thay_duoc(html)


def _chu_thay_duoc(html: str) -> str:
    """Bóc chữ khách đọc ra khỏi thẻ HTML. Bỏ hẳn <style> và <script>."""
    t = re.sub(r"<(style|script)\b.*?</\1>", " ", html, flags=re.S | re.I)
    t = re.sub(r"<[^>]+>", " ", t)
    t = (t.replace("&nbsp;", " ").replace("&amp;", "&")
          .replace("&lt;", "<").replace("&gt;", ">").replace("&#39;", "'"))
    return re.sub(r"\s+", " ", t)


def ra_trang_khach():
    """Rà chữ trên trang khách: Tầng A · tầng tiên đoán · lộ trạng thái nội bộ."""
    dinh = defaultdict(list)
    so = 0
    for nhan, duong, van in van_trang_khach():
        so += 1
        for tang, ten, trich in vi_pham(van):
            dinh[f"{tang}:{ten}"].append((nhan, trich))
        # LO_NOI_BO khớp trên chữ GỐC, không hạ thường: "HD-09", "Thầy" và tên
        # hằng viết hoa sẽ lọt hết nếu hạ thường trước rồi mới so.
        for ten, pat in LO_NOI_BO.items():
            for m in re.finditer(pat, van, re.IGNORECASE):
                dinh[f"lộ nội bộ:{ten}"].append(
                    (nhan, van[max(0, m.start() - 50):m.end() + 50]))

    print("═" * 62)
    print("TRANG KHÁCH — chữ khách thật sự đọc")
    print("═" * 62)
    print(f"Rà {so} trang, chế độ BAN=public\n")
    if not dinh:
        print("  ✅ Không trang nào dính Tầng A, tầng tiên đoán, hay lộ trạng thái nội bộ.")
        return 0
    for ten, ds in sorted(dinh.items(), key=lambda x: -len(x[1])):
        print(f"\n  🔴 {ten} — {len(ds)} chỗ")
        for nhan, trich in ds[:5]:
            print(f"     {nhan}")
            print(f"       …{trich.strip()}…")
        if len(ds) > 5:
            print(f"     … và {len(ds)-5} chỗ nữa")
    return sum(len(v) for v in dinh.values())


def ra_tang_thoi_gian():
    """Rà tầng năm + tầng tháng bằng vi_pham(). In ra mọi chỗ dính."""
    dinh = defaultdict(list)
    so_cua_so = so_moc = so_cau = 0
    for nhan, duong, van in van_tang_thoi_gian():
        so_cau += 1
        if duong.startswith("transit.") and duong.endswith(".chu_de"):
            so_cua_so += 1
        if duong.startswith("moc_doi.") and duong.endswith(".du_kien"):
            so_moc += 1
        for tang, ten, trich in vi_pham(van):
            dinh[f"{tang}:{ten}"].append((nhan, duong, trich))

    print("═" * 62)
    print("TẦNG THỜI GIAN — tầng năm + tầng tháng")
    print("═" * 62)
    print(f"Rà {so_cua_so} cửa sổ tháng · {so_moc} bản luận mốc đời · {so_cau} câu")
    print(f"Phủ {len(PHU_MOC)}/36 tổ hợp mốc đời (4 khoá × 9 trung tâm)\n")
    if not dinh:
        print("  ✅ Không câu nào dính Tầng A hay tầng tiên đoán.")
        return 0
    for ten, ds in sorted(dinh.items(), key=lambda x: -len(x[1])):
        print(f"\n  🔴 {ten} — {len(ds)} chỗ")
        for nhan, duong, trich in ds[:6]:
            print(f"     {nhan} ({duong})")
            print(f"       …{trich.strip()}…")
        if len(ds) > 6:
            print(f"     … và {len(ds)-6} chỗ nữa")
    return sum(len(v) for v in dinh.values())


if __name__ == "__main__":
    C = json.load(open("hd-content-v1.json", encoding="utf-8"))
    tong = sum(len(C[k]) for k in ("types", "authorities", "profiles", "centers", "gates", "channels"))
    a, b = quet(C)

    print(f"Rà {tong} mục nội dung\n")
    print("═" * 62)
    print("TẦNG A — PHẢI SỬA, kể cả bản nội bộ")
    print("═" * 62)
    if not a:
        print("  ✅ Sạch. Không mục nào dính từ Tầng A.\n")
    else:
        for ten, ds in sorted(a.items(), key=lambda x: -len(x[1])):
            print(f"\n  🔴 {ten} — {len(ds)} chỗ")
            for khoi, duong, trich in ds[:4]:
                print(f"     {khoi} ({duong})")
                print(f"       …{trich.strip()}…")

    print("\n" + "═" * 62)
    print("TẦNG B — giữ bản nội bộ, GỠ ở bản public")
    print("═" * 62)
    if not b:
        print("  ✅ Không mục nào dùng tới Tầng B.")
    else:
        for ten, ds in sorted(b.items(), key=lambda x: -len(x[1])):
            khoi_rieng = sorted({k for k, _, _ in ds})
            print(f"\n  🟡 {ten} — {len(ds)} chỗ, {len(khoi_rieng)} khối")
            print(f"     {', '.join(khoi_rieng[:9])}{' …' if len(khoi_rieng) > 9 else ''}")
            for khoi, duong, trich in ds[:2]:
                print(f"       …{trich.strip()}…")

    print()
    if a:
        print(f"⛔ Còn {sum(len(v) for v in a.values())} chỗ Tầng A phải sửa trước khi dùng ở BẤT KỲ đâu.")
        sys.exit(1)
    print(f"✅ Tầng A sạch. Tầng B: {sum(len(v) for v in b.values())} chỗ cần gỡ khi làm bản public.")

    # Tầng năm + tầng tháng. Chạy mặc định — để không ai quên như lần trước.
    if "--chi-ban-do" in sys.argv:
        sys.exit(0)
    print()
    hong = ra_tang_thoi_gian()
    print()
    hong += ra_trang_khach()
    if hong:
        print("\n⛔ Còn chỗ dính — phải sửa TRƯỚC khi đẩy lên VPS.")
        sys.exit(1)
