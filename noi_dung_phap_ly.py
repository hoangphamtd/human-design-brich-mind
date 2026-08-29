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
"""noi_dung_phap_ly.py — Trang chính sách riêng tư và trang giới thiệu hệ thống.

Bắt buộc: tên công ty và một kênh liên hệ — đã có sẵn.
Mã số thuế và địa chỉ trụ sở KHÔNG bắt buộc cho trang công cụ miễn phí.
Chúng là yêu cầu của NĐ 52/2013 áp cho trang có thu tiền trực tiếp.
Muốn thêm thì điền vào CONG_TY, trang tự hiện thêm dòng.
"""

CONG_TY = {
    "ten": "CÔNG TY TNHH B-RICH",
    "zalo": "0339057793",
    "web": "brichmind.com",
    # Không bắt buộc. Để trống thì trang tự bỏ dòng đó đi.
    # Chỉ cần khi trang này có thu tiền trực tiếp (NĐ 52/2013 về thương mại điện tử).
    "mst": "",
    "dia_chi": "",
    "email": "",
}

RIENG_TU = """
# Chính sách riêng tư

*Áp dụng cho công cụ Bản đồ năng lượng tại {web}/human-design*

## Chúng tôi thu thập gì

Để dựng được bản đồ, công cụ cần **ngày sinh, giờ sinh và nơi sinh** của bạn.
Tên bạn nhập chỉ dùng để hiển thị trên trang kết quả.

Theo Nghị định 13/2023/NĐ-CP, ngày sinh và nơi sinh là **dữ liệu cá nhân cơ bản**.
Chúng tôi coi trọng điều đó.

## Chúng tôi làm gì với dữ liệu đó

Tính ra bản đồ rồi hiển thị lên màn hình cho bạn xem. Hết.

**Chúng tôi không lưu.** Dữ liệu bạn nhập chỉ nằm trong bộ nhớ máy chủ trong
vài giây lúc tính toán, rồi mất đi. Đóng trang là không còn dấu vết nào.

Nghĩa là chúng tôi cũng không tra lại được bản đồ cũ của bạn. Muốn giữ thì bạn
tự bấm In hoặc Lưu PDF ngay trên trang kết quả.

## Khi nào chúng tôi mới lưu

Chỉ khi bạn **chủ động để lại** số điện thoại hoặc email, ví dụ khi nhận tài liệu
hoặc đăng ký tư vấn. Lúc đó chúng tôi sẽ nói rõ ngay tại chỗ bạn nhập, và bạn
tự quyết định có để lại hay không.

## Chúng tôi không chia sẻ với ai

Không bán, không trao đổi, không chuyển dữ liệu của bạn cho bên thứ ba vì mục
đích thương mại.

Công cụ có dùng phông chữ của Google Fonts nên trình duyệt của bạn sẽ kết nối
tới máy chủ Google khi tải trang. Chúng tôi không gửi dữ liệu sinh của bạn qua đó.

## Quyền của bạn

Theo Nghị định 13/2023, bạn có quyền được biết, rút lại đồng ý, xoá dữ liệu,
hạn chế hoặc phản đối việc xử lý, yêu cầu cung cấp dữ liệu, và khiếu nại.

Vì chúng tôi không lưu gì khi bạn chỉ xem bản đồ, nên phần lớn các quyền này
không phát sinh. Nếu bạn đã để lại số điện thoại hoặc email và muốn chúng tôi
xoá đi, chỉ cần nhắn Zalo {zalo} — chúng tôi xoá trong vòng 72 giờ và báo lại.

## Trẻ dưới 16 tuổi

Công cụ này dành cho người từ 16 tuổi trở lên. Người dưới 16 tuổi cần có sự
đồng ý của cha mẹ hoặc người giám hộ trước khi nhập dữ liệu.

## Về nội dung bản đồ

Human Design là hệ thống chiêm nghiệm mang tính biểu tượng, không phải khoa học
y học hay tâm lý học lâm sàng. Nội dung tại đây nhằm mục đích tham khảo và khám
phá bản thân, không phải chẩn đoán, điều trị, hay lời khuyên y tế, tài chính,
pháp lý. Bạn là người quyết định cuối cùng cho cuộc đời mình.

## Liên hệ

{khoi_lien_he}

*Chính sách này có thể được cập nhật. Bản mới nhất luôn nằm tại trang này.*
"""

VE_HE_THONG = """
# Về Human Design

## Nó là gì

Human Design là hệ thống do Ra Uru Hu công bố năm 1987, ghép bốn nguồn có sẵn
từ trước: Kinh Dịch với 64 quẻ, chiêm tinh nhiệt đới, Kabbalah, và hệ luân xa
Ấn Độ. Đầu ra là một biểu đồ cố định suốt đời, suy ra từ ngày, giờ và nơi sinh
của bạn.

## Phần nào chính xác, phần nào không

Chúng tôi tách bạch hai phần, vì chúng rất khác nhau:

**Phần tính toán là khách quan.** Vị trí các thiên thể tại thời điểm bạn sinh
được tính bằng thuật toán thiên văn tiêu chuẩn, sai số dưới một giây cung. Ai
tính cũng ra kết quả như nhau. Phần này kiểm chứng được.

**Phần diễn giải thì không.** Việc gán ý nghĩa cho từng cổng, từng kênh, từng
trung tâm là hệ biểu tượng. Không có nghiên cứu khoa học nào chứng minh giá trị
dự báo của nó. Chúng tôi không nói ngược lại điều đó.

Nên hãy đọc bản đồ này như một tấm gương để soi, không phải như một kết luận về
bạn. Chỗ nào đúng thì giữ, chỗ nào không đúng thì bỏ. Bạn là người kiểm nghiệm
cuối cùng trên chính đời mình.

## Vì sao giờ sinh quan trọng đến vậy

Bản đồ đổi theo từng khoảng hai giờ đồng hồ. Lệch một giờ có thể đổi Profile,
đôi khi đổi cả cách bạn ra quyết định. Nếu bạn không nhớ chính xác, hãy đánh
dấu ô đó — trang kết quả sẽ ghi rõ cảnh báo, và bạn nên dựng thêm vài mốc giờ
để so trước khi tin.

## Một điều riêng cho người Việt

Miền Bắc và miền Nam Việt Nam từng dùng **hai múi giờ khác nhau**, lệch nhau
một giờ, suốt từ đầu năm 1960 tới ngày 13 tháng 6 năm 1975. Phần lớn công cụ
Human Design nước ngoài không biết chuyện này nên tính sai cho người Việt sinh
trong giai đoạn đó.

Công cụ của chúng tôi có hỏi bạn sinh miền nào, và áp đúng múi giờ từng miền.

## Nội dung do ai viết

Toàn bộ phần mô tả trên trang này do B-RICH MIND biên soạn bằng tiếng Việt,
không dịch từ nguồn nào. Chúng tôi có tham khảo hệ thống của Jovian Archive và
các tài liệu Human Design quốc tế để nắm cơ học, nhưng câu chữ là của chúng tôi.

Riêng phần 64 quẻ Kinh Dịch, chúng tôi dẫn về gốc Hán Việt mà người Việt vốn
quen, và ghi rõ những chỗ Human Design hiểu khác với Dịch truyền thống.

## Mã nguồn mở

**Phần mềm này là mã nguồn mở.** Toàn bộ cách tính bản đồ đều công khai, ai
cũng kiểm tra được. Chúng tôi nghĩ điều đó quan trọng: bạn không cần tin lời
chúng tôi về việc bản đồ được tính đúng — bạn tự xem được.
<a href="{goc}/ma-nguon">Xem mã nguồn và giấy phép</a>
"""

KHO_MA_NGUON = "https://github.com/hoangphamtd/human-design-brich-mind"

MA_NGUON = """
# Mã nguồn mở

Phần mềm Human Design này là **mã nguồn mở**. Toàn bộ mã tính toán, mã vẽ biểu
đồ, và toàn bộ nội dung mô tả đều công khai. Bạn xem được, tải về được, và dùng
lại được.

## Xem mã nguồn ở đâu

<a href="{kho}">{kho_gon}</a>

Ở đó có đầy đủ: cỗ máy tính bản đồ, phần vẽ BodyGraph, và toàn bộ kho nội dung
tiếng Việt mô tả 5 loại năng lượng, 7 cách ra quyết định, 12 vai trong đời,
9 trung tâm, 64 cổng và 36 kênh.

## Giấy phép

Phần mềm này phát hành theo **GNU Affero General Public License phiên bản 3
(AGPL-3.0)**.

Nói ngắn gọn, giấy phép này cho phép bạn dùng phần mềm cho bất kỳ mục đích gì,
kể cả kinh doanh; đọc, sửa và cải tiến mã nguồn; chia sẻ lại bản gốc hoặc bản
bạn đã sửa.

Kèm một điều kiện: nếu bạn sửa rồi đem phục vụ người khác — dù trên web hay
dưới dạng phần mềm tải về — bạn cũng phải công khai mã nguồn bản của bạn theo
cùng giấy phép này.

Nguyên văn giấy phép nằm ở file `LICENSE` trong kho mã nguồn.

## Vì sao chúng tôi mở

Phần tính toán thiên văn trong phần mềm này dựa trên thư viện **Swiss
Ephemeris**, một thư viện phát hành theo giấy phép kép: hoặc AGPL, hoặc bản
thương mại có phí. Chúng tôi chọn AGPL.

Đó là lựa chọn có chủ ý. Chúng tôi làm phần mềm này để tặng, không để bán. Mở
mã nguồn là cách nhất quán với điều đó — và nếu có ai muốn dựng một phiên bản
tốt hơn, chúng tôi thấy đó là chuyện đáng mừng.

## Ghi nhận

Phần tính toán vị trí thiên thể sử dụng thư viện **Swiss Ephemeris**,
Copyright © 1997–2021 Astrodienst AG, Thuỵ Sĩ, theo nhánh AGPL trong hệ cấp
phép kép của thư viện này.

`Swiss Ephemeris Inside`
"""


def _khoi_lien_he() -> str:
    """Chỉ in những dòng có thông tin. Không bịa, không để dòng trống."""
    d = [f"**{CONG_TY['ten']}**"]
    if CONG_TY.get("mst"):
        d.append(f"Mã số thuế: {CONG_TY['mst']}")
    if CONG_TY.get("dia_chi"):
        d.append(f"Địa chỉ: {CONG_TY['dia_chi']}")
    kenh = [f"Zalo: {CONG_TY['zalo']}"]
    if CONG_TY.get("email"):
        kenh.insert(0, f"Email: {CONG_TY['email']}")
    d.append(" · ".join(kenh))
    return "\n".join(d)


def rieng_tu() -> str:
    return RIENG_TU.format(khoi_lien_he=_khoi_lien_he(), **CONG_TY).strip()


def ve_he_thong(goc: str = "") -> str:
    return VE_HE_THONG.format(goc=goc).strip()


def ma_nguon() -> str:
    """Trang /ma-nguon — AGPL không chỉ đòi mở mã, mà đòi CUNG CẤP mã cho
    chính người dùng qua mạng. Nên phải có đường dẫn thấy được từ web."""
    return MA_NGUON.format(kho=KHO_MA_NGUON,
                           kho_gon=KHO_MA_NGUON.replace("https://", "")).strip()


# Giấy phép Swiss Ephemeris CẤM dùng tên Astrodienst / Dieter Koch /
# Alois Treindl để quảng bá. Tên họ chỉ được ở phần ghi nhận bản quyền —
# không viết "dùng công nghệ Astrodienst" ở bài đăng hay landing page.
# Nhãn "Swiss Ephemeris Inside" thì cả hai nhánh giấy phép đều cho dùng.
CHAN_TRANG_MA_NGUON = (
    'Mã nguồn mở theo giấy phép AGPL-3.0 · '
    '<a href="{goc}/ma-nguon">Xem mã nguồn</a>')


def chan_trang(goc: str = "") -> str:
    return CHAN_TRANG_MA_NGUON.format(goc=goc)


def con_thieu() -> list[str]:
    """Chỗ BẮT BUỘC còn thiếu. Mã số thuế và địa chỉ không bắt buộc với
    trang công cụ miễn phí — chỉ cần khi trang có thu tiền trực tiếp."""
    bat_buoc = ("ten", "zalo")
    return [k for k in bat_buoc if not CONG_TY.get(k) or str(CONG_TY[k]).startswith("ĐIỀN_")]


if __name__ == "__main__":
    thieu = con_thieu()
    if thieu:
        print("⚠️  CHƯA ĐIỀN:", ", ".join(thieu))
        print("   Sửa trong noi_dung_phap_ly.py, phần CONG_TY.")
    else:
        print("✅ Đã điền đủ thông tin công ty.")
