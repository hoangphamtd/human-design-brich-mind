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
"""Nội dung 12 Profile — viết gốc tiếng Việt cho B-RICH MIND.
Hào 1 (Cá tính) / hào 2 (Thiết kế). Hào trước là phần bạn ý thức được,
hào sau là phần vận hành ngầm mà người ngoài thấy rõ hơn bạn.
"""

LINE_NAMES = {
  1: {"vi": "Nhà Nghiên Cứu", "en": "Investigator",
      "core": "Cần nền móng chắc trước khi bước. An toàn đến từ việc biết rõ."},
  2: {"vi": "Ẩn Sĩ", "en": "Hermit",
      "core": "Có tài năng tự nhiên mà chính mình không thấy. Cần được người khác gọi ra."},
  3: {"vi": "Người Thử Sai", "en": "Martyr",
      "core": "Học bằng cách va vào. Mỗi lần trật là một lần biết thêm cái không dùng được."},
  4: {"vi": "Người Kết Nối", "en": "Opportunist",
      "core": "Cơ hội đến qua mạng lưới quan hệ đã có, không đến từ người lạ."},
  5: {"vi": "Người Dị Giáo", "en": "Heretic",
      "core": "Bị người khác phóng chiếu kỳ vọng lên. Giỏi đưa giải pháp thực dụng khi được gọi."},
  6: {"vi": "Hình Mẫu", "en": "Role Model",
      "core": "Đời chia ba chặng: va vấp, quan sát, rồi sống thành hình mẫu."},
}

PROFILES = {
"1/3": {
  "name_vi": "1/3 — Nhà Nghiên Cứu / Người Thử Sai",
  "tagline": "Bạn đào đến tận đáy, rồi tự mình va vào để kiểm chứng xem cái đáy đó có thật không.",
  "mechanics": (
    "Hào 1 khiến bạn không yên khi chưa hiểu tới gốc. Bạn đọc, bạn hỏi, bạn tra cứu cho tới khi "
    "thấy nền móng chắc. Hào 3 ở tầng vô thức lại đẩy bạn vào thử nghiệm thực tế, và phần lớn "
    "thử nghiệm sẽ không ra như dự tính. Hai hào này bổ cho nhau: bạn nghiên cứu để có nền, rồi "
    "va vào để biết cái nền đó đứng được tới đâu."
  ),
  "aligned": (
    "Bạn trở thành người hiểu một lĩnh vực theo cách rất khó lung lay, vì bạn vừa có lý thuyết "
    "vừa có vết sẹo. Khi bạn nói, người ta tin, vì bạn nói từ chỗ đã thử rồi. Bạn coi mỗi lần "
    "trật là dữ liệu chứ không phải thất bại — đó là chỗ bạn khoẻ nhất."
  ),
  "misaligned": (
    "Bạn nghiên cứu mãi mà không dám bắt đầu, vì luôn thấy mình chưa biết đủ. Hoặc ngược lại, "
    "bạn va vào hết lần này tới lần khác rồi coi đó là bằng chứng mình kém cỏi. Cả hai đều là "
    "cùng một sai lầm: tưởng rằng phải đúng ngay từ đầu."
  ),
  "practice": "Với việc đang treo: đặt hạn cho phần tìm hiểu, rồi thử một phiên bản nhỏ nhất có thể sai được mà không đau.",
  "questions": [
    "Bạn đang tìm hiểu thứ gì đủ lâu rồi mà vẫn chưa bắt đầu?",
    "Lần trật gần nhất dạy bạn điều gì mà lý thuyết không dạy được?"
  ]
},

"1/4": {
  "name_vi": "1/4 — Nhà Nghiên Cứu / Người Kết Nối",
  "tagline": "Bạn xây nền cho chắc, rồi mang nó đi qua những người đã biết bạn.",
  "mechanics": (
    "Hào 1 cần sự chắc chắn trước khi bước ra. Hào 4 ở tầng vô thức làm cho mọi cơ hội của bạn "
    "đến qua mạng lưới quen: bạn bè, đồng nghiệp cũ, người từng làm việc chung. Bạn không phải "
    "kiểu gửi hồ sơ cho người lạ rồi được nhận."
  ),
  "aligned": (
    "Bạn dành thời gian học cho tới nơi, rồi chia sẻ lại trong vòng người quen. Từ đó cơ hội tự "
    "tới. Mối quan hệ của bạn ít mà bền, và mỗi mối đều có sức nặng. Bạn là người mà bạn bè cũ "
    "nghĩ tới đầu tiên khi có việc cần người chắc tay."
  ),
  "misaligned": (
    "Bạn học xong rồi giữ cho riêng mình, không nói với ai, và tự hỏi sao không ai biết tới mình. "
    "Hoặc bạn đốt cầu với người cũ rồi phải bắt đầu lại từ con số không ở môi trường mới — với "
    "cấu hình này, đó là con đường rất tốn sức."
  ),
  "practice": "Liệt kê năm người từng làm việc chung mà bạn đã lâu không liên lạc. Nhắn cho hai người, không nhờ vả gì, chỉ hỏi thăm.",
  "questions": [
    "Ai trong mạng lưới cũ của bạn đang không biết bạn giỏi cái gì?",
    "Bạn có đang chờ đủ giỏi mới dám kết nối không?"
  ]
},

"2/4": {
  "name_vi": "2/4 — Ẩn Sĩ / Người Kết Nối",
  "tagline": "Bạn cần được ở một mình để làm việc, và cần người khác gọi bạn ra.",
  "mechanics": (
    "Hào 2 mang một tài năng tự nhiên mà bạn thường không nhận ra là tài năng — với bạn nó chỉ "
    "là chuyện bình thường. Hào 4 lại đặt bạn trong một mạng lưới quan hệ, và chính những người "
    "đó là người nhìn thấy cái bạn không thấy rồi gọi bạn ra. Bạn sống giữa hai lực: muốn được "
    "yên và bị gọi liên tục."
  ),
  "aligned": (
    "Bạn bảo vệ được khoảng thời gian một mình để làm cái mình giỏi, đồng thời giữ được vài mối "
    "quan hệ thật. Khi có lời gọi đúng, bạn bước ra, làm, rồi lại rút về. Nhịp ra-vào này là "
    "nhịp tự nhiên của bạn, không phải sự thất thường."
  ),
  "misaligned": (
    "Bạn nhận mọi lời gọi vì ngại từ chối, và không còn giờ nào để một mình — tài năng cạn dần. "
    "Hoặc bạn rút hẳn, cắt liên lạc với mọi người, rồi tài năng đó không bao giờ được ai gọi ra."
  ),
  "practice": "Chặn cứng một buổi mỗi tuần không tiếp ai. Và trả lời một lời mời bạn đang lảng tránh.",
  "questions": [
    "Người khác hay khen bạn giỏi cái gì mà bạn thấy chuyện đó bình thường?",
    "Bạn đang thiếu thời gian một mình hay đang thiếu người gọi mình ra?"
  ]
},

"2/5": {
  "name_vi": "2/5 — Ẩn Sĩ / Người Dị Giáo",
  "tagline": "Bạn muốn được yên, nhưng người ta cứ nhìn thấy ở bạn một vị cứu tinh.",
  "mechanics": (
    "Hào 2 cần không gian riêng và có tài năng bẩm sinh. Hào 5 ở tầng vô thức khiến người khác "
    "phóng chiếu lên bạn những kỳ vọng lớn — họ nhìn thấy ở bạn thứ họ đang cần, chưa chắc đã "
    "là con người thật của bạn. Bạn vừa muốn trốn, vừa liên tục bị kéo ra làm người giải quyết vấn đề."
  ),
  "aligned": (
    "Bạn chọn lọc kỹ lời gọi nào mình nhận. Khi nhận, bạn đưa ra giải pháp rất thực tế và làm "
    "xong thì rút. Bạn học được cách nói rõ ngay từ đầu mình làm được gì và không làm được gì — "
    "điều đó giữ bạn không bị kỳ vọng nghiền nát."
  ),
  "misaligned": (
    "Bạn cố sống cho vừa cái hình ảnh người ta gán cho mình, rồi kiệt sức và bị trách khi không "
    "đáp ứng nổi. Hoặc bạn trốn hẳn để khỏi bị nhìn. Với cấu hình này, danh tiếng lên xuống rất "
    "nhanh, và đó là cơ chế chứ không phải lỗi của bạn."
  ),
  "practice": "Trước khi nhận việc tiếp theo, viết ra một dòng: mình làm được đúng cái gì, trong bao lâu. Nói câu đó ra trước.",
  "questions": [
    "Người ta đang trông đợi ở bạn điều gì mà bạn chưa bao giờ hứa?",
    "Bạn có đang gánh một hình ảnh không phải mình không?"
  ]
},

"3/5": {
  "name_vi": "3/5 — Người Thử Sai / Người Dị Giáo",
  "tagline": "Bạn biết cái gì không dùng được vì bạn đã tự tay thử — và người ta tìm bạn vì điều đó.",
  "mechanics": (
    "Hào 3 đưa bạn vào hết thử nghiệm này tới thử nghiệm khác, nhiều cái không thành. Hào 5 khiến "
    "người khác trông cậy bạn đưa ra giải pháp. Kết hợp lại: bạn là người đã đi qua đủ thứ rồi "
    "nên biết đường nào cụt, và đó chính là thứ có giá trị nhất bạn mang lại."
  ),
  "aligned": (
    "Bạn không giấu những lần trật của mình mà biến chúng thành vốn. Bạn nói thẳng với người ta "
    "cái gì không chạy được và tại sao. Bạn thay đổi hướng đi nhiều lần trong đời mà không thấy "
    "đó là thất bại."
  ),
  "misaligned": (
    "Bạn mang mặc cảm rằng đời mình toàn đổ vỡ, rồi giấu quá khứ đi. Hoặc bạn hứa nhiều hơn cái "
    "mình chắc chắn làm được, và khi không xong thì niềm tin của người ta sụp rất nhanh — với "
    "hào 5, sự sụp đổ niềm tin luôn mạnh hơn bình thường."
  ),
  "practice": "Kể một lần bạn làm hỏng chuyện cho ai đó đang định làm y hệt. Xem phản ứng của họ.",
  "questions": [
    "Bạn đang gọi những lần trật của mình là thất bại hay là kinh nghiệm?",
    "Bạn có hay hứa quá tay để giữ hình ảnh không?"
  ]
},

"3/6": {
  "name_vi": "3/6 — Người Thử Sai / Hình Mẫu",
  "tagline": "Nửa đầu đời bạn va rất nhiều. Nửa sau, chính những vết đó làm nên bạn.",
  "mechanics": (
    "Hào 3 học bằng va chạm. Hào 6 chia đời bạn thành ba chặng: khoảng ba mươi năm đầu sống như "
    "hào 3, va vào đủ thứ; rồi một giai đoạn lùi lại quan sát, ít tham gia hơn, gần như đứng trên "
    "mái nhà nhìn xuống; rồi bước xuống sống như một hình mẫu của điều mình đã học."
  ),
  "aligned": (
    "Bạn cho phép chặng đầu là chặng thử, không đòi hỏi mình phải xong xuôi sớm. Đến chặng giữa "
    "bạn không sốt ruột khi thấy mình chậm lại. Đến chặng sau, bạn sống thành ví dụ sống chứ "
    "không phải người đi giảng."
  ),
  "misaligned": (
    "Bạn so mình với người cùng tuổi ở chặng đầu rồi kết luận mình kém. Hoặc ở chặng giữa bạn "
    "hoảng vì thấy mình mất lửa, rồi lao vào làm bừa cho có. Cả hai đều là việc chống lại nhịp "
    "tự nhiên của chính mình."
  ),
  "practice": "Vẽ một đường thời gian đời bạn, đánh dấu tuổi 30 và 50. Nhìn xem bạn đang ở chặng nào, và bạn đang đòi hỏi mình điều gì của chặng khác.",
  "questions": [
    "Bạn đang ở chặng nào, và bạn đang tự ép mình sống theo chặng nào?",
    "Điều gì bạn đã học được mà chỉ có thể học bằng cách tự va vào?"
  ]
},

"4/6": {
  "name_vi": "4/6 — Người Kết Nối / Hình Mẫu",
  "tagline": "Vốn lớn nhất của bạn là những người tin bạn, tích lại qua nhiều năm.",
  "mechanics": (
    "Hào 4 đưa cơ hội tới qua mạng lưới thân quen. Hào 6 đặt bạn vào ba chặng đời, và ở chặng "
    "sau bạn trở thành người mà cộng đồng quanh bạn nhìn vào để lấy chuẩn. Hai hào này cộng lại "
    "thành một thứ rất bền: uy tín tích lũy trong một nhóm người cụ thể."
  ),
  "aligned": (
    "Bạn giữ quan hệ tử tế và lâu dài, không đốt cầu. Bạn sống đúng điều mình nói, vì bạn biết "
    "người ta đang nhìn. Đến giữa đời, mạng lưới đó tự mang việc và cơ hội tới cho bạn mà bạn "
    "không cần chào mời."
  ),
  "misaligned": (
    "Bạn nóng vội ở chặng đầu, làm tổn thương quan hệ để lấy kết quả ngắn hạn, rồi mất luôn "
    "kênh chính của mình. Hoặc bạn cố tỏ ra hoàn hảo quá sớm, và khi vỡ thì vỡ trước mặt tất cả "
    "những người quan trọng nhất với bạn."
  ),
  "practice": "Nhớ lại một quan hệ bạn để nguội mà không có lý do gì lớn. Khôi phục nó tuần này.",
  "questions": [
    "Có cây cầu nào bạn đốt mà bây giờ nhìn lại thấy không đáng không?",
    "Bạn đang sống đúng cái mình nói với người khác chứ?"
  ]
},

"4/1": {
  "name_vi": "4/1 — Người Kết Nối / Nhà Nghiên Cứu",
  "tagline": "Bạn có một hướng đi cố định. Việc của bạn là đi đúng hướng đó và mang theo người của mình.",
  "mechanics": (
    "Đây là cấu hình cố định nhất trong mười hai profile. Hào 1 cho bạn một nền móng sâu, hào 4 "
    "cho bạn một mạng lưới. Bạn không được thiết kế để đổi hướng liên tục — bạn được thiết kế để "
    "đi sâu vào một thứ và truyền nó đi qua những người xung quanh."
  ),
  "aligned": (
    "Bạn tìm ra thứ mình muốn đào sâu, rồi đào thật sâu, và nói về nó với vòng người quen. Cơ "
    "hội đến từ đúng vòng đó. Bạn ổn định, đáng tin, và người ta biết chính xác tìm bạn để làm gì."
  ),
  "misaligned": (
    "Bạn ép mình phải linh hoạt, phải đổi ngành, phải làm nhiều thứ như người khác — và bạn khổ, "
    "vì cấu hình này không chịu được sự trôi nổi. Hoặc bạn đào sâu nhưng cắt hết quan hệ, rồi "
    "kiến thức đó không đi tới đâu."
  ),
  "practice": "Viết ra một câu duy nhất: thứ tôi muốn hiểu sâu nhất trong mười năm tới là gì. Nếu chưa viết được, đó chính là việc cần làm trước.",
  "questions": [
    "Bạn có đang ép mình phải đa năng trong khi bản chất bạn muốn đi sâu?",
    "Ai cần biết về thứ bạn đang đào sâu mà chưa biết?"
  ]
},

"5/1": {
  "name_vi": "5/1 — Người Dị Giáo / Nhà Nghiên Cứu",
  "tagline": "Người ta tìm bạn khi có vấn đề — và bạn phải chắc chắn mình thật sự giải được.",
  "mechanics": (
    "Hào 5 khiến người khác phóng chiếu lên bạn hình ảnh người có thể cứu tình thế. Hào 1 ở tầng "
    "vô thức buộc bạn phải có nền móng thật để không phụ cái kỳ vọng đó. Bạn thường được gọi vào "
    "đúng lúc khủng hoảng, và bạn thường giải được."
  ),
  "aligned": (
    "Bạn chuẩn bị kỹ trước khi nhận, và bạn nói rõ phạm vi mình làm được. Bạn đưa giải pháp thực "
    "tế, xong việc thì rút, không ở lại để bị gán vai anh hùng lâu dài. Danh tiếng bạn tốt vì nó "
    "đứng trên năng lực thật."
  ),
  "misaligned": (
    "Bạn nhận việc vì được tâng lên rồi mới đi tìm cách làm — với hào 5, khi vỡ thì tiếng xấu "
    "lan rất nhanh và rất đậm. Hoặc bạn sợ bị kỳ vọng nên trốn hẳn, không nhận gì cả, và cái nền "
    "móng bạn có không dùng được vào đâu."
  ),
  "practice": "Lần tới có người nhờ, hỏi lại ba câu về vấn đề của họ trước khi nhận. Chỉ nhận nếu bạn thật sự đã làm được việc tương tự.",
  "questions": [
    "Bạn có đang nhận việc vì được khen chứ không phải vì làm được?",
    "Người ta đang nghĩ bạn giỏi cái gì mà thật ra bạn chưa vững?"
  ]
},

"5/2": {
  "name_vi": "5/2 — Người Dị Giáo / Ẩn Sĩ",
  "tagline": "Bạn bị kéo ra ánh sáng liên tục, trong khi phần sâu nhất trong bạn chỉ muốn được yên.",
  "mechanics": (
    "Hào 5 hút kỳ vọng của người khác về phía bạn. Hào 2 ở tầng vô thức mang tài năng tự nhiên "
    "và nhu cầu được ở một mình. Đây là cặp hào kéo hai hướng ngược nhau mạnh nhất trong mười "
    "hai profile: bên ngoài người ta gọi, bên trong bạn muốn đóng cửa."
  ),
  "aligned": (
    "Bạn xây được một nhịp: rút vào làm cái mình giỏi, ra ngoài khi có lời gọi đúng, rồi rút "
    "về lại. Bạn từ chối phần lớn lời gọi mà không thấy áy náy. Cái bạn mang ra lần nào cũng có "
    "trọng lượng, vì nó được nuôi trong yên tĩnh."
  ),
  "misaligned": (
    "Bạn để bị kéo ra liên tục, không còn không gian riêng, và tài năng cạn. Rồi bạn không đáp "
    "ứng nổi kỳ vọng và chịu tiếng xấu — trong khi kỳ vọng đó chưa bao giờ do bạn tạo ra."
  ),
  "practice": "Từ chối một lời mời trong tuần này mà không giải thích dài. Chỉ một câu: \"Cảm ơn, lần này mình không tham gia.\"",
  "questions": [
    "Bạn còn bao nhiêu giờ một mình mỗi tuần?",
    "Kỳ vọng nào người ta đặt lên bạn mà bạn chưa từng nhận?"
  ]
},

"6/2": {
  "name_vi": "6/2 — Hình Mẫu / Ẩn Sĩ",
  "tagline": "Bạn sống thành ví dụ, không phải bằng cách giảng, mà bằng cách được nhìn thấy.",
  "mechanics": (
    "Hào 6 chia đời bạn ba chặng: va vấp, quan sát, rồi làm hình mẫu. Hào 2 mang tài năng bẩm "
    "sinh và nhu cầu ở ẩn. Bạn không đi tìm sự chú ý, nhưng ở chặng sau của đời, sự chú ý tìm "
    "tới bạn — vì cách bạn sống chứ không vì cái bạn nói."
  ),
  "aligned": (
    "Bạn để chặng đầu là chặng thử mà không tự trách. Chặng giữa bạn cho phép mình lùi lại, đọc, "
    "quan sát, ít tham gia. Chặng sau bạn xuất hiện với một sự chắc chắn tự nhiên, và người ta "
    "học từ bạn mà bạn không phải cố dạy."
  ),
  "misaligned": (
    "Bạn ép mình phải là hình mẫu ngay từ trẻ, sống theo tiêu chuẩn của người khác và mệt mỏi. "
    "Hoặc bạn rút quá sâu ở chặng giữa và không bao giờ bước ra lại, để cái mình đã tích lũy "
    "nằm im không ai chạm tới."
  ),
  "practice": "Hỏi hai người thân: theo họ, mình sống thế nào? Nghe mà không thanh minh.",
  "questions": [
    "Bạn đang ở chặng nào của đời mình?",
    "Bạn có đang cố dạy người khác thứ mà chính mình chưa sống qua không?"
  ]
},

"6/3": {
  "name_vi": "6/3 — Hình Mẫu / Người Thử Sai",
  "tagline": "Bạn trở thành hình mẫu không phải nhờ làm đúng, mà nhờ dám thử và dám kể lại.",
  "mechanics": (
    "Hào 6 mang ba chặng đời và một nhu cầu sâu về sự chính trực. Hào 3 ở tầng vô thức lại đẩy "
    "bạn vào thử nghiệm liên tục, nhiều cái không thành. Bạn sống trong một mâu thuẫn quen thuộc: "
    "muốn làm gương, mà lại là người hay va nhất."
  ),
  "aligned": (
    "Bạn hiểu rằng chính những lần trật mới là chất liệu làm nên hình mẫu của bạn. Ở chặng sau, "
    "bạn kể lại chúng một cách thẳng thắn, và người nghe thấy được vì bạn không tô vẽ. Bạn là "
    "kiểu người mà ai cũng biết đã đi qua thật rồi mới nói."
  ),
  "misaligned": (
    "Bạn giấu những lần trật để giữ hình ảnh, và mất đúng thứ làm bạn có giá trị. Hoặc bạn tự "
    "kết luận mình không xứng làm gương vì đời mình quá nhiều đổ vỡ — trong khi số lần đổ vỡ "
    "ấy chính là thiết kế."
  ),
  "practice": "Kể công khai một lần bạn làm sai và bạn đã học được gì. Với một người thôi cũng được.",
  "questions": [
    "Bạn đang giấu lần trật nào vì sợ mất hình ảnh?",
    "Nếu những lần va của bạn là chất liệu chứ không phải vết nhơ, bạn sẽ kể lại chúng thế nào?"
  ]
},
}
