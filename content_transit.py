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
"""content_transit.py — 64 cặp "nên / tránh" cho tầng transit.

Dùng khi Mặt Trời hoặc Trái Đất đi qua một cổng. Khác với nội dung cổng
trong bản đồ sinh: ở đó là "bạn vốn có cổng này suốt đời", ở đây là
"tuần này bầu trời bật cổng này cho mọi người, kể cả người không có nó".

RANH GIỚI (theo chuẩn thị trường quốc tế đang dùng — xem HD-10):
  ✅ "tuần này dễ bực, nên dừng lại trước khi phản ứng"
  ✅ "quanh những ngày này tránh ký hợp đồng chưa xem kỹ"
  ❌ "tuần này bạn sẽ cãi nhau với vợ"
  ❌ "ngày 11 bạn bị lừa hợp đồng"
Cảnh báo xu hướng và khuyên hành động — KHÔNG tuyên bố biến cố sẽ xảy ra.
"""

NEN_TRANH = {
1:  ("Cái riêng của bạn đòi được nói ra", "Làm việc sáng tạo của riêng mình, đưa nó cho một người xem", "Chờ tới khi thấy đủ hay mới dám đưa"),
2:  ("Hướng đi được nhắc lại", "Ngồi xuống xem mình đang đi đâu, viết ra một câu", "Ép mình phải tự lo hết mọi nguồn lực"),
3:  ("Cái mới còn lộn xộn", "Bắt đầu nhỏ, chấp nhận đoạn đầu chưa gọn", "Bỏ cuộc vì thấy rối, hoặc thúc cho nhanh"),
4:  ("Đầu muốn có câu trả lời", "Đưa giả thuyết ra thử, nói rõ đó là giả thuyết", "Tin công thức của mình là chân lý rồi áp lên người khác"),
5:  ("Nhịp sinh hoạt đòi được giữ", "Bảo vệ giờ giấc riêng, từ chối lịch phá nhịp", "Nhận thêm việc làm xáo trộn nhịp đang ổn"),
6:  ("Ranh giới thân mật căng lên", "Nói ra ranh giới của mình trước khi bị vượt", "Nổ ra xung đột ngay lúc cảm xúc đang dâng"),
7:  ("Vai người dẫn phía sau", "Hỗ trợ người đứng trước, đưa hướng cho họ", "Giành lấy vị trí đứng trước khi chưa ai mời"),
8:  ("Muốn đóng góp bằng cách làm mẫu", "Đưa cái độc đáo của người khác ra ánh sáng", "Cố tỏ ra khác biệt để được chú ý"),
9:  ("Sức tập trung vào chi tiết", "Chọn một việc nhỏ đáng làm rồi làm tới nơi", "Sa vào chi tiết vụn mà quên bức tranh lớn"),
10: ("Câu hỏi mình là ai quay lại", "Sống theo cách của mình, không xin lỗi vì nó", "Sửa mình cho vừa khuôn của người khác"),
11: ("Ý tưởng đến nhiều hơn thường lệ", "Ghi lại và kể cho người cần nghe", "Lao vào thực hiện hết mọi ý tưởng vừa nảy"),
12: ("Lời nói lên xuống theo tâm trạng", "Chọn lúc trong người thông mới nói việc quan trọng", "Ép mình phát biểu khi đang đóng"),
13: ("Người ta muốn kể chuyện cho bạn", "Lắng nghe mà không góp ý, giữ kín điều được kể", "Kể lại chuyện người khác không đúng chỗ"),
14: ("Sức làm ra nguồn lực dâng lên", "Dồn sức vào việc đúng hướng mình muốn đi", "Đổ sức vào việc chỉ vì nó ra tiền"),
15: ("Nhịp sống dao động mạnh", "Chấp nhận nhịp mình không đều, đừng ép", "Tự trách vì không giữ được kỷ luật như người khác"),
16: ("Hăng hái muốn nhảy vào thử", "Chọn một thứ rồi luyện thật, đủ ba mươi ngày", "Nhảy vào rồi bỏ ngay khi hết hứng"),
17: ("Ý kiến bật ra rất nhanh", "Chờ có người hỏi rồi mới nói, nói rõ đó là ý kiến", "Đưa ý kiến cho mọi thứ dù không ai hỏi"),
18: ("Mắt nhìn ra chỗ chưa hoàn thiện", "Chỉ ra chỗ hỏng khi có người nhờ, chỉ vào việc không vào người", "Chỉ trích liên tục, hoặc quay sự phê phán vào chính mình"),
19: ("Nhạy với nhu cầu của người thân", "Nói thẳng nhu cầu của mình bằng một câu đơn giản", "Chờ người khác đoán ra rồi ấm ức khi họ không đoán"),
20: ("Khoảnh khắc hiện tại được nhấn", "Có mặt thật trong cuộc trò chuyện, tắt điện thoại", "Buột miệng nói ra thứ chưa kịp lọc"),
21: ("Muốn nắm quyền kiểm soát", "Kiểm soát đúng phần việc của mình và làm tốt", "Kiểm soát người và việc không thuộc về mình"),
22: ("Cởi mở lên xuống theo sóng", "Gặp gỡ vào lúc mình đang mở", "Ép mình xã giao khi trong người không muốn"),
23: ("Muốn nói ra điều khó diễn đạt", "Giữ lại cho tới khi có người hỏi", "Nói ra khi chưa ai sẵn sàng nghe rồi thấy cô đơn"),
24: ("Một câu hỏi cũ quay lại", "Cho phép mình nghĩ lại, viết một đoạn ngắn", "Tự trách vì cứ nghĩ mãi một chuyện"),
25: ("Tinh thần hồn nhiên được nhắc", "Làm một việc tử tế cho người không liên quan", "Cứng lại vì một tổn thương cũ"),
26: ("Muốn thuyết phục người khác", "Kể điều mình thật sự tin", "Nói quá lên để bán được"),
27: ("Nhu cầu chăm sóc dâng lên", "Chăm người thật sự cần, và chăm chính mình trước", "Chăm người không nhờ rồi cạn sức"),
28: ("Câu hỏi điều gì đáng sống", "Chọn một thứ đáng dồn hết vào", "Đặt cược bừa vào mọi thứ, hoặc tê liệt không chọn gì"),
29: ("Dễ gật đầu cam kết", "Xin hai mươi tư giờ trước khi nhận việc lớn", "Nói có bằng cái đầu rồi mắc kẹt nhiều năm"),
30: ("Khao khát bùng lên", "Ghi lại điều mình đang thèm, cất ba tuần rồi đọc lại", "Đuổi theo ngay khao khát vừa bùng"),
31: ("Tiếng nói dẫn dắt được nhấn", "Lên tiếng nếu nhóm đã tin và đã chọn mình", "Tự nhận vai dẫn khi chưa ai mời"),
32: ("Bản năng đo cái gì trụ được", "Hỏi bản năng chứ không hỏi lý trí về việc đang giữ", "Tiếc công mà giữ lại thứ đã báo là không trụ"),
33: ("Muốn rút lui để tiêu hoá", "Cho mình một ngày không gặp ai, rồi viết ra điều rút được", "Chạy liên tục không cho mình khoảng lặng"),
34: ("Sức lực dồi dào hơn thường lệ", "Dành một buổi làm việc của riêng mình", "Đổ hết sức vào việc của người khác"),
35: ("Muốn trải nghiệm cái mới", "Rút một bài học từ trải nghiệm vừa qua trước khi tìm cái mới", "Nhảy sang cái mới ngay khi vừa chán"),
36: ("Dễ lao vào chuyện chưa từng làm", "Cho mình ba ngày trước khi nhảy vào", "Lao vào lúc đang phấn khích rồi tạo lộn xộn"),
37: ("Lời hứa trong nhà được nhắc", "Nói rõ mình làm gì và mong đổi lại điều gì", "Hứa mà không nói rõ đổi lại, rồi ấm ức"),
38: ("Sức đối kháng dâng lên", "Chọn một trận đáng đánh, buông hai trận không đáng", "Chống lại mọi thứ kể cả chuyện không đáng"),
39: ("Dễ khiêu khích và dễ bị khiêu khích", "Hỏi mình đang chọc để giúp hay để xả", "Chọc bừa lúc trong người khó chịu"),
40: ("Muốn làm xong rồi rút", "Làm phần của mình rồi nghỉ, không thấy có lỗi", "Làm mãi không nghỉ vì sợ bị coi là ích kỷ"),
41: ("Một khao khát chưa rõ hình dạng", "Viết ba dòng mô tả cảm giác đó, chưa mua gì", "Mua sắm hoặc ăn để lấp cảm giác mơ hồ"),
42: ("Muốn làm cho xong một chu kỳ", "Chọn một việc bỏ dở, làm xong hoặc khai tử hẳn", "Bỏ ngang rồi bắt cái mới"),
43: ("Cái biết bên trong bật ra", "Viết nó ra bằng ba cách diễn đạt khác nhau", "Buột miệng nói khi chưa ai hỏi"),
44: ("Bản năng đọc người sắc lên", "Ghi lại ấn tượng ba mươi giây đầu về người mới gặp", "Gán cho người mới bộ mặt của người cũ"),
45: ("Chuyện tài nguyên chung nổi lên", "Trông coi và chia đúng phần cho nhóm mình", "Dẫn một nhóm chưa chọn mình, hoặc giữ mà không chia"),
46: ("Thân thể đòi được chú ý", "Dành ba mươi phút mỗi ngày cho cơ thể", "Coi thân thể như cái máy phải chạy"),
47: ("Đang bí, chưa vỡ ra", "Chịu được đoạn bí, làm việc chân tay cho khuây", "Vơ một lời giải thích cho xong"),
48: ("Cảm giác mình chưa đủ giỏi", "Nhận một việc mình mới đủ tám mươi phần trăm", "Chờ đủ giỏi mới dám bắt đầu"),
49: ("Nguyên tắc bị đem ra thử", "Nói rõ nguyên tắc của mình từ đầu", "Cắt đứt đột ngột mà người kia không hiểu vì sao"),
50: ("Trách nhiệm với nhóm nặng lên", "Đánh dấu trách nhiệm nào thật sự của mình, trả lại một cái không phải", "Ôm hết trách nhiệm của cả nhóm"),
51: ("Dễ gây sốc và dễ bị sốc", "Dám làm điều mình vẫn ngại, có chuẩn bị", "Gây sốc chỉ để chứng tỏ mình"),
52: ("Muốn ngồi yên", "Cho mình hai mươi phút ngồi yên không điện thoại", "Ép mình phải luôn bận rộn cho giống người khác"),
53: ("Áp lực muốn bắt đầu cái mới", "Mở một thứ, và nói rõ ai sẽ làm tiếp", "Mở thêm khi còn nhiều thứ đang dở"),
54: ("Muốn đi lên một bậc", "Làm tốt phần của mình để người trên nhìn thấy", "Chen lên bằng mọi giá"),
55: ("Tinh thần lên xuống không lý do", "Ghi tâm trạng mỗi tối, không tìm lý do bên ngoài", "Đổ cho người gần nhất khi mình xuống đáy"),
56: ("Muốn kể chuyện và đi xa", "Kể cho người muốn nghe, dừng khi họ nhìn đi chỗ khác", "Kể liên tục để giữ sự chú ý"),
57: ("Trực giác nói rất khẽ", "Làm theo tín hiệu đầu tiên trong ba việc nhỏ", "Đi tìm lý do rồi để tín hiệu tan mất"),
58: ("Muốn làm mọi thứ tốt lên", "Chọn một việc mình thích cải thiện và làm", "Muốn sửa cả người khác dù không ai nhờ"),
59: ("Rào cản thân mật mỏng đi", "Hỏi một câu trước khi đi vào chuyện riêng của ai", "Xuyên qua ranh giới người khác khi họ chưa cho phép"),
60: ("Giới hạn hiện ra rõ", "Viết ba việc vẫn làm được trong khuôn khổ đang có", "Chờ giới hạn biến mất rồi mới bắt đầu"),
61: ("Áp lực muốn biết điều lớn", "Viết câu hỏi lớn ra giấy rồi cất đi", "Thức đêm ép mình phải hiểu cho ra"),
62: ("Chi tiết và trật tự được nhấn", "Sắp xếp lại việc đang bừa, đặt tên cho từng phần", "Sa vào tiểu tiết hoặc bắt bẻ chữ nghĩa"),
63: ("Nghi ngờ nổi lên", "Viết ra mình nghi cái gì, gạch cái nào không kiểm chứng được", "Quay sự nghi ngờ vào chính mình và người thân"),
64: ("Đầu đầy hình ảnh rối", "Đứng dậy làm việc chân tay ba mươi phút", "Cố ép mình nghĩ cho ra ngay"),
}

assert len(NEN_TRANH) == 64, f"phải đủ 64 cổng, đang có {len(NEN_TRANH)}"
assert sorted(NEN_TRANH) == list(range(1, 65)), "thiếu hoặc thừa cổng"
