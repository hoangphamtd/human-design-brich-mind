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
"""36 KÊNH — khối cuối của kho nội dung.

Kênh = cả hai cổng đều hoạt hoá. Kênh nối hai trung tâm và làm chúng được định nghĩa.
Ba mạch: cá thể (đột biến, tự thân) · tập thể (chia sẻ cho số đông) · bộ tộc (nuôi nhóm thân).

BẢN NỘI BỘ ĐẦY ĐỦ — chưa qua bộ lọc NĐ38.
"""

CHANNELS = {

# ═══════════ MẠCH CÁ THỂ — đột biến, tự thân, thường bị coi là kỳ lạ ═══════════

"1-8": {
 "name_vi": "Cảm hứng", "gates": [1, 8], "centers": ["g", "throat"], "mach": "cá thể",
 "tagline": "Bạn tạo ra thứ độc đáo, và bạn đưa được nó ra thế giới.",
 "mechanics": (
   "Cổng 1 ở Trung tâm G tạo ra cái riêng, cổng 8 ở Cổ họng mang nó ra ngoài. Đây là kênh "
   "của người có một dấu ấn không lẫn được và có khả năng làm cho người khác nhìn thấy dấu "
   "ấn đó. Vì thuộc mạch cá thể, nó vận hành theo nhịp riêng chứ không theo lịch."
 ),
 "aligned": (
   "Bạn làm cái của mình khi cảm hứng tới, và bạn trình bày nó ra đúng lúc có người sẵn sàng "
   "nhìn. Cái bạn tạo ra làm người khác muốn tạo ra cái của họ — đó là cách kênh này lan ra."
 ),
 "misaligned": (
   "Bạn ép sáng tạo theo lịch rồi ra thứ nhạt. Hoặc bạn giữ cái của mình trong ngăn kéo vì "
   "sợ chưa đủ hay, và cả kênh nằm im."
 ),
 "practice": "Đưa một thứ bạn đã làm ra cho đúng một người xem tuần này. Không giải thích, chỉ đưa.",
 "questions": ["Bạn đang giữ tác phẩm nào trong ngăn kéo?", "Ai là người xứng đáng được xem nó đầu tiên?"]
},

"2-14": {
 "name_vi": "Nhịp đập", "gates": [2, 14], "centers": ["g", "sacral"], "mach": "cá thể",
 "tagline": "Bạn biết hướng, và bạn có nhiên liệu để đi. Hiếm ai có cả hai.",
 "mechanics": (
   "Cổng 2 ở Trung tâm G biết phải đi đâu, cổng 14 ở Xương cùng mang sức để đi. Đây là kênh "
   "của người vừa có phương hướng vừa có nguồn lực vật chất — hệ thống mô tả nó là mạch của "
   "sự dẫn dắt bằng chính con đường mình đang đi."
 ),
 "aligned": (
   "Bạn phản hồi đúng thứ hợp hướng rồi dồn sức vào. Nguồn lực theo sau chứ không phải mục "
   "tiêu. Người khác nhìn hướng bạn đi mà tự chỉnh hướng của họ."
 ),
 "misaligned": (
   "Bạn dùng sức cho việc ra tiền nhưng sai hướng, rồi giàu mà rỗng. Hoặc bạn để người khác "
   "quyết hướng còn bạn chỉ đi làm."
 ),
 "practice": "Viết ra hướng bạn muốn đi trong năm năm. Rồi soi việc bạn đang dồn sức nhiều nhất — nó có nằm trên hướng đó không?",
 "questions": ["Bạn đang dồn sức vào đâu, và nó dẫn bạn tới đâu?", "Hướng đó là của bạn hay của ai?"]
},

"3-60": {
 "name_vi": "Đột biến", "gates": [3, 60], "centers": ["sacral", "root"], "mach": "cá thể",
 "tagline": "Cái mới ra đời khi bị nén, không phải khi thoải mái.",
 "mechanics": (
   "Cổng 60 ở Gốc là áp lực của giới hạn, cổng 3 ở Xương cùng là sức đưa trật tự vào cái vừa "
   "bật ra. Đây là kênh sinh ra đột biến: bị bó, nén lại, rồi bung thành cái chưa từng có. "
   "Nhịp của nó không đều — có giai đoạn tắc dài rồi bật đột ngột."
 ),
 "aligned": (
   "Bạn chịu được giai đoạn tắc mà không kết luận đời mình hỏng. Bạn làm hết mức trong khuôn "
   "khổ đang có. Khi cái mới bật ra, bạn sắp xếp được nó thành thứ dùng được."
 ),
 "misaligned": (
   "Bạn than về giới hạn và chờ nó biến mất. Hoặc bạn u uất trong giai đoạn tắc vì tưởng nó "
   "là vĩnh viễn — hệ thống mô tả đây là một trong những kênh dễ sinh buồn nặng nhất."
 ),
 "practice": "Giới hạn lớn nhất của bạn hiện giờ — viết ra ba việc bạn vẫn làm được bên trong nó.",
 "questions": ["Bạn đang tắc ở đâu, và tắc bao lâu rồi?", "Bạn có đang chờ điều gì biến mất mới bắt đầu không?"]
},

"10-20": {
 "name_vi": "Tỉnh thức", "gates": [10, 20], "centers": ["g", "throat"], "mach": "cá thể",
 "tagline": "Bạn nói ra cách sống của mình, ngay tại lúc này.",
 "mechanics": (
   "Cổng 10 ở Trung tâm G là cách hành xử và tình yêu với chính mình, cổng 20 ở Cổ họng nói "
   "ra cái đang thật ở khoảnh khắc hiện tại. Kênh này biến việc sống đúng với mình thành lời."
 ),
 "aligned": (
   "Bạn sống theo cách của mình và nói ra được nó một cách tự nhiên. Người nghe cảm được sự "
   "thật đó. Bạn không thuyết giảng — bạn chỉ đang là."
 ),
 "misaligned": (
   "Bạn nói về sống thật với chính mình trong khi đang sống theo khuôn của ai đó. Người tinh "
   "ý nhận ra sự vênh ngay lập tức."
 ),
 "practice": "Nói với một người thân một điều thật về cách bạn muốn sống, không kèm lời xin lỗi nào.",
 "questions": ["Cách bạn sống và cách bạn nói có khớp không?", "Bạn đang sống theo khuôn của ai?"]
},

"10-34": {
 "name_vi": "Thăm dò", "gates": [10, 34], "centers": ["g", "sacral"], "mach": "cá thể",
 "tagline": "Bạn có sức để đi tìm chính mình. Đó là việc của cả đời.",
 "mechanics": (
   "Cổng 34 ở Xương cùng là sức mạnh thuần, cổng 10 ở Trung tâm G là cách sống của mình. "
   "Kênh này dồn toàn bộ sức lực vào việc trở thành chính mình. Hệ thống mô tả đây là kênh "
   "của người tự tin theo cách rất riêng, và cũng dễ bị coi là ích kỷ."
 ),
 "aligned": (
   "Bạn dùng sức cho việc của mình và bạn trở nên rất thuyết phục vì bạn thật. Người ta không "
   "đi theo lời bạn nói mà đi theo cách bạn sống."
 ),
 "misaligned": (
   "Bạn dồn sức vào việc của người khác rồi đánh mất mình. Hoặc bạn bận rộn không ngừng mà "
   "không đi tới đâu — bận cho có bận."
 ),
 "practice": "Dành một buổi trọn vẹn tuần này làm việc của riêng bạn. Không giúp ai, không trả lời ai.",
 "questions": ["Sức của bạn đang chảy về đâu?", "Nếu không phải làm gì cho ai, bạn sẽ làm gì?"]
},

"10-57": {
 "name_vi": "Hình hài", "gates": [10, 57], "centers": ["g", "spleen"], "mach": "cá thể",
 "tagline": "Bản năng dẫn bạn sống đúng cách của mình, ngay trong khoảnh khắc.",
 "mechanics": (
   "Cổng 57 ở Lá lách là trực giác nhạy nhất trong bản đồ, cổng 10 ở Trung tâm G là cách hành "
   "xử. Kênh này để trực giác dẫn đường cho cách sống. Hệ thống mô tả nó gắn với sự sinh tồn "
   "ở tầng bản năng — biết ngay điều gì tốt cho mình."
 ),
 "aligned": (
   "Bạn nghe tín hiệu tức thời và điều chỉnh cách sống theo nó. Bạn ít khi rơi vào hoàn cảnh "
   "sai, vì bạn cảm được sớm và tránh trước."
 ),
 "misaligned": (
   "Bạn phủ quyết bản năng bằng lý lẽ, rồi ở lại trong những hoàn cảnh mà cơ thể đã báo động "
   "từ lâu. Hoặc bạn để nỗi sợ ngày mai chiếm chỗ của trực giác."
 ),
 "practice": "Ba ngày liền, làm theo phản ứng đầu tiên trong ba việc nhỏ. Ghi lại kết quả.",
 "questions": ["Bản năng bạn đang báo điều gì mà bạn chưa nghe?", "Nơi bạn đang ở — cơ thể bạn nói gì?"]
},

"12-22": {
 "name_vi": "Cởi mở", "gates": [12, 22], "centers": ["throat", "solar_plexus"], "mach": "cá thể",
 "tagline": "Có lúc bạn nói ra điều đẹp nhất. Có lúc bạn không nói nổi. Đó là nhịp, không phải lỗi.",
 "mechanics": (
   "Cổng 22 ở Đám rối mặt trời là sự cởi mở theo sóng cảm xúc, cổng 12 ở Cổ họng là khả năng "
   "diễn đạt mang màu tâm trạng. Kênh này chạy hoàn toàn theo sóng: khi lên, bạn nói ra được "
   "thứ chạm tới người khác; khi xuống, bạn đóng lại và không có gì để nói."
 ),
 "aligned": (
   "Bạn sắp xếp việc nói và việc gặp gỡ theo nhịp của mình. Khi đúng lúc, cái bạn nói ra có "
   "sức lay động mà người nói đều đều cả năm không có được. Đây là kênh của nghệ sĩ và người "
   "đứng trước đám đông."
 ),
 "misaligned": (
   "Bạn ép mình nói khi đang đóng, rồi ra thứ gượng. Hoặc bạn tự trách mình là người thất "
   "thường, khó gần."
 ),
 "practice": "Trước buổi nói quan trọng, tự chấm mình đang mở hay đóng. Nếu đóng mà dời được thì dời.",
 "questions": ["Bạn có tự trách mình vì hôm nay không nói hay bằng hôm qua không?", "Lần bạn nói hay nhất, tâm trạng lúc đó thế nào?"]
},

"20-34": {
 "name_vi": "Sức hút", "gates": [20, 34], "centers": ["throat", "sacral"], "mach": "cá thể",
 "tagline": "Bạn nói là bạn làm ngay. Sức hút của bạn đến từ chỗ đó.",
 "mechanics": (
   "Cổng 34 ở Xương cùng là sức mạnh thuần, cổng 20 ở Cổ họng là biểu đạt của khoảnh khắc "
   "hiện tại. Đây là kênh duy nhất nối thẳng Xương cùng lên Cổ họng — nó biến người có nó "
   "thành Manifesting Generator. Sức và lời đi cùng nhau, gần như không có độ trễ."
 ),
 "aligned": (
   "Bạn phản hồi rồi bật ra hành động ngay. Bạn làm được nhiều thứ cùng lúc và làm nhanh. "
   "Người khác đứng gần bạn cũng thấy hăng lên — đó là sức hút thật, không phải kỹ thuật."
 ),
 "misaligned": (
   "Bạn nói và làm trước khi cơ thể kịp xác nhận, rồi phải quay lại dọn. Hoặc bạn bận rộn "
   "liên tục mà không hướng, và sức hút biến thành sự ồn ào."
 ),
 "practice": "Trước ba hành động tuần này, báo trước một câu cho người bị ảnh hưởng. Xem sức cản giảm bao nhiêu.",
 "questions": ["Bạn có hay làm xong rồi mới nói không?", "Bạn bận có hướng hay bận cho có?"]
},

"20-57": {
 "name_vi": "Sóng não", "gates": [20, 57], "centers": ["throat", "spleen"], "mach": "cá thể",
 "tagline": "Trực giác của bạn bật ra thành lời, đúng một lần, ngay lúc đó.",
 "mechanics": (
   "Cổng 57 ở Lá lách là trực giác, cổng 20 ở Cổ họng nói ra khoảnh khắc hiện tại. Kênh này "
   "biến cái biết bản năng thành lời gần như tức thời. Hệ thống mô tả đây là kênh của sự "
   "sáng suốt trong khoảnh khắc — không lý luận, không nhắc lại."
 ),
 "aligned": (
   "Bạn nói ra cái mình vừa cảm được, đúng lúc có người hỏi. Điều bạn nói thường chính xác "
   "một cách kỳ lạ, và người nghe nhớ rất lâu."
 ),
 "misaligned": (
   "Bạn nói ra khi chưa ai hỏi, và bị coi là phán bừa. Hoặc bạn nghi ngờ chính trực giác của "
   "mình rồi im, và cái biết đó tan mất."
 ),
 "practice": "Tuần này giữ lại một nhận định cho tới khi có người hỏi. So sánh cách họ đón nhận.",
 "questions": ["Bạn có hay nói ra trước khi ai hỏi không?", "Lần gần nhất bạn nghi ngờ trực giác mình — kết cục thế nào?"]
},

"23-43": {
 "name_vi": "Cấu trúc", "gates": [23, 43], "centers": ["throat", "ajna"], "mach": "cá thể",
 "tagline": "Bạn biết một điều lạ và bạn nói được nó ra. Nhưng chỉ khi đúng lúc.",
 "mechanics": (
   "Cổng 43 ở Ajna là cái biết đột ngột từ bên trong, cổng 23 ở Cổ họng biến nó thành ngôn "
   "ngữ. Đây là kênh của thiên tài và của kẻ lập dị — cùng một nội dung, khác nhau ở thời "
   "điểm nói. Hệ thống mô tả nó là kênh mang cái mới vào ngôn ngữ chung."
 ),
 "aligned": (
   "Bạn chờ có người hỏi rồi nói, và cái bạn nói làm họ đổi cách nhìn. Bạn diễn đạt được "
   "điều mà người khác chỉ mơ hồ cảm thấy."
 ),
 "misaligned": (
   "Bạn nói khi chưa ai sẵn sàng nghe, rồi bị gạt. Lặp nhiều lần, bạn im hẳn và mang cảm giác "
   "cô đơn dai dẳng — biết một điều mà không ai chia sẻ được."
 ),
 "practice": "Điều bạn muốn nói với ai đó — giữ lại tới khi họ hỏi. Nếu một tháng không ai hỏi, viết ra thay vì nói.",
 "questions": ["Bạn đang chờ ai hỏi mình điều gì?", "Bạn có hay bị coi là nói chuyện khó hiểu không?"]
},

"24-61": {
 "name_vi": "Nhận biết", "gates": [24, 61], "centers": ["ajna", "head"], "mach": "cá thể",
 "tagline": "Cùng một câu hỏi lớn quay lại mãi, cho tới ngày nó tự mở.",
 "mechanics": (
   "Cổng 61 ở Đầu là áp lực muốn biết cái không biết được, cổng 24 ở Ajna quay lại câu hỏi "
   "đó hết lần này tới lần khác. Kênh này chạy vòng lặp: nghĩ, buông, nghĩ lại, cho tới lúc "
   "vỡ ra. Hệ thống mô tả nó là kênh của người đào rất sâu một chủ đề trong nhiều năm."
 ),
 "aligned": (
   "Bạn cho phép vòng lặp chạy mà không ép nó phải xong. Cái hiểu đến khi nó đến, thường bất "
   "chợt. Bạn thành người nói ra được điều mà người lướt qua không thấy."
 ),
 "misaligned": (
   "Bạn tự trách vì cứ nghĩ mãi một chuyện, hoặc cố quên đi. Kênh này cũng dễ chuyển thành "
   "vòng lặp hành vi — quay lại một thói quen dù biết không tốt."
 ),
 "practice": "Câu hỏi hay quay lại nhất với bạn — mỗi tuần viết một đoạn ngắn về nó, mười tuần liền, không cần kết luận.",
 "questions": ["Chuyện gì bạn nghĩ đi nghĩ lại nhiều năm rồi?", "Có hành vi nào bạn cứ quay lại dù biết không tốt không?"]
},

"25-51": {
 "name_vi": "Khởi phát", "gates": [25, 51], "centers": ["g", "heart"], "mach": "cá thể",
 "tagline": "Cú sốc đẩy bạn vào một tầng nhận thức mới. Đó là cách kênh này vận hành.",
 "mechanics": (
   "Cổng 51 ở Tim là năng lượng gây sốc và cạnh tranh, cổng 25 ở Trung tâm G là tinh thần "
   "hồn nhiên yêu mọi thứ như nhau. Kênh này đưa người ta qua những cú va để mở ra tầng nhận "
   "thức mới. Hệ thống mô tả đây là kênh của người khai tâm cho người khác."
 ),
 "aligned": (
   "Bạn dám đi trước, dám làm điều người khác chưa dám, và giữ được sự hồn nhiên qua các cú "
   "va. Bạn hồi phục nhanh — thứ làm người khác gục thì làm bạn tỉnh ra."
 ),
 "misaligned": (
   "Bạn gây sốc chỉ để chứng tỏ mình. Hoặc bạn cứng lại sau vài lần tổn thương và mất luôn "
   "phần hồn nhiên — lúc đó kênh chỉ còn lại sự hung hăng."
 ),
 "practice": "Nhớ lại cú sốc lớn nhất đời bạn. Viết ra điều nó mở ra mà không có nó thì không có.",
 "questions": ["Bạn có cứng lại sau lần tổn thương nào không?", "Bạn đang cạnh tranh với ai không đáng?"]
},

"28-38": {
 "name_vi": "Vật lộn", "gates": [28, 38], "centers": ["spleen", "root"], "mach": "cá thể",
 "tagline": "Bạn đi tìm thứ đáng để đánh đổi cả đời. Cuộc tìm đó chính là ý nghĩa.",
 "mechanics": (
   "Cổng 38 ở Gốc là áp lực chiến đấu, cổng 28 ở Lá lách là bản năng đi tìm điều đáng sống. "
   "Kênh này mang nỗi sợ đời mình trôi qua vô nghĩa, và biến nỗi sợ đó thành sức để đấu tranh. "
   "Hệ thống mô tả đây là kênh của người sẵn sàng đặt cược lớn."
 ),
 "aligned": (
   "Bạn chọn kỹ trận nào đáng đánh rồi dồn hết. Mỗi lần thua bạn biết thêm cái gì không đáng. "
   "Đời bạn có chiều sâu vì bạn dám mất."
 ),
 "misaligned": (
   "Bạn đấu với mọi thứ, kể cả chuyện không đáng, rồi kiệt và cô lập. Hoặc bạn tê liệt vì nỗi "
   "sợ vô nghĩa, không dám chọn gì."
 ),
 "practice": "Liệt kê những thứ bạn đang chống lại. Chọn một cái đáng nhất, buông hai cái không đáng.",
 "questions": ["Bạn đang đánh bao nhiêu trận cùng lúc?", "Điều gì đáng để bạn dồn hết vào?"]
},

"34-57": {
 "name_vi": "Sức mạnh", "gates": [34, 57], "centers": ["sacral", "spleen"], "mach": "cá thể",
 "tagline": "Sức của bạn được bản năng dẫn đường. Không cần nghĩ nhiều.",
 "mechanics": (
   "Cổng 57 ở Lá lách là trực giác, cổng 34 ở Xương cùng là sức mạnh thuần. Kênh này để bản "
   "năng dẫn sức lực. Hệ thống mô tả nó gắn với sự sinh tồn và với khả năng biết ngay nên "
   "dồn sức vào đâu."
 ),
 "aligned": (
   "Bạn cảm được ngay việc nào đáng dồn sức và bạn vào việc luôn. Bạn hiếm khi phí sức, vì "
   "bản năng đã lọc trước."
 ),
 "misaligned": (
   "Bạn để cái đầu phủ quyết bản năng rồi đổ sức vào việc sai. Hoặc bạn hoài nghi chính mình "
   "tới mức không dám hành động."
 ),
 "practice": "Trước việc lớn tiếp theo, để ý phản ứng đầu tiên trong cơ thể trước khi phân tích. Ghi lại rồi đối chiếu sau.",
 "questions": ["Bạn có hay dùng lý lẽ để phủ quyết cảm nhận không?", "Sức bạn đang đổ vào đâu?"]
},

"39-55": {
 "name_vi": "Cảm xúc", "gates": [39, 55], "centers": ["root", "solar_plexus"], "mach": "cá thể",
 "tagline": "Bạn khiêu khích để người khác lộ ra tinh thần thật của họ.",
 "mechanics": (
   "Cổng 39 ở Gốc là áp lực khiêu khích, cổng 55 ở Đám rối mặt trời là tinh thần lúc đầy lúc "
   "vơi. Kênh này chạy theo sóng rất mạnh và mang tính khiêu khích: bạn tạo trở ngại, phản "
   "ứng của người kia cho thấy họ là ai. Hệ thống mô tả đây là kênh của tinh thần và nghệ thuật."
 ),
 "aligned": (
   "Bạn khiêu khích đúng người đúng lúc để đẩy họ vượt chỗ đang kẹt. Bạn cũng thôi đi tìm "
   "nguyên nhân bên ngoài cho tâm trạng của mình — đó là chỗ nhiều xung đột gia đình tự tan."
 ),
 "misaligned": (
   "Bạn chọc bừa lúc trong người khó chịu, gây tổn thương không cần thiết. Hoặc mỗi lần xuống "
   "tinh thần bạn đi tìm thủ phạm, và người gần nhất lãnh đủ."
 ),
 "practice": "Ba mươi ngày chấm tinh thần từ 1 tới 10, không ghi lý do. Cuối kỳ nhìn biểu đồ.",
 "questions": ["Lần gần nhất xuống tinh thần, bạn đổ cho ai?", "Bạn chọc người khác để giúp họ hay để xả?"]
},

# ═══════════ MẠCH TẬP THỂ — chia sẻ cho số đông, logic và trải nghiệm ═══════════

"4-63": {
 "name_vi": "Logic", "gates": [4, 63], "centers": ["ajna", "head"], "mach": "tập thể",
 "tagline": "Bạn nghi ngờ, rồi bạn đưa ra một công thức. Công thức đó cần thời gian kiểm chứng.",
 "mechanics": (
   "Cổng 63 ở Đầu là áp lực nghi ngờ, cổng 4 ở Ajna đáp lại bằng một cách giải thích khả dĩ. "
   "Đây là khởi điểm của toàn bộ mạch logic. Điểm cốt lõi: câu trả lời của kênh này là **giả "
   "thuyết**, chưa phải sự thật."
 ),
 "aligned": (
   "Bạn hướng nghi ngờ vào những thứ bên ngoài cần kiểm tra, và bạn đưa giải pháp kèm câu "
   "'thử xem sao'. Bạn phát hiện lỗ hổng trước khi nó thành tai nạn."
 ),
 "misaligned": (
   "Bạn quay nghi ngờ vào chính mình và người thân, soi mòn cả hai. Hoặc bạn tin công thức "
   "của mình là chân lý rồi áp lên người khác."
 ),
 "practice": "Mỗi lần nghi ngờ nổi lên, viết một dòng: nghi cái gì, có kiểm chứng được không. Cái nào không kiểm chứng được thì gạch.",
 "questions": ["Bạn đang nghi ngờ điều gì mà không có cách nào kiểm chứng?", "Công thức nào bạn đang áp lên đời mình chưa kiểm chứng?"]
},

"5-15": {
 "name_vi": "Nhịp điệu", "gates": [5, 15], "centers": ["sacral", "g"], "mach": "tập thể",
 "tagline": "Bạn có nhịp riêng, và nhịp đó dao động nhiều hơn người khác.",
 "mechanics": (
   "Cổng 5 ở Xương cùng là nhịp sinh học cố định, cổng 15 ở Trung tâm G là biên độ cực đoan. "
   "Kênh này ghép sự đều đặn với sự dao động: bạn cần nhịp, nhưng nhịp của bạn không giống "
   "khuôn chung. Hệ thống mô tả nó gắn với dòng chảy tự nhiên của sự sống."
 ),
 "aligned": (
   "Bạn tìm ra nhịp thật của mình và bảo vệ nó. Bạn cũng chấp nhận rằng có giai đoạn mình rất "
   "kỷ luật, có giai đoạn lộn xộn — và cả hai đều là mình."
 ),
 "misaligned": (
   "Bạn ép mình theo lịch của người khác rồi thấy trong người lệch lạc. Hoặc bạn tự trách vì "
   "không giữ được kỷ luật đều đặn như thiên hạ."
 ),
 "practice": "Ghi nhật ký giờ giấc ba mươi ngày. Bạn sẽ thấy nhịp thật, không phải nhịp bạn nghĩ mình nên có.",
 "questions": ["Nhịp thật của bạn là gì nếu không ai can thiệp?", "Ai đang phá nhịp của bạn nhiều nhất?"]
},

"7-31": {
 "name_vi": "Người dẫn", "gates": [7, 31], "centers": ["g", "throat"], "mach": "tập thể",
 "tagline": "Bạn dẫn được — nhưng chỉ khi người ta đã chọn bạn.",
 "mechanics": (
   "Cổng 7 ở Trung tâm G là vai lãnh đạo, cổng 31 ở Cổ họng là tiếng nói dẫn dắt. Kênh này "
   "làm nên người đứng đầu trong mạch tập thể. Điểm quyết định: quyền dẫn đến từ việc **được "
   "bầu**, không từ việc tự nhận."
 ),
 "aligned": (
   "Bạn lên tiếng khi nhóm đã tin và đã chọn. Lời bạn nói được cả nhóm đi theo. Bạn cũng biết "
   "vai này không vĩnh viễn, hết nhiệm kỳ thì trả lại."
 ),
 "misaligned": (
   "Bạn tự nhận vai dẫn khi chưa ai chọn, và nhóm không theo. Hoặc bạn dẫn vì thích quyền, "
   "và người ta rời đi dần."
 ),
 "practice": "Hỏi ba người trong nhóm: nếu được chọn lại, họ có chọn bạn không. Nghe mà không thanh minh.",
 "questions": ["Bạn đang dẫn vì được chọn hay vì tự nhận?", "Bạn dẫn vì lợi ích chung hay vì vị trí đó?"]
},

"9-52": {
 "name_vi": "Chuyên chú", "gates": [9, 52], "centers": ["sacral", "root"], "mach": "tập thể",
 "tagline": "Bạn ngồi yên được rất lâu và cắm vào chi tiết rất sâu.",
 "mechanics": (
   "Cổng 52 ở Gốc là áp lực dừng lại, cổng 9 ở Xương cùng là sức tập trung vào chi tiết. Kênh "
   "này nén năng lượng thành sự bất động rồi dồn hết vào một điểm. Hệ thống mô tả nó là kênh "
   "của sự quyết tâm bền bỉ."
 ),
 "aligned": (
   "Bạn chọn đúng chi tiết đáng chú tâm rồi làm tới nơi. Bạn hoàn thiện được những phần mà "
   "người khác thấy chán. Đây là lợi thế lớn ở bất kỳ nghề nào cần độ chính xác."
 ),
 "misaligned": (
   "Bạn dồn hết vào một chi tiết không quan trọng và bỏ lỡ bức tranh lớn. Hoặc bạn ngồi yên "
   "quá lâu thành trì trệ."
 ),
 "practice": "Trước khi cắm đầu vào việc tiếp theo, viết một câu: việc này đóng góp gì cho mục tiêu lớn hơn.",
 "questions": ["Bạn có đang dồn sức vào chi tiết không quan trọng không?", "Bức tranh lớn của bạn là gì?"]
},

"11-56": {
 "name_vi": "Tò mò", "gates": [11, 56], "centers": ["ajna", "throat"], "mach": "tập thể",
 "tagline": "Ý tưởng đến với bạn để bạn kể lại, không phải để bạn đi làm.",
 "mechanics": (
   "Cổng 11 ở Ajna là kho ý tưởng, cổng 56 ở Cổ họng kể chúng thành chuyện. Đây là chỗ hay "
   "bị hiểu sai nhất trong bản đồ: ý tưởng của kênh này **không phải để thực hiện**. Chúng "
   "là chất liệu để truyền cảm hứng."
 ),
 "aligned": (
   "Bạn kể ý tưởng cho người khác nghe, ai cần thì nhặt lấy. Bạn trở thành nguồn cảm hứng mà "
   "không phải gánh trách nhiệm thực hiện. Đây là kênh rất mạnh cho việc dạy học và dẫn chuyện."
 ),
 "misaligned": (
   "Bạn thấy ý tưởng hay rồi lao vào làm, hết cái này tới cái khác, không cái nào tới nơi. "
   "Rồi bạn tự trách mình là kiểu người nhiều ý mà chẳng làm được gì."
 ),
 "practice": "Lập sổ ý tưởng. Ghi vào, kể cho ít nhất một người, và không tự nhận làm cái nào trong ba mươi ngày.",
 "questions": ["Bạn đang ôm bao nhiêu ý tưởng chưa làm?", "Ai quanh bạn đang cần đúng ý tưởng bạn đang giữ?"]
},

"13-33": {
 "name_vi": "Đứa con hoang", "gates": [13, 33], "centers": ["g", "throat"], "mach": "tập thể",
 "tagline": "Người ta kể cho bạn nghe, bạn rút lui để tiêu hoá, rồi bạn kể lại.",
 "mechanics": (
   "Cổng 13 ở Trung tâm G thu nhận câu chuyện của người khác, cổng 33 ở Cổ họng rút lui rồi "
   "kể lại thành bài học. Hệ thống mô tả đây là kênh giữ ký ức tập thể — người nhớ chuyện đã "
   "qua để thế hệ sau khỏi lặp lại."
 ),
 "aligned": (
   "Bạn nghe mà không phán xét, giữ được bí mật, và biết chọn cái gì nên kể lại. Bạn cho mình "
   "khoảng lặng sau mỗi chặng để tiêu hoá."
 ),
 "misaligned": (
   "Bạn ôm hết chuyện thiên hạ mà không đặt xuống được. Hoặc bạn kể lại chuyện của người khác "
   "không đúng chỗ, và mất lòng tin — với kênh này, mất rồi rất khó lấy lại."
 ),
 "practice": "Sau lần nghe chuyện nặng tiếp theo, viết ra một trang rồi xé đi.",
 "questions": ["Bạn đang mang chuyện của ai mà chưa đặt xuống?", "Bạn có cho mình khoảng lặng sau mỗi chặng không?"]
},

"16-48": {
 "name_vi": "Bước sóng", "gates": [16, 48], "centers": ["throat", "spleen"], "mach": "tập thể",
 "tagline": "Bạn có chiều sâu và bạn có sự hăng hái. Nghề của bạn nằm ở chỗ đó.",
 "mechanics": (
   "Cổng 48 ở Lá lách là chiều sâu năng lực kèm nỗi sợ không đủ giỏi, cổng 16 ở Cổ họng là "
   "sự hăng hái nhảy vào thử. Kênh này biến chiều sâu thành tài năng thực. Hệ thống mô tả nó "
   "là kênh của người có nghề — nghệ sĩ, thợ giỏi, chuyên gia."
 ),
 "aligned": (
   "Bạn để nhiệt tình dẫn vào một thứ rồi luyện cho tới thành thạo thật. Bạn dùng nỗi sợ chưa "
   "đủ giỏi làm động lực học tiếp chứ không để nó chặn."
 ),
 "misaligned": (
   "Bạn nhảy vào rồi bỏ khi hết hứng, hết lần này tới lần khác. Hoặc bạn chờ đủ giỏi mới dám "
   "ra mắt — và ngày đó không tới."
 ),
 "practice": "Chọn một kỹ năng bạn từng hào hứng rồi bỏ dở. Luyện lại ba mươi ngày, mỗi ngày mười lăm phút.",
 "questions": ["Bạn đang chờ đủ giỏi để làm gì?", "Bạn đã bỏ dở bao nhiêu thứ ngay sau khi hết hứng?"]
},

"17-62": {
 "name_vi": "Chấp nhận", "gates": [17, 62], "centers": ["ajna", "throat"], "mach": "tập thể",
 "tagline": "Bạn có ý kiến kèm chi tiết chứng minh. Ý kiến vẫn không phải sự thật.",
 "mechanics": (
   "Cổng 17 ở Ajna sinh ra ý kiến dựa trên mẫu hình đã quan sát, cổng 62 ở Cổ họng diễn đạt "
   "nó thành chi tiết cụ thể. Kênh này làm nên người tổ chức: bạn có quan điểm và bạn chứng "
   "minh được bằng dữ kiện."
 ),
 "aligned": (
   "Bạn chờ được hỏi rồi đưa ý kiến, và nói rõ đó là ý kiến. Người ta tìm bạn khi cần một góc "
   "nhìn có cơ sở. Bạn cũng biết sắp xếp mớ hỗn độn thành thứ trình bày được."
 ),
 "misaligned": (
   "Bạn đưa ý kiến cho mọi thứ dù không ai hỏi, rồi người ta ngại nói chuyện với bạn. Hoặc "
   "bạn nhầm ý kiến là sự thật rồi tranh cãi để bảo vệ."
 ),
 "practice": "Ba ngày, đếm số lần bạn đưa ý kiến khi không ai hỏi. Chỉ đếm, không sửa.",
 "questions": ["Bạn có hay đưa ý kiến khi không được hỏi không?", "Ý kiến nào của bạn đang được coi như sự thật?"]
},

"18-58": {
 "name_vi": "Phán xét", "gates": [18, 58], "centers": ["spleen", "root"], "mach": "tập thể",
 "tagline": "Bạn thấy chỗ hỏng ngay. Niềm vui của bạn là làm nó tốt lên.",
 "mechanics": (
   "Cổng 58 ở Gốc là áp lực của niềm vui sống, cổng 18 ở Lá lách là bản năng phát hiện chỗ "
   "chưa hoàn thiện. Kênh này ghép niềm vui với nhu cầu sửa: bạn vui khi mọi thứ tốt lên. "
   "Cổng 18 mang nỗi sợ uy quyền, nên kênh này thường bắt đầu bằng việc thách thức bề trên."
 ),
 "aligned": (
   "Bạn chỉ ra chỗ hỏng khi có người hỏi, và chỉ vào việc chứ không vào người. Bạn làm cho "
   "mọi thứ quanh mình tốt lên thật, và niềm vui của bạn lây sang người khác."
 ),
 "misaligned": (
   "Bạn phê phán liên tục dù không ai hỏi, và người ta tránh bạn. Hoặc bạn quay sự phê phán "
   "vào chính mình, soi mòn lòng tự trọng từng ngày."
 ),
 "practice": "Ba ngày, mỗi lần định chỉ ra chỗ sai, hỏi thầm: người này có đang hỏi mình không?",
 "questions": ["Bạn đang muốn sửa ai mà không ai nhờ?", "Bạn đang phê phán chính mình về điều gì?"]
},

"29-46": {
 "name_vi": "Khám phá", "gates": [29, 46], "centers": ["sacral", "g"], "mach": "tập thể",
 "tagline": "Bạn nói có với những thứ chưa biết trước kết quả. Đó vừa là sức mạnh vừa là bẫy.",
 "mechanics": (
   "Cổng 29 ở Xương cùng là sức cam kết, cổng 46 ở Trung tâm G là tình yêu với cơ thể và sự "
   "có mặt đúng chỗ. Kênh này đưa người ta vào những trải nghiệm sâu mà không biết trước sẽ "
   "ra sao. Hệ thống mô tả nó là kênh của sự thành công qua kiên trì."
 ),
 "aligned": (
   "Bạn chỉ cam kết khi bụng thật sự gật, và khi đã gật thì đi tới cùng. Bạn hay rơi vào những "
   "tình huống tình cờ mà hoá ra đúng — đó là cơ chế của kênh, không phải may."
 ),
 "misaligned": (
   "Bạn nói có bằng cái đầu rồi mắc kẹt nhiều năm. Đây là kênh dễ dẫn tới kiệt sức nhất, vì "
   "bạn có sức chịu đựng rất lâu trong thứ sai."
 ),
 "practice": "Trước cam kết tiếp theo, xin hai mươi tư giờ. Để ý bụng mình mỗi lần nghĩ tới việc đó.",
 "questions": ["Bạn đang mắc kẹt trong cam kết nào mà bụng chưa bao giờ muốn?", "Bạn có hay nói có cho xong chuyện không?"]
},

"30-41": {
 "name_vi": "Nhận ra", "gates": [30, 41], "centers": ["solar_plexus", "root"], "mach": "tập thể",
 "tagline": "Một khao khát dâng lên trước cả khi bạn biết mình thèm gì.",
 "mechanics": (
   "Cổng 41 ở Gốc là áp lực nén trước khi bung — điểm khởi đầu của cả bánh xe. Cổng 30 ở Đám "
   "rối mặt trời là ngọn lửa khao khát. Kênh này khởi động mọi trải nghiệm: thèm muốn dâng "
   "lên, rồi mới dần rõ là thèm cái gì."
 ),
 "aligned": (
   "Bạn chịu được cảm giác thèm một thứ chưa rõ hình dạng, và chờ cho tới khi nó rõ. Trí tưởng "
   "tượng của bạn rất mạnh, và bạn dùng nó làm nhiên liệu chứ không làm nơi trốn."
 ),
 "misaligned": (
   "Bạn vơ đại một thứ để lấp — mua sắm, ăn uống, một mối quan hệ mới — rồi nó không lấp được. "
   "Hoặc bạn tin rằng đạt được thứ đó xong sẽ hết cháy, và khi vẫn cháy thì hụt hẫng sâu."
 ),
 "practice": "Khi thấy thèm mà không rõ thèm gì, viết ba dòng mô tả cảm giác đó. Không mua gì trong hai mươi tư giờ.",
 "questions": ["Bạn có hay mua hoặc ăn để lấp một cảm giác mơ hồ không?", "Khao khát nào đang dẫn bạn đi mà chưa xét lại?"]
},

"35-36": {
 "name_vi": "Vô thường", "gates": [35, 36], "centers": ["throat", "solar_plexus"], "mach": "tập thể",
 "tagline": "Cái gì bạn cũng thử qua rồi. Câu hỏi là bạn rút được gì.",
 "mechanics": (
   "Cổng 36 ở Đám rối mặt trời lao vào trải nghiệm chưa từng có, cổng 35 ở Cổ họng kể lại "
   "trải nghiệm đó. Kênh này chạy theo sóng: khao khát cái mới, nhảy vào, vỡ mộng, rồi lại "
   "khao khát. Hệ thống mô tả nó là kênh của sự thay đổi và của người từng trải."
 ),
 "aligned": (
   "Bạn chờ qua sóng trước khi nhảy vào cái mới, và mỗi trải nghiệm bạn rút được điều gì đó "
   "để kể lại. Bạn thành người có vốn sống thật, không phải người đọc sách."
 ),
 "misaligned": (
   "Bạn nhảy từ cái mới này sang cái mới khác mà không đọng lại gì. Cảm giác chán ngay sau "
   "khi đạt được điều mình muốn là dấu hiệu quen thuộc nhất."
 ),
 "practice": "Liệt kê năm trải nghiệm lớn đã qua. Mỗi cái viết một câu về điều học được. Cái nào không viết được là cái chưa tiêu hoá xong.",
 "questions": ["Bạn có hay chán ngay sau khi đạt được thứ mình muốn không?", "Trải nghiệm nào bạn đi qua mà chưa rút ra được gì?"]
},

"42-53": {
 "name_vi": "Trưởng thành", "gates": [42, 53], "centers": ["sacral", "root"], "mach": "tập thể",
 "tagline": "Mở đầu rồi đi hết. Cả hai đầu đều cần, và bạn có cả hai.",
 "mechanics": (
   "Cổng 53 ở Gốc là áp lực bắt đầu chu kỳ mới, cổng 42 ở Xương cùng là sức đi hết chu kỳ đó. "
   "Kênh này cho người ta khả năng mở ra và đóng lại trọn vẹn. Hệ thống mô tả sự trưởng thành "
   "đến từ việc hoàn tất, không từ việc bắt đầu."
 ),
 "aligned": (
   "Bạn chỉ bắt đầu thứ mình định đi hết, và bạn đi hết. Việc hoàn tất trọn vẹn một chu kỳ "
   "cho bạn sự trưởng thành mà bỏ dở không bao giờ cho được."
 ),
 "misaligned": (
   "Bạn bỏ ngang rồi bắt cái mới, hết lần này tới lần khác, và không bao giờ có cảm giác hoàn "
   "tất. Hoặc bạn cố kéo dài một chu kỳ đã tới lúc kết thúc."
 ),
 "practice": "Chọn một việc đang bỏ dở. Hoặc làm xong trong ba mươi ngày, hoặc chính thức khai tử. Không để lửng.",
 "questions": ["Bạn đang để lửng bao nhiêu việc?", "Có chu kỳ nào đã tới lúc kết thúc mà bạn vẫn cố kéo không?"]
},

"47-64": {
 "name_vi": "Trừu tượng", "gates": [47, 64], "centers": ["ajna", "head"], "mach": "tập thể",
 "tagline": "Đầu bạn đầy mảnh hình ảnh rối. Chúng sẽ ghép lại, nhưng theo nhịp riêng.",
 "mechanics": (
   "Cổng 64 ở Đầu là áp lực của những hình ảnh quá khứ chưa xử lý xong, cổng 47 ở Ajna dần "
   "ghép chúng thành ý nghĩa. Quẻ gốc của cổng 47 là Khốn — bị vây. Giai đoạn bí là phần bắt "
   "buộc của quá trình, không phải sự cố."
 ),
 "aligned": (
   "Bạn để mớ hình ảnh chạy mà không ép phải hiểu ngay. Sự sáng tỏ đến bất chợt, thường lúc "
   "bạn đang làm việc khác. Khi hiểu ra, bạn kể lại được cho người khác dùng."
 ),
 "misaligned": (
   "Bạn ép mình phải hiểu ngay, càng ép càng rối. Hoặc bạn vơ đại một lời giải thích cho đỡ "
   "khó chịu rồi sống theo cách hiểu sai suốt nhiều năm."
 ),
 "practice": "Lần tới khi đầu rối, đứng dậy làm việc chân tay ba mươi phút. Đừng cố nghĩ cho ra.",
 "questions": ["Bạn đang bí ở chỗ nào, và bao lâu rồi?", "Bạn có đang vơ một lời giải thích cho xong không?"]
},

# ═══════════ MẠCH BỘ TỘC — nuôi nhóm thân, thoả thuận, tài nguyên ═══════════

"6-59": {
 "name_vi": "Kết đôi", "gates": [6, 59], "centers": ["solar_plexus", "sacral"], "mach": "bộ tộc",
 "tagline": "Bạn phá được rào cản của người khác. Và bạn cũng có rào của riêng mình.",
 "mechanics": (
   "Cổng 59 ở Xương cùng là sức phá vỡ rào cản để đi tới thân mật, cổng 6 ở Đám rối mặt trời "
   "là lớp màng đóng mở theo sóng cảm xúc. Hệ thống nối kênh này với khả năng sinh sản và với "
   "sự gần gũi ở tầng sâu nhất."
 ),
 "aligned": (
   "Bạn đi qua rào cản của người khác khi họ sẵn sàng, và bạn tôn trọng nhịp đóng mở của chính "
   "mình. Bạn nói ra cho người thân hiểu nhịp đó. Từ đó quan hệ lành mạnh hơn nhiều."
 ),
 "misaligned": (
   "Bạn xuyên qua ranh giới người khác khi họ chưa cho phép. Hoặc bạn nổ ra xung đột ngay lúc "
   "cảm xúc dâng, rồi hối. Hoặc bạn đóng chặt mãi rồi cô đơn trong chính quan hệ của mình."
 ),
 "practice": "Lần tới thấy muốn nổ, viết ra hết rồi để hai ngày. Đọc lại trước khi nói.",
 "questions": ["Người thân bạn có hiểu nhịp đóng mở của bạn không?", "Bạn tìm gần gũi để kết nối hay để lấp trống?"]
},

"19-49": {
 "name_vi": "Tổng hợp", "gates": [19, 49], "centers": ["root", "solar_plexus"], "mach": "bộ tộc",
 "tagline": "Bạn cảm được nhóm mình thiếu gì, và bạn có nguyên tắc về ai được vào.",
 "mechanics": (
   "Cổng 19 ở Gốc là áp lực nhận biết nhu cầu của nhóm, cổng 49 ở Đám rối mặt trời là nguyên "
   "tắc chấp nhận hay từ chối. Kênh này quyết định ai thuộc về nhóm và nhóm cần gì. Hệ thống "
   "mô tả nó gắn với sự nhạy cảm rất cao, cả với người lẫn với con vật."
 ),
 "aligned": (
   "Bạn nói ra nhu cầu của mình thay vì chờ người ta đoán, và bạn nói rõ nguyên tắc từ đầu "
   "thay vì để người ta vi phạm rồi mới cắt. Bạn giữ cho nhóm không ai bị bỏ rơi."
 ),
 "misaligned": (
   "Bạn nhạy với nhu cầu mọi người nhưng giấu nhu cầu của mình rồi ấm ức. Hoặc bạn cắt đứt "
   "đột ngột mà người kia không hiểu tại sao."
 ),
 "practice": "Nói thẳng một nhu cầu của bạn với người thân, bằng câu đơn giản: mình cần điều này.",
 "questions": ["Bạn có chờ người khác đoán ra nhu cầu của mình không?", "Bạn từng cắt ai đó đột ngột mà họ không hiểu lý do chưa?"]
},

"21-45": {
 "name_vi": "Tiền bạc", "gates": [21, 45], "centers": ["heart", "throat"], "mach": "bộ tộc",
 "tagline": "Bạn trông coi tài nguyên của nhóm. Trong địa hạt của mình, bạn phải được tự quyết.",
 "mechanics": (
   "Cổng 21 ở Tim là ý chí kiểm soát tài nguyên, cổng 45 ở Cổ họng là tiếng nói của người "
   "đứng đầu. Kênh này làm nên người chủ — người vừa có ý chí giành giữ vừa có quyền phân "
   "chia. Hệ thống mô tả nó là kênh gắn với vật chất trong mạch bộ tộc."
 ),
 "aligned": (
   "Bạn kiểm soát đúng phần thuộc về mình và làm rất tốt. Bạn phân chia cho nhóm một cách công "
   "bằng, nên nhóm chấp nhận bạn đứng đầu. Được tự quyết là điều kiện sống còn của kênh này."
 ),
 "misaligned": (
   "Bạn kiểm soát cả những chỗ không phải của mình rồi vấp chống đối. Hoặc bạn bị người khác "
   "chỉ đạo và phản kháng dữ dội — kênh này rất khó chịu khi bị sai bảo."
 ),
 "practice": "Vẽ ranh giới địa hạt của bạn trên giấy: việc nào của mình, việc nào không. Buông một việc nằm ngoài.",
 "questions": ["Bạn đang cố kiểm soát điều gì không thuộc về mình?", "Bạn có đang bị chỉ đạo trong địa hạt của mình không?"]
},

"26-44": {
 "name_vi": "Buông bỏ", "gates": [26, 44], "centers": ["heart", "spleen"], "mach": "bộ tộc",
 "tagline": "Bạn nhớ mọi thứ và bạn kể lại rất hay. Ranh giới giữa kể hay và nói quá rất mỏng.",
 "mechanics": (
   "Cổng 44 ở Lá lách là bản năng nhận biết mẫu hình từ quá khứ kèm nỗi sợ quá khứ lặp lại, "
   "cổng 26 ở Tim là ý chí thuyết phục. Kênh này biến ký ức thành câu chuyện bán được. Hệ "
   "thống mô tả đây là kênh của người bán hàng và người làm thương hiệu."
 ),
 "aligned": (
   "Bạn kể điều mình thật sự tin và làm người ta tin theo. Bạn cũng đọc được người rất nhanh, "
   "nên chọn cộng sự rất chuẩn."
 ),
 "misaligned": (
   "Bạn nói quá lên để bán được, rồi phải nói dối thêm để đỡ cho lời đầu. Hoặc bạn bán thứ "
   "mình không tin, và ý chí cạn rất nhanh vì nó phải chống lại chính mình."
 ),
 "practice": "Nhìn lại lời chào bán gần nhất. Gạch bỏ mọi câu bạn không đặt tay lên ngực khẳng định được.",
 "questions": ["Bạn có đang nói quá về điều gì không?", "Bạn có thật sự tin vào thứ bạn đang bán không?"]
},

"27-50": {
 "name_vi": "Gìn giữ", "gates": [27, 50], "centers": ["sacral", "spleen"], "mach": "bộ tộc",
 "tagline": "Bạn nuôi và bạn giữ luật cho nhóm mình. Cả hai đều nặng.",
 "mechanics": (
   "Cổng 27 ở Xương cùng là sức chăm sóc nuôi dưỡng, cổng 50 ở Lá lách giữ giá trị và luật lệ "
   "của nhóm kèm nỗi sợ trách nhiệm. Kênh này làm nên người mà cả nhà dựa vào. Hệ thống mô tả "
   "nó là kênh của sự bảo hộ trong mạch bộ tộc."
 ),
 "aligned": (
   "Bạn chăm người thật sự cần và thuộc nhóm mình, và bạn chăm chính mình trước. Bạn giữ "
   "những nguyên tắc còn đúng và buông những cái đã lỗi thời. Nhóm dựa được vào bạn vì bạn "
   "còn sức."
 ),
 "misaligned": (
   "Bạn ôm hết trách nhiệm của cả nhóm rồi kiệt, kèm cảm giác tội lỗi triền miên. Hoặc bạn "
   "chăm sóc quá mức tới chỗ người kia không tự lớn lên được."
 ),
 "practice": "Liệt kê những trách nhiệm bạn đang gánh. Đánh dấu cái nào thật sự là của bạn. Giao trả một cái không phải.",
 "questions": ["Bạn đang gánh trách nhiệm nào không phải của mình?", "Ai đang chăm sóc bạn?"]
},

"32-54": {
 "name_vi": "Chuyển hoá", "gates": [32, 54], "centers": ["spleen", "root"], "mach": "bộ tộc",
 "tagline": "Bạn muốn đi lên, và bạn cảm được cái gì sẽ trụ được.",
 "mechanics": (
   "Cổng 54 ở Gốc là áp lực thăng tiến — quẻ gốc là Quy Muội, vào bằng cửa phụ. Cổng 32 ở Lá "
   "lách là bản năng nhận biết cái gì tồn tại lâu dài, kèm nỗi sợ thất bại. Kênh này làm nên "
   "tham vọng có tính toán: muốn lên, nhưng biết chọn thứ đáng để leo."
 ),
 "aligned": (
   "Bạn làm thật tốt phần của mình và để người ở trên nhìn thấy. Bạn kiên trì với thứ bản năng "
   "báo là sẽ trụ, và bỏ thứ sẽ sụp. Khi cửa mở, bạn đã sẵn sàng."
 ),
 "misaligned": (
   "Bạn chen lên bằng mọi giá rồi bị đẩy ngược. Hoặc nỗi sợ thất bại chặn hết, không dám bắt "
   "đầu gì. Hoặc bạn tiếc công mà giữ lại thứ bản năng đã báo là không trụ được."
 ),
 "practice": "Chọn một người ở vị trí bạn muốn tới. Tuần này tìm cách để họ thấy được một việc bạn làm tốt.",
 "questions": ["Bạn đang tiếc công mà giữ lại thứ gì?", "Ai có thể mở cửa cho bạn, và họ có biết bạn làm được gì không?"]
},

"37-40": {
 "name_vi": "Cộng đồng", "gates": [37, 40], "centers": ["solar_plexus", "heart"], "mach": "bộ tộc",
 "tagline": "Bạn hứa, và bạn có sức giữ lời. Miễn là thoả thuận sòng phẳng.",
 "mechanics": (
   "Cổng 37 ở Đám rối mặt trời là lời hứa và thoả thuận trong nhóm thân, cổng 40 ở Tim là ý "
   "chí làm việc để nuôi nhóm kèm nhu cầu rút lui sau đó. Kênh này giữ gia đình lại với nhau "
   "bằng những thoả thuận rõ ràng."
 ),
 "aligned": (
   "Bạn làm thoả thuận rõ: tôi làm phần này, đổi lại tôi nhận cái này. Bạn làm phần của mình "
   "rồi nghỉ mà không thấy có lỗi. Chính sự sòng phẳng giữ quan hệ bền."
 ),
 "misaligned": (
   "Bạn hứa mà không nói rõ đổi lại là gì, rồi ấm ức. Hoặc bạn làm mãi không nghỉ vì sợ bị "
   "coi là ích kỷ, rồi cạn và sinh oán ngầm."
 ),
 "practice": "Chọn một thoả thuận đang lệch trong nhà bạn. Nói thẳng: mình làm phần này, mình mong đổi lại điều này.",
 "questions": ["Thoả thuận nào trong nhà bạn đang không còn công bằng?", "Bạn có thấy có lỗi khi nghỉ ngơi không?"]
},

}
