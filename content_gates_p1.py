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
"""64 CỔNG — ĐỢT 1: Trung tâm Đầu (3) · Ajna (6) · Cổ họng (11) = 20 cổng.

BẢN NỘI BỘ ĐẦY ĐỦ — giữ nguyên nội dung gốc hệ thống, chưa qua bộ lọc NĐ38.
Khi publish phải chạy qua bộ lọc §5.3 trước.
Quẻ Kinh Dịch lấy tự động từ iching_map.py, không nhập tay ở đây.
"""

GATES_P1 = {

# ══════════ TRUNG TÂM ĐẦU — áp lực tư duy ══════════

61: {
 "name_vi": "Bí ẩn bên trong",
 "kenh": "61-24 (Nhận biết) — nối lên Ajna",
 "tagline": "Áp lực muốn biết thứ không ai biết được.",
 "mechanics": (
   "Cổng 61 nằm ở trung tâm Đầu, là áp lực đi tìm câu trả lời cho những câu hỏi lớn nhất: "
   "tại sao mình tồn tại, đằng sau mọi thứ là gì. Đây không phải tò mò thông thường mà là "
   "một sức ép thật sự đè lên bạn. Cổng này nối với cổng 24 ở Ajna — khi cả hai cùng có, "
   "áp lực đó được chuyển thành quá trình suy ngẫm lặp đi lặp lại cho tới khi vỡ ra."
 ),
 "aligned": (
   "Bạn để câu hỏi lớn ở đó mà không ép nó phải có đáp án hôm nay. Bạn hiểu rằng cảm hứng "
   "kiểu này đến rồi đi theo nhịp của nó. Những lúc bạn thật sự chạm được vào một tầng hiểu "
   "biết mới, nó đến bất ngờ, thường là lúc bạn không cố."
 ),
 "misaligned": (
   "Bạn biến áp lực đó thành nỗi ám ảnh, thức đêm đi tìm ý nghĩa cho mọi thứ, và không ngủ "
   "được. Hoặc bạn dùng nó để phán xét — cho rằng mình đã chạm tới sự thật mà người khác chưa. "
   "Cổng 61 lệch hướng dễ sinh ra kiểu tự cho mình đã ngộ."
 ),
 "practice": "Viết câu hỏi lớn nhất đang đè bạn ra một tờ giấy, gấp lại, cất đi. Hẹn ba tháng sau mở lại.",
 "questions": [
   "Câu hỏi nào bạn đã đi tìm lời giải nhiều năm rồi?",
   "Bạn có đang tin mình hiểu ra điều mà người quanh mình chưa hiểu không?"
 ]
},

63: {
 "name_vi": "Nghi ngờ",
 "kenh": "63-4 (Logic) — nối lên Ajna",
 "tagline": "Bạn luôn thấy chỗ có thể sai. Đó là năng lực, nếu bạn hướng nó ra ngoài.",
 "mechanics": (
   "Cổng 63 là áp lực nghi ngờ — nhìn vào một hệ thống, một kế hoạch, một lời hứa, và tự động "
   "thấy chỗ nào chưa vững. Đây là khởi điểm của toàn bộ mạch logic trong bản đồ. Cổng 63 nối "
   "với cổng 4, nơi nghi ngờ được biến thành công thức để kiểm chứng."
 ),
 "aligned": (
   "Bạn hướng sự nghi ngờ vào những thứ bên ngoài cần được kiểm tra: một bản kế hoạch, một "
   "con số, một quy trình. Bạn trở thành người mà nhóm nào cũng cần — người phát hiện lỗ hổng "
   "trước khi nó thành tai nạn. Bạn cũng học được rằng nghi ngờ chỉ là câu hỏi, không phải kết luận."
 ),
 "misaligned": (
   "Bạn quay sự nghi ngờ vào chính mình và vào những người thân, rồi soi mòn cả hai. Bạn nghi "
   "ngờ chính mình có làm nổi không, nghi người kia có thật lòng không — và cái nghi đó không "
   "bao giờ có đáp án vì bạn hỏi sai đối tượng."
 ),
 "practice": "Tuần này, mỗi lần thấy nghi ngờ nổi lên, viết ra một dòng: mình đang nghi cái gì, và có kiểm chứng được không. Cái nào không kiểm chứng được thì gạch bỏ.",
 "questions": [
   "Bạn đang nghi ngờ ai hoặc điều gì mà không có cách nào kiểm chứng?",
   "Người quanh bạn có thấy bạn hay xét nét không?"
 ]
},

64: {
 "name_vi": "Rối",
 "kenh": "64-47 (Trừu tượng) — nối lên Ajna",
 "tagline": "Đầu bạn đầy những mảnh hình ảnh chưa ghép lại được. Đó là bình thường.",
 "mechanics": (
   "Cổng 64 là áp lực của những hình ảnh quá khứ chạy trong đầu mà chưa xử lý xong — như một "
   "cuộn phim rối tua đi tua lại. Đây là khởi điểm của mạch trừu tượng. Cổng 64 nối với cổng "
   "47, nơi mớ hình ảnh đó dần dần ghép được thành ý nghĩa."
 ),
 "aligned": (
   "Bạn để những mảnh hình ảnh đó chạy mà không ép mình phải hiểu ngay. Bạn biết rằng sự sáng "
   "tỏ sẽ đến, nhưng theo nhịp riêng của nó, thường là bất chợt và thường là khi bạn đang làm "
   "việc khác. Bạn tin vào quá trình đó."
 ),
 "misaligned": (
   "Bạn cố ép mình phải hiểu cho ra ngay lúc này, rồi càng ép càng rối. Bạn tưởng sự rối là "
   "dấu hiệu mình có vấn đề, trong khi nó chỉ là cơ chế của cổng này đang chạy."
 ),
 "practice": "Lần tới khi đầu rối, đứng dậy làm một việc chân tay trong ba mươi phút. Đừng cố nghĩ cho ra.",
 "questions": [
   "Ký ức hay hình ảnh nào cứ quay lại trong đầu bạn?",
   "Bạn có đang tự trách mình vì không nghĩ cho ra không?"
 ]
},

# ══════════ AJNA — nhận thức bằng lý trí ══════════

47: {
 "name_vi": "Vỡ lẽ",
 "kenh": "47-64 (Trừu tượng) — nối lên Đầu",
 "tagline": "Bạn phải đi qua chỗ bí trước khi hiểu ra. Không có đường tắt.",
 "mechanics": (
   "Cổng 47 là nơi mớ hình ảnh từ cổng 64 được xử lý thành ý nghĩa. Quẻ gốc là Khốn — bị vây, "
   "bí bách. Cơ chế của cổng này đúng như tên quẻ: bạn rơi vào trạng thái bế tắc, không thấy "
   "đường ra, rồi đột nhiên vỡ lẽ. Giai đoạn bí là một phần bắt buộc của quá trình, không phải sự cố."
 ),
 "aligned": (
   "Bạn chịu được giai đoạn bí mà không hoảng. Bạn hiểu rằng mình đang trong quá trình chứ "
   "không phải đang thất bại. Và khi hiểu ra, bạn kể lại được cho người khác nghe theo cách "
   "họ dùng được — vì bạn đã đi qua cả đoạn tối."
 ),
 "misaligned": (
   "Bạn coi giai đoạn bí là bằng chứng đời mình đang hỏng. Bạn ép mình phải tìm ra ý nghĩa "
   "ngay, hoặc bạn vơ đại một lời giải thích nào đó cho đỡ khó chịu — rồi sống theo một cách "
   "hiểu sai suốt nhiều năm."
 ),
 "practice": "Nhớ lại một giai đoạn bí trong đời mà cuối cùng bạn đã vỡ ra. Nó kéo dài bao lâu? Con số đó là thước đo cho lần bí hiện tại.",
 "questions": [
   "Bạn đang bí ở chỗ nào, và bí bao lâu rồi?",
   "Bạn có đang vơ một lời giải thích cho xong không?"
 ]
},

24: {
 "name_vi": "Quay lại",
 "kenh": "24-61 (Nhận biết) — nối lên Đầu",
 "tagline": "Cùng một câu hỏi quay lại mãi, cho tới ngày nó tự mở ra.",
 "mechanics": (
   "Cổng 24 nhận áp lực từ cổng 61 và biến nó thành một vòng lặp suy ngẫm. Quẻ gốc là Phục — "
   "trở lại. Bạn quay về cùng một câu hỏi hết lần này tới lần khác, mỗi lần nhìn từ một góc "
   "hơi khác, cho tới khi một ngày nó vỡ ra thành cái hiểu."
 ),
 "aligned": (
   "Bạn cho phép mình quay lại mà không thấy mình lì lợm hay lẩn quẩn. Bạn biết rằng cái hiểu "
   "sẽ đến đúng lúc nó đến. Người có cổng này thường là người đào rất sâu một chủ đề trong "
   "nhiều năm, và cuối cùng nói ra được điều mà người lướt qua không thấy."
 ),
 "misaligned": (
   "Bạn tự trách mình vì cứ nghĩ mãi một chuyện. Hoặc bạn cưỡng lại vòng lặp đó, cố quên đi, "
   "và câu hỏi chỉ chìm xuống rồi nổi lên mạnh hơn. Cổng 24 lệch hướng cũng dễ biến thành thói "
   "nghiện — cứ quay lại một hành vi cũ dù biết không tốt."
 ),
 "practice": "Chọn câu hỏi hay quay lại nhất với bạn. Mỗi tuần viết một đoạn ngắn về nó, không cần kết luận. Làm mười tuần.",
 "questions": [
   "Chuyện gì bạn nghĩ đi nghĩ lại nhiều năm rồi?",
   "Có hành vi nào bạn cứ quay lại dù biết nó không tốt cho mình không?"
 ]
},

4: {
 "name_vi": "Công thức",
 "kenh": "4-63 (Logic) — nối lên Đầu",
 "tagline": "Bạn đưa ra câu trả lời có thể sai — và đó chính là việc của bạn.",
 "mechanics": (
   "Cổng 4 nhận nghi ngờ từ cổng 63 và đáp lại bằng một công thức, một cách giải thích khả dĩ. "
   "Quẻ gốc là Mông — non dại, cần được dạy. Điểm cốt lõi: câu trả lời của cổng 4 là **giả "
   "thuyết**, chưa phải sự thật. Nó cần thời gian và thực tế kiểm chứng."
 ),
 "aligned": (
   "Bạn đưa ra cách giải thích của mình mà không tuyên bố đó là chân lý. Bạn nói \"thử cách "
   "này xem\" thay vì \"phải làm thế này\". Bạn trở thành người giải quyết vấn đề rất hữu ích "
   "vì bạn luôn có sẵn một hướng để thử."
 ),
 "misaligned": (
   "Bạn tin công thức của mình là đúng rồi áp lên người khác, hoặc lên chính đời mình, mà chưa "
   "kiểm chứng. Bạn cũng dễ rơi vào trạng thái đầu óc mệt nhoài vì lúc nào cũng phải có câu "
   "trả lời cho một nghi ngờ nào đó."
 ),
 "practice": "Lần tới khi bạn đưa ra một giải pháp, thêm vào câu \"đây là giả thuyết của mình, chưa chắc đúng\". Xem người nghe phản ứng khác thế nào.",
 "questions": [
   "Bạn đang áp công thức nào lên đời mình mà chưa kiểm chứng?",
   "Bạn có mệt đầu vì lúc nào cũng phải có câu trả lời không?"
 ]
},

11: {
 "name_vi": "Ý tưởng",
 "kenh": "11-56 (Tò mò) — nối xuống Cổ họng",
 "tagline": "Ý tưởng đến với bạn không phải để bạn thực hiện. Chúng đến để bạn kể lại.",
 "mechanics": (
   "Cổng 11 là kho ý tưởng. Đây là một trong những chỗ hay bị hiểu sai nhất trong bản đồ: ý "
   "tưởng của cổng 11 **không phải để bạn đi làm**. Chúng là chất liệu để chia sẻ, để truyền "
   "cảm hứng cho người khác. Cổng 11 nối với cổng 56 ở Cổ họng, nơi ý tưởng được kể ra thành chuyện."
 ),
 "aligned": (
   "Bạn nhận ra ý tưởng đến rồi đi như mây, và bạn thoải mái để chúng đi. Bạn kể chúng cho "
   "người khác nghe, và người nào cần thì nhặt lấy. Bạn trở thành nguồn cảm hứng mà không phải "
   "gánh trách nhiệm thực hiện."
 ),
 "misaligned": (
   "Bạn thấy một ý tưởng hay rồi lao vào làm, hết ý này tới ý khác, và không cái nào tới nơi. "
   "Bạn tự trách mình là người nhiều ý mà không làm được gì. Thật ra bạn đang dùng sai chức "
   "năng của cổng này."
 ),
 "practice": "Lập một cuốn sổ ý tưởng. Ghi vào đó, rồi kể cho ít nhất một người. Không tự nhận làm cái nào trong ba mươi ngày.",
 "questions": [
   "Bạn đang ôm bao nhiêu ý tưởng chưa làm, và bạn thấy thế nào về chúng?",
   "Có ai quanh bạn đang cần đúng cái ý tưởng bạn đang giữ không?"
 ]
},

43: {
 "name_vi": "Biết trong lòng",
 "kenh": "43-23 (Cấu trúc) — nối xuống Cổ họng",
 "tagline": "Bạn biết một điều mà chưa nói ra được thành lời. Đó là chỗ cô đơn nhất.",
 "mechanics": (
   "Cổng 43 là cái biết đến từ bên trong, đột ngột, không qua lý luận. Quẻ gốc là Quải — quyết "
   "đoán, dứt khoát. Vấn đề là cái biết này ở dạng thô, chưa thành ngôn ngữ. Cổng 43 nối với "
   "cổng 23 ở Cổ họng — chỉ khi có cầu nối đó thì cái biết mới thành lời người khác hiểu được."
 ),
 "aligned": (
   "Bạn chờ đúng lúc có người hỏi rồi mới nói ra. Bạn chấp nhận rằng cái mình biết thường "
   "khác với cách nghĩ chung, và bạn không cần được đồng ý ngay. Khi đúng thời điểm, cái bạn "
   "nói làm người ta đổi cách nhìn."
 ),
 "misaligned": (
   "Bạn buột miệng nói ra khi chưa ai hỏi, người nghe không hiểu, rồi bạn bị coi là kỳ quặc. "
   "Lặp lại nhiều lần, bạn im hẳn và mang cảm giác cô đơn dai dẳng — biết một điều mà không "
   "chia sẻ được với ai."
 ),
 "practice": "Điều bạn biết mà chưa nói được — thử viết nó ra bằng ba cách diễn đạt khác nhau. Chọn cách nào người ngoài ngành hiểu được.",
 "questions": [
   "Bạn đang biết điều gì mà chưa diễn đạt được?",
   "Bạn có hay bị coi là nói chuyện khó hiểu không?"
 ]
},

17: {
 "name_vi": "Ý kiến",
 "kenh": "17-62 (Chấp nhận) — nối xuống Cổ họng",
 "tagline": "Bạn luôn có ý kiến. Ý kiến không phải sự thật, và đó là điều bạn cần nhớ nhất.",
 "mechanics": (
   "Cổng 17 sinh ra ý kiến dựa trên mạch logic. Đây là cổng có độ lệch lớn nhất so với gốc "
   "Kinh Dịch: quẻ Tùy nghĩa là thuận theo, còn Human Design lại dùng cổng này làm nơi đưa ra "
   "quan điểm của riêng mình. Cổng 17 nối với cổng 62 ở Cổ họng, nơi ý kiến được diễn đạt "
   "thành chi tiết cụ thể."
 ),
 "aligned": (
   "Bạn chờ được hỏi rồi mới đưa ý kiến, và bạn nói rõ đó là ý kiến chứ không phải kết luận. "
   "Ý kiến của bạn có giá trị vì nó dựa trên mẫu hình bạn đã quan sát. Người ta tìm bạn khi "
   "cần một góc nhìn có cơ sở."
 ),
 "misaligned": (
   "Bạn đưa ý kiến cho mọi thứ dù không ai hỏi, và dần dần người ta ngại nói chuyện với bạn. "
   "Hoặc bạn nhầm ý kiến của mình là sự thật rồi tranh cãi để bảo vệ nó."
 ),
 "practice": "Trong ba ngày, đếm số lần bạn đưa ý kiến khi không ai hỏi. Chỉ đếm, không sửa. Con số sẽ nói cho bạn nghe.",
 "questions": [
   "Bạn có hay đưa ý kiến khi không được hỏi không?",
   "Ý kiến nào của bạn đang được bạn coi như sự thật?"
 ]
},

# ══════════ CỔ HỌNG — biểu đạt và hành động ══════════

62: {
 "name_vi": "Chi tiết",
 "kenh": "62-17 (Chấp nhận) — nối lên Ajna",
 "tagline": "Bạn đặt tên cho mọi thứ, và nhờ đó người khác nắm được chúng.",
 "mechanics": (
   "Cổng 62 biến ý kiến trừu tượng thành chi tiết cụ thể: tên gọi, con số, thứ tự, danh sách. "
   "Quẻ gốc là Tiểu Quá — chú ý cái nhỏ. Đây là cổng của người làm việc với dữ kiện, người "
   "biết sắp xếp mớ hỗn độn thành thứ có thể trình bày được."
 ),
 "aligned": (
   "Bạn dùng khả năng chi tiết để làm rõ, để người khác nắm được vấn đề. Bạn là người viết "
   "được quy trình, lập được bảng, đặt được tên đúng cho thứ mà mọi người mơ hồ cảm thấy."
 ),
 "misaligned": (
   "Bạn sa vào chi tiết tới mức mất bức tranh lớn, hoặc bạn bắt bẻ chữ nghĩa của người khác. "
   "Bạn cũng có thể dùng sự tỉ mỉ để trì hoãn — chuẩn bị mãi mà không bắt đầu."
 ),
 "practice": "Lấy một việc bạn đang sa lầy vào chi tiết. Viết ra trong ba câu: mục tiêu là gì, ai cần, bao giờ xong.",
 "questions": [
   "Bạn có đang chuẩn bị quá kỹ để trì hoãn việc bắt đầu không?",
   "Người quanh bạn có thấy bạn hay bắt bẻ không?"
 ]
},

23: {
 "name_vi": "Nói cho hiểu",
 "kenh": "23-43 (Cấu trúc) — nối lên Ajna",
 "tagline": "Cùng một ý, bạn nói lúc đúng thì thành thiên tài, nói lúc sai thì thành kẻ lập dị.",
 "mechanics": (
   "Cổng 23 biến cái biết thô của cổng 43 thành ngôn ngữ người khác hiểu được. Quẻ gốc là Bác "
   "— bóc mòn, tách ra; ở đây là bóc lớp vỏ để lộ cái bên trong. Điểm quyết định của cổng này "
   "là **thời điểm**, không phải nội dung."
 ),
 "aligned": (
   "Bạn giữ im cho tới khi có người hỏi, rồi nói ra rõ ràng và gọn. Cái bạn nói làm người "
   "nghe thấy sáng ra một chuyện họ vốn mơ hồ. Bạn trở thành người diễn đạt được điều khó nói."
 ),
 "misaligned": (
   "Bạn nói ra khi chưa ai sẵn sàng nghe, và bị gạt đi. Rồi bạn cố giải thích thêm, càng giải "
   "thích càng bị coi là lạ. Cảm giác không ai hiểu mình là dấu hiệu rất quen của cổng 23 lệch hướng."
 ),
 "practice": "Điều bạn đang muốn nói với ai đó — hãy giữ lại tới khi họ hỏi. Nếu một tháng không ai hỏi, viết nó ra thay vì nói.",
 "questions": [
   "Bạn có hay nói ra rồi thấy không ai đón nhận không?",
   "Bạn đang chờ ai hỏi mình điều gì?"
 ]
},

56: {
 "name_vi": "Kể chuyện",
 "kenh": "56-11 (Tò mò) — nối lên Ajna",
 "tagline": "Bạn kể lại trải nghiệm theo cách làm người nghe muốn đi tìm trải nghiệm của họ.",
 "mechanics": (
   "Cổng 56 lấy ý tưởng từ cổng 11 và kể chúng thành chuyện. Quẻ gốc là Lữ — người đi xa, kẻ "
   "lữ hành. Đây là cổng của người dẫn chuyện: bạn không truyền dữ kiện, bạn truyền sự kích "
   "thích, khiến người nghe muốn tự đi trải nghiệm."
 ),
 "aligned": (
   "Bạn kể khi có người muốn nghe, và bạn kể sinh động. Bạn giữ người ta ở lại bằng chính "
   "cách bạn dựng câu chuyện. Đây là cổng rất mạnh cho việc dạy học, dẫn chương trình, hay bán hàng."
 ),
 "misaligned": (
   "Bạn kể liên tục để giữ sự chú ý, kể cả khi không ai muốn nghe, rồi bị coi là nói nhiều. "
   "Hoặc bạn thêm thắt cho chuyện hay hơn tới mức mất độ tin cậy."
 ),
 "practice": "Lần kể chuyện tiếp theo, để ý ánh mắt người nghe. Khi họ bắt đầu nhìn đi chỗ khác thì dừng, dù chuyện chưa hết.",
 "questions": [
   "Bạn có hay kể khi người ta không thật sự muốn nghe không?",
   "Bạn có thêm thắt cho chuyện hay hơn không?"
 ]
},

35: {
 "name_vi": "Đổi thay",
 "kenh": "35-36 (Vô thường) — nối xuống Đám rối mặt trời",
 "tagline": "Bạn đã trải qua đủ thứ. Câu hỏi là bạn có rút được gì từ đó không.",
 "mechanics": (
   "Cổng 35 là động lực đi tìm trải nghiệm mới. Quẻ gốc là Tấn — tiến lên. Cổng này nối với "
   "cổng 36 ở Đám rối mặt trời, nên khi thành kênh, nó mang cảm xúc: khao khát, chán, rồi lại "
   "khao khát. Câu nói đặc trưng của cổng 35 là \"cái gì mình cũng thử qua rồi\"."
 ),
 "aligned": (
   "Bạn đi qua trải nghiệm và rút được điều gì đó từ mỗi cái, rồi kể lại cho người khác. Bạn "
   "trở thành người có vốn sống thật, không phải người đọc sách. Bạn cũng biết chờ cảm xúc "
   "lắng xuống trước khi lao vào cái mới."
 ),
 "misaligned": (
   "Bạn nhảy từ trải nghiệm này sang trải nghiệm khác mà không đọng lại gì, và bên trong luôn "
   "có một cảm giác trống. Cảm giác chán chường sau mỗi lần đạt được điều mình muốn là dấu "
   "hiệu quen thuộc nhất của cổng 35."
 ),
 "practice": "Liệt kê năm trải nghiệm lớn bạn đã đi qua. Với mỗi cái, viết một câu về điều bạn học được. Cái nào không viết được là cái bạn chưa tiêu hoá xong.",
 "questions": [
   "Bạn có hay chán ngay sau khi đạt được thứ mình muốn không?",
   "Trải nghiệm nào bạn đã đi qua mà chưa rút ra được gì?"
 ]
},

12: {
 "name_vi": "Dè dặt",
 "kenh": "12-22 (Cởi mở) — nối xuống Đám rối mặt trời",
 "tagline": "Có lúc bạn nói ra được điều đẹp đẽ nhất. Có lúc bạn không nói nổi một câu.",
 "mechanics": (
   "Cổng 12 là biểu đạt mang màu cảm xúc. Quẻ gốc là Bĩ — bế tắc, không thông. Cơ chế của "
   "cổng này là thất thường theo tâm trạng: cùng một con người, có lúc nói ra lời làm rung "
   "động cả phòng, có lúc tắc nghẹn không thốt được. Cổng 12 nối với cổng 22 ở Đám rối mặt trời."
 ),
 "aligned": (
   "Bạn chấp nhận rằng khả năng nói của mình lên xuống, và bạn chỉ nói khi tâm trạng cho phép. "
   "Khi đúng lúc, bạn nói ra được điều mà không ai khác diễn đạt nổi. Đây là cổng của nghệ sĩ, "
   "của người viết, của người nói trước đám đông vào đúng khoảnh khắc."
 ),
 "misaligned": (
   "Bạn ép mình phải nói khi chưa sẵn sàng, rồi ra một thứ nhạt nhẽo hoặc gượng gạo. Hoặc bạn "
   "tự trách mình vì hôm nay không nói được như hôm qua, rồi kết luận mình kém."
 ),
 "practice": "Trước buổi nói quan trọng tiếp theo, nếu thấy trong người không thông, hãy dời lại nếu dời được. Ghi lại kết quả cả hai kiểu.",
 "questions": [
   "Bạn có tự trách mình vì hôm nay nói không hay bằng hôm qua không?",
   "Lần bạn nói hay nhất — lúc đó tâm trạng bạn thế nào?"
 ]
},

45: {
 "name_vi": "Người đứng đầu",
 "kenh": "45-21 (Tiền bạc) — nối xuống Tim",
 "tagline": "Tiếng nói của người trông coi tài nguyên chung.",
 "mechanics": (
   "Cổng 45 là tiếng nói của người đứng đầu một nhóm, một gia đình, một bộ tộc — người nói "
   "\"tôi có\" và \"chúng ta có\". Quẻ gốc là Tụy — tụ họp. Đây là cổng thuộc mạch bộ tộc, "
   "gắn với tài nguyên vật chất. Nối với cổng 21 ở Tim thành kênh Tiền bạc."
 ),
 "aligned": (
   "Bạn đứng ra trông coi và phân chia tài nguyên cho nhóm mình, và nhóm chấp nhận điều đó. "
   "Bạn không cần giành quyền — người ta giao cho bạn vì bạn làm được. Đây là cổng của người "
   "chủ doanh nghiệp, người quản gia, người giữ quỹ."
 ),
 "misaligned": (
   "Bạn cố lãnh đạo một nhóm chưa chọn bạn, và bị coi là độc đoán. Hoặc bạn nắm tài nguyên "
   "nhưng không chia, rồi mất nhóm."
 ),
 "practice": "Nhìn vào nhóm bạn đang dẫn. Hỏi thẳng một người: có phải mọi người đang tự nguyện theo, hay đang phải theo?",
 "questions": [
   "Nhóm bạn đang dẫn có thật sự chọn bạn không?",
   "Bạn có đang giữ thứ gì đáng ra phải chia không?"
 ]
},

33: {
 "name_vi": "Rút lui và kể lại",
 "kenh": "33-13 (Đứa con hoang) — nối xuống Trung tâm G",
 "tagline": "Bạn cần rút đi để tiêu hoá, rồi quay lại kể cho người khác nghe.",
 "mechanics": (
   "Cổng 33 là nhu cầu rút lui sau một chu kỳ trải nghiệm, để tiêu hoá rồi kể lại. Quẻ gốc là "
   "Độn — lui ẩn. Đây là cổng của người giữ ký ức tập thể: bạn nhớ chuyện đã qua và kể lại cho "
   "thế hệ sau để họ khỏi lặp lại sai lầm. Nối với cổng 13 ở Trung tâm G."
 ),
 "aligned": (
   "Bạn cho mình khoảng lặng sau mỗi chặng, không thấy có lỗi vì điều đó. Sau khi rút, bạn "
   "quay lại với một câu chuyện có ý nghĩa. Bạn cũng biết giữ bí mật của người khác, vì cổng "
   "này gắn với việc biết cái gì nên kể và cái gì không."
 ),
 "misaligned": (
   "Bạn không cho mình rút, chạy liên tục, và không bao giờ tiêu hoá được gì. Hoặc bạn rút đi "
   "rồi không quay lại, giữ hết cho riêng mình."
 ),
 "practice": "Sau việc lớn gần nhất, dành trọn một ngày không gặp ai. Cuối ngày viết ra điều bạn rút được.",
 "questions": [
   "Bạn có cho mình khoảng lặng sau mỗi chặng không?",
   "Có câu chuyện nào bạn đang giữ mà đáng ra nên kể cho ai đó?"
 ]
},

8: {
 "name_vi": "Góp phần",
 "kenh": "8-1 (Cảm hứng) — nối xuống Trung tâm G",
 "tagline": "Bạn không cần là người sáng tạo. Bạn là người làm cho cái sáng tạo được nhìn thấy.",
 "mechanics": (
   "Cổng 8 là đóng góp bằng cách làm gương và bằng cách đưa cái độc đáo của người khác ra ánh "
   "sáng. Quẻ gốc là Tỷ — thân gần, liên kết. Nối với cổng 1 ở Trung tâm G thành kênh Cảm hứng: "
   "cổng 1 tạo ra, cổng 8 mang nó ra thế giới."
 ),
 "aligned": (
   "Bạn tìm ra người có cái gì đó thật sự riêng và giúp họ được nhìn thấy. Bạn cũng sống theo "
   "đúng điều mình tin, và chính điều đó thuyết phục người khác. Đây là cổng của người làm "
   "quản lý nghệ sĩ, người biên tập, người dẫn dắt tài năng."
 ),
 "misaligned": (
   "Bạn cố tỏ ra độc đáo để được chú ý, trong khi việc của bạn là làm cho cái độc đáo của "
   "người khác được thấy. Hoặc bạn nói về giá trị mình tin mà không sống theo nó."
 ),
 "practice": "Chọn một người quanh bạn có tài mà chưa ai biết. Tuần này làm một việc cụ thể để đưa họ ra ánh sáng.",
 "questions": [
   "Bạn có đang cố tỏ ra khác biệt thay vì giúp người khác được thấy không?",
   "Bạn có sống theo đúng điều mình nói không?"
 ]
},

31: {
 "name_vi": "Dẫn dắt",
 "kenh": "31-7 (Người dẫn) — nối xuống Trung tâm G",
 "tagline": "Bạn nói \"tôi dẫn\" — nhưng chỉ có giá trị khi người ta đã chọn bạn.",
 "mechanics": (
   "Cổng 31 là tiếng nói của người lãnh đạo trong mạch tập thể. Quẻ gốc là Hàm — cảm ứng, rung "
   "động lẫn nhau. Điểm cốt lõi: quyền dẫn dắt của cổng 31 đến từ việc **được bầu**, không "
   "phải từ việc bạn tự nhận. Nối với cổng 7 ở Trung tâm G."
 ),
 "aligned": (
   "Bạn lên tiếng khi nhóm đã tin và đã chọn bạn. Khi đó lời bạn nói ra được cả nhóm đi theo, "
   "và bạn dẫn họ tới chỗ tốt hơn. Bạn cũng biết rằng vai trò này không vĩnh viễn — hết nhiệm "
   "kỳ thì trả lại."
 ),
 "misaligned": (
   "Bạn tự nhận vai dẫn khi chưa ai chọn, và nhóm không theo. Hoặc bạn dẫn vì thích quyền chứ "
   "không vì lợi ích chung, và người ta rời đi dần."
 ),
 "practice": "Trong nhóm bạn đang dẫn, hỏi ba người: nếu được chọn lại, họ có chọn bạn không. Nghe mà không thanh minh.",
 "questions": [
   "Bạn đang dẫn vì được chọn hay vì bạn tự nhận?",
   "Bạn dẫn nhóm này vì lợi ích chung hay vì bạn muốn vị trí đó?"
 ]
},

20: {
 "name_vi": "Ngay bây giờ",
 "kenh": "20-34 (Sức hút) · 20-57 (Sóng não) · 20-10 (Tỉnh thức) — nối xuống Sacral, Lá lách, G",
 "tagline": "Bạn nói ra điều đang xảy ra ngay lúc này, không phải hôm qua hay ngày mai.",
 "mechanics": (
   "Cổng 20 là biểu đạt của khoảnh khắc hiện tại. Quẻ gốc là Quán — quan sát, chiêm ngưỡng. "
   "Đây là cổng nối được với nhiều nơi nhất trong Cổ họng: với Xương cùng thành sức hút, với "
   "Lá lách thành trực giác nói thành lời, với Trung tâm G thành sự tỉnh thức trong hành xử."
 ),
 "aligned": (
   "Bạn nói cái đang thật ở thời điểm này, và điều đó tạo ra sức hút tự nhiên. Người ta chú ý "
   "tới bạn không vì bạn cố gây chú ý mà vì bạn đang thật sự có mặt ở đây."
 ),
 "misaligned": (
   "Bạn nói về hiện tại nhưng đầu đang ở chỗ khác, và người nghe cảm được sự giả. Hoặc bạn "
   "buột miệng nói ra mọi thứ vừa hiện lên mà không lọc, gây rắc rối cho chính mình."
 ),
 "practice": "Trong một cuộc trò chuyện tuần này, tắt điện thoại và chỉ ở đó. Để ý xem cuộc nói chuyện khác đi thế nào.",
 "questions": [
   "Khi nói chuyện với người khác, đầu bạn có thật sự ở đó không?",
   "Bạn có hay buột miệng nói ra thứ chưa kịp lọc không?"
 ]
},

16: {
 "name_vi": "Nhiệt tình",
 "kenh": "16-48 (Bước sóng) — nối xuống Lá lách",
 "tagline": "Bạn nhảy vào trước, rồi mới học cách làm. Cần một chút nền, không cần chờ đủ.",
 "mechanics": (
   "Cổng 16 là sự hăng hái nhảy vào thử. Quẻ gốc là Dự — vui vẻ, hăng hái chuẩn bị. Nối với "
   "cổng 48 ở Lá lách thành kênh Bước sóng: cổng 48 là chiều sâu năng lực, cổng 16 là sự nhiệt "
   "tình đưa chiều sâu đó ra thành kỹ năng thực."
 ),
 "aligned": (
   "Bạn để sự nhiệt tình dẫn mình vào một thứ, rồi kiên trì luyện tập cho tới khi thành thạo "
   "thật. Nhiệt tình của bạn cũng lây sang người khác — bạn làm cả nhóm muốn thử."
 ),
 "misaligned": (
   "Bạn hăng hái nhảy vào rồi bỏ khi hết hứng, hết lần này tới lần khác. Hoặc bạn giả vờ hăng "
   "hái với thứ mình không thật sự muốn, và người tinh ý nhận ra ngay."
 ),
 "practice": "Chọn một kỹ năng bạn từng hào hứng rồi bỏ dở. Cam kết luyện lại ba mươi ngày, mỗi ngày mười lăm phút.",
 "questions": [
   "Bạn đã bỏ dở bao nhiêu thứ ngay sau khi hết hứng?",
   "Bạn có đang giả vờ hào hứng với việc gì không?"
 ]
},

}
