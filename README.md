# Human Design B-RICH MIND

Phần mềm dựng bản đồ Human Design bằng tiếng Việt.

Nhập ngày, giờ và nơi sinh, phần mềm tính ra bản đồ và diễn giải: loại năng
lượng, cách ra quyết định, vai trong đời, chín trung tâm, các kênh, các cổng,
cùng hai tầng thời gian — mốc chuyển đời và cửa sổ tháng.

Bản đang chạy: <https://brichmind.com/human-design/>

---

## Phần mềm này gồm những gì

| Phần | File |
|---|---|
| Bộ tính bản đồ | `hd_engine.py` |
| Vẽ BodyGraph dạng SVG | `bodygraph.py` |
| Dựng trang kết quả | `render_chart.py` · `template.html` |
| Web app | `app.py` |
| Kho nội dung tiếng Việt | `content_*.py` → `build_content.py` → `hd-content-public.json` |
| Tầng năm — mốc chuyển đời | `moc_doi.py` · `content_moc_doi.py` · `luan_moc_doi.py` |
| Tầng tháng — cửa sổ Mặt Trời | `transit_thang.py` · `content_transit.py` · `luan_transit_thang.py` |
| Bộ lọc ngôn ngữ | `loc_nd38.py` |
| Kiểm định | `test_engine.py` · `test_loc_tien_doan.py` · `bo_50_chart.py` |

Kho nội dung tiếng Việt là bài viết gốc, không dịch máy: 142 khối, khoảng
28.000 từ.

---

## Chạy thử

Cần **Python 3.11**. `pyswisseph` chỉ có bản dựng sẵn tới cp311.

```bash
python -m venv .venv
.venv/bin/pip install -r requirements.txt

# dựng một bản đồ ra file HTML
.venv/bin/python render_chart.py 1985-03-15 07:30 --ten "TK-06" --noi "Cần Thơ"

# chạy web app
BAN=public .venv/bin/uvicorn app:app --host 127.0.0.1 --port 8010
```

Sinh lại kho nội dung sau khi sửa `content_*.py`:

```bash
python build_content.py          # sinh hd-content-public.json
python -m unittest test_engine   # 45 bài
python loc_nd38.py               # rà bộ lọc ngôn ngữ
```

---

## Kiểm định

`test_engine.py` — 45 bài, gồm một bài neo SVG BodyGraph vào md5 để hình
không đổi mà không ai biết.

`bo_50_chart.py` — 50 ca dựng có chủ đích: quanh mốc múi giờ Việt Nam, sát
nửa đêm, năm nhuận, nước ngoài có giờ mùa hè, sát biên hào. Kết quả đã đối
chiếu với hai nguồn ngoài (`ket-qua-humdes.md`, `ket-qua-jovianarchive.md`).

`test_loc_tien_doan.py` — 7 bài kiểm bộ lọc ngôn ngữ, gồm cả các bài tự kiểm
chính phép kiểm: nhét câu hỏng vào xem bộ lọc có bắt được không.

Các ca kiểm định dùng **nhãn** (`TK-06`, `CA-01`…), không dùng tên người —
ngày giờ nơi sinh của một người có thật là dữ liệu cá nhân.

---

## Giấy phép

Phần mềm này là phần mềm tự do: bạn được phát hành lại và sửa đổi theo
**GNU Affero General Public License phiên bản 3**, hoặc (tuỳ bạn chọn) bất
kỳ phiên bản nào sau đó, do Free Software Foundation công bố.

Phần mềm được phát hành với mong muốn nó hữu ích, nhưng **KHÔNG KÈM BẤT KỲ
BẢO ĐẢM NÀO** — kể cả bảo đảm ngầm định về khả năng bán được hay phù hợp cho
một mục đích cụ thể. Đọc GNU Affero General Public License để biết chi tiết.

Nguyên văn giấy phép ở file [`LICENSE`](LICENSE), hoặc
<https://www.gnu.org/licenses/>.

AGPL có điều khoản mạng: nếu bạn sửa phần mềm này rồi cho người khác dùng qua
mạng, bạn phải cung cấp mã nguồn đã sửa cho chính những người dùng đó.

---

## Ghi nhận bản quyền

Phần mềm này dùng thư viện **Swiss Ephemeris**, bản quyền © 1997–2021
Astrodienst AG, Thuỵ Sĩ, theo nhánh AGPL của giấy phép kép của thư viện.

Swiss Ephemeris Inside.

---

## Xin đọc kỹ

Human Design là hệ thống chiêm nghiệm mang tính biểu tượng, không phải khoa
học y học hay tâm lý học lâm sàng. Nội dung do phần mềm sinh ra nhằm mục đích
tham khảo và khám phá bản thân, **không phải chẩn đoán, điều trị, hay lời
khuyên y tế, tài chính, pháp lý**. Bạn là người quyết định cuối cùng cho cuộc
đời mình.

---

Copyright © 2026 B-RICH MIND
