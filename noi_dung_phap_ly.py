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


def ve_he_thong() -> str:
    return VE_HE_THONG.strip()


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
