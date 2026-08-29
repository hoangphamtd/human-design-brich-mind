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
"""app.py — Web app Human Design cho B-RICH MIND.

Chạy tại máy:   uvicorn app:app --reload --port 8000
Rồi mở:         http://localhost:8000

Đường dẫn:
    GET  /            trang nhập liệu
    POST /chart       trả trang kết quả đầy đủ
    POST /api/chart   trả JSON cơ học (cho app khác gọi)
    GET  /khoe        kiểm tra sống
"""
from __future__ import annotations
import json
import os
import re
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo, available_timezones

from fastapi import FastAPI, Form, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse

import hd_engine as E
import noi_dung_phap_ly as PL
from render_chart import render, NOI_SINH

HERE = Path(__file__).parent

# BAN=noibo  → kho đầy đủ, gồm phần cơ thể theo hệ thống gốc (Tầng B §7.3)
# BAN=public → đã gỡ Tầng B. MẶC ĐỊNH, vì đây là bản người ngoài thấy.
BAN = os.getenv("BAN", "public")

# App nằm dưới brichmind.com/human-design nên MỌI đường dẫn phải có tiền tố này.
# Để rỗng khi chạy tại máy hoặc chạy ở gốc tên miền.
GOC = os.getenv("GOC", "").rstrip("/")


def d(duong: str) -> str:
    """Ghép tiền tố vào một đường dẫn nội bộ."""
    return f"{GOC}{duong}"
_F = {"noibo": "hd-content-v1.json", "public": "hd-content-public.json"}
if BAN not in _F:
    raise SystemExit(f"BAN phải là 'noibo' hoặc 'public', không phải '{BAN}'")
_duong = HERE / _F[BAN]
if not _duong.exists():
    raise SystemExit(f"Thiếu file {_F[BAN]} — chạy build_content.py trước.")
CONTENT = json.loads(_duong.read_text(encoding="utf-8"))
CSS = (HERE / "template.html").read_text(encoding="utf-8").split("<style>")[1].split("</style>")[0]

app = FastAPI(title="Human Design — B-RICH MIND", docs_url=None, redoc_url=None,
              root_path=GOC)

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?'
         'family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700&'
         'family=Be+Vietnam+Pro:wght@300;400;500;600&'
         'family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">')

FORM_CSS = """
body{display:flex;flex-direction:column;min-height:100vh}
.hero{background:var(--lac);color:var(--giay2);padding:56px 0 44px;flex:0 0 auto}
main{flex:1 0 auto;padding:44px 0 64px}
form{max-width:560px}
.row{display:flex;gap:16px;flex-wrap:wrap;margin-bottom:22px}
.f{flex:1 1 200px}
label{display:block;font-family:"JetBrains Mono",monospace;font-size:10px;
  letter-spacing:.15em;text-transform:uppercase;color:var(--muc-nhat);margin-bottom:7px}
input,select{width:100%;padding:12px 13px;border:1px solid var(--vien);
  background:var(--giay2);color:var(--muc);border-radius:2px;
  font-family:"Be Vietnam Pro",sans-serif;font-size:1rem}
input:focus,select:focus{outline:2px solid var(--son);outline-offset:1px;border-color:var(--son)}
.chk{display:flex;gap:11px;align-items:flex-start;margin-bottom:8px}
.chk input{width:auto;margin-top:4px;accent-color:var(--son)}
.chk label{font-family:"Be Vietnam Pro",sans-serif;font-size:.95rem;letter-spacing:0;
  text-transform:none;color:var(--muc);margin:0;cursor:pointer}
.hint{font-size:.82rem;color:var(--muc-nhat);margin-top:5px;line-height:1.55}
button{background:var(--lac);color:var(--giay2);border:0;padding:15px 34px;
  font-family:"Bricolage Grotesque",sans-serif;font-weight:700;font-size:1.02rem;
  letter-spacing:-.01em;cursor:pointer;border-radius:2px;margin-top:8px}
button:hover{background:var(--son)}
button:focus-visible{outline:2px solid var(--son);outline-offset:3px}
.adv{border-top:1px solid var(--vien);margin-top:30px;padding-top:24px}
.adv summary{cursor:pointer;font-family:"JetBrains Mono",monospace;font-size:10px;
  letter-spacing:.15em;text-transform:uppercase;color:var(--muc-nhat)}
.adv summary:hover{color:var(--son)}
.adv[open] summary{margin-bottom:20px;color:var(--son)}
.err{background:var(--son);color:#fff;padding:15px 19px;margin-bottom:26px;
  border-radius:2px;font-size:.95rem}
.topbar{background:var(--lac2);padding:13px 0}
.topbar a{color:var(--vang);text-decoration:none;font-family:"JetBrains Mono",monospace;
  font-size:11px;letter-spacing:.14em;text-transform:uppercase}
.topbar a:hover{text-decoration:underline}
@media print{.topbar{display:none}}
"""


def page(body: str, title: str) -> str:
    return (f'<!DOCTYPE html><html lang="vi"><head><meta charset="utf-8">'
            f'<meta name="viewport" content="width=device-width, initial-scale=1">'
            f'<title>{title}</title>{FONTS}<style>{CSS}{FORM_CSS}</style></head>'
            f'<body>{body}</body></html>')


def form_html(err: str = "", **v) -> str:
    tinh = "".join(
        f'<option value="{k}"{" selected" if v.get("noi","").lower()==k else ""}>'
        f'{k.title()}</option>' for k in NOI_SINH)
    e = lambda k, d="": v.get(k, d)
    return page(f"""
<div class="hero"><div class="wrap">
<p class="eyebrow">B-RICH MIND</p>
<h1 style="font-size:clamp(2.1rem,6vw,3.4rem)">Bản đồ năng lượng</h1>
<p class="tag">Nhập ngày, giờ và nơi sinh. Hệ thống dựng bản đồ Human Design
đầy đủ: loại năng lượng, cách ra quyết định, chín trung tâm, kênh và cổng.</p>
</div></div>
<main><div class="wrap">
{f'<p class="err">{err}</p>' if err else ''}
<form method="post" action="{d("/chart")}">
  <div class="row"><div class="f">
    <label for="ten">Tên</label>
    <input id="ten" name="ten" value="{e('ten')}" placeholder="Tên của bạn" required>
  </div></div>

  <div class="row">
    <div class="f"><label for="ngay">Ngày sinh</label>
      <input id="ngay" name="ngay" type="date" value="{e('ngay')}" required></div>
    <div class="f"><label for="gio">Giờ sinh</label>
      <input id="gio" name="gio" type="time" value="{e('gio')}" required></div>
  </div>

  <div class="row"><div class="f">
    <label for="noi">Nơi sinh</label>
    <select id="noi" name="noi">{tinh}</select>
    <p class="hint">Nơi khác thì mở phần Tuỳ chọn nâng cao bên dưới để nhập toạ độ.</p>
  </div></div>

  <div class="row" id="omien" style="display:none"><div class="f">
    <label for="mien">Anh/chị sinh ở miền nào?</label>
    <select id="mien" name="mien">
      <option value="">— chọn miền —</option>
      <option value="nam">Miền Nam (từ Đà Nẵng trở vào)</option>
      <option value="bac">Miền Bắc (từ Huế trở ra)</option>
    </select>
    <p class="hint"><b>Bắt buộc với người sinh trước 14/6/1975.</b>
    Khi đó hai miền dùng hai múi giờ lệch nhau một giờ — chọn sai là lệch Profile.</p>
  </div></div>

  <div class="chk">
    <input id="kc" name="gio_khong_chac" type="checkbox" value="1">
    <label for="kc"><b>Khách không nhớ chính xác giờ sinh</b><br>
      <span class="hint">Lệch một giờ có thể đổi Profile và Authority.
      Đánh dấu ô này để trang kết quả in cảnh báo, và nên dựng thêm vài mốc giờ để so.</span>
    </label>
  </div>

  <details class="adv"><summary>Tuỳ chọn nâng cao</summary>
    <div class="row">
      <div class="f"><label for="lat">Vĩ độ</label>
        <input id="lat" name="lat" placeholder="10.8231"></div>
      <div class="f"><label for="lon">Kinh độ</label>
        <input id="lon" name="lon" placeholder="106.6297"></div>
    </div>
    <div class="row"><div class="f">
      <label for="tz">Múi giờ</label>
      <input id="tz" name="tz" value="Asia/Ho_Chi_Minh">
      <p class="hint">Sinh ngoài Việt Nam thì đổi, ví dụ <b>Australia/Melbourne</b>.
      Miền Nam Việt Nam trước 13/6/1975 dùng UTC+8 — hệ thống tự xử lý.</p>
    </div></div>
  </details>

  <button type="submit">Dựng bản đồ</button>
</form>
<script>
// Ô chọn miền chỉ có nghĩa với người sinh trước 14/6/1975.
(function () {{
  var ngay = document.getElementById("ngay"),
      om = document.getElementById("omien"),
      ms = document.getElementById("mien");
  function xet() {{
    var can = ngay.value && ngay.value < "1975-06-14";
    om.style.display = can ? "" : "none";
    ms.required = !!can;
    if (!can) ms.value = "";
  }}
  ngay.addEventListener("change", xet);
  ngay.addEventListener("input", xet);
  xet();
}})();
</script>
</div></main>
<footer><div class="wrap"><p class="disc"><strong>Xin đọc kỹ</strong>{CONTENT['disclaimer']}</p>
<p class="disc" style="margin-top:10px">{PL.chan_trang(GOC)}</p>
<p style="margin-top:14px;font-size:.85rem">
<a href="{d('/ve-human-design')}" style="color:var(--muc-nhat)">Về Human Design</a>
&nbsp;·&nbsp;
<a href="{d('/rieng-tu')}" style="color:var(--muc-nhat)">Chính sách riêng tư</a>
&nbsp;·&nbsp;
<a href="{d('/ma-nguon')}" style="color:var(--muc-nhat)">Mã nguồn</a></p>
<p class="brand">B-RICH MIND</p></div></footer>""", "Bản đồ năng lượng — B-RICH MIND")


@app.get("/", response_class=HTMLResponse)
def trang_chu():
    return form_html()


def _md(txt: str) -> str:
    """Markdown đơn giản sang HTML. Gộp các dòng liền nhau thành một đoạn —
    xuống dòng trong nguồn chỉ để dễ đọc, không phải để ngắt đoạn."""
    html_out, doan = [], []

    def xa():
        if doan:
            t = " ".join(doan)
            t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
            if t.startswith("*") and t.endswith("*"):
                html_out.append(f'<p class="sub">{t[1:-1]}</p>')
            else:
                html_out.append(f"<p>{t}</p>")
            doan.clear()

    for dong in txt.split("\n"):
        t = dong.strip()
        if not t:
            xa()
        elif t.startswith("#"):
            xa()
            n = len(t) - len(t.lstrip("#"))
            noi = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t[n:].strip())
            html_out.append(f"<h{n}>{noi}</h{n}>")
        else:
            doan.append(t)
    xa()
    return "".join(html_out)


def _trang_van(md: str, tieu_de: str) -> str:
    return page(f'''<div class="topbar" style="background:#231A15;padding:13px 0">
<div class="wrap"><a href="{d("/")}" style="color:#C9A227;text-decoration:none;
font-family:JetBrains Mono,monospace;font-size:11px;letter-spacing:.14em;
text-transform:uppercase">← Về trang dựng bản đồ</a></div></div>
<main><div class="wrap" style="max-width:680px">{_md(md)}</div></main>
<footer><div class="wrap"><p class="disc">{PL.chan_trang(GOC)}</p>
<p class="brand">B-RICH MIND</p></div></footer>''', tieu_de)


@app.get("/rieng-tu", response_class=HTMLResponse)
def trang_rieng_tu():
    return _trang_van(PL.rieng_tu(), "Chính sách riêng tư — B-RICH MIND")


@app.get("/ve-human-design", response_class=HTMLResponse)
def trang_gioi_thieu():
    return _trang_van(PL.ve_he_thong(GOC), "Về Human Design — B-RICH MIND")


@app.get("/ma-nguon", response_class=HTMLResponse)
def trang_ma_nguon():
    """AGPL §13 — phải cung cấp mã nguồn cho chính người dùng qua mạng,
    không chỉ để mã ở đâu đó trên Internet."""
    return _trang_van(PL.ma_nguon(), "Mã nguồn — B-RICH MIND")


@app.get("/khoe")
def khoe():
    return {"ok": True, "ban": BAN, "goc": GOC or "/",
            "thieu_thong_tin_cong_ty": PL.con_thieu(), "khoi": sum(len(CONTENT[k]) for k in
            ("types", "authorities", "profiles", "centers", "gates", "channels"))}


def _dep_ten_noi(noi: str) -> str:
    noi = (noi or "").strip()
    if not noi:
        return "TP. Hồ Chí Minh"
    return " ".join(w.upper() if "." in w else
                    (w if w.isupper() else w.capitalize()) for w in noi.split())


def _dung_chart(ten, ngay, gio, noi, tz, lat, lon, kc, mien="") -> dict:
    try:
        y, mo, d = map(int, ngay.split("-"))
        h, mi = map(int, gio.split(":")[:2])
    except ValueError:
        raise HTTPException(400, "Ngày hoặc giờ không đúng định dạng.")
    if tz not in available_timezones():
        raise HTTPException(400, f"Không nhận ra múi giờ '{tz}'.")
    try:
        datetime(y, mo, d, h, mi, tzinfo=ZoneInfo(tz))
    except ValueError as ex:
        raise HTTPException(400, f"Ngày giờ không hợp lệ: {ex}")

    la, lo = NOI_SINH.get((noi or "").strip().lower(), (10.8231, 106.6297))
    if lat and lon:
        try:
            la, lo = float(lat), float(lon)
        except ValueError:
            raise HTTPException(400, "Toạ độ phải là số.")
        if not (-90 <= la <= 90 and -180 <= lo <= 180):
            raise HTTPException(400, "Toạ độ ngoài phạm vi cho phép.")

    if mien and mien not in ("bac", "nam"):
        raise HTTPException(400, "Miền sinh không hợp lệ.")
    if not mien and tz in (E.TZ_NAM, E.TZ_BAC) and (y, mo, d) < E.MOC_THONG_NHAT:
        raise HTTPException(400, "Sinh trước 14/6/1975 tại Việt Nam thì phải chọn miền — "
                                 "khi đó hai miền lệch nhau một giờ, chọn sai là lệch Profile.")
    return E.build_chart(y, mo, d, h, mi, tz=tz, lat=la, lon=lo,
                         noi_sinh=_dep_ten_noi(noi), gio_chac_chan=not kc,
                         mien=mien or None)


@app.post("/chart", response_class=HTMLResponse)
def dung_chart(ten: str = Form(...), ngay: str = Form(...), gio: str = Form(...),
               noi: str = Form("TP. Hồ Chí Minh"), tz: str = Form("Asia/Ho_Chi_Minh"),
               lat: str = Form(""), lon: str = Form(""),
               gio_khong_chac: str = Form(""), mien: str = Form("")):
    try:
        chart = _dung_chart(ten, ngay, gio, noi, tz, lat, lon, bool(gio_khong_chac), mien)
    except HTTPException as ex:
        return HTMLResponse(form_html(err=ex.detail, ten=ten, ngay=ngay, gio=gio, noi=noi, mien=mien),
                            status_code=400)

    html = render(chart, ten.strip() or "Khách", CONTENT)
    thanh = (
        ('<div style="background:#A8342A;color:#fff;padding:8px 0;text-align:center;'
         'font-family:JetBrains Mono,monospace;font-size:10px;letter-spacing:.14em">'
         'BẢN NỘI BỘ — CHỨA NỘI DUNG TẦNG B, KHÔNG CHIA SẺ RA NGOÀI</div>'
         if BAN == "noibo" else '') +
        '<div style="background:#231A15;padding:13px 0" class="topbar">'
        '<div class="wrap" style="display:flex;justify-content:space-between;'
        'align-items:center;gap:16px">'
        f'<a href="{d("/")}" style="color:#C9A227;text-decoration:none;'
        'font-family:JetBrains Mono,monospace;font-size:11px;letter-spacing:.14em;'
        'text-transform:uppercase">← Dựng bản đồ khác</a>'
        '<button onclick="window.print()" style="background:none;border:1px solid #4a3a30;'
        'color:#D6DBDC;padding:7px 15px;font-family:JetBrains Mono,monospace;font-size:10px;'
        'letter-spacing:.14em;text-transform:uppercase;cursor:pointer;border-radius:2px">'
        'In / Lưu PDF</button></div></div>'
        '<style>@media print{.topbar{display:none}'
        '.acc>summary{display:none}.acc-body{padding-bottom:14px}'
        'details{display:block}}</style>')
    return HTMLResponse(html.replace("<body>", f"<body>{thanh}", 1))


@app.post("/api/chart")
def api_chart(ngay: str = Form(...), gio: str = Form(...),
              noi: str = Form("TP. Hồ Chí Minh"), tz: str = Form("Asia/Ho_Chi_Minh"),
              lat: str = Form(""), lon: str = Form(""),
              gio_khong_chac: str = Form(""), mien: str = Form("")):
    chart = _dung_chart("", ngay, gio, noi, tz, lat, lon, bool(gio_khong_chac), mien)
    return JSONResponse(json.loads(json.dumps(chart, default=str)))
