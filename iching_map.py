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
"""Ánh xạ 64 cổng Human Design ↔ 64 quẻ Kinh Dịch (thứ tự King Wen).

DỮ KIỆN: Human Design lấy thẳng số hiệu quẻ King Wen làm số hiệu cổng.
Cổng 1 = quẻ 1, cổng 64 = quẻ 64. Đây là tuyên bố của chính hệ thống,
không phải suy diễn thêm.

Trường "khop" = mức khớp giữa tên cổng HD và nghĩa quẻ Kinh Dịch truyền thống:
  "cao"   — tên cổng gần như dịch thẳng nghĩa quẻ
  "vua"   — cùng gốc ý nhưng HD đã chuyển hướng diễn giải
  "lech"  — HD diễn giải khác hẳn Dịch truyền thống, phải ghi chú khi dạy
"""

# (số quẻ, tên Hán Việt, chữ Hán, nghĩa gốc ngắn, tên cổng HD, mức khớp)
ICHING = [
 (1,"Càn","乾","Trời, sức sáng tạo thuần dương","Self-Expression","vua"),
 (2,"Khôn","坤","Đất, sức thụ nhận, chở che","Direction of the Self","vua"),
 (3,"Truân","屯","Khó khăn buổi đầu, mầm chưa nhú","Ordering","vua"),
 (4,"Mông","蒙","Non dại, cần được dạy","Formulization","vua"),
 (5,"Nhu","需","Chờ đợi, nuôi dưỡng đúng lúc","Fixed Rhythms","cao"),
 (6,"Tụng","訟","Tranh tụng, xung đột","Friction","cao"),
 (7,"Sư","師","Quân đội, người dẫn quân","The Role of the Self","cao"),
 (8,"Tỷ","比","Thân gần, liên kết","Contribution","vua"),
 (9,"Tiểu Súc","小畜","Chứa nhỏ, tích từng chút","Focus","vua"),
 (10,"Lý","履","Bước đi, cách hành xử","Behaviour of the Self","cao"),
 (11,"Thái","泰","Thông suốt, hanh thông","Ideas","lech"),
 (12,"Bĩ","否","Bế tắc, không thông","Caution","cao"),
 (13,"Đồng Nhân","同人","Cùng người, hoà đồng","The Listener","vua"),
 (14,"Đại Hữu","大有","Có lớn, của cải nhiều","Power Skills","vua"),
 (15,"Khiêm","謙","Khiêm nhường","Extremes","lech"),
 (16,"Dự","豫","Vui vẻ, hăng hái chuẩn bị","Skills","vua"),
 (17,"Tùy","隨","Theo, thuận theo","Opinions","lech"),
 (18,"Cổ","蠱","Đồ hỏng cần sửa","Correction","cao"),
 (19,"Lâm","臨","Đến gần, tiếp cận","Wanting","vua"),
 (20,"Quán","觀","Quan sát, chiêm ngưỡng","The Now","vua"),
 (21,"Phệ Hạp","噬嗑","Cắn xuyên, dùng hình phạt","The Hunter","vua"),
 (22,"Bí","賁","Trang sức, vẻ đẹp bên ngoài","Openness","vua"),
 (23,"Bác","剝","Bóc mòn, tan rã","Assimilation","lech"),
 (24,"Phục","復","Trở lại, quay về","Rationalization","vua"),
 (25,"Vô Vọng","無妄","Không càn bậy, hồn nhiên chân thật","Spirit of the Self","vua"),
 (26,"Đại Súc","大畜","Chứa lớn, tích tụ lớn","The Egoist","vua"),
 (27,"Di","頤","Nuôi dưỡng, hàm nuôi","Caring","cao"),
 (28,"Đại Quá","大過","Quá lớn, vượt mức chịu đựng","The Game Player","vua"),
 (29,"Khảm","坎","Hiểm, nước sâu lặp lại","Perseverance","vua"),
 (30,"Ly","離","Lửa, bám vào, sáng rực","Recognition of Feelings","vua"),
 (31,"Hàm","咸","Cảm ứng, rung động lẫn nhau","Leading","vua"),
 (32,"Hằng","恆","Bền lâu, thường hằng","Continuity","cao"),
 (33,"Độn","遯","Lui ẩn, rút đi","Privacy","cao"),
 (34,"Đại Tráng","大壯","Lớn mạnh, sức thịnh","Power","cao"),
 (35,"Tấn","晉","Tiến lên, tiến bộ","Change","vua"),
 (36,"Minh Di","明夷","Ánh sáng bị che, thời tối","Crisis","cao"),
 (37,"Gia Nhân","家人","Người trong nhà","Friendship","cao"),
 (38,"Khuê","睽","Chống đối, xa cách","The Fighter","cao"),
 (39,"Kiển","蹇","Trở ngại, đi khó","Provocation","vua"),
 (40,"Giải","解","Cởi bỏ, giải toả","Aloneness","vua"),
 (41,"Tổn","損","Giảm bớt, tổn đi","Contraction","cao"),
 (42,"Ích","益","Tăng thêm, lợi ích","Growth","cao"),
 (43,"Quải","夬","Quyết đoán, dứt khoát","Insight","vua"),
 (44,"Cấu","姤","Gặp gỡ bất ngờ","Alertness","lech"),
 (45,"Tụy","萃","Tụ họp","Gatherer","cao"),
 (46,"Thăng","升","Đi lên, thăng tiến","Determination","vua"),
 (47,"Khốn","困","Khốn cùng, bị vây","Realization","lech"),
 (48,"Tỉnh","井","Giếng, nguồn sâu không cạn","Depth","cao"),
 (49,"Cách","革","Thay đổi, cách mạng","Principles","vua"),
 (50,"Đỉnh","鼎","Vạc, luật lệ và tế tự","Values","cao"),
 (51,"Chấn","震","Sấm, chấn động","Shock","cao"),
 (52,"Cấn","艮","Núi, dừng lại","Stillness","cao"),
 (53,"Tiệm","漸","Tiến dần từng bước","Beginnings","vua"),
 (54,"Quy Muội","歸妹","Gả em gái, vào bằng cửa phụ","Ambition","vua"),
 (55,"Phong","豐","Thịnh vượng, sung mãn","Spirit","vua"),
 (56,"Lữ","旅","Lữ khách, đi xa","Stimulation","vua"),
 (57,"Tốn","巽","Gió, thấm vào nhẹ nhàng","Intuitive Insight","vua"),
 (58,"Đoài","兌","Đầm, vui vẻ","Vitality","cao"),
 (59,"Hoán","渙","Tan ra, phân tán","Sexuality","lech"),
 (60,"Tiết","節","Đốt tre, giới hạn có chừng mực","Limitation","cao"),
 (61,"Trung Phu","中孚","Lòng thành bên trong","Inner Truth","cao"),
 (62,"Tiểu Quá","小過","Vượt nhỏ, chú ý chi tiết","Detail","cao"),
 (63,"Ký Tế","既濟","Đã qua sông, đã hoàn tất","Doubt","lech"),
 (64,"Vị Tế","未濟","Chưa qua sông, chưa hoàn tất","Confusion","vua"),
]

GHI_CHU_LECH = {
 11: "Dịch: Thái là thời hanh thông. HD: cổng 11 là kho ý tưởng. Nối được qua ý 'trời đất giao hoà sinh ra cái mới'.",
 15: "Dịch: Khiêm là khiêm nhường. HD: cổng 15 là biên độ cực đoan trong nhịp sống. Hai nghĩa gần như không gặp nhau.",
 17: "Dịch: Tùy là thuận theo. HD: cổng 17 là ý kiến, quan điểm. HD đảo chiều: từ theo người thành đưa ra cái của mình.",
 23: "Dịch: Bác là bóc mòn tan rã. HD: cổng 23 là năng lực diễn đạt cái mới thành lời. Nối qua ý 'bóc lớp vỏ để lộ ra bên trong'.",
 44: "Dịch: Cấu là gặp gỡ bất ngờ. HD: cổng 44 là bản năng nhận biết mẫu hình quá khứ. Khác hướng rõ rệt.",
 47: "Dịch: Khốn là bị vây khốn. HD: cổng 47 là quá trình vỡ ra hiểu biết. HD lấy phần 'bí bách trước khi thông'.",
 59: "Dịch: Hoán là tan ra phân tán. HD: cổng 59 là phá vỡ rào cản để thân mật. Nối qua ý 'làm tan ranh giới'.",
 63: "Dịch: Ký Tế là đã hoàn tất. HD: cổng 63 là nghi ngờ, kiểm tra logic. HD lấy phần 'xong rồi vẫn phải soi lại'.",
}
