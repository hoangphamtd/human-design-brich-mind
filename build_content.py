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
"""Gộp 3 module nội dung → hd-content-v1.json (cho frontend) + bản .md (cho Thầy duyệt)."""
import json, re
from content_types import TYPES
from content_authorities import AUTHORITIES
from content_profiles import PROFILES, LINE_NAMES
from content_centers import CENTERS
from content_channels import CHANNELS as CH
from iching_map import ICHING, GHI_CHU_LECH
try:
    from content_gates_p1 import GATES_P1
except ImportError:
    GATES_P1 = {}
try:
    from content_gates_p2 import GATES_P2
except ImportError:
    GATES_P2 = {}
try:
    from content_gates_p3 import GATES_P3
except ImportError:
    GATES_P3 = {}
try:
    from content_gates_p4 import GATES_P4
except ImportError:
    GATES_P4 = {}
GATES = {**GATES_P1, **GATES_P2, **GATES_P3, **GATES_P4}

# Tầng B nằm ở file riêng, KHÔNG đẩy lên GitHub (§7.3 / HD-02 §9.3).
# Thiếu file thì bản nội bộ dựng thiếu Tầng B — bản public vẫn đúng, vì bản
# public vốn không có Tầng B. Không dừng build, chỉ báo.
try:
    from noi_dung_tang_b import NOI_BO, NOI_SO
    CO_TANG_B = True
except ImportError:
    NOI_BO, NOI_SO, CO_TANG_B = {}, {}, False


def _chen(d: dict, khoa: str, gia_tri, sau: str) -> dict:
    """Chèn khoá vào ĐÚNG vị trí cũ, không phải nối vào cuối.

    JSON giữ nguyên thứ tự khoá, nên nối vào cuối là đổi md5 của cả file dù
    không một chữ nào khác. Bản đang chạy trên VPS có `noi_bo` sau `gates` và
    `noi_so` sau `name_vi` — phải đặt lại đúng chỗ đó.
    """
    if gia_tri is None or khoa in d:
        return d
    ra = {}
    for k, v in d.items():
        ra[k] = v
        if k == sau:
            ra[khoa] = gia_tri
    return ra

DISCLAIMER = (
  "Human Design là hệ thống chiêm nghiệm mang tính biểu tượng, không phải khoa học y học "
  "hay tâm lý học lâm sàng. Nội dung tại đây nhằm mục đích tham khảo và khám phá bản thân, "
  "không phải chẩn đoán, điều trị, hay lời khuyên y tế, tài chính, pháp lý. "
  "Bạn là người quyết định cuối cùng cho cuộc đời mình."
)

# §5.3 Instructions — bộ lọc ngôn ngữ
BANNED = ["chữa bệnh", "điều trị", "khỏi bệnh", "trị bệnh", "thay thế bác sĩ",
          "thay thuốc", "vận hạn", "giải hạn", "hoá giải", "tiên đoán",
          "số mệnh đã định", "100% chính xác", "chắc chắn bạn sẽ", "gây bệnh",
          "miễn dịch", "bệnh tật", "triệu chứng", "chẩn đoán", "vận hạn"]


def wc(s):
    return len(re.findall(r"\S+", s))


FLAGGED = []

def check(name, blob):
    """Bản nội bộ giữ nguyên nội dung gốc. Chỉ đánh dấu chỗ cần lọc khi publish."""
    hits = [w for w in BANNED if w in blob.lower()]
    if hits:
        FLAGGED.append((name, hits))


def build():
    out = {"version": "1.0", "lang": "vi", "brand": "B-RICH MIND",
           "disclaimer": DISCLAIMER,
           "line_names": LINE_NAMES,
           "audience": "internal", "nd38_filtered": False,
           "types": {}, "authorities": {}, "profiles": {}, "centers": {}, "gates": {}, "channels": {}}
    stats = []

    for k, v in TYPES.items():
        blob = " ".join(str(x) for x in v.values() if isinstance(x, str))
        check(f"type/{k}", blob)
        out["types"][k] = v
        stats.append(("Type", v["name_vi"], wc(blob)))

    for k, v in AUTHORITIES.items():
        blob = " ".join(str(x) for x in v.values() if isinstance(x, str))
        check(f"authority/{k}", blob)
        out["authorities"][k] = v
        stats.append(("Authority", v["name_vi"], wc(blob)))

    for k, v in PROFILES.items():
        blob = " ".join(str(x) for x in v.values() if isinstance(x, str))
        check(f"profile/{k}", blob)
        p, d = k.split("/")
        v = dict(v, lines={"personality": int(p), "design": int(d)})
        out["profiles"][k] = v
        stats.append(("Profile", v["name_vi"], wc(blob)))

    for k, v in CENTERS.items():
        v = _chen(v, "noi_bo", NOI_BO.get(k), "gates")
        for state in ("defined", "open"):
            blob = " ".join(str(x) for x in v[state].values() if isinstance(x, str))
            check(f"center/{k}/{state}", blob)
            stats.append(("Center", f"{v['name_vi']} ({state})", wc(blob)))
        out["centers"][k] = v

    iching = {r[0]: r for r in ICHING}
    for g, v in sorted(GATES.items()):
        v = _chen(v, "noi_so", NOI_SO.get(g), "name_vi")
        blob = " ".join(str(x) for x in v.values() if isinstance(x, str))
        check(f"gate/{g}", blob)
        n, hv, han, ngh, hd, mk = iching[g]
        v = dict(v, gate=g, name_en=hd,
                 iching={"que_so": n, "ten_han_viet": hv,
                         "nghia_goc": ngh, "muc_khop": mk,
                         "ghi_chu": GHI_CHU_LECH.get(n)})
        out["gates"][str(g)] = v
        stats.append(("Gate", f"Cổng {g} — {v['name_vi']}", wc(blob)))

    for k, v in CH.items():
        blob = " ".join(str(x) for x in v.values() if isinstance(x, str))
        check(f"channel/{k}", blob)
        out["channels"][k] = v
        stats.append(("Channel", f"Kênh {k} — {v['name_vi']}", wc(blob)))

    return out, stats


def to_md(d):
    L = ["# Kho nội dung Human Design — BẢN NỘI BỘ",
         "", "> ⛔ Bản đầy đủ, giữ nguyên nội dung gốc hệ thống, CHƯA qua bộ lọc NĐ38.", "> Không publish trực tiếp. Khi đưa ra công khai phải chạy bộ lọc §5.3 trước.", ""]

    L += ["---", "", "## PHẦN 1 — 5 TYPE", ""]
    for v in d["types"].values():
        L += [f"### {v['name_vi']}", f"*{v['tagline']}*", "",
              f"- **Chiến lược:** {v['strategy']}",
              f"- **Dấu hiệu đi đúng:** {v['signature']} · **Đi lệch:** {v['not_self']}",
              f"- **Trường năng lượng:** {v['aura']} · {v['pct']}", "",
              f"**Cơ học.** {v['mechanics']}", "",
              f"**Khi vận hành thuận.** {v['aligned']}", "",
              f"**Khi vận hành lệch.** {v['misaligned']}", "",
              f"**Việc làm ngay.** {v['practice']}", "",
              "**Câu tự vấn.**"] + [f"{i}. {q}" for i, q in enumerate(v["questions"], 1)] + [""]

    L += ["---", "", "## PHẦN 2 — 7 AUTHORITY", ""]
    for v in d["authorities"].values():
        L += [f"### {v['name_vi']}", f"*{v['tagline']}*", "",
              f"- **Điều kiện cơ học:** {v['rule']}",
              f"- **Nhịp quyết định:** {v['timeframe']}", "",
              f"**Cơ học.** {v['mechanics']}", "",
              f"**Khi vận hành thuận.** {v['aligned']}", "",
              f"**Khi vận hành lệch.** {v['misaligned']}", "",
              f"**Việc làm ngay.** {v['practice']}", "",
              "**Câu tự vấn.**"] + [f"{i}. {q}" for i, q in enumerate(v["questions"], 1)] + [""]

    L += ["---", "", "## PHẦN 3 — 12 PROFILE", "",
          "**Ý nghĩa 6 hào:**", ""]
    for n, ln in d["line_names"].items():
        L.append(f"- **Hào {n} — {ln['vi']}:** {ln['core']}")
    L.append("")
    for k, v in d["profiles"].items():
        L += [f"### {v['name_vi']}", f"*{v['tagline']}*", "",
              f"**Cơ học.** {v['mechanics']}", "",
              f"**Khi vận hành thuận.** {v['aligned']}", "",
              f"**Khi vận hành lệch.** {v['misaligned']}", "",
              f"**Việc làm ngay.** {v['practice']}", "",
              "**Câu tự vấn.**"] + [f"{i}. {q}" for i, q in enumerate(v["questions"], 1)] + [""]

    L += ["---", "", "## PHẦN 4 — 9 TRUNG TÂM", ""]
    lbl = {"defined": "ĐƯỢC ĐỊNH NGHĨA", "open": "MỞ"}
    for v in d["centers"].values():
        L += [f"### {v['name_vi']}", f"{v['role']} · Cổng: {', '.join(map(str, v['gates']))}", ""]
        for st in ("defined", "open"):
            b = v[st]
            L += [f"#### {v['name_vi']} — {lbl[st]}", f"*{b['tagline']}*", ""]
            if b.get("false_pursuit"):
                L += [f"**Điều bạn dễ đuổi theo.** {b['false_pursuit']}", ""]
            L += [f"**Cơ học.** {b['mechanics']}", "",
                  f"**Khi vận hành thuận.** {b['aligned']}", "",
                  f"**Khi vận hành lệch.** {b['misaligned']}", "",
                  f"**Việc làm ngay.** {b['practice']}", "",
                  "**Câu tự vấn.**"] + [f"{i}. {q}" for i, q in enumerate(b["questions"], 1)] + [""]

    if d["gates"]:
        L += ["---", "", f"## PHẦN 5 — CÁC CỔNG ({len(d['gates'])}/64)", ""]
        for g in sorted(d["gates"], key=int):
            v = d["gates"][g]
            ic = v["iching"]
            L += [f"### Cổng {g} — {v['name_vi']}",
                  f"*{v['tagline']}*", "",
                  f"- **Tên hệ thống:** {v['name_en']}",
                  f"- **Quẻ Kinh Dịch:** {ic['que_so']}. {ic['ten_han_viet']} — {ic['nghia_goc']} *(mức khớp: {ic['muc_khop']})*"]
            if ic.get("ghi_chu"):
                L.append(f"- **Ghi chú lệch:** {ic['ghi_chu']}")
            L.append(f"- **Kênh:** {v['kenh']}")
            if v.get("noi_so"):
                L.append(f"- **Nỗi sợ nguyên thuỷ:** {v['noi_so']}")
            L += ["",
                  f"**Cơ học.** {v['mechanics']}", "",
                  f"**Khi vận hành thuận.** {v['aligned']}", "",
                  f"**Khi vận hành lệch.** {v['misaligned']}", "",
                  f"**Việc làm ngay.** {v['practice']}", "",
                  "**Câu tự vấn.**"] + [f"{i}. {q}" for i, q in enumerate(v["questions"], 1)] + [""]

    if d.get("channels"):
        L += ["---", "", f"## PHẦN 6 — 36 KÊNH", ""]
        for mach in ("cá thể", "tập thể", "bộ tộc"):
            L += [f"### Mạch {mach}", ""]
            for k, v in d["channels"].items():
                if v["mach"] != mach:
                    continue
                L += [f"#### Kênh {k} — {v['name_vi']}", f"*{v['tagline']}*", "",
                      f"- **Nối:** {' ↔ '.join(v['centers'])}", "",
                      f"**Cơ học.** {v['mechanics']}", "",
                      f"**Khi vận hành thuận.** {v['aligned']}", "",
                      f"**Khi vận hành lệch.** {v['misaligned']}", "",
                      f"**Việc làm ngay.** {v['practice']}", "",
                      "**Câu tự vấn.**"] + [f"{i}. {q}" for i, q in enumerate(v["questions"], 1)] + [""]

    L += ["---", "", "## Disclaimer bắt buộc", "", f"> {d['disclaimer']}", ""]
    return "\n".join(L)


def ban_public(d):
    """Bản cho khách ngoài: gỡ mọi trường Tầng B, gỡ nỗi sợ ở cổng Lá lách."""
    import copy
    p = copy.deepcopy(d)
    p["audience"] = "public"
    p["nd38_filtered"] = True
    for v in p["centers"].values():
        v.pop("noi_bo", None)
    for v in p["gates"].values():
        v.pop("noi_so", None)
    return p


if __name__ == "__main__":
    data, stats = build()
    assert len(data["types"]) == 5
    assert len(data["authorities"]) == 7
    assert len(data["profiles"]) == 12
    assert len(data["centers"]) == 9
    print(f"📦 Cổng {len(data['gates'])}/64 · Kênh {len(data['channels'])}/36")
    assert len(data["channels"]) == 36
    # newline="\n" là bắt buộc, không phải cho gọn.
    # Không có nó thì trên Windows Python đổi \n thành \r\n lúc ghi, và hai
    # file JSON đổi md5 hoàn toàn dù không một chữ nào khác. Bản đang chạy
    # trên VPS là LF; build lại trên Windows mà thiếu dòng này là mọi phép so
    # md5 báo động giả, và scp lên VPS một file khác byte mà không rõ vì sao.
    with open("hd-content-v1.json", "w", encoding="utf-8", newline="\n") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    pub = ban_public(data)
    with open("hd-content-public.json", "w", encoding="utf-8", newline="\n") as f:
        json.dump(pub, f, ensure_ascii=False, indent=2)
    con = sum(1 for v in data["centers"].values() if v.get("noi_bo")) \
        + sum(1 for v in data["gates"].values() if v.get("noi_so"))
    print(f"📤 Xuất 2 bản: nội bộ (đủ) · public (đã gỡ {con} mục Tầng B)")
    # Tên file phải khớp file đang có trong thư mục và trong HD-11 §3.
    # Tên cũ "HD-03-NOI-DUNG-TYPE-AUTHORITY-PROFILE.md" sinh ra file thứ hai
    # thay vì cập nhật file đang dùng.
    with open("HD-03-KHO-NOI-DUNG-NOI-BO.md", "w", encoding="utf-8", newline="\n") as f:
        f.write(to_md(data))
    total = sum(s[2] for s in stats)
    print(f"✅ {len(stats)} khối · {total} từ · trung bình {total//len(stats)} từ/khối")
    if FLAGGED:
        print(f"🔒 BẢN NỘI BỘ — {len(FLAGGED)} khối có từ cần lọc khi publish:")
        for n, h in FLAGGED:
            print(f"     {n}: {h}")
    else:
        print("✅ Không khối nào chứa từ cần lọc")
    short = [s for s in stats if s[2] < 120]
    print("⚠️ Khối quá ngắn (dưới 120 từ):", [s[1] for s in short] or "không có")
