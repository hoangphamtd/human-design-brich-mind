# HD-05 — Hướng dẫn dùng Chart Engine

## Cài một lần
```bash
pip install pyswisseph tzdata --break-system-packages
```

## Dựng bản đồ cho một khách
```bash
python3 render_chart.py 1985-03-15 07:30 --ten "TK-06" --noi "Cần Thơ"
```
→ ra file `ket-qua-tk-06.html`, mở bằng trình duyệt.

**Tham số:**

| Cờ | Ý nghĩa |
|---|---|
| `--ten` | Tên hiện trên đầu trang |
| `--noi` | Nơi sinh. Có sẵn 10 tỉnh thành lớn |
| `--lat --lon` | Toạ độ, dùng khi nơi sinh không có trong danh sách |
| `--tz` | Múi giờ, mặc định `Asia/Ho_Chi_Minh` |
| `--gio-khong-chac` | **Bật khi khách không nhớ chính xác giờ sinh** |
| `--json` | Chỉ in dữ liệu cơ học, không dựng trang |

## Khi khách không nhớ giờ sinh
Luôn bật `--gio-khong-chac`, và dựng vài bản theo khoảng giờ để so:
```bash
for h in 06 09 12 15 18 21; do
  python3 render_chart.py 1985-03-15 $h:00 --ten "Lan $h" --gio-khong-chac
done
```
Nếu Profile và Authority giống nhau ở mọi mốc thì luận được. Nếu khác nhau thì **chưa luận**,
phải hỏi lại khách trước.

## Ba điều engine tự cảnh báo
1. Giờ sinh chưa chắc chắn.
2. Sinh trước 13/6/1975 — giai đoạn miền Nam dùng UTC+8. Engine áp đúng, nhưng nên
   xác nhận lại nơi sinh, vì miền Bắc cùng thời kỳ dùng múi giờ khác.
3. Nút Bắc đang dùng True Node — điểm còn treo, chưa đối chiếu nguồn ngoài.

## Chạy kiểm định
```bash
python3 -m unittest test_engine -v
```
27 test, gồm: neo bánh xe, biên hào, 88° cung mặt trời, mốc múi giờ 1975,
liên thông đồ thị motor–Cổ họng, thứ tự ưu tiên Authority, đếm cụm Definition.

## ⚠ Việc còn treo trước khi ra mắt công khai
- [ ] Đối chiếu 50 chart chuẩn với Jovian Archive · Genetic Matrix · HumDes. **Tiêu chí: 0 lệch.**
- [ ] Chốt True Node hay Mean Node.
- [ ] 36 kênh — chưa có nội dung diễn giải.
- [ ] Vẽ BodyGraph dạng hình.
- [ ] Chạy toàn bộ nội dung qua bộ lọc NĐ38 trước khi public.
