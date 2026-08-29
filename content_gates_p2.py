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
"""64 CỔNG — ĐỢT 2: Trung tâm G (8) · Tim (4) · Lá lách (7) = 19 cổng.

BẢN NỘI BỘ ĐẦY ĐỦ — giữ nguyên nội dung gốc hệ thống, chưa qua bộ lọc NĐ38.
Bảy cổng Lá lách giữ đủ bảy nỗi sợ gốc và phần hệ thống nối với miễn dịch.
"""

GATES_P2 = {

# ══════════ TRUNG TÂM G — bản thể và phương hướng ══════════

1: {
 "name_vi": "Biểu đạt cái riêng",
 "kenh": "1-8 (Cảm hứng) — nối lên Cổ họng",
 "tagline": "Bạn có một thứ chỉ mình bạn làm được. Nó không đến theo lịch.",
 "mechanics": (
   "Cổng 1 là nguồn sáng tạo thuần khiết trong bản đồ, quẻ gốc là Càn — trời, sức sáng tạo "
   "thuần dương. Đây là cổng của cái độc đáo cá nhân: thứ bạn tạo ra mang dấu vân tay riêng "
   "không lẫn được. Cổng 1 nối với cổng 8 ở Cổ họng — cổng 1 tạo ra, cổng 8 mang nó ra thế giới."
 ),
 "aligned": (
   "Bạn để cái sáng tạo đến theo nhịp của nó, không ép. Bạn cũng không đợi ai cho phép mới "
   "làm cái của mình. Khi tới lúc, bạn tạo ra thứ không ai bắt chước được, và người ta nhận "
   "ra ngay đó là của bạn."
 ),
 "misaligned": (
   "Bạn ép mình phải sáng tạo theo lịch, rồi ra một thứ nhạt. Hoặc bạn giữ cái của mình lại "
   "vì sợ không đủ hay, và nó nằm im mãi. Cổng 1 lệch hướng cũng dễ rơi vào trạng thái buồn "
   "sâu — cảm giác có điều gì trong mình mà không đưa ra được."
 ),
 "practice": "Dành mỗi ngày ba mươi phút cho việc sáng tạo của bạn, không đặt mục tiêu phải ra kết quả. Làm ba mươi ngày rồi nhìn lại.",
 "questions": [
   "Bạn đang giữ lại thứ gì vì sợ nó chưa đủ hay?",
   "Lần cuối bạn làm một thứ chỉ vì mình muốn làm là khi nào?"
 ]
},

13: {
 "name_vi": "Người lắng nghe",
 "kenh": "13-33 (Đứa con hoang) — nối lên Cổ họng",
 "tagline": "Người ta kể cho bạn nghe những điều họ không kể với ai. Đó là gánh nặng lẫn món quà.",
 "mechanics": (
   "Cổng 13 là nơi thu nhận câu chuyện của người khác, quẻ gốc là Đồng Nhân — hoà đồng với "
   "người. Trường năng lượng của cổng này khiến người lạ cũng tự nhiên mở lòng với bạn. Cổng "
   "13 nối với cổng 33 ở Cổ họng, nơi những gì thu nhận được kể lại thành bài học chung."
 ),
 "aligned": (
   "Bạn nghe mà không phán xét, và bạn biết giữ bí mật. Bạn cũng biết chọn cái gì nên kể lại "
   "và cái gì phải chôn. Người ta tìm bạn khi cần một chỗ để nói ra, và điều đó là một vai trò thật."
 ),
 "misaligned": (
   "Bạn ôm hết chuyện của thiên hạ vào người và nặng dần mà không biết đổ đi đâu. Hoặc bạn kể "
   "lại chuyện của người khác không đúng chỗ, và mất luôn lòng tin — với cổng này, mất lòng "
   "tin rất khó lấy lại."
 ),
 "practice": "Sau lần nghe chuyện nặng tiếp theo, viết ra một trang rồi xé đi. Đừng để nó nằm lại trong người.",
 "questions": [
   "Bạn đang mang chuyện của ai mà chưa đặt xuống được?",
   "Có chuyện nào bạn đã kể lại mà đáng ra không nên không?"
 ]
},

25: {
 "name_vi": "Tinh thần hồn nhiên",
 "kenh": "25-51 (Khởi phát) — nối sang Tim",
 "tagline": "Bạn yêu mọi thứ như nhau, và điều đó làm người thân bạn khó hiểu.",
 "mechanics": (
   "Cổng 25 là tình yêu vô điều kiện, không phân biệt đối tượng — quẻ gốc là Vô Vọng, không "
   "càn bậy, hồn nhiên chân thật. Đây là tình yêu ở tầng phổ quát, hướng về sự sống nói chung "
   "chứ không hướng vào một người cụ thể. Nối với cổng 51 ở Tim thành kênh Khởi phát."
 ),
 "aligned": (
   "Bạn giữ được sự hồn nhiên đó qua các cú sốc của đời. Bạn đối xử với con chó ngoài đường "
   "cũng như với người quan trọng, và điều đó tạo ra một trường rất trong. Bạn cũng chấp nhận "
   "được rằng người thân đôi khi thấy tổn thương vì bạn không dành riêng cho họ."
 ),
 "misaligned": (
   "Bạn cứng lại sau vài lần bị tổn thương và mất đi sự hồn nhiên. Hoặc bạn dùng tình yêu phổ "
   "quát làm cớ để không cam kết sâu với ai."
 ),
 "practice": "Tuần này làm một việc tử tế cho một người hoàn toàn không liên quan tới bạn, không cho ai biết.",
 "questions": [
   "Bạn có cứng lại sau lần tổn thương nào không?",
   "Người thân bạn có thấy bạn xa cách không?"
 ]
},

46: {
 "name_vi": "Đúng nơi đúng lúc",
 "kenh": "46-29 (Khám phá) — nối xuống Xương cùng",
 "tagline": "Có những lúc mọi thứ tự xếp vào chỗ. Đó không phải may mắn.",
 "mechanics": (
   "Cổng 46 là tình yêu dành cho cơ thể và sự có mặt đúng chỗ đúng lúc. Quẻ gốc là Thăng — "
   "đi lên. Hệ thống mô tả cổng này gắn với việc bạn ở trong thân xác này và trân trọng nó. "
   "Nối với cổng 29 ở Xương cùng thành kênh Khám phá."
 ),
 "aligned": (
   "Bạn chăm sóc cơ thể mình và bạn có mặt thật ở nơi mình đang đứng. Người có cổng này thường "
   "hay rơi vào những tình huống tình cờ mà hoá ra đúng — đó là cơ chế của cổng, không phải "
   "may. Bạn cũng dễ được người khác nhận ra và cất nhắc."
 ),
 "misaligned": (
   "Bạn bỏ bê thân thể, coi nó như cái máy phải chạy. Hoặc bạn cố ép mình vào những chỗ mình "
   "không thuộc về, rồi mọi thứ đều trầy trật."
 ),
 "practice": "Tuần này dành ba mươi phút mỗi ngày làm gì đó cho thân thể — đi bộ, kéo giãn, tắm lâu. Không phải để đạt gì cả.",
 "questions": [
   "Bạn đối xử với cơ thể mình thế nào trong sáu tháng qua?",
   "Có chỗ nào bạn đang cố ở lại mà thấy trầy trật liên tục không?"
 ]
},

2: {
 "name_vi": "Hướng đi",
 "kenh": "2-14 (Nhịp đập) — nối xuống Xương cùng",
 "tagline": "Bạn biết đường phải đi, nhưng bạn cần người khác cung cấp nhiên liệu.",
 "mechanics": (
   "Cổng 2 là hướng đi của bản thể, quẻ gốc là Khôn — đất, sức thụ nhận. Đây là cổng tiếp nhận: "
   "nó biết phải đi đâu nhưng tự nó không có động lực. Nối với cổng 14 ở Xương cùng thành kênh "
   "Nhịp đập — cổng 14 mang nhiên liệu, cổng 2 chỉ hướng."
 ),
 "aligned": (
   "Bạn tin vào cảm thức phương hướng của mình, kể cả khi chưa giải thích được. Bạn cũng chấp "
   "nhận rằng mình cần người khác hoặc hoàn cảnh mang tới nguồn lực, và bạn không thấy đó là "
   "yếu. Việc của bạn là chỉ đường, không phải kéo xe."
 ),
 "misaligned": (
   "Bạn ép mình phải tự lo hết, rồi cạn. Hoặc bạn để người khác quyết hướng đi thay mình vì "
   "nghĩ họ chắc chắn hơn — và bạn đi một con đường không phải của mình."
 ),
 "practice": "Viết ra hướng bạn muốn đi trong năm năm tới. Rồi liệt kê ba người có thể mang tới nguồn lực. Nói chuyện với một người.",
 "questions": [
   "Bạn có đang tự lo hết mọi thứ không?",
   "Hướng bạn đang đi là của bạn hay của ai?"
 ]
},

15: {
 "name_vi": "Biên độ",
 "kenh": "15-5 (Nhịp điệu) — nối xuống Xương cùng",
 "tagline": "Nhịp sống của bạn không đều, và bạn không cần phải làm cho nó đều.",
 "mechanics": (
   "Cổng 15 là biên độ cực đoan trong nhịp sống, cùng với tình yêu dành cho nhân loại nói "
   "chung. Đây là cổng lệch nhiều so với gốc Kinh Dịch: quẻ Khiêm nghĩa là khiêm nhường, còn "
   "hệ thống lại dùng cổng này cho sự dao động lớn. Nối với cổng 5 ở Xương cùng."
 ),
 "aligned": (
   "Bạn chấp nhận rằng có giai đoạn mình dậy sớm chăm chỉ, có giai đoạn mình lộn xộn — và cả "
   "hai đều là mình. Bạn không ép bản thân vào một khuôn giờ giấc cố định. Bạn cũng có sức "
   "chứa lớn với những kiểu người rất khác mình."
 ),
 "misaligned": (
   "Bạn cố sống theo nhịp đều đặn của người khác, rồi thấy mình luôn thất bại trong việc giữ "
   "kỷ luật. Hoặc bạn để biên độ đó kéo mình đi quá xa về một phía mà không tự kéo lại."
 ),
 "practice": "Ghi nhật ký giờ giấc trong ba mươi ngày. Bạn sẽ thấy nhịp thật của mình, không phải nhịp bạn nghĩ mình nên có.",
 "questions": [
   "Bạn có tự trách mình vì không giữ được giờ giấc đều không?",
   "Nhịp thật của bạn là gì, nếu không ai bắt bạn phải theo ai?"
 ]
},

10: {
 "name_vi": "Cách sống của mình",
 "kenh": "10-20 (Tỉnh thức) · 10-34 (Thăm dò) · 10-57 (Hình hài) — nối lên Cổ họng, xuống Sacral và Lá lách",
 "tagline": "Yêu chính mình không phải là một khẩu hiệu. Nó là điều kiện để bạn làm được mọi thứ khác.",
 "mechanics": (
   "Cổng 10 là cách bạn hành xử và yêu chính mình, quẻ gốc là Lý — bước đi, cách hành xử. Đây "
   "là cổng nối được với ba nơi, nên nó xuất hiện rất nhiều trong các bản đồ. Nguyên tắc nền: "
   "bạn chỉ sống đúng khi bạn chấp nhận chính mình như đang là."
 ),
 "aligned": (
   "Bạn sống theo cách của mình mà không cần xin lỗi vì nó. Bạn cũng không cố sửa mình cho vừa "
   "khuôn của ai. Người có cổng này khi ổn thì có một sự tự tại rất dễ nhận ra."
 ),
 "misaligned": (
   "Bạn liên tục cố sửa mình cho hợp với người khác, và mất dần cảm giác mình là ai. Hoặc bạn "
   "dùng cái gọi là sống thật với mình để biện minh cho việc làm tổn thương người khác."
 ),
 "practice": "Viết ra ba điều về bản thân bạn đang cố sửa. Với mỗi cái, hỏi: sửa cho ai?",
 "questions": [
   "Bạn đang cố sửa điều gì ở mình, và sửa cho ai?",
   "Bạn có phải xin lỗi vì cách sống của mình không?"
 ]
},

7: {
 "name_vi": "Vai người dẫn",
 "kenh": "7-31 (Người dẫn) — nối lên Cổ họng",
 "tagline": "Bạn dẫn từ phía sau. Người đứng trước chưa chắc là người dẫn.",
 "mechanics": (
   "Cổng 7 là vai trò lãnh đạo trong mạch tập thể, quẻ gốc là Sư — quân đội và người dẫn quân. "
   "Điểm đặc trưng: cổng 7 dẫn ở phía sau, cố vấn cho người đứng trước, chứ không phải người "
   "cầm micro. Nối với cổng 31 ở Cổ họng."
 ),
 "aligned": (
   "Bạn tìm được người đứng trước phù hợp và bạn hỗ trợ họ. Bạn có tầm nhìn về tương lai chung "
   "và bạn dùng nó để định hướng. Bạn thoải mái với việc không phải mình là người được vỗ tay."
 ),
 "misaligned": (
   "Bạn giành lấy vị trí đứng trước rồi thấy nó không hợp. Hoặc bạn ấm ức vì người đứng trước "
   "được ghi công trong khi bạn mới là người vạch đường."
 ),
 "practice": "Nghĩ về người đứng trước trong nhóm của bạn. Tuần này làm một việc cụ thể để họ làm tốt hơn, không cần ai biết là bạn làm.",
 "questions": [
   "Bạn có ấm ức vì không được ghi công không?",
   "Ai là người đứng trước mà bạn đang muốn hỗ trợ?"
 ]
},

# ══════════ TRUNG TÂM TIM — ý chí và lời hứa ══════════

21: {
 "name_vi": "Người săn",
 "kenh": "21-45 (Tiền bạc) — nối lên Cổ họng",
 "tagline": "Bạn cần kiểm soát địa hạt của mình. Vấn đề là bạn thường muốn kiểm soát cả những chỗ không phải của mình.",
 "mechanics": (
   "Cổng 21 là ý chí kiểm soát tài nguyên và lãnh thổ, quẻ gốc là Phệ Hạp — cắn xuyên, dùng "
   "hình phạt. Đây là một động cơ ý chí thật: bạn có sức để giành và giữ. Nối với cổng 45 ở "
   "Cổ họng thành kênh Tiền bạc."
 ),
 "aligned": (
   "Bạn kiểm soát đúng phần việc và tài sản thuộc về mình, và bạn làm tốt. Bạn cũng buông "
   "những chỗ không phải của mình. Khi bạn được quyền tự quyết trong địa hạt của mình, bạn "
   "làm ra kết quả rất mạnh."
 ),
 "misaligned": (
   "Bạn kiểm soát người và việc không phải của mình, rồi vấp phải sự chống đối liên tục. Hoặc "
   "bạn bị người khác kiểm soát và bạn phản kháng dữ dội — cổng 21 rất khó chịu khi bị chỉ đạo."
 ),
 "practice": "Vẽ ra ranh giới địa hạt của bạn trên giấy: việc nào là của mình, việc nào không. Buông một việc nằm ngoài ranh giới đó.",
 "questions": [
   "Bạn đang cố kiểm soát điều gì không thuộc về mình?",
   "Ai đang chỉ đạo bạn, và bạn phản ứng thế nào?"
 ]
},

40: {
 "name_vi": "Làm rồi rút",
 "kenh": "40-37 (Cộng đồng) — nối xuống Đám rối mặt trời",
 "tagline": "Bạn làm hết mình cho gia đình, rồi bạn cần một mình. Cả hai đều thật.",
 "mechanics": (
   "Cổng 40 là ý chí làm việc để nuôi nhóm mình, kèm nhu cầu rút lui sau đó. Quẻ gốc là Giải "
   "— cởi bỏ, giải toả. Nối với cổng 37 ở Đám rối mặt trời thành kênh Cộng đồng: cổng 37 là "
   "lời hứa, cổng 40 là sức để giữ lời hứa đó."
 ),
 "aligned": (
   "Bạn làm phần của mình rồi rút về nghỉ mà không thấy có lỗi. Bạn cũng đòi hỏi sự công bằng "
   "trong thoả thuận: tôi làm phần này, đổi lại tôi nhận cái này. Sự sòng phẳng đó giữ mối "
   "quan hệ bền."
 ),
 "misaligned": (
   "Bạn làm mãi không nghỉ vì sợ bị coi là ích kỷ, rồi cạn và sinh oán. Hoặc bạn hứa với gia "
   "đình những thứ vượt sức mình, rồi không giữ được lời."
 ),
 "practice": "Sau đợt làm việc nặng tiếp theo, tự cho mình một ngày trọn vẹn không làm gì cho ai. Nói trước với người nhà.",
 "questions": [
   "Bạn có thấy có lỗi khi nghỉ ngơi không?",
   "Thoả thuận giữa bạn và gia đình có sòng phẳng không?"
 ]
},

26: {
 "name_vi": "Người thuyết phục",
 "kenh": "26-44 (Buông bỏ) — nối xuống Lá lách",
 "tagline": "Bạn nhớ mọi thứ và bạn kể lại rất hay. Ranh giới giữa kể hay và nói quá rất mỏng.",
 "mechanics": (
   "Cổng 26 là ý chí bán hàng và thuyết phục, quẻ gốc là Đại Súc — chứa lớn, tích tụ lớn. Hệ "
   "thống mô tả cổng này là nơi ký ức được nén lại rồi bung ra thành câu chuyện có sức thuyết "
   "phục. Nối với cổng 44 ở Lá lách."
 ),
 "aligned": (
   "Bạn kể lại điều mình thật sự tin và bạn làm người ta tin theo. Bạn biết cách trình bày giá "
   "trị của một thứ mà không cần bịa. Đây là cổng rất mạnh cho người bán hàng, người làm "
   "thương hiệu, người gọi vốn."
 ),
 "misaligned": (
   "Bạn nói quá lên để bán được, rồi phải nói dối thêm để đỡ cho lời đầu. Hoặc bạn bán một thứ "
   "mình không tin, và ý chí bạn cạn rất nhanh vì nó phải chống lại chính mình."
 ),
 "practice": "Nhìn lại lời chào bán gần nhất của bạn. Gạch bỏ mọi câu bạn không đặt tay lên ngực khẳng định được.",
 "questions": [
   "Bạn có đang nói quá về điều gì không?",
   "Bạn có thật sự tin vào thứ bạn đang bán không?"
 ]
},

51: {
 "name_vi": "Cú sốc",
 "kenh": "51-25 (Khởi phát) — nối sang Trung tâm G",
 "tagline": "Bạn đẩy người khác vào chỗ khó, và đôi khi đó là điều tốt nhất bạn làm cho họ.",
 "mechanics": (
   "Cổng 51 là năng lượng cạnh tranh và gây sốc, quẻ gốc là Chấn — sấm, chấn động. Hệ thống "
   "mô tả cổng này là nơi con người bị đẩy ra khỏi vùng quen thuộc, và chính cú đẩy đó mở ra "
   "một tầng nhận thức mới. Nối với cổng 25 thành kênh Khởi phát."
 ),
 "aligned": (
   "Bạn dám đi trước, dám làm điều người khác chưa dám, và bạn kéo người khác theo. Bạn cũng "
   "hồi phục nhanh sau cú sốc — thứ làm người khác gục thì làm bạn tỉnh ra."
 ),
 "misaligned": (
   "Bạn gây sốc cho người khác chỉ để chứng tỏ mình, không vì mục đích gì. Hoặc bạn lao vào "
   "cạnh tranh với tất cả mọi người, kể cả những cuộc không đáng."
 ),
 "practice": "Nhớ lại cú sốc lớn gần nhất trong đời bạn. Viết ra điều nó đã mở ra cho bạn mà không có nó thì không có.",
 "questions": [
   "Bạn có đang cạnh tranh với những người không đáng để cạnh tranh không?",
   "Cú sốc nào đã làm bạn thành người như hôm nay?"
 ]
},

# ══════════ TRUNG TÂM LÁ LÁCH — bản năng, sinh tồn, sức khoẻ ══════════
# GIỮ NGUYÊN GỐC. Hệ thống mô tả Lá lách gắn với hệ miễn dịch và sức khoẻ thể chất,
# và mỗi cổng mang một nỗi sợ nguyên thuỷ. Không cắt. Lọc khi publish.

48: {
 "name_vi": "Chiều sâu",
 "kenh": "48-16 (Bước sóng) — nối lên Cổ họng",
 "tagline": "Bạn có một cái giếng rất sâu bên trong, và bạn luôn thấy nó chưa đủ sâu.",
 "mechanics": (
   "Cổng 48 là chiều sâu năng lực, quẻ gốc là Tỉnh — cái giếng, nguồn sâu không cạn. Đây là "
   "một trong bảy cổng của Lá lách, và như mọi cổng Lá lách, nó mang một nỗi sợ nguyên thuỷ: "
   "sợ mình không đủ năng lực. Nỗi sợ này là nhiên liệu, không phải khuyết tật. Nối với cổng "
   "16 ở Cổ họng — cổng 48 là chiều sâu, cổng 16 đưa nó thành kỹ năng thực."
 ),
 "aligned": (
   "Bạn dùng nỗi sợ không đủ giỏi làm động lực học tiếp, chứ không để nó chặn bạn lại. Bạn "
   "trở thành người có nghề thật sâu trong một lĩnh vực. Bạn cũng chấp nhận rằng cảm giác "
   "chưa đủ sẽ không bao giờ hết — đó là cơ chế, không phải sự thật về bạn."
 ),
 "misaligned": (
   "Bạn để nỗi sợ chặn mình lại, không dám nhận việc, không dám ra mắt, chờ tới khi đủ giỏi — "
   "và ngày đó không tới. Hoặc bạn học mãi mà không bao giờ đem ra dùng."
 ),
 "practice": "Nhận một việc mà bạn thấy mình mới đủ tám mươi phần trăm năng lực. Làm và học phần còn lại trong lúc làm.",
 "questions": [
   "Bạn đang chờ đủ giỏi để làm gì?",
   "Nếu cảm giác chưa đủ không bao giờ hết, bạn sẽ bắt đầu khi nào?"
 ]
},

57: {
 "name_vi": "Trực giác",
 "kenh": "57-10 (Hình hài) · 57-20 (Sóng não) · 57-34 (Sức mạnh) — nối sang G, Cổ họng, Xương cùng",
 "tagline": "Bạn nghe thấy điều người khác không nghe. Nó nói đúng một lần.",
 "mechanics": (
   "Cổng 57 là trực giác nhạy nhất trong bản đồ, quẻ gốc là Tốn — gió, thấm vào nhẹ nhàng. "
   "Hệ thống mô tả cổng này gắn với thính giác ở tầng bản năng: bạn cảm được qua âm thanh và "
   "qua trường của người khác. Nỗi sợ nguyên thuỷ của nó là sợ ngày mai, sợ điều chưa tới."
 ),
 "aligned": (
   "Bạn tin tín hiệu đầu tiên và làm theo ngay, không đợi lý lẽ. Bạn cũng biết rằng cổng này "
   "chỉ nói về khoảnh khắc hiện tại, không phải về tương lai — nên bạn không dùng nó để lo xa."
 ),
 "misaligned": (
   "Bạn nghe tín hiệu rồi đi tìm lý do, và tín hiệu tan. Hoặc bạn để nỗi sợ ngày mai chiếm "
   "chỗ, sống trong trạng thái phòng thủ liên tục với những chuyện chưa xảy ra."
 ),
 "practice": "Ba ngày liền, chọn quán ăn hoặc đường đi theo phản ứng đầu tiên. Không sửa lại. Ghi kết quả.",
 "questions": [
   "Bạn đang lo về điều gì chưa xảy ra?",
   "Lần gần nhất bạn phủ quyết linh cảm của mình, chuyện gì đã xảy ra?"
 ]
},

44: {
 "name_vi": "Cảnh giác",
 "kenh": "44-26 (Buông bỏ) — nối lên Tim",
 "tagline": "Bạn ngửi thấy vấn đề ở một người trước khi có bất kỳ dấu hiệu nào.",
 "mechanics": (
   "Cổng 44 là bản năng nhận biết mẫu hình từ quá khứ, quẻ gốc là Cấu — gặp gỡ bất ngờ. Đây "
   "là cổng lệch rõ so với Kinh Dịch. Hệ thống mô tả cổng này gắn với khứu giác ở tầng bản "
   "năng: bạn gặp một người và cảm ngay được họ có đáng tin không. Nỗi sợ gốc là sợ quá khứ lặp lại."
 ),
 "aligned": (
   "Bạn tin cảm nhận của mình về người, và bạn dùng nó để chọn cộng sự. Đây là cổng rất giá "
   "trị trong tuyển người và trong làm ăn. Bạn cũng biết phân biệt giữa cảnh giác đúng chỗ "
   "và định kiến."
 ),
 "misaligned": (
   "Bạn để nỗi sợ quá khứ lặp lại chi phối, rồi gán cho người mới bộ mặt của người cũ. Hoặc "
   "bạn bỏ qua cảm nhận ban đầu vì thấy nó vô lý, rồi sau này hối."
 ),
 "practice": "Lần tới gặp người mới, ghi lại ấn tượng đầu tiên trong ba mươi giây đầu. Sáu tháng sau đọc lại và đối chiếu.",
 "questions": [
   "Bạn có đang nhìn ai đó qua bộ mặt của một người trong quá khứ không?",
   "Lần bạn bỏ qua cảm nhận ban đầu về một người — kết cục thế nào?"
 ]
},

50: {
 "name_vi": "Giá trị và luật lệ",
 "kenh": "50-27 (Gìn giữ) — nối xuống Xương cùng",
 "tagline": "Bạn giữ luật cho nhóm mình, kể cả khi không ai giao việc đó cho bạn.",
 "mechanics": (
   "Cổng 50 là nơi giữ giá trị và luật lệ của bộ tộc, quẻ gốc là Đỉnh — cái vạc dùng trong tế "
   "tự, biểu tượng của luật và trật tự. Hệ thống mô tả cổng này gắn với bản năng bảo vệ nhóm. "
   "Nỗi sợ gốc là sợ trách nhiệm — cảm giác gánh nặng của người phải giữ trật tự. Nối với "
   "cổng 27 ở Xương cùng."
 ),
 "aligned": (
   "Bạn giữ những nguyên tắc thật sự cần giữ, và bạn buông những luật đã lỗi thời. Bạn là "
   "người mà nhóm dựa vào khi cần biết đâu là ranh giới. Bạn cũng nhận trách nhiệm đúng phần "
   "mình, không ôm hết."
 ),
 "misaligned": (
   "Bạn ôm hết trách nhiệm của cả nhóm rồi kiệt. Hoặc bạn áp luật lệ cũ lên hoàn cảnh mới và "
   "trở thành người cản đường. Cổng 50 lệch hướng cũng hay sinh cảm giác tội lỗi triền miên."
 ),
 "practice": "Liệt kê những trách nhiệm bạn đang gánh. Đánh dấu cái nào thật sự là của bạn. Giao trả một cái không phải.",
 "questions": [
   "Bạn đang gánh trách nhiệm nào không phải của mình?",
   "Có luật lệ nào bạn đang giữ mà nó đã hết thời rồi không?"
 ]
},

32: {
 "name_vi": "Bền bỉ",
 "kenh": "32-54 (Chuyển hoá) — nối xuống Gốc",
 "tagline": "Bạn nhìn ra cái gì sẽ trụ được và cái gì sẽ tan. Đó là bản năng, không phải phân tích.",
 "mechanics": (
   "Cổng 32 là bản năng nhận biết điều gì có khả năng tồn tại lâu dài, quẻ gốc là Hằng — bền "
   "lâu. Nỗi sợ gốc là sợ thất bại. Hệ thống mô tả nỗi sợ này là thứ giữ cho người có cổng 32 "
   "không đầu tư vào những thứ sẽ sụp. Nối với cổng 54 ở Gốc thành kênh Chuyển hoá."
 ),
 "aligned": (
   "Bạn dùng bản năng đó để chọn việc đáng làm và bỏ việc không đáng. Bạn kiên trì với thứ "
   "bạn cảm được là sẽ trụ. Đây là cổng rất giá trị trong đầu tư và trong xây dựng lâu dài."
 ),
 "misaligned": (
   "Bạn để nỗi sợ thất bại chặn mọi thứ, không dám bắt đầu gì. Hoặc bạn kiên trì với một thứ "
   "mà bản năng đã báo là sẽ không trụ, chỉ vì tiếc công đã bỏ ra."
 ),
 "practice": "Nhìn vào việc bạn đang cố duy trì lâu nhất. Hỏi bản năng chứ không hỏi lý trí: cái này có trụ được không?",
 "questions": [
   "Bạn đang tiếc công mà giữ lại thứ gì?",
   "Nỗi sợ thất bại đang chặn bạn khỏi việc gì?"
 ]
},

28: {
 "name_vi": "Người chơi",
 "kenh": "28-38 (Vật lộn) — nối xuống Gốc",
 "tagline": "Bạn đi tìm thứ đáng để đánh đổi cả đời. Cuộc tìm đó chính là ý nghĩa.",
 "mechanics": (
   "Cổng 28 là bản năng đi tìm điều đáng sống, quẻ gốc là Đại Quá — vượt quá mức chịu đựng. "
   "Nỗi sợ gốc là sợ đời mình trôi qua mà vô nghĩa. Hệ thống mô tả cổng này là người sẵn sàng "
   "đặt cược lớn. Nối với cổng 38 ở Gốc thành kênh Vật lộn."
 ),
 "aligned": (
   "Bạn chọn được vài thứ thật sự đáng và bạn dồn hết vào đó. Bạn cũng chấp nhận rằng nhiều "
   "cuộc đặt cược sẽ thua, và mỗi lần thua bạn biết thêm cái gì không đáng. Bạn sống một đời "
   "có chiều sâu vì bạn dám mất."
 ),
 "misaligned": (
   "Bạn đặt cược vào mọi thứ một cách bừa bãi, kể cả những chỗ không đáng. Hoặc bạn tê liệt "
   "vì nỗi sợ vô nghĩa, không dám chọn gì, và cuối cùng đúng là chẳng có gì."
 ),
 "practice": "Viết ra một câu: nếu chỉ được dồn hết vào một thứ trong ba năm tới, đó là gì.",
 "questions": [
   "Bạn có đang đặt cược vào những chỗ không đáng không?",
   "Điều gì đáng để bạn dồn hết vào?"
 ]
},

18: {
 "name_vi": "Sửa cho đúng",
 "kenh": "18-58 (Phán xét) — nối xuống Gốc",
 "tagline": "Bạn nhìn ra chỗ hỏng ngay lập tức. Cách bạn nói về nó quyết định tất cả.",
 "mechanics": (
   "Cổng 18 là bản năng phát hiện chỗ chưa hoàn thiện, quẻ gốc là Cổ — đồ vật đã hỏng cần "
   "sửa. Nỗi sợ gốc là sợ uy quyền: hệ thống mô tả cổng này thường bắt đầu bằng việc thách "
   "thức những gì cha mẹ và bề trên đặt ra. Nối với cổng 58 ở Gốc thành kênh Phán xét."
 ),
 "aligned": (
   "Bạn chỉ ra chỗ hỏng khi có người hỏi, và bạn chỉ vào việc chứ không vào người. Bạn trở "
   "thành người làm cho mọi thứ tốt lên thật sự. Bạn cũng phân biệt được đâu là chỗ đáng sửa "
   "và đâu là chỗ chỉ khác ý mình."
 ),
 "misaligned": (
   "Bạn chỉ trích liên tục dù không ai hỏi, và dần dần người ta tránh bạn. Hoặc bạn quay sự "
   "phê phán vào chính mình, và tự soi mòn lòng tự trọng của mình từng ngày."
 ),
 "practice": "Ba ngày liền, mỗi lần định chỉ ra chỗ sai, hỏi thầm: người này có đang hỏi mình không? Nếu không, giữ lại.",
 "questions": [
   "Bạn có hay chỉ trích khi không ai hỏi không?",
   "Bạn đang phê phán chính mình về điều gì?"
 ]
},

}
