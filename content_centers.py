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
"""Nội dung 9 Trung tâm × 2 trạng thái (định nghĩa / mở) — viết gốc tiếng Việt.

LƯU Ý PHÁP LÝ (§7.3 Instructions): phần thân bài dùng ngôn ngữ an toàn ở mọi nơi.

Phần cơ thể theo hệ thống gốc (Tầng B §7.3) KHÔNG nằm trong file này. Nó tách
sang `noi_dung_tang_b.py` ngày 29/08/2026, và `build_content.py` chỉ ghép nó
vào bản nội bộ. Đừng thêm nội dung Tầng B trở lại đây — file này là mã nguồn
công khai theo AGPL.
"""

CENTERS = {

"head": {
 "name_vi": "Trung tâm Đầu", "name_en": "Head Center",
 "role": "Áp lực tư duy — nơi câu hỏi và cảm hứng sinh ra",
 "gates": [61, 63, 64],
 "defined": {
   "tagline": "Bạn có nguồn câu hỏi của riêng mình, và nó không bao giờ ngừng.",
   "mechanics": (
     "Trung tâm Đầu là một trung tâm áp lực. Khi nó được định nghĩa, áp lực suy nghĩ trong "
     "bạn là cố định và đến từ bên trong. Bạn luôn có thứ gì đó để nghĩ tới, dù xung quanh "
     "yên tĩnh. Đây là nguồn cảm hứng ổn định — nhưng nó cũng có nghĩa là bạn không tắt được."
   ),
   "aligned": (
     "Bạn để những câu hỏi tự nảy ra mà không ép mình phải trả lời hết. Bạn học được rằng "
     "suy nghĩ của bạn không phải để giải quyết vấn đề đời mình — nó là để truyền cảm hứng, "
     "cho bạn và cho người khác. Quyết định thì để cho nội quyền lo, không để cái đầu lo."
   ),
   "misaligned": (
     "Bạn dùng cái đầu để ra quyết định, và bạn quay vòng mãi trong đó. Hoặc bạn tự ép mình "
     "phải giải cho xong mọi câu hỏi vừa hiện ra, rồi kiệt sức trong đầu mà ngoài đời chẳng "
     "có gì đổi khác."
   ),
   "practice": "Ghi lại năm câu hỏi đang chạy trong đầu bạn tuần này. Khoanh tròn câu nào thật sự cần bạn hành động. Phần còn lại để yên.",
   "questions": [
     "Bạn đang nghĩ về việc gì mà nghĩ mãi không xong?",
     "Nếu không cần trả lời câu hỏi đó hôm nay, bạn có nhẹ hơn không?"
   ]
 },
 "open": {
   "tagline": "Phần lớn thứ bạn đang nghĩ không phải của bạn.",
   "false_pursuit": "Cố trả lời cho xong những câu hỏi mà thật ra không phải việc của mình.",
   "mechanics": (
     "Trung tâm Đầu của bạn không cố định, nên nó hấp thụ áp lực suy nghĩ từ người xung quanh "
     "rồi khuếch đại lên. Bạn ngồi cạnh ai đang lo, một lát sau bạn cũng lo — về đúng chuyện "
     "của họ. Bạn nhạy với ý tưởng và cảm hứng của người khác hơn bạn tưởng."
   ),
   "aligned": (
     "Bạn nhận ra được đâu là câu hỏi của mình và đâu là câu hỏi bạn vừa nhặt về. Bạn trở "
     "thành người đọc được không khí trí tuệ của cả một nhóm. Và bạn cho phép mình không "
     "trả lời những gì không phải việc của mình."
   ),
   "misaligned": (
     "Bạn ôm hết mọi câu hỏi vào đầu và cố giải, kể cả những câu chẳng liên quan tới đời bạn. "
     "Ban đêm không ngủ được vì đầu quay. Bạn tưởng mình là người hay nghĩ ngợi, trong khi "
     "thật ra bạn đang mang giúp người khác."
   ),
   "practice": "Tối nay khi đầu không chịu yên, hỏi một câu: chuyện này của ai? Nếu không phải của mình, nói thầm một câu trả lại cho người đó rồi buông.",
   "questions": [
     "Bạn thường nghĩ nhiều nhất sau khi nói chuyện với ai?",
     "Có câu hỏi nào bạn đang mang giúp người khác không?"
   ]
 }
},

"ajna": {
 "name_vi": "Trung tâm Ajna", "name_en": "Ajna Center",
 "role": "Nhận thức — cách bạn xử lý và sắp xếp thông tin",
 "gates": [47, 24, 4, 11, 43, 17],
 "defined": {
   "tagline": "Bạn có một cách tư duy cố định, và bạn không đổi được nó.",
   "mechanics": (
     "Ajna là trung tâm nhận thức bằng lý trí. Khi được định nghĩa, cách bạn xử lý thông tin "
     "là nhất quán suốt đời: bạn luôn phân tích theo một kiểu, luôn sắp xếp theo một trật tự. "
     "Người ngoài thấy bạn chắc chắn, có chính kiến, khó lay."
   ),
   "aligned": (
     "Bạn tin cách nghĩ của mình và dùng nó để làm rõ mọi thứ cho người khác. Bạn cũng nhận ra "
     "được rằng chắc chắn không có nghĩa là đúng — bạn có thể rất chắc về một điều sai. Nên "
     "bạn vẫn để nội quyền quyết, còn cái đầu chỉ làm nhiệm vụ sắp xếp."
   ),
   "misaligned": (
     "Bạn dùng sự chắc chắn của mình để áp người khác, và bạn không nghe được ý khác. Hoặc "
     "bạn tự tin vào một kết luận rồi hành động theo nó mà không kiểm tra lại với cơ thể — "
     "đây là kiểu sai lầm mà người có Ajna định nghĩa hay mắc nhất."
   ),
   "practice": "Tuần này, khi bạn thấy mình rất chắc về một điều, hãy hỏi một người có cách nghĩ khác hẳn. Không để tranh cãi, chỉ để nghe.",
   "questions": [
     "Bạn từng rất chắc về điều gì rồi hoá ra sai?",
     "Cách nghĩ của bạn có đang giúp người khác sáng ra, hay đang làm họ im?"
   ]
 },
 "open": {
   "tagline": "Bạn không cần phải chắc chắn về mọi thứ. Đó là tự do, không phải thiếu sót.",
   "false_pursuit": "Cố tỏ ra chắc chắn, cố có chính kiến về mọi chuyện để khỏi bị coi là hời hợt.",
   "mechanics": (
     "Ajna mở nghĩa là cách tư duy của bạn không cố định. Hôm nay bạn nghĩ kiểu này, mai kiểu "
     "khác, tuỳ vào việc bạn đang ở gần ai. Đây là một trung tâm nhận thức, nên bạn có khả năng "
     "hiểu được nhiều lối tư duy khác nhau — nhưng bạn không có lối nào là của riêng mình mãi mãi."
   ),
   "aligned": (
     "Bạn thoải mái nói \"tôi chưa biết\" mà không thấy xấu hổ. Bạn linh hoạt, học nhanh, và "
     "hiểu được cách nghĩ của rất nhiều kiểu người — đó là một tài sản hiếm. Bạn dùng sự cởi "
     "mở đó để làm cầu nối giữa những người không hiểu nhau."
   ),
   "misaligned": (
     "Bạn giả vờ chắc chắn để không bị coi thường, rồi phải bảo vệ một quan điểm mà chính bạn "
     "cũng không tin. Hoặc bạn thay đổi ý liên tục rồi tự trách mình là người không có lập trường."
   ),
   "practice": "Trong một cuộc trò chuyện tuần này, thử nói thật câu \"cái này mình chưa nghĩ ra\" thay vì đưa ra một ý cho có.",
   "questions": [
     "Bạn có đang giả vờ chắc chắn về điều gì không?",
     "Bạn có tự trách mình vì hay đổi ý không?"
   ]
 }
},

"throat": {
 "name_vi": "Trung tâm Cổ họng", "name_en": "Throat Center",
 "role": "Biểu đạt và hành động — nơi mọi thứ bên trong đi ra ngoài",
 "gates": [62, 23, 56, 35, 12, 45, 33, 8, 31, 20, 16],
 "defined": {
   "tagline": "Bạn nói ra được, và bạn làm ra được. Vấn đề là nói đúng lúc.",
   "mechanics": (
     "Cổ họng là nơi biến năng lượng thành lời và thành hành động. Khi được định nghĩa, bạn có "
     "một kênh biểu đạt ổn định: bạn nói theo một kiểu nhất quán, và bạn có thể chủ động mở lời "
     "mà không cần ai gợi."
   ),
   "aligned": (
     "Bạn nói khi đúng thời điểm — sau khi nội quyền đã gật, chứ không phải ngay khi ý vừa hiện. "
     "Lời bạn có sức nặng vì bạn không nói tràn. Người ta nghe bạn vì bạn không phí lời."
   ),
   "misaligned": (
     "Bạn nói trước khi cơ thể kịp xác nhận, rồi phải chịu trách nhiệm cho những lời đã lỡ. "
     "Hoặc bạn nói nhiều để lấp khoảng trống, và dần dần lời bạn mất trọng lượng."
   ),
   "practice": "Trong một cuộc họp tuần này, để người khác nói trước. Chỉ lên tiếng khi có người hỏi hoặc khi bạn thật sự thấy cần.",
   "questions": [
     "Lần gần nhất bạn hối vì đã nói ra một điều, bạn đã nói nó nhanh thế nào?",
     "Bạn có đang nói nhiều hơn mức cần thiết ở đâu không?"
   ]
 },
 "open": {
   "tagline": "Bạn không cần giành lời. Khi đúng lúc, người ta sẽ hỏi bạn.",
   "false_pursuit": "Cố gây chú ý, cố chen vào để được nhìn thấy và được công nhận.",
   "mechanics": (
     "Cổ họng mở nghĩa là cách bạn biểu đạt thay đổi theo người và theo hoàn cảnh. Cùng một "
     "con người, bạn nói với nhóm này rất trôi chảy, với nhóm khác lại nghẹn. Bạn cũng nhạy "
     "với việc mình có đang được lắng nghe hay không, nhạy hơn người khác nhiều."
   ),
   "aligned": (
     "Bạn học được cách chờ đến khi có người hỏi rồi mới nói — và bạn nhận ra khi đó lời bạn "
     "được nghe khác hẳn. Bạn cũng linh hoạt trong cách diễn đạt, có thể nói chuyện được với "
     "rất nhiều kiểu người, điều mà người có Cổ họng cố định khó làm."
   ),
   "misaligned": (
     "Bạn cố chen vào cuộc trò chuyện, nói nhiều, nói to, để được chú ý — rồi sau đó thấy trống "
     "rỗng và tự trách mình. Hoặc bạn nói ra một điều rồi thấy không ai phản ứng, và hiểu đó là "
     "mình không có giá trị."
   ),
   "practice": "Trong buổi gặp tiếp theo, đặt cho mình một luật: chỉ nói khi có người hỏi trực tiếp. Để ý xem cảm giác của bạn thay đổi thế nào sau đó.",
   "questions": [
     "Bạn có hay chen vào để được chú ý không?",
     "Với ai bạn nói dễ nhất, và với ai bạn hay nghẹn?"
   ]
 }
},

"g": {
 "name_vi": "Trung tâm G", "name_en": "G / Identity Center",
 "role": "Bản thể, phương hướng và tình yêu",
 "gates": [1, 13, 25, 46, 2, 15, 10, 7],
 "defined": {
   "tagline": "Bạn có một hướng đi của riêng mình, kể cả khi bạn chưa nhìn ra nó.",
   "mechanics": (
     "Trung tâm G là nơi của bản thể và phương hướng. Khi được định nghĩa, bạn mang một cảm "
     "thức ổn định về mình là ai — nó có thể mơ hồ, nhưng nó cố định. Hướng đi của bạn đến từ "
     "bên trong, không phụ thuộc vào nơi bạn đứng."
   ),
   "aligned": (
     "Bạn tin vào hướng của mình kể cả khi chưa giải thích được. Bạn không cần người khác xác "
     "nhận bạn là ai. Khi bạn đi đúng hướng, mọi thứ có cảm giác đúng chỗ, ngay cả trong lúc khó."
   ),
   "misaligned": (
     "Bạn để người khác định nghĩa bạn là ai và bạn nên đi đâu. Rồi bạn đi một con đường rất "
     "hợp lý mà trong lòng thấy nhạt. Cảm giác lạc hướng dai dẳng ở người có G định nghĩa "
     "thường là dấu hiệu bạn đang sống theo bản thiết kế của ai khác."
   ),
   "practice": "Viết ra ba việc bạn đang làm vì người khác mong đợi. Với mỗi việc, tự hỏi: nếu không ai biết, mình có làm không?",
   "questions": [
     "Bạn đang đi theo hướng của mình hay hướng của ai?",
     "Lần gần nhất bạn thấy rõ mình là ai là khi nào?"
   ]
 },
 "open": {
   "tagline": "Bạn không có một bản thể cố định để bảo vệ. Nơi bạn đứng quan trọng hơn bạn nghĩ.",
   "false_pursuit": "Cố tìm cho ra mình thật sự là ai và đời mình phải đi đâu, rồi bám vào câu trả lời đó.",
   "mechanics": (
     "Trung tâm G mở nghĩa là bản thể và phương hướng của bạn không cố định — chúng thay đổi "
     "theo người và theo nơi. Bạn ở với nhóm này thì thành một phiên bản, sang nhóm khác thành "
     "phiên bản khác. Với bạn, môi trường không phải yếu tố phụ, nó gần như quyết định tất cả."
   ),
   "aligned": (
     "Bạn thôi đi tìm một câu trả lời cố định cho câu hỏi mình là ai, và thay vào đó bạn chú "
     "tâm vào việc chọn nơi mình ở và người mình ở cùng. Bạn linh hoạt, hoà được với nhiều kiểu "
     "người, và bạn phản chiếu lại cho họ chính bản thể của họ."
   ),
   "misaligned": (
     "Bạn cố ép mình phải nhất quán, phải có một danh tính rõ ràng, rồi thấy mình giả tạo. Hoặc "
     "bạn bám vào một người hay một nơi chỉ vì ở đó bạn thấy mình có hình dạng — kể cả khi nơi "
     "đó không tốt cho bạn."
   ),
   "practice": "Trong hai tuần, mỗi khi đổi chỗ ngồi làm việc hoặc đổi nhóm người, ghi một dòng: ở đây mình thấy mình thế nào. Cuối kỳ đọc lại.",
   "questions": [
     "Nơi nào bạn đến mà tự nhiên thấy mình rõ ràng hơn?",
     "Bạn có đang bám vào ai hoặc nơi nào chỉ vì ở đó bạn thấy mình có hình dạng không?"
   ]
 }
},

"heart": {
 "name_vi": "Trung tâm Tim / Ý chí", "name_en": "Heart / Ego Center",
 "role": "Ý chí, lời hứa và giá trị bản thân",
 "gates": [21, 40, 26, 51],
 "defined": {
   "tagline": "Bạn có ý chí thật, nhưng nó có giới hạn và cần được nghỉ.",
   "mechanics": (
     "Trung tâm Tim là một động cơ, nguồn của ý chí và của khả năng giữ lời. Khi được định "
     "nghĩa, bạn có sức ý chí thật sự — bạn hứa được và làm được. Nhưng động cơ này hoạt động "
     "theo nhịp có nghỉ, không chạy liên tục."
   ),
   "aligned": (
     "Bạn hứa những điều bạn thật lòng muốn, và bạn giữ lời. Bạn biết xen kẽ giai đoạn làm và "
     "giai đoạn nghỉ mà không thấy có lỗi. Giá trị của bạn tự chứng minh qua việc bạn làm, "
     "không cần nói ra."
   ),
   "misaligned": (
     "Bạn hứa liên tục để chứng tỏ mình, rồi chạy đến cạn. Hoặc bạn dùng ý chí để ép người khác "
     "phải theo mình. Người có Tim định nghĩa mà không cho mình nghỉ thường rơi vào trạng thái "
     "làm nhiều mà lòng trống rỗng."
   ),
   "practice": "Nhìn lại các cam kết bạn đang giữ. Chọn một cái bạn hứa không phải vì muốn, và nói thẳng với người liên quan rằng bạn cần rút.",
   "questions": [
     "Bạn đang hứa gì mà thật ra không muốn?",
     "Lần cuối bạn cho mình nghỉ mà không thấy có lỗi là khi nào?"
   ]
 },
 "open": {
   "tagline": "Bạn không có gì phải chứng minh. Đó là điều khó tin nhất với bạn.",
   "false_pursuit": "Cố chứng minh giá trị của mình, cố cho người ta thấy mình xứng đáng.",
   "mechanics": (
     "Tim mở nghĩa là bạn không có nguồn ý chí cố định. Sức ý chí của bạn lên xuống thất "
     "thường. Đây là trung tâm bị điều kiện hoá nặng nhất trong đời sống hiện đại, vì cả xã hội "
     "được xây trên niềm tin rằng ai cũng phải chứng minh mình đáng giá."
   ),
   "aligned": (
     "Bạn thôi hứa những thứ vượt sức mình. Bạn nhận ra giá trị của bạn không nằm ở việc bạn "
     "làm được bao nhiêu. Ngược lại, bạn rất nhạy trong việc nhìn ra ai thật sự có ý chí và ai "
     "chỉ đang nói to — đó là sự khôn ngoan mà người có Tim định nghĩa không có."
   ),
   "misaligned": (
     "Bạn hứa quá tay để chứng minh mình, rồi không làm nổi, rồi tự kết luận mình là kẻ vô "
     "dụng. Vòng lặp này lặp lại nhiều năm và ăn mòn lòng tự trọng của bạn. Bạn cũng dễ bị "
     "cuốn vào các cuộc so đo hơn thua mà bạn không bao giờ thắng."
   ),
   "practice": "Tuần này, từ chối một lời đề nghị mà bạn định nhận chỉ để người ta thấy mình được việc. Không giải thích dài.",
   "questions": [
     "Bạn đang cố chứng minh điều gì, và với ai?",
     "Nếu không phải chứng minh gì với ai, tuần này bạn sẽ bỏ việc gì?"
   ]
 }
},

"spleen": {
 "name_vi": "Trung tâm Lá lách", "name_en": "Spleen Center",
 "role": "Bản năng trong khoảnh khắc — cảm giác an toàn hay không an toàn",
 "gates": [48, 57, 44, 50, 32, 28, 18],
 "defined": {
   "tagline": "Bạn có một hệ cảnh báo bẩm sinh, và nó nói rất khẽ.",
   "mechanics": (
     "Lá lách là trung tâm nhận biết cổ xưa nhất, gắn với bản năng và cảm giác an toàn ngay "
     "trong khoảnh khắc hiện tại. Khi được định nghĩa, bạn mang một cảm thức nền ổn định về "
     "việc mình có ổn hay không. Nó không lý luận và không nhắc lại."
   ),
   "aligned": (
     "Bạn tin vào tín hiệu tức thời của mình và làm theo, kể cả khi chưa giải thích được. Bạn "
     "sống khá thoải mái với hiện tại, ít lo xa. Bạn cũng cảm được rất nhanh một người hay một "
     "chỗ có ổn với mình hay không."
   ),
   "misaligned": (
     "Bạn nghe tín hiệu rồi đi tìm lý do, và trong lúc tìm thì tín hiệu tan. Hoặc bạn giữ thói "
     "quen cũ chỉ vì quen, dù bản năng đã nói nên đổi từ lâu."
   ),
   "practice": "Tuần này, chọn ba việc nhỏ không quan trọng và làm theo phản ứng đầu tiên, không phân tích. Tập trên việc nhỏ để tin được khi việc lớn tới.",
   "questions": [
     "Bạn đã bao nhiêu lần nói câu \"tôi biết ngay từ đầu mà\"?",
     "Có thói quen nào bạn giữ chỉ vì quen, không phải vì nó còn hợp?"
   ]
 },
 "open": {
   "tagline": "Bạn hay bám vào những thứ không còn tốt cho mình, chỉ vì sợ buông ra thì không an toàn.",
   "false_pursuit": "Bám lấy người, việc hay thói quen đã hết hạn, vì buông ra thấy chông chênh.",
   "mechanics": (
     "Lá lách mở nghĩa là cảm thức an toàn của bạn không cố định — nó vay từ người và nơi xung "
     "quanh. Ở cạnh một người có Lá lách định nghĩa, bạn thấy yên; rời ra, bạn thấy chông chênh. "
     "Đây là lý do sâu xa khiến nhiều người có cấu hình này rất khó dứt một mối quan hệ hay một "
     "công việc đã hết hạn từ lâu."
   ),
   "aligned": (
     "Bạn nhận ra cảm giác chông chênh khi rời đi là cơ chế của trung tâm mở, không phải bằng "
     "chứng rằng bạn đang sai. Từ đó bạn dứt được những thứ cần dứt. Đổi lại, bạn có sự nhạy "
     "cảm rất lớn: bạn đọc được tình trạng của người khác trước khi họ tự nhận ra."
   ),
   "misaligned": (
     "Bạn ở lại quá lâu trong những thứ không còn đúng — một công việc, một mối quan hệ, một "
     "nếp sinh hoạt — vì mỗi lần định rời đi thì thấy bất an. Rồi bạn gọi sự bám víu đó là "
     "chung thuỷ hay kiên trì."
   ),
   "practice": "Chọn một thứ bạn biết đã hết hạn từ lâu. Đặt một hạn cụ thể để rời khỏi nó, viết ngày tháng ra giấy. Chưa cần làm ngay, chỉ cần có ngày.",
   "questions": [
     "Bạn đang giữ điều gì chỉ vì buông ra thấy sợ?",
     "Ở cạnh ai bạn thấy yên nhất, và bạn có đang phụ thuộc vào cảm giác đó không?"
   ]
 }
},

"solar_plexus": {
 "name_vi": "Trung tâm Đám rối mặt trời", "name_en": "Solar Plexus Center",
 "role": "Cảm xúc — chạy theo sóng, có đỉnh và có đáy",
 "gates": [36, 22, 37, 6, 49, 55, 30],
 "defined": {
   "tagline": "Cảm xúc của bạn chạy theo sóng riêng, không phải phản ứng với việc bên ngoài.",
   "mechanics": (
     "Đám rối mặt trời vừa là động cơ vừa là trung tâm nhận biết. Khi được định nghĩa, nó chạy "
     "theo sóng: dâng lên, đạt đỉnh, hạ xuống, chạm đáy, rồi lại dâng — theo nhịp riêng, phần "
     "lớn không liên quan tới việc gì đang xảy ra. Bạn cũng phát sóng đó ra cho người quanh mình."
   ),
   "aligned": (
     "Bạn hiểu sóng của mình và không quyết định ở đỉnh cũng không quyết định ở đáy. Bạn cho "
     "mình thời gian trước mọi cam kết. Bạn cũng thôi đổ lỗi cho hoàn cảnh mỗi khi tâm trạng "
     "xuống, vì bạn biết đó là nhịp."
   ),
   "misaligned": (
     "Bạn quyết ngay lúc phấn khích rồi hối. Hoặc bạn tránh xung đột bằng mọi giá, dồn nén, cho "
     "tới khi vỡ ra một lần lớn. Bạn cũng có thể đổ cho người xung quanh mỗi khi mình xuống đáy."
   ),
   "practice": "Ba mươi ngày, mỗi tối chấm tâm trạng của bạn từ 1 tới 10 và ghi một dòng lý do. Cuối kỳ nhìn lại — Thầy sẽ thấy phần lớn lý do không giải thích được biểu đồ.",
   "questions": [
     "Quyết định nào bạn đã đưa ra lúc đang ở đỉnh cảm xúc?",
     "Bạn có đang né một cuộc nói chuyện cần phải có không?"
   ]
 },
 "open": {
   "tagline": "Cảm xúc bạn đang thấy thường không phải của bạn — bạn chỉ đang khuếch đại nó lên.",
   "false_pursuit": "Né tránh mọi va chạm và căng thẳng, làm mọi cách để không khí đừng nặng.",
   "mechanics": (
     "Đám rối mở nghĩa là bạn không có sóng cảm xúc của riêng mình. Bạn hấp thụ sóng của người "
     "khác rồi khuếch đại lên — thường mạnh hơn cả bản gốc. Ai đó bực trong phòng, bạn là người "
     "thấy nặng nhất, và bạn tưởng đó là mình."
   ),
   "aligned": (
     "Bạn phân biệt được đâu là cảm xúc của mình và đâu là của người khác. Bạn học được rằng "
     "khi rời khỏi phòng thì phần lớn cảm giác đó tan đi — và đó là bằng chứng. Bạn cũng trở "
     "thành người đọc được trạng thái cảm xúc của cả một nhóm rất chính xác."
   ),
   "misaligned": (
     "Bạn né mọi sự thật khó nói để giữ không khí êm. Bạn nói dối cho lành, bạn nhượng bộ, bạn "
     "làm hoà sớm trước khi vấn đề được nói ra. Lâu dần bạn mất tiếng nói của chính mình và "
     "tích lại một cục uất mà bạn không biết từ đâu."
   ),
   "practice": "Lần tới khi bạn thấy nặng đột ngột, ra khỏi phòng năm phút. Nếu cảm giác tan, nó không phải của bạn.",
   "questions": [
     "Bạn có hay né những cuộc nói chuyện khó không?",
     "Cảm giác nặng gần nhất của bạn — nó bắt đầu sau khi bạn gặp ai?"
   ]
 }
},

"sacral": {
 "name_vi": "Trung tâm Xương cùng", "name_en": "Sacral Center",
 "role": "Nguồn sinh lực — sức làm việc và sức sáng tạo",
 "gates": [5, 14, 29, 59, 9, 3, 42, 27, 34],
 "defined": {
   "tagline": "Bạn có sức bền lớn, nhưng chỉ khi nó được dùng đúng chỗ.",
   "mechanics": (
     "Xương cùng là động cơ có sức bền lớn nhất trong bản đồ. Khi được định nghĩa, bạn có một "
     "nguồn năng lượng tái tạo mỗi ngày. Nó không tự khởi động — nó bật lên khi có thứ gì đó "
     "bên ngoài chạm vào và bạn phản hồi."
   ),
   "aligned": (
     "Bạn làm việc mình thật sự muốn làm, và bạn làm được rất nhiều mà không cạn. Bạn đi ngủ "
     "khi đã dùng hết năng lượng trong ngày, và bạn ngủ ngon. Cái mệt của bạn là cái mệt dễ chịu."
   ),
   "misaligned": (
     "Bạn làm việc mà bụng không muốn, và bạn kéo lê từng ngày. Hoặc bạn đi ngủ khi năng lượng "
     "chưa dùng hết, rồi trằn trọc. Trạng thái bực bội kéo dài là dấu hiệu rõ nhất."
   ),
   "practice": "Cuối ngày mai, tự hỏi: hôm nay mình đã dùng hết sức chưa? Nếu chưa, làm một việc chân tay nào đó cho hết trước khi đi ngủ.",
   "questions": [
     "Việc bạn làm nhiều nhất hiện nay — bụng bạn có muốn không?",
     "Bạn đang bực bội với điều gì lâu nhất?"
   ]
 },
 "open": {
   "tagline": "Bạn không được thiết kế để làm việc liên tục. Biết dừng là kỹ năng sống còn của bạn.",
   "false_pursuit": "Cố làm cho bằng người khác, cố chứng minh mình cũng bền sức, không dám dừng trước.",
   "mechanics": (
     "Xương cùng mở nghĩa là bạn không có nguồn sinh lực cố định của riêng mình. Bạn vay năng "
     "lượng từ người xung quanh và khuếch đại nó lên — nên ở giữa một tập thể đang chạy, bạn "
     "thấy mình cũng chạy được, thậm chí chạy hăng hơn cả họ. Nhưng đó là năng lượng vay."
   ),
   "aligned": (
     "Bạn học được điểm dừng của mình và dừng trước khi cạn, không đợi tới lúc gục. Bạn sắp xếp "
     "công việc theo đợt ngắn thay vì tám tiếng liên tục. Bạn cũng biết mình cần ở một mình một "
     "lát trước khi ngủ để năng lượng vay tan ra."
   ),
   "misaligned": (
     "Bạn cố theo nhịp của người khác cho tới lúc gục. Bạn không biết thế nào là đủ, nên bạn "
     "làm quá, ăn quá, cố quá — vì bạn không có cái phanh bên trong. Rồi bạn tự trách mình yếu."
   ),
   "practice": "Tuần này, dừng công việc sớm hơn mười lăm phút so với lúc bạn thấy cạn. Làm đủ năm ngày rồi so cảm giác cuối tuần.",
   "questions": [
     "Bạn có biết điểm dừng của mình ở đâu không?",
     "Bạn đang cố theo nhịp của ai?"
   ]
 }
},

"root": {
 "name_vi": "Trung tâm Gốc", "name_en": "Root Center",
 "role": "Áp lực và đà — thứ đẩy bạn bắt đầu và đẩy bạn đi tiếp",
 "gates": [53, 60, 52, 19, 39, 41, 58, 38, 54],
 "defined": {
   "tagline": "Bạn có một nguồn áp lực cố định. Nó đẩy bạn đi, và nó không tắt.",
   "mechanics": (
     "Gốc vừa là động cơ vừa là trung tâm áp lực. Khi được định nghĩa, bạn mang một mức áp lực "
     "nền ổn định suốt đời — thứ khiến bạn luôn có việc phải làm, luôn có cảm giác cần đi tiếp. "
     "Đây là nhiên liệu, nhưng nó cũng là thứ khiến bạn khó ngồi yên."
   ),
   "aligned": (
     "Bạn dùng áp lực đó làm nhiên liệu chứ không để nó điều khiển mình. Bạn nhận ra rằng áp "
     "lực sẽ luôn ở đó, làm xong việc này thì nó chuyển sang việc khác — nên bạn thôi đuổi theo "
     "cái ngày mọi thứ xong xuôi."
   ),
   "misaligned": (
     "Bạn vội vàng làm cho xong để được thảnh thơi, rồi phát hiện áp lực không giảm. Bạn ép cả "
     "người quanh mình chạy theo nhịp đó mà không nhận ra."
   ),
   "practice": "Viết ra danh sách việc đang đè bạn. Chọn ra ba việc và gạch phần còn lại khỏi tuần này. Xem áp lực có giảm không — câu trả lời sẽ dạy bạn nhiều.",
   "questions": [
     "Bạn đang vội vì việc thật sự gấp, hay vì bạn quen vội?",
     "Nếu làm xong hết mọi thứ, bạn tin là mình sẽ thảnh thơi chứ?"
   ]
 },
 "open": {
   "tagline": "Sự vội vã bạn đang thấy phần lớn không phải của bạn.",
   "false_pursuit": "Cố làm cho xong thật nhanh để thoát khỏi áp lực — trong khi áp lực đó là vay của người khác.",
   "mechanics": (
     "Gốc mở nghĩa là bạn không có áp lực nền cố định. Bạn hấp thụ sự gấp gáp của người xung "
     "quanh rồi khuếch đại lên. Một tin nhắn của sếp, một người bạn đang cuống — bạn nhận vào "
     "và thấy như chính mình đang cháy."
   ),
   "aligned": (
     "Bạn dừng lại và hỏi việc này có thật sự gấp không, trước khi lao đi. Bạn nhận ra rằng khi "
     "rời khỏi nguồn áp lực, sự vội vã tan mất — và đó là bằng chứng nó không phải của bạn. Bạn "
     "làm ít việc hơn nhưng làm ra hồn hơn."
   ),
   "misaligned": (
     "Bạn sống trong trạng thái lúc nào cũng gấp, làm vội cho xong việc này để sang việc khác, "
     "và không bao giờ tới được chỗ thảnh thơi. Bạn nhận thêm việc vì không chịu nổi cảm giác "
     "có thứ đang treo."
   ),
   "practice": "Lần tới nhận một yêu cầu gấp, hỏi lại đúng một câu: \"Việc này cần xong lúc nào?\" Rất nhiều lần câu trả lời sẽ không gấp như bạn tưởng.",
   "questions": [
     "Việc bạn đang thấy gấp nhất — ai là người đặt cái hạn đó?",
     "Bạn có nhận thêm việc chỉ để hết cảm giác có thứ đang treo không?"
   ]
 }
},
}
