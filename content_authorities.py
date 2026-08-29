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
"""Nội dung 7 Authority (Nội quyền) — viết gốc tiếng Việt cho B-RICH MIND."""

AUTHORITIES = {
"emotional": {
  "name_vi": "Nội quyền Cảm xúc",
  "name_en": "Emotional (Solar Plexus) Authority",
  "priority": 1,
  "rule": "Trung tâm Đám rối mặt trời được định nghĩa",
  "timeframe": "Chờ qua trọn một con sóng cảm xúc — thường vài giờ tới vài ngày tuỳ việc lớn nhỏ",
  "tagline": "Với bạn, không có sự thật trong khoảnh khắc. Chỉ có sự thật qua thời gian.",
  "mechanics": (
    "Trung tâm cảm xúc của bạn được định nghĩa, và nó chạy theo sóng: có lúc dâng cao, có lúc "
    "hạ thấp, không phụ thuộc vào việc gì đang xảy ra bên ngoài. Cùng một lời đề nghị, nếu đến "
    "lúc bạn đang ở đỉnh sóng, bạn thấy nó tuyệt vời; nếu đến lúc bạn đang ở đáy, bạn thấy nó "
    "tệ hại. Cả hai đều không phải câu trả lời. Câu trả lời chỉ hiện ra khi bạn nhìn nó từ đủ "
    "nhiều điểm trên con sóng."
  ),
  "aligned": (
    "Bạn tập được thói quen nói \"để tôi nghĩ thêm rồi trả lời\" và giữ được thói quen đó kể "
    "cả khi bị hối. Sau vài ngày, cái muốn ban đầu hoặc là còn nguyên — thì đó là thật — hoặc "
    "là tan đi, và bạn vừa tránh được một quyết định sai. Người có nội quyền cảm xúc mà biết "
    "chờ thì rất ít khi hối hận, vì họ đã hối hận trước rồi, ngay trong lúc chờ."
  ),
  "misaligned": (
    "Bạn quyết ngay lúc đang phấn khích, rồi hôm sau tỉnh ra thấy mình vừa cam kết một thứ "
    "không muốn. Hoặc bạn cắt đứt một quan hệ ngay lúc đang ở đáy, rồi tuần sau thấy tiếc. "
    "Vòng lặp phấn khích rồi hối hận lặp đi lặp lại là dấu hiệu rõ nhất rằng bạn đang quyết "
    "bằng khoảnh khắc thay vì bằng thời gian."
  ),
  "practice": (
    "Đặt một quy tắc cứng cho chính mình: mọi cam kết trên một mức tiền hoặc một mức thời gian "
    "nhất định đều phải ngủ qua ít nhất ba đêm. Viết ra cảm nhận của bạn ở đêm thứ nhất và đêm "
    "thứ ba, rồi so."
  ),
  "questions": [
    "Ba quyết định bạn hối hận nhất — bạn đã quyết trong bao lâu?",
    "Bạn có sợ mình mất cơ hội nếu không trả lời ngay không? Cơ hội nào từng thật sự mất vì bạn chờ ba ngày?",
    "Ai trong đời bạn hay hối bạn quyết nhanh?"
  ]
},

"sacral": {
  "name_vi": "Nội quyền Xương cùng",
  "name_en": "Sacral Authority",
  "priority": 2,
  "rule": "Xương cùng được định nghĩa và Đám rối mặt trời KHÔNG được định nghĩa",
  "timeframe": "Tức thời — âm thanh bật ra trong khoảnh khắc đầu tiên",
  "tagline": "Câu trả lời của bạn nằm ở bụng, và nó bật ra trước khi đầu kịp lên tiếng.",
  "mechanics": (
    "Xương cùng của bạn được định nghĩa và không bị lớp sóng cảm xúc phủ lên. Nghĩa là bạn có "
    "một cơ chế trả lời gần như tức thời, biểu hiện bằng âm thanh trong cổ họng và một cảm giác "
    "trong bụng: một bên là tiếng \"ừ-hự\" kèm cảm giác mở ra và có lực; một bên là tiếng "
    "\"un-un\" kèm cảm giác đóng lại và xẹp xuống. Đây không phải suy nghĩ. Nó nhanh hơn suy nghĩ."
  ),
  "aligned": (
    "Bạn học cách nghe âm thanh đầu tiên đó và tin nó, kể cả khi cái đầu chưa giải thích được "
    "tại sao. Năng lượng của bạn đi đúng chỗ, và bạn giữ được sức bền suốt ngày dài. Nhiều "
    "người có nội quyền này nhận ra rằng khi họ nói không với thứ bụng không muốn, họ không hề "
    "mất gì — họ chỉ để trống chỗ cho thứ đúng."
  ),
  "misaligned": (
    "Bạn để cái đầu phủ quyết cái bụng: bụng nói không nhưng đầu nói việc này hợp lý, nên bạn "
    "vẫn nhận. Rồi bạn làm nó trong trạng thái nặng nề, kéo lê, và tự hỏi sao mình lúc nào cũng "
    "mệt. Một dấu hiệu khác là bạn hay trả lời bằng những câu vòng vo — \"chắc là được\", \"để "
    "xem\" — thay vì để cơ thể trả lời thẳng."
  ),
  "practice": (
    "Nhờ một người thân hỏi bạn hai mươi câu có-không trong mười phút, hỏi nhanh, không cho bạn "
    "kịp nghĩ. Đừng trả lời bằng lời — để âm thanh tự bật ra. Đây là cách nhanh nhất để bạn "
    "nhận ra cơ chế này có thật."
  ),
  "questions": [
    "Việc bạn đang làm hôm nay — nếu có người hỏi bụng bạn ngay bây giờ, nó sẽ nói ừ hay không?",
    "Lần gần nhất bạn nhận một việc mà trong bụng đã biết là không, chuyện gì xảy ra sau đó?",
    "Bạn có được phép nói không trong môi trường bạn đang sống không?"
  ]
},

"splenic": {
  "name_vi": "Nội quyền Lá lách",
  "name_en": "Splenic Authority",
  "priority": 3,
  "rule": "Lá lách được định nghĩa; Đám rối mặt trời và Xương cùng KHÔNG được định nghĩa",
  "timeframe": "Tức thời và chỉ một lần — nó không nói lại lần thứ hai",
  "tagline": "Trực giác của bạn nói rất khẽ, đúng một lần, ngay tại chỗ.",
  "mechanics": (
    "Lá lách là trung tâm nhận biết cổ xưa nhất trong bản đồ, gắn với bản năng sinh tồn và sự "
    "an toàn trong khoảnh khắc hiện tại. Nó không lý luận, không nhắc lại, không tranh cãi. Nó "
    "đưa ra một tín hiệu duy nhất ngay lúc bạn tiếp xúc với người hay tình huống đó — thường "
    "rất khẽ, dễ bị tiếng ồn của cái đầu át đi."
  ),
  "aligned": (
    "Bạn nhận ra tín hiệu đó và làm theo ngay, kể cả khi không giải thích được. Bạn bước vào "
    "một căn phòng và biết mình nên ra. Bạn gặp một người và biết không nên ký. Những người có "
    "nội quyền lá lách mà tin được vào nó thường sống rất an toàn theo nghĩa sâu, vì họ tránh "
    "được rất nhiều thứ trước khi nó kịp thành vấn đề."
  ),
  "misaligned": (
    "Bạn nghe thấy tín hiệu, rồi bạn hỏi \"nhưng tại sao?\", và trong lúc đi tìm lý do thì tín "
    "hiệu đã tan. Sau đó bạn quyết bằng lý lẽ, và thường là quyết sai. Câu nói quen thuộc của "
    "người lệch nội quyền này là: \"tôi đã biết ngay từ đầu mà tôi không nghe.\""
  ),
  "practice": (
    "Tuần này, chọn ba việc nhỏ không có hậu quả lớn — chọn quán ăn, chọn đường đi, chọn ngồi "
    "chỗ nào. Làm theo tín hiệu đầu tiên, không phân tích. Tập trên việc nhỏ để đủ tin khi việc lớn tới."
  ),
  "questions": [
    "Đã bao nhiêu lần bạn nói câu \"tôi đã biết ngay từ đầu\"?",
    "Bạn thường lấy lý do gì để phủ quyết linh cảm của mình?",
    "Nơi bạn đang sống hoặc làm việc — lá lách của bạn nói gì về nó ngay lúc này?"
  ]
},

"ego": {
  "name_vi": "Nội quyền Tim / Ý chí",
  "name_en": "Ego (Heart) Authority",
  "priority": 4,
  "rule": "Tim được định nghĩa; Đám rối, Xương cùng và Lá lách KHÔNG được định nghĩa",
  "timeframe": "Tức thời, nhưng phải nghe được câu \"tôi muốn\" thật của mình",
  "tagline": "Câu hỏi duy nhất bạn cần trả lời là: tôi có thật sự muốn cái này không?",
  "mechanics": (
    "Trung tâm Tim là nơi của ý chí, của cam kết và của lời hứa. Với bạn, quyết định đúng không "
    "đến từ việc nó hợp lý hay tốt cho ai, mà từ việc bạn có thật sự muốn nó cho chính mình hay "
    "không. Cơ chế này nghe có vẻ ích kỷ, nhưng nó là cách duy nhất để ý chí của bạn không bị "
    "rút cạn — vì bạn chỉ giữ được lời hứa cho những thứ mình thật lòng muốn."
  ),
  "aligned": (
    "Bạn nói ra được câu \"tôi muốn cái này\" hoặc \"tôi không muốn\" mà không phải xin lỗi vì "
    "nó. Bạn cam kết ít hơn nhưng giữ được nhiều hơn. Người quanh bạn dần hiểu rằng khi bạn đã "
    "nhận thì bạn làm tới, và uy tín của bạn đến từ đó."
  ),
  "misaligned": (
    "Bạn nhận lời vì thấy có lỗi khi từ chối, vì muốn được quý, vì thấy mình phải có trách nhiệm. "
    "Rồi bạn không đủ ý chí để hoàn thành, và bạn bắt đầu tự trách mình là người không giữ lời. "
    "Vấn đề không nằm ở ý chí của bạn — nó nằm ở chỗ bạn hứa cho những việc bạn chưa bao giờ muốn."
  ),
  "practice": (
    "Trước lời đề nghị tiếp theo, hãy nói to lên một mình hai câu: \"Tôi muốn làm việc này\" và "
    "\"Tôi không muốn làm việc này.\" Câu nào nghe ra thật hơn khi chính miệng bạn nói? Đi theo câu đó."
  ),
  "questions": [
    "Bạn đang giữ lời hứa nào mà thật ra bạn chưa bao giờ muốn hứa?",
    "Bạn có được phép nói \"tôi muốn\" mà không thấy có lỗi không?",
    "Điều gì bạn thật sự muốn cho riêng mình, không phải cho ai khác?"
  ]
},

"self_projected": {
  "name_vi": "Nội quyền Tự Chiếu",
  "name_en": "Self-Projected Authority",
  "priority": 5,
  "rule": "Trung tâm G nối tới Cổ họng, và không có trung tâm nội quyền nào ưu tiên hơn",
  "timeframe": "Trong lúc nói ra thành lời với người mình tin",
  "tagline": "Bạn không tìm câu trả lời trong đầu. Bạn nghe nó khi chính mình nói ra.",
  "mechanics": (
    "Trung tâm G — nơi của bản thể và phương hướng — được nối thẳng tới Cổ họng. Nghĩa là sự "
    "thật của bạn đi ra qua giọng nói. Không phải qua nội dung bạn nói, mà qua âm sắc: cùng một "
    "câu, khi nó đúng hướng thì giọng bạn mở ra và có sức; khi nó sai hướng thì giọng bạn nhỏ "
    "lại, phẳng đi, hoặc trôi tuột."
  ),
  "aligned": (
    "Bạn tìm được vài người chịu ngồi nghe bạn nói mà không góp ý, không cắt lời, không cho lời "
    "khuyên. Bạn nói ra hết mọi phương án, và trong lúc nói bạn tự nghe thấy phương án nào làm "
    "giọng mình sáng lên. Người nghe không cần trả lời gì — họ chỉ cần có mặt để bạn được nghe chính mình."
  ),
  "misaligned": (
    "Bạn ngồi một mình phân tích trong đầu hàng tuần mà không ra được quyết định, vì cơ chế của "
    "bạn không nằm trong đầu. Hoặc bạn nói ra nhưng người nghe liên tục chen vào cho lời khuyên, "
    "và bạn kết thúc bằng quyết định của họ chứ không phải của mình. Cảm giác lạc hướng, không "
    "biết mình là ai và đang đi đâu, là dấu hiệu quen thuộc."
  ),
  "practice": (
    "Chọn một người bạn tin và nói trước với họ: \"Mình cần nói ra một chuyện trong mười phút, "
    "bạn đừng góp ý gì nhé, chỉ nghe thôi.\" Rồi nói. Nếu không có ai, hãy ghi âm chính mình và nghe lại."
  ),
  "questions": [
    "Khi bạn nói về công việc hiện tại, giọng bạn nghe thế nào?",
    "Trong đời bạn có ai chịu nghe mà không góp ý không?",
    "Bạn đã phân tích trong đầu bao lâu rồi mà chưa quyết được?"
  ]
},

"mental_projected": {
  "name_vi": "Nội quyền Ngoại cảnh (Trí)",
  "name_en": "Mental / Environmental Authority",
  "priority": 6,
  "rule": "Projector không có trung tâm nội quyền nào được định nghĩa",
  "timeframe": "Qua nhiều cuộc trò chuyện, ở nhiều môi trường khác nhau",
  "tagline": "Với bạn, môi trường quan trọng hơn lý lẽ. Đúng chỗ thì mọi thứ tự sáng ra.",
  "mechanics": (
    "Bạn có trung tâm Đầu và Ajna được định nghĩa, nhưng không có trung tâm nội quyền nào bên "
    "dưới. Cái đầu của bạn rất sắc — nhưng nó được thiết kế để suy nghĩ cho người khác, không "
    "phải để quyết định cho bạn. Cơ chế của bạn nằm ở bên ngoài: ở môi trường bạn đứng và ở "
    "những người bạn nói chuyện cùng."
  ),
  "aligned": (
    "Bạn nói cùng một vấn đề với vài người tin cậy, ở vài nơi khác nhau, và bạn để ý không phải "
    "họ nói gì, mà chính bạn nghe thấy mình nói gì ở mỗi nơi. Dần dần một hướng nổi lên rõ hơn "
    "các hướng còn lại. Khi bạn ở đúng môi trường vật lý — đúng ánh sáng, đúng không gian, đúng "
    "người — thì mọi thứ tự trở nên rõ ràng mà không cần cố."
  ),
  "misaligned": (
    "Bạn tin rằng nếu nghĩ đủ kỹ thì sẽ ra câu trả lời, nên bạn nghĩ mãi và kiệt sức trong đầu. "
    "Hoặc bạn hỏi ý kiến quá nhiều người rồi bị rối, vì bạn đi tìm lời khuyên thay vì đi tìm âm "
    "vang của chính mình. Ở sai môi trường, bạn thấy mọi quyết định đều nặng và đều sai."
  ),
  "practice": (
    "Lấy một quyết định bạn đang treo. Nói về nó với ba người khác nhau, ở ba nơi khác nhau, "
    "trong ba ngày. Sau mỗi lần, ghi lại một dòng cảm nhận. Đừng hỏi họ nên làm gì."
  ),
  "questions": [
    "Nơi nào bạn đến mà đầu óc tự nhiên nhẹ đi?",
    "Bạn đang đi tìm lời khuyên, hay đang đi tìm chỗ để nghe chính mình?",
    "Có ai bạn nói chuyện xong thấy sáng ra, và ai nói xong thấy rối thêm?"
  ]
},

"lunar": {
  "name_vi": "Nội quyền Mặt Trăng",
  "name_en": "Lunar Authority",
  "priority": 7,
  "rule": "Reflector — không trung tâm nào được định nghĩa",
  "timeframe": "Trọn một chu kỳ mặt trăng, khoảng 28 ngày",
  "tagline": "Bạn cần đi hết một vòng trăng để nhìn cùng một việc từ mọi phía.",
  "mechanics": (
    "Không có trung tâm nào trong bản đồ bạn cố định, nên bạn không có một nội quyền bên trong "
    "để tựa vào. Cơ chế của bạn là thời gian: trong khoảng 28 ngày, Mặt Trăng lần lượt kích hoạt "
    "các phần khác nhau trong bản đồ bạn, và bạn đi qua nhiều trạng thái rất khác nhau. Cùng một "
    "quyết định, nhìn từ ngày thứ ba và ngày thứ hai mươi là hai bức tranh khác hẳn."
  ),
  "aligned": (
    "Bạn cho phép mình chờ đủ vòng trước những việc lớn — đổi việc, chuyển nhà, cam kết dài hạn. "
    "Bạn ghi lại cảm nhận mỗi vài ngày. Đến cuối chu kỳ, thứ nào còn đứng vững qua tất cả các "
    "trạng thái thì đó là thứ đúng. Bạn cũng chọn kỹ nơi ở và người ở gần, vì với bạn môi trường "
    "gần như quyết định tất cả."
  ),
  "misaligned": (
    "Bạn bị hối và quyết vội, rồi mắc kẹt trong một thứ mà chỉ hai tuần sau bạn đã thấy không "
    "hợp. Hoặc bạn tự trách mình vì hôm nay nghĩ khác hôm qua, và cố ép mình phải nhất quán — "
    "trong khi sự không nhất quán đó chính là công cụ đo lường của bạn."
  ),
  "practice": (
    "Với quyết định lớn tiếp theo, nói thẳng với người liên quan: \"Tôi cần bốn tuần.\" Trong "
    "bốn tuần đó, mỗi ba ngày ghi một dòng về cảm nhận của bạn với việc đó. Cuối cùng đọc lại toàn bộ."
  ),
  "questions": [
    "Ai đang hối bạn quyết, và việc đó có thật sự gấp không?",
    "Bạn có đang tự trách mình vì hay đổi ý không?",
    "Nơi bạn đang sống — sau một tháng ở đó, bạn thấy sáng lên hay tối đi?"
  ]
},
}
