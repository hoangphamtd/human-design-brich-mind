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
"""Sinh file dữ liệu lõi Human Design (hd-core-data.json).
Nguồn quy chiếu: Rave Mandala - cổng 41 bắt đầu tại 2°00'00" Bảo Bình (302° hoàng đạo nhiệt đới).
Mỗi cổng = 360/64 = 5.625°, mỗi hào = 5.625/6 = 0.9375°.
"""
import json

# Thứ tự 64 cổng quanh bánh xe Rave, bắt đầu từ cổng 41 tại 302.0°
WHEEL = [41, 19, 13, 49, 30, 55, 37, 63, 22, 36, 25, 17, 21, 51, 42, 3,
         27, 24, 2, 23, 8, 20, 16, 35, 45, 12, 15, 52, 39, 53, 62, 56,
         31, 33, 7, 4, 29, 59, 40, 64, 47, 6, 46, 18, 48, 57, 32, 50,
         28, 44, 1, 43, 14, 34, 9, 5, 26, 11, 10, 58, 38, 54, 61, 60]

START_DEG = 302.0
GATE_ARC = 360.0 / 64          # 5.625
LINE_ARC = GATE_ARC / 6        # 0.9375
COLOR_ARC = LINE_ARC / 6       # 0.15625
TONE_ARC = COLOR_ARC / 6       # 0.0260416...
BASE_ARC = TONE_ARC / 5        # 0.0052083...

GATE_NAME = {
 1:"Self-Expression",2:"Direction of the Self",3:"Ordering",4:"Formulization",
 5:"Fixed Rhythms",6:"Friction",7:"The Role of the Self",8:"Contribution",
 9:"Focus",10:"Behaviour of the Self",11:"Ideas",12:"Caution",13:"The Listener",
 14:"Power Skills",15:"Extremes",16:"Skills",17:"Opinions",18:"Correction",
 19:"Wanting",20:"The Now",21:"The Hunter",22:"Openness",23:"Assimilation",
 24:"Rationalization",25:"Spirit of the Self",26:"The Egoist",27:"Caring",
 28:"The Game Player",29:"Perseverance",30:"Recognition of Feelings",
 31:"Leading",32:"Continuity",33:"Privacy",34:"Power",35:"Change",36:"Crisis",
 37:"Friendship",38:"The Fighter",39:"Provocation",40:"Aloneness",
 41:"Contraction",42:"Growth",43:"Insight",44:"Alertness",45:"Gatherer",
 46:"Determination",47:"Realization",48:"Depth",49:"Principles",50:"Values",
 51:"Shock",52:"Stillness",53:"Beginnings",54:"Ambition",55:"Spirit",
 56:"Stimulation",57:"Intuitive Insight",58:"Vitality",59:"Sexuality",
 60:"Limitation",61:"Inner Truth",62:"Detail",63:"Doubt",64:"Confusion"}

CENTER_GATES = {
 "head":[61,63,64],
 "ajna":[47,24,4,11,43,17],
 "throat":[62,23,56,35,12,45,33,8,31,20,16],
 "g":[1,13,25,46,2,15,10,7],
 "heart":[21,40,26,51],
 "spleen":[48,57,44,50,32,28,18],
 "solar_plexus":[36,22,37,6,49,55,30],
 "sacral":[5,14,29,59,9,3,42,27,34],
 "root":[53,60,52,19,39,41,58,38,54]}

CENTERS = {
 "head":{"vi":"Đầu","type":"pressure","motor":False,"awareness":False},
 "ajna":{"vi":"Ajna (Trí)","type":"awareness","motor":False,"awareness":True},
 "throat":{"vi":"Cổ họng","type":"expression","motor":False,"awareness":False},
 "g":{"vi":"Trung tâm G (Bản ngã/Định hướng)","type":"identity","motor":False,"awareness":False},
 "heart":{"vi":"Tim / Ego","type":"motor","motor":True,"awareness":False},
 "spleen":{"vi":"Lá lách","type":"awareness","motor":False,"awareness":True},
 "solar_plexus":{"vi":"Đám rối mặt trời (Cảm xúc)","type":"motor+awareness","motor":True,"awareness":True},
 "sacral":{"vi":"Xương cùng","type":"motor","motor":True,"awareness":False},
 "root":{"vi":"Gốc","type":"motor+pressure","motor":True,"awareness":False}}

CHANNELS = [
 (1,8,"Inspiration","g","throat","individual"),
 (2,14,"The Beat","g","sacral","individual"),
 (3,60,"Mutation","sacral","root","individual"),
 (4,63,"Logic","ajna","head","collective"),
 (5,15,"Rhythm","sacral","g","collective"),
 (6,59,"Mating","solar_plexus","sacral","tribal"),
 (7,31,"The Alpha","g","throat","collective"),
 (9,52,"Concentration","sacral","root","collective"),
 (10,20,"Awakening","g","throat","individual"),
 (10,34,"Exploration","g","sacral","individual"),
 (10,57,"Perfected Form","g","spleen","individual"),
 (11,56,"Curiosity","ajna","throat","collective"),
 (12,22,"Openness","throat","solar_plexus","individual"),
 (13,33,"The Prodigal","g","throat","collective"),
 (16,48,"The Wavelength","throat","spleen","collective"),
 (17,62,"Acceptance","ajna","throat","collective"),
 (18,58,"Judgment","spleen","root","collective"),
 (19,49,"Synthesis","root","solar_plexus","tribal"),
 (20,34,"Charisma","throat","sacral","individual"),
 (20,57,"The Brainwave","throat","spleen","individual"),
 (21,45,"Money","heart","throat","tribal"),
 (23,43,"Structuring","throat","ajna","individual"),
 (24,61,"Awareness","ajna","head","individual"),
 (25,51,"Initiation","g","heart","individual"),
 (26,44,"Surrender","heart","spleen","tribal"),
 (27,50,"Preservation","sacral","spleen","tribal"),
 (28,38,"Struggle","spleen","root","individual"),
 (29,46,"Discovery","sacral","g","collective"),
 (30,41,"Recognition","solar_plexus","root","collective"),
 (32,54,"Transformation","spleen","root","tribal"),
 (34,57,"Power","sacral","spleen","individual"),
 (35,36,"Transitoriness","throat","solar_plexus","collective"),
 (37,40,"Community","solar_plexus","heart","tribal"),
 (39,55,"Emoting","root","solar_plexus","individual"),
 (42,53,"Maturation","sacral","root","collective"),
 (47,64,"Abstraction","ajna","head","collective")]

BODIES = ["sun","earth","north_node","south_node","moon","mercury","venus","mars",
          "jupiter","saturn","uranus","neptune","pluto"]

TYPES = {
 "manifestor":{"vi":"Manifestor (Người Khởi Tạo)","strategy":"Thông báo trước khi hành động",
   "signature":"Bình an","not_self":"Tức giận","aura":"Đóng & đẩy","pct":"~9%"},
 "generator":{"vi":"Generator (Người Kiến Tạo)","strategy":"Chờ đợi để phản hồi",
   "signature":"Thoả mãn","not_self":"Bực bội","aura":"Mở & bao bọc","pct":"~37%"},
 "manifesting_generator":{"vi":"Manifesting Generator","strategy":"Phản hồi rồi thông báo",
   "signature":"Thoả mãn & Bình an","not_self":"Bực bội & Tức giận","aura":"Mở & bao bọc","pct":"~33%"},
 "projector":{"vi":"Projector (Người Dẫn Dắt)","strategy":"Chờ được mời",
   "signature":"Thành công","not_self":"Cay đắng","aura":"Tập trung & thẩm thấu","pct":"~20%"},
 "reflector":{"vi":"Reflector (Người Phản Chiếu)","strategy":"Chờ một chu kỳ mặt trăng (~28 ngày)",
   "signature":"Ngạc nhiên","not_self":"Thất vọng","aura":"Lấy mẫu & kháng cự","pct":"~1%"}}

AUTHORITIES = [
 {"key":"emotional","vi":"Nội quyền Cảm xúc","priority":1,
  "rule":"Đám rối mặt trời được định nghĩa","advice":"Không có sự thật trong khoảnh khắc - chờ qua sóng cảm xúc"},
 {"key":"sacral","vi":"Nội quyền Xương cùng","priority":2,
  "rule":"Xương cùng định nghĩa & Đám rối không định nghĩa","advice":"Phản hồi tức thời từ bụng (uh-huh / un-un)"},
 {"key":"splenic","vi":"Nội quyền Lá lách","priority":3,
  "rule":"Lá lách định nghĩa & Đám rối, Xương cùng không định nghĩa","advice":"Trực giác tức thời, chỉ nói một lần"},
 {"key":"ego","vi":"Nội quyền Tim/Ego","priority":4,
  "rule":"Tim định nghĩa & Đám rối, Xương cùng, Lá lách không định nghĩa","advice":"Ý chí - 'tôi muốn / tôi không muốn'"},
 {"key":"self_projected","vi":"Nội quyền Tự Chiếu (G)","priority":5,
  "rule":"G nối Cổ họng & không có trung tâm ưu tiên trên","advice":"Nghe chính giọng nói của mình khi nói ra"},
 {"key":"mental_projected","vi":"Nội quyền Ngoại cảnh / Trí","priority":6,
  "rule":"Projector không có trung tâm nội quyền nào","advice":"Nói chuyện với người tin cậy trong môi trường đúng"},
 {"key":"lunar","vi":"Nội quyền Mặt trăng","priority":7,
  "rule":"Reflector - không trung tâm nào định nghĩa","advice":"Chờ trọn 28 ngày chu kỳ mặt trăng trước quyết định lớn"}]

PROFILES = {
 "1/3":"Nhà nghiên cứu / Người thử-sai","1/4":"Nhà nghiên cứu / Người kết nối",
 "2/4":"Ẩn sĩ / Người kết nối","2/5":"Ẩn sĩ / Người dị giáo",
 "3/5":"Người thử-sai / Người dị giáo","3/6":"Người thử-sai / Hình mẫu",
 "4/6":"Người kết nối / Hình mẫu","4/1":"Người kết nối / Nhà nghiên cứu",
 "5/1":"Người dị giáo / Nhà nghiên cứu","5/2":"Người dị giáo / Ẩn sĩ",
 "6/2":"Hình mẫu / Ẩn sĩ","6/3":"Hình mẫu / Người thử-sai"}


def build():
    gate_to_center = {g: c for c, gs in CENTER_GATES.items() for g in gs}
    gates = []
    for i, g in enumerate(WHEEL):
        start = (START_DEG + i * GATE_ARC) % 360
        gates.append({
            "gate": g, "name_en": GATE_NAME[g], "center": gate_to_center[g],
            "wheel_index": i,
            "start_deg": round(start, 6),
            "end_deg": round((start + GATE_ARC) % 360, 6),
            "lines": [{"line": l + 1,
                       "start_deg": round((start + l * LINE_ARC) % 360, 6)}
                      for l in range(6)]})

    channels = [{"key": f"{a}-{b}", "gates": [a, b], "name_en": n,
                 "centers": [c1, c2], "circuit": circ}
                for a, b, n, c1, c2, circ in CHANNELS]

    return {
        "meta": {
            "system": "Human Design (Rave)",
            "zodiac": "tropical",
            "wheel_anchor": "Cổng 41 bắt đầu tại 2°00'00\" Bảo Bình = 302.0° hoàng đạo",
            "arc": {"gate": GATE_ARC, "line": LINE_ARC, "color": COLOR_ARC,
                    "tone": TONE_ARC, "base": BASE_ARC},
            "design_offset": "88°00'00\" cung mặt trời TRƯỚC vị trí Mặt Trời lúc sinh (~88 ngày 5-6 giờ)",
            "bodies": BODIES,
            "activation_count": len(BODIES) * 2},
        "gates": gates, "centers": CENTERS, "channels": channels,
        "types": TYPES, "authorities": AUTHORITIES, "profiles": PROFILES}


if __name__ == "__main__":
    data = build()
    # kiểm tra tính toàn vẹn
    assert len(data["gates"]) == 64 and len(set(WHEEL)) == 64
    assert len(data["channels"]) == 36
    assert sum(len(v) for v in CENTER_GATES.values()) == 64
    ch_gates = sorted({g for c in CHANNELS for g in c[:2]})
    assert len(ch_gates) == 64, f"cổng trong kênh: {len(ch_gates)}"
    with open("hd-core-data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("OK - 64 cổng, 36 kênh, 9 trung tâm. 360° =",
          round(64 * GATE_ARC, 6))
