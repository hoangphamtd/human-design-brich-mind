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
"""render_chart.py — Từ dữ liệu sinh của khách → trang kết quả HTML hoàn chỉnh.

Dùng:
    python3 render_chart.py 1985-03-15 07:30 --ten "TK-06" --noi "Cần Thơ"
    python3 render_chart.py 1970-05-01 14:20 --gio-khong-chac
    python3 render_chart.py 1985-03-15 07:30 --json     # chỉ in JSON cơ học

Ra: ket-qua-<tên>.html trong thư mục hiện tại.
"""
from __future__ import annotations
import argparse, json, html, os, re, unicodedata
from pathlib import Path

import hd_engine as E
import bodygraph as BG
import luan_moc_doi as MD
import luan_transit_thang as TT
import noi_dung_phap_ly as PL

# App nằm dưới brichmind.com/human-design nên link ở chân trang phải có tiền
# tố này. Chạy từ dòng lệnh thì GOC rỗng, link thành /ma-nguon — file HTML
# lưu ra để đọc offline, không bấm link.
GOC = os.getenv("GOC", "").rstrip("/")

HERE = Path(__file__).parent
NOI_SINH = {   # toạ độ một số nơi hay gặp; nơi khác thì truyền --lat --lon
    "tp. hồ chí minh": (10.8231, 106.6297), "sài gòn": (10.8231, 106.6297),
    "hà nội": (21.0278, 105.8342), "đà nẵng": (16.0544, 108.2022),
    "cần thơ": (10.0452, 105.7469), "huế": (16.4637, 107.5909),
    "hải phòng": (20.8449, 106.6881), "nha trang": (12.2388, 109.1967),
    "biên hoà": (10.9574, 106.8426), "vũng tàu": (10.3460, 107.0843),
}

CENTER_VI = {"head": "Đầu", "ajna": "Ajna", "throat": "Cổ họng", "g": "Trung tâm G",
             "heart": "Tim / Ý chí", "spleen": "Lá lách",
             "solar_plexus": "Đám rối mặt trời", "sacral": "Xương cùng", "root": "Gốc"}
BODY_VI = {"sun": "Mặt Trời", "earth": "Trái Đất", "north_node": "Nút Bắc",
           "south_node": "Nút Nam", "moon": "Mặt Trăng", "mercury": "Thuỷ",
           "venus": "Kim", "mars": "Hoả", "jupiter": "Mộc", "saturn": "Thổ",
           "uranus": "Thiên Vương", "neptune": "Hải Vương", "pluto": "Diêm Vương"}


def slug(s: str) -> str:
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if unicodedata.category(c) != "Mn").replace("đ", "d").replace("Đ", "D")
    return re.sub(r"[^a-zA-Z0-9]+", "-", s).strip("-").lower() or "khach"


def e(x) -> str:
    return html.escape(str(x))


def blocks(chart: dict, C: dict) -> str:
    """Ghép nội dung từ kho vào đúng cấu hình của khách."""
    out = []
    t = C["types"][chart["type"]]
    a = C["authorities"][chart["authority"]]
    p = C["profiles"][chart["profile"]]

    def khoi(nhan, tieu_de, tag, d, extra=""):
        q = "".join(f"<li>{e(x)}</li>" for x in d["questions"])
        fp = (f'<div class="blk duoi"><h3>Điều bạn dễ đuổi theo</h3><p>{e(d["false_pursuit"])}</p></div>'
              if d.get("false_pursuit") else "")
        return f"""<section><div class="wrap">
<p class="sec-no">{e(nhan)}</p><h2>{e(tieu_de)}</h2><p class="sub">{e(tag)}</p>{extra}{fp}
<div class="blk"><h3>Cơ học</h3><p>{e(d['mechanics'])}</p></div>
<div class="blk thuan"><h3>Khi vận hành thuận</h3><p>{e(d['aligned'])}</p></div>
<div class="blk lech"><h3>Khi vận hành lệch</h3><p>{e(d['misaligned'])}</p></div>
<div class="blk lam"><h3>Việc làm ngay</h3><p>{e(d['practice'])}</p></div>
<ol class="hoi">{q}</ol></div></section>"""

    facts_t = (f'<dl class="facts"><div><dt>Chiến lược</dt><dd>{e(t["strategy"])}</dd></div>'
               f'<div><dt>Trường năng lượng</dt><dd>{e(t["aura"])}</dd></div>'
               f'<div><dt>Tỉ lệ</dt><dd>{e(t["pct"])}</dd></div></dl>')
    out.append(khoi("Phần một — Loại năng lượng", t["name_vi"], t["tagline"], t, facts_t))

    facts_a = (f'<dl class="facts"><div><dt>Điều kiện cơ học</dt><dd>{e(a["rule"])}</dd></div>'
               f'<div><dt>Nhịp quyết định</dt><dd>{e(a["timeframe"])}</dd></div></dl>')
    out.append(khoi("Phần hai — Cách bạn ra quyết định", a["name_vi"], a["tagline"], a, facts_a))

    L = C["line_names"]
    pl, dl = p["lines"]["personality"], p["lines"]["design"]
    stack = "".join(
        f'<div class="hao{" on" if n == pl else ""}{" on d" if n == dl else ""}">'
        f'<span class="n">{n}</span><span class="bar"><i></i></span></div>' for n in range(1, 7))
    legend = (f'<p><b>Hào {pl} — {e(L[str(pl)]["vi"])} (ý thức)</b>{e(L[str(pl)]["core"])}</p>'
              f'<p><b>Hào {dl} — {e(L[str(dl)]["vi"])} (vô thức)</b>{e(L[str(dl)]["core"])}</p>')
    out.append(khoi("Phần ba — Vai bạn đóng trong đời", p["name_vi"], p["tagline"], p,
                    f'<div class="hexa"><div class="stack">{stack}</div>'
                    f'<div class="legend">{legend}</div></div>'))

    # Trung tâm — theo đúng trạng thái thật của khách
    tt = []
    for k in ["head", "ajna", "throat", "g", "heart", "spleen", "solar_plexus", "sacral", "root"]:
        st = "defined" if k in chart["trung_tam_dinh_nghia"] else "open"
        c, b = C["centers"][k], C["centers"][k][st]
        nhan = "được định nghĩa" if st == "defined" else "mở"
        fp = (f'<p class="duoi-in"><b>Điều bạn dễ đuổi theo.</b> {e(b["false_pursuit"])}</p>'
              if b.get("false_pursuit") else "")
        ns = f'<p class="cgates">Vai trò: {e(c["role"])}</p>'
        # Tầng B — chỉ có mặt ở bản nội bộ
        nb = (f'<div class="tangb"><h3>Theo hệ thống gốc — chỉ dùng khi tư vấn riêng</h3>'
              f'<p>{e(c["noi_bo"])}</p></div>') if c.get("noi_bo") else ""
        q = "".join(f"<li>{e(x)}</li>" for x in b["questions"])
        tt.append(f"""<details class="acc"{' open' if st == 'defined' else ''}>
<summary><span class="dot {st}"></span>{e(c['name_vi'])} — <b>{nhan}</b></summary>
<div class="acc-body">{ns}<p class="sub">{e(b['tagline'])}</p>{fp}{nb}
<p><b>Cơ học.</b> {e(b['mechanics'])}</p>
<p><b>Khi vận hành thuận.</b> {e(b['aligned'])}</p>
<p><b>Khi vận hành lệch.</b> {e(b['misaligned'])}</p>
<p><b>Việc làm ngay.</b> {e(b['practice'])}</p>
<ol class="hoi">{q}</ol></div></details>""")
    out.append(f"""<section><div class="wrap"><p class="sec-no">Phần bốn — Chín trung tâm</p>
<h2>Nơi bạn ổn định và nơi bạn dễ bị cuốn theo</h2>
<p class="sub">Chấm đỏ là trung tâm được định nghĩa — chỗ bạn nhất quán suốt đời.
Chấm rỗng là trung tâm mở — chỗ bạn hấp thụ và khuếch đại năng lượng của người xung quanh.</p>
{''.join(tt)}</div></section>""")

    # Kênh định nghĩa của khách — giải thích vì sao ra Type này
    if chart["kenh"]:
        kk = []
        for key in chart["kenh"]:
            a, b = sorted(map(int, key.split("-")))
            cd = C["channels"].get(f"{a}-{b}")
            if not cd:
                continue
            q = "".join(f"<li>{e(x)}</li>" for x in cd["questions"])
            noi = " ↔ ".join(CENTER_VI[x] for x in cd["centers"])
            kk.append(f"""<details class="acc" open><summary>
<span class="pl">{a}-{b}</span>{e(cd['name_vi'])} — <b>{noi}</b></summary>
<div class="acc-body"><p class="cgates">Mạch {e(cd['mach'])}</p>
<p class="sub">{e(cd['tagline'])}</p>
<p><b>Cơ học.</b> {e(cd['mechanics'])}</p>
<p><b>Khi vận hành thuận.</b> {e(cd['aligned'])}</p>
<p><b>Khi vận hành lệch.</b> {e(cd['misaligned'])}</p>
<p><b>Việc làm ngay.</b> {e(cd['practice'])}</p>
<ol class="hoi">{q}</ol></div></details>""")
        out.append(f"""<section><div class="wrap"><p class="sec-no">Phần năm — Kênh của bạn</p>
<h2>{len(kk)} kênh định nghĩa</h2>
<p class="sub">Kênh là chỗ hai cổng cùng hoạt hoá và nối hai trung tâm lại.
Chính các kênh này quyết định bạn thuộc loại năng lượng nào và ra quyết định bằng cách nào.</p>
{''.join(kk)}</div></section>""")
    else:
        out.append("""<section><div class="wrap"><p class="sec-no">Phần năm — Kênh của bạn</p>
<h2>Không có kênh định nghĩa</h2>
<p class="sub">Không kênh nào được định nghĩa, nên cả chín trung tâm đều mở.
Bạn không mang một cấu hình cố định nào — bạn phản chiếu môi trường quanh mình.</p>
</div></section>""")

    # ── Mốc chuyển đời (tầng năm) ──────────────────────────────
    try:
        md = MD.luan_moc_doi(chart, C["gates"])
    except Exception:
        md = None
    if md and (md["dang_o_trong"] or md["sap_toi"]):
        kh = []
        for b in md["dang_o_trong"] + md["sap_toi"]:
            nhan = "Đang ở trong" if b in md["dang_o_trong"] else b.get("con_bao_lau", "Sắp tới")
            q = "".join(f"<li>{e(x)}</li>" for x in b["cau_hoi"])
            kh.append(f"""<div class="moc">
<p class="moc-nhan">{e(nhan)}</p>
<h3>{e(b['ten'])}</h3><p class="sub">{e(b['tagline'])}</p>
<dl class="facts"><div><dt>Thời gian</dt><dd>{e(b['thoi_gian'])}</dd></div>
<div><dt>Tuổi</dt><dd>{e(b['tuoi'])}</dd></div>
<div><dt>Chạm cổng</dt><dd>{e(b['cong'])} — {e(b['ten_cong'])}</dd></div></dl>
<p><b>Dữ kiện.</b> {e(b['du_kien'])}</p>
<p><b>Riêng bạn.</b> {e(b['noi_vao_doi'])}</p>
<p><b>Thường thấy.</b> {e(b['thuong_thay'])}</p>
<div class="blk thuan"><h3>Đi qua thuận</h3><p>{e(b['thuan'])}</p></div>
<div class="blk lech"><h3>Đi qua lệch</h3><p>{e(b['lech'])}</p></div>
<ol class="hoi">{q}</ol></div>""")
        qua = " · ".join(f"{e(b['ten'])} ({e(b['tuoi'])}t)" for b in md["da_qua"][-4:])
        out.append(f"""<section><div class="wrap"><p class="sec-no">Phần sáu — Mốc chuyển đời</p>
<h2>Những chặng lớn tính được trước</h2>
<p class="sub">Đây là phần chắc chắn nhất trong bản đồ, vì nó chỉ phụ thuộc chu kỳ
quỹ đạo hành tinh — tính trước được hàng chục năm, sai số dưới một ngày.
Mốc rơi vào cổng nào thì câu hỏi của giai đoạn ấy nghiêng về lĩnh vực đó,
nên cùng một tuổi mà mỗi người một khác.</p>
{''.join(kh)}
{f'<p class="cgates">Đã qua: {qua}</p>' if qua else ''}</div></section>""")

    # ── Tháng này (tầng tháng) ─────────────────────────────────
    try:
        from datetime import datetime as _dt
        from zoneinfo import ZoneInfo as _Z
        _n = _dt.now(_Z("Asia/Ho_Chi_Minh"))
        bt = TT.bai_thang(chart, _n.year, _n.month, C["gates"])
    except Exception:
        bt = None
    if bt:
        cs = []
        for w in bt["cua_so"]:
            cs.append(f"""<details class="acc"><summary>
<span class="pl">{w['tu'].strftime('%d/%m')}–{w['den'].strftime('%d/%m')}</span>
{e(w['chu_de'])}</summary>
<div class="acc-body">
<p class="cgates">Mặt Trời cổng {e(w['mat_troi'])} — {e(w['ten_mt'])}
&nbsp;·&nbsp; Trái Đất cổng {e(w['trai_dat'])} — {e(w['ten_td'])}
&nbsp;·&nbsp; {w['so_ngay']} ngày</p>
<p><b>Riêng bạn.</b> {e(w['rieng_ban'])}</p>
<p class="nen">✔ <b>Nên:</b> {e(w['nen'])}</p>
<p class="tranh">✘ <b>Tránh:</b> {e(w['tranh'])}</p></div></details>""")
        out.append(f"""<section><div class="wrap"><p class="sec-no">Phần bảy — Tháng {bt['thang']}</p>
<h2>Bầu trời tháng này đi qua bản đồ của bạn</h2>
<p class="sub">Mặt Trời đổi cổng khoảng năm sáu ngày một lần, đặt ra chủ đề chung
cho mọi người. Trái Đất luôn ở cổng đối diện, giữ chân cho chủ đề ấy.
Phần “riêng bạn” cho biết cửa sổ đó có chạm vào bản đồ của chính bạn không.</p>
{''.join(cs)}
<div class="blk lam"><h3>Với {e(chart['type'])}</h3><p>{e(bt['loi_theo_type'])}</p></div>
</div></section>""")

    # Cổng của khách, nhóm theo Cá tính / Thiết kế
    def cong_list(acts, nhan):
        rows = []
        for k, v in acts.items():
            g = str(v["gate"])
            if g not in C["gates"]:
                continue
            gd, ic = C["gates"][g], C["gates"][g]["iching"]
            ns = (f'<span class="ns">Nỗi sợ: {e(gd["noi_so"])}</span>' if gd.get("noi_so") else "")
            rows.append(f"""<details class="acc"><summary>
<span class="pl">{e(BODY_VI[k])}</span> Cổng {g}.{v['line']} — {e(gd['name_vi'])}</summary>
<div class="acc-body"><p class="cgates">Quẻ {ic['que_so']}. {e(ic['ten_han_viet'])} — {e(ic['nghia_goc'])}
&nbsp;·&nbsp; {e(gd['kenh'])} {ns}</p>
<p class="sub">{e(gd['tagline'])}</p>
<p><b>Cơ học.</b> {e(gd['mechanics'])}</p>
<p><b>Khi vận hành thuận.</b> {e(gd['aligned'])}</p>
<p><b>Khi vận hành lệch.</b> {e(gd['misaligned'])}</p>
<p><b>Việc làm ngay.</b> {e(gd['practice'])}</p></div></details>""")
        return f'<h3 class="grp">{nhan}</h3>' + "".join(rows)

    out.append(f"""<section><div class="wrap"><p class="sec-no">Phần tám — Các cổng của bạn</p>
<h2>Hai mươi sáu điểm kích hoạt</h2>
<p class="sub">Phần Cá tính là những gì bạn ý thức được về mình.
Phần Thiết kế là phần vận hành ngầm — người ngoài thường thấy rõ hơn chính bạn.</p>
{cong_list(chart['ca_tinh'], 'Cá tính — ý thức')}
{cong_list(chart['thiet_ke'], 'Thiết kế — vô thức')}</div></section>""")
    return "".join(out)


def utc_label(chart: dict) -> str:
    """'8:00:00' → 'UTC+8', '-5:00:00' → 'UTC-5'. Không để rơi mất dấu."""
    raw = chart["dau_vao"]["utc_offset"]
    neg = raw.startswith("-")
    h, m, *_ = raw.lstrip("-").split(":")
    s = f"UTC{'-' if neg else '+'}{int(h)}"
    return s + (f":{m}" if m != "00" else "")


def render(chart: dict, ten: str, C: dict) -> str:
    t = C["types"][chart["type"]]
    a = C["authorities"][chart["authority"]]
    # Ẩn hẳn khối khi không có gì để nói. Trước đây luôn có một câu về NODE nên
    # khối lúc nào cũng hiện; bỏ câu đó rồi thì bản đồ bình thường sẽ ra một hộp
    # trống nếu vẫn dựng vô điều kiện.
    #
    # Tiêu đề là "Lưu ý về dữ liệu sinh của bạn", không phải "Ghi chú kỹ thuật
    # cho người luận": ba câu còn lại đều nói về dữ liệu khách khai — giờ chưa
    # chắc, chưa chọn miền, sinh trước 1955. Đó là chuyện của khách.
    khoi_canh_bao = ""
    if chart["canh_bao"]:
        muc = "".join(f"<li>{e(x)}</li>" for x in chart["canh_bao"])
        khoi_canh_bao = (f'<div class="canh"><h3>Lưu ý về dữ liệu sinh của bạn</h3>'
                         f'<ul>{muc}</ul></div>')
    css = (HERE / "template.html").read_text(encoding="utf-8")
    css = css.split("<style>")[1].split("</style>")[0]
    extra = BG.css_bang() + """
.acc{border-top:1px solid var(--vien)}
.acc summary{padding:14px 0;cursor:pointer;font-size:.98rem;list-style:none}
.acc summary::-webkit-details-marker{display:none}
.acc summary:hover{color:var(--son)}
.acc[open] summary{color:var(--son)}
.acc-body{padding:0 0 22px 0}
@media print{.acc[open] summary,.acc summary{color:var(--muc)}}
.acc-body p{margin-bottom:12px}
.dot{display:inline-block;width:8px;height:8px;border-radius:50%;margin-right:10px;
  border:1px solid var(--muc)}
.dot.defined{background:var(--son);border-color:var(--son)}
.pl{font-family:"JetBrains Mono",monospace;font-size:10px;letter-spacing:.1em;
  text-transform:uppercase;color:var(--muc-nhat);margin-right:10px}
.grp{font-family:"JetBrains Mono",monospace;font-size:11px;letter-spacing:.16em;
  text-transform:uppercase;color:var(--son);margin:32px 0 6px}
.ns{color:var(--son)}
.duoi-in{border-left:2px solid var(--muc-nhat);padding-left:16px}
.tangb{border:1px solid var(--son);padding:15px 17px;margin:16px 0}
.tangb h3{font-family:"JetBrains Mono",monospace;font-size:10px;letter-spacing:.14em;text-transform:uppercase;color:var(--son);margin-bottom:8px}
.tangb p{margin:0;font-size:.93rem}
.moc{border-left:3px solid var(--son);padding-left:22px;margin-bottom:38px}
.moc-nhan{font-family:"JetBrains Mono",monospace;font-size:10px;letter-spacing:.14em;text-transform:uppercase;color:var(--son);margin-bottom:6px}
.moc h3{font-family:"Bricolage Grotesque",sans-serif;font-size:1.3rem;margin-bottom:4px}
.nen{color:#3F6B3F}
.tranh{color:var(--son)}
.bgwrap{margin-bottom:40px}
.bgrow{display:flex;gap:26px;align-items:flex-start;justify-content:center;flex-wrap:wrap}
@media(max-width:640px){.bgrow{gap:16px}}
.bgwrap svg{max-width:100%;height:auto}
.bg-leg{display:flex;flex-wrap:wrap;gap:8px 20px;justify-content:center;margin-top:20px;
  font-size:.78rem;color:var(--muc-nhat)}
.bg-leg span{display:inline-flex;align-items:center;gap:7px}
.bg-leg i{width:16px;height:5px;display:inline-block;background:var(--muc)}
.bg-leg i.son{background:var(--son)}
.bg-leg i.half{background:linear-gradient(90deg,var(--muc) 50%,var(--son) 50%)}
.bg-leg i.op{width:11px;height:11px;background:var(--giay2);border:1.5px solid var(--vien)}
.bg-leg i.hang{width:16px;background:linear-gradient(90deg,var(--muc) 50%,transparent 50%)}
.canh{background:var(--lac);color:var(--giay2);padding:22px 26px;margin-bottom:34px}
.canh h3{font-family:"JetBrains Mono",monospace;font-size:10px;letter-spacing:.16em;
  text-transform:uppercase;color:var(--vang);margin-bottom:10px}
.canh ul{margin:0;padding-left:18px;font-size:.9rem;line-height:1.65}
"""
    return f"""<!DOCTYPE html><html lang="vi"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Bản đồ năng lượng — {e(ten)}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700&family=Be+Vietnam+Pro:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>{css}{extra}</style></head><body>
<header><div class="wrap">
<p class="eyebrow">Bản đồ năng lượng cá nhân</p>
<h1><span>{e(ten)}</span><span class="en">{e(t['name_vi'])} · {e(chart['profile'])}</span></h1>
<p class="tag">{e(t['tagline'])}</p>
<dl class="meta">
<div><dt>Sinh</dt><dd>{e(chart['dau_vao']['ngay_sinh'])}</dd></div>
<div><dt>Nơi sinh</dt><dd>{e(chart['dau_vao']['noi_sinh'])}</dd></div>
<div><dt>Múi giờ</dt><dd>{e(utc_label(chart))}</dd></div>
<div><dt>Nội quyền</dt><dd>{e(a['name_vi'].replace('Nội quyền ', ''))}</dd></div>
<div><dt>Definition</dt><dd>{e(chart['definition'])}</dd></div>
<div><dt>Cross</dt><dd>{'/'.join(map(str, chart['incarnation_cross']['cong']))} · {e(chart['incarnation_cross']['goc'])}</dd></div>
</dl></div></header>
<section><div class="wrap">
<div class="bgwrap"><div class="bgrow">{BG.render(chart, 460)}
{BG.bang_kich_hoat(chart)}</div>
<p class="bg-leg"><span><i class="ink"></i>Cá tính — ý thức</span>
<span><i class="son"></i>Thiết kế — vô thức</span>
<span><i class="half"></i>Cả hai</span>
<span><i class="op"></i>Trung tâm mở</span>
<span><i class="hang"></i>Cổng treo — thiếu cổng kia mới thành kênh</span></p></div>
{khoi_canh_bao}
<p class="sec-no">Cơ học — dữ kiện thô</p>
<dl class="facts">
<div><dt>Kênh định nghĩa</dt><dd>{e(', '.join(chart['kenh']) or 'không có')}</dd></div>
<div><dt>Trung tâm định nghĩa</dt><dd>{e(', '.join(CENTER_VI[x] for x in chart['trung_tam_dinh_nghia']) or 'không có')}</dd></div>
<div><dt>Thời điểm Thiết kế (UTC)</dt><dd>{e(chart['thoi_diem']['thiet_ke_utc'])} — lùi {chart['thoi_diem']['so_ngay_lui']} ngày</dd></div>
</dl>
<dl class="facts">{''.join(f"<div><dt>{e(v['nghia'])}</dt><dd>Mũi tên {e(v['huong'])} · tông {v['tone']}</dd></div>" for v in chart['variables'].values())}</dl>
</div></section>
{blocks(chart, C)}
<footer><div class="wrap"><p class="disc"><strong>Xin đọc kỹ</strong>{e(C['disclaimer'])}</p>
<p class="disc" style="margin-top:10px">{PL.chan_trang(GOC)}</p>
<p class="brand">B-RICH MIND</p></div></footer></body></html>"""


def main():
    ap = argparse.ArgumentParser(description="Dựng bản đồ Human Design cho một người")
    ap.add_argument("ngay", help="YYYY-MM-DD")
    ap.add_argument("gio", help="HH:MM")
    ap.add_argument("--ten", default="Khách")
    ap.add_argument("--noi", default="TP. Hồ Chí Minh")
    ap.add_argument("--tz", default="Asia/Ho_Chi_Minh")
    ap.add_argument("--lat", type=float), ap.add_argument("--lon", type=float)
    ap.add_argument("--gio-khong-chac", action="store_true")
    ap.add_argument("--mien", choices=["bac", "nam"],
                    help="miền sinh — BẮT BUỘC nếu sinh tại VN trước 14/6/1975")
    ap.add_argument("--json", action="store_true", help="chỉ in JSON cơ học")
    ap.add_argument("--noi-bo", action="store_true",
                    help="dùng kho đầy đủ có Tầng B (phần cơ thể theo hệ thống gốc)")
    args = ap.parse_args()

    y, mo, d = map(int, args.ngay.split("-"))
    h, mi = map(int, args.gio.split(":"))
    lat, lon = NOI_SINH.get(args.noi.strip().lower(), (10.8231, 106.6297))
    if args.lat is not None:
        lat, lon = args.lat, args.lon

    chart = E.build_chart(y, mo, d, h, mi, tz=args.tz, lat=lat, lon=lon,
                          noi_sinh=args.noi, gio_chac_chan=not args.gio_khong_chac,
                          mien=args.mien)

    if args.json:
        print(json.dumps(chart, ensure_ascii=False, indent=2, default=str))
        return

    ten_kho = "hd-content-v1.json" if args.noi_bo else "hd-content-public.json"
    C = json.loads((HERE / ten_kho).read_text(encoding="utf-8"))
    out = Path(f"ket-qua-{slug(args.ten)}.html")
    out.write_text(render(chart, args.ten, C), encoding="utf-8")

    print(f"✅ {out}  [{'NỘI BỘ' if args.noi_bo else 'public'}]")
    print(f"   {C['types'][chart['type']]['name_vi']} · "
          f"{C['authorities'][chart['authority']]['name_vi']} · Profile {chart['profile']}")
    print(f"   {chart['definition']} · kênh: {', '.join(chart['kenh']) or 'không có'}")
    for c in chart["canh_bao"]:
        print(f"   ⚠ {c}")


if __name__ == "__main__":
    main()
