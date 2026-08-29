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
"""bo_50_chart.py — Dựng bộ 50 chart chuẩn để đối chiếu với nguồn ngoài.

Chạy:
    python bo_50_chart.py            → xuất bảng đối chiếu + bảng so True/Mean Node
    python bo_50_chart.py --csv      → xuất thêm file CSV để điền tay

Bộ 50 ca được chọn có chủ đích, không lấy ngẫu nhiên:
  · trước và sau mốc múi giờ 13/6/1975, cả hai miền
  · sát nửa đêm (00:01 và 23:59) — dễ lệch ngày
  · năm nhuận, ngày 29/2
  · sinh nước ngoài có giờ mùa hè
  · nam bán cầu
  · sát biên hào — chỗ dễ lệch nhất
"""
from __future__ import annotations
import argparse, csv, sys
import hd_engine as E

# (nhãn, năm, tháng, ngày, giờ, phút, múi giờ, miền, ghi chú)
BO_50 = [
    # ── Mốc múi giờ Việt Nam (12 ca) ───────────────────────────────
    ("VN-01", 1965, 4, 20, 7, 15, "Asia/Ho_Chi_Minh", "bac", "miền Bắc, giai đoạn hai múi giờ"),
    ("VN-02", 1965, 4, 20, 7, 15, "Asia/Ho_Chi_Minh", "nam", "miền Nam, cùng giờ đồng hồ"),
    ("VN-03", 1970, 8, 8, 3, 30, "Asia/Ho_Chi_Minh", "bac", "miền Bắc"),
    ("VN-04", 1970, 8, 8, 3, 30, "Asia/Ho_Chi_Minh", "nam", "miền Nam"),
    ("VN-05", 1975, 6, 12, 23, 59, "Asia/Ho_Chi_Minh", "nam", "áp chót mốc đổi giờ"),
    ("VN-06", 1975, 6, 13, 0, 1, "Asia/Ho_Chi_Minh", "nam", "ngay mốc đổi giờ"),
    ("VN-07", 1975, 6, 14, 0, 1, "Asia/Ho_Chi_Minh", "nam", "sau mốc, đã thống nhất"),
    ("VN-08", 1960, 1, 1, 12, 0, "Asia/Ho_Chi_Minh", "nam", "ngày miền Nam đổi sang UTC+8"),
    ("VN-09", 1959, 12, 31, 12, 0, "Asia/Ho_Chi_Minh", "nam", "hôm trước khi đổi"),
    ("VN-10", 1957, 3, 3, 6, 0, "Asia/Ho_Chi_Minh", "bac", "giai đoạn hai miền cùng UTC+7"),
    ("VN-11", 1950, 5, 5, 12, 0, "Asia/Ho_Chi_Minh", "bac", "trước 1955, nguồn chưa thống nhất"),
    ("VN-12", 1980, 10, 10, 10, 10, "Asia/Ho_Chi_Minh", None, "sau thống nhất, không cần miền"),

    # ── Sát nửa đêm (6 ca) ─────────────────────────────────────────
    ("NĐ-01", 1988, 7, 15, 0, 1, "Asia/Ho_Chi_Minh", None, "đầu ngày"),
    ("NĐ-02", 1988, 7, 15, 23, 59, "Asia/Ho_Chi_Minh", None, "cuối ngày"),
    ("NĐ-03", 1993, 11, 30, 0, 0, "Asia/Ho_Chi_Minh", None, "đúng 0 giờ"),
    ("NĐ-04", 1993, 12, 1, 0, 0, "Asia/Ho_Chi_Minh", None, "0 giờ hôm sau"),
    ("NĐ-05", 2000, 12, 31, 23, 59, "Asia/Ho_Chi_Minh", None, "giao thừa thiên niên kỷ"),
    ("NĐ-06", 2001, 1, 1, 0, 1, "Asia/Ho_Chi_Minh", None, "đầu thiên niên kỷ"),

    # ── Năm nhuận (4 ca) ───────────────────────────────────────────
    ("NH-01", 1960, 2, 29, 12, 0, "Asia/Ho_Chi_Minh", "nam", "29/2 năm nhuận"),
    ("NH-02", 2000, 2, 29, 6, 30, "Asia/Ho_Chi_Minh", None, "năm 2000 nhuận"),
    ("NH-03", 2024, 2, 29, 18, 45, "Asia/Ho_Chi_Minh", None, "29/2 gần đây"),
    ("NH-04", 1996, 3, 1, 0, 5, "Asia/Ho_Chi_Minh", None, "ngay sau 29/2"),

    # ── Nước ngoài, có giờ mùa hè (10 ca) ──────────────────────────
    ("NN-01", 1975, 7, 4, 14, 30, "America/New_York", None, "Mỹ, đang giờ mùa hè"),
    ("NN-02", 1975, 1, 4, 14, 30, "America/New_York", None, "Mỹ, giờ chuẩn"),
    ("NN-03", 1982, 6, 21, 9, 0, "Europe/London", None, "Anh, giờ mùa hè"),
    ("NN-04", 1982, 12, 21, 9, 0, "Europe/London", None, "Anh, giờ chuẩn"),
    ("NN-05", 1990, 3, 25, 2, 30, "Europe/Paris", None, "Pháp, sát lúc nhảy giờ"),
    ("NN-06", 1995, 9, 9, 16, 20, "Australia/Melbourne", None, "Úc, nam bán cầu"),
    ("NN-07", 1995, 1, 9, 16, 20, "Australia/Melbourne", None, "Úc, giờ mùa hè nam bán cầu"),
    ("NN-08", 1987, 5, 12, 11, 11, "Asia/Tokyo", None, "Nhật"),
    ("NN-09", 2005, 8, 30, 20, 40, "America/Los_Angeles", None, "bờ Tây Mỹ"),
    ("NN-10", 1978, 11, 2, 5, 15, "Asia/Kolkata", None, "Ấn Độ, lệch nửa giờ"),

    # ── Rải đều thế kỷ (10 ca) ─────────────────────────────────────
    ("TK-01", 1940, 1, 20, 8, 0, "Asia/Ho_Chi_Minh", "bac", ""),
    ("TK-02", 1948, 6, 6, 15, 45, "Asia/Ho_Chi_Minh", "nam", ""),
    ("TK-03", 1955, 9, 18, 21, 30, "Asia/Ho_Chi_Minh", "bac", ""),
    ("TK-04", 1968, 12, 25, 4, 20, "Asia/Ho_Chi_Minh", "nam", ""),
    ("TK-05", 1977, 2, 14, 13, 5, "Asia/Ho_Chi_Minh", None, ""),
    ("TK-06", 1985, 3, 15, 7, 30, "Asia/Ho_Chi_Minh", None, "ca dùng trong caidat.sh"),
    ("TK-07", 1992, 11, 8, 3, 15, "Asia/Ho_Chi_Minh", None, ""),
    ("TK-08", 1999, 4, 1, 17, 50, "Asia/Ho_Chi_Minh", None, ""),
    ("TK-09", 2010, 10, 10, 10, 10, "Asia/Ho_Chi_Minh", None, ""),
    ("TK-10", 2020, 6, 30, 22, 22, "Asia/Ho_Chi_Minh", None, ""),

    # ── Sát biên hào — chỗ dễ lệch nhất (8 ca) ─────────────────────
    ("BH-01", 1990, 1, 1, 11, 58, "Asia/Ho_Chi_Minh", None, "quét biên hào"),
    ("BH-02", 1990, 1, 1, 12, 0, "Asia/Ho_Chi_Minh", None, "cách trên 2 phút"),
    ("BH-03", 1990, 1, 1, 12, 2, "Asia/Ho_Chi_Minh", None, "cách trên 4 phút"),
    ("BH-04", 1990, 1, 1, 12, 4, "Asia/Ho_Chi_Minh", None, "cách trên 6 phút"),
    ("BH-05", 1972, 8, 17, 5, 58, "Asia/Ho_Chi_Minh", "nam", "quét biên hào, có miền"),
    ("BH-06", 1972, 8, 17, 6, 0, "Asia/Ho_Chi_Minh", "nam", ""),
    ("BH-07", 1972, 8, 17, 6, 2, "Asia/Ho_Chi_Minh", "nam", ""),
    ("BH-08", 1972, 8, 17, 6, 4, "Asia/Ho_Chi_Minh", "nam", ""),
]

TOA_DO = {
    "Asia/Ho_Chi_Minh": (10.8231, 106.6297, "TP. Hồ Chí Minh"),
    "America/New_York": (40.7128, -74.0060, "New York"),
    "Europe/London": (51.5074, -0.1278, "London"),
    "Europe/Paris": (48.8566, 2.3522, "Paris"),
    "Australia/Melbourne": (-37.8136, 144.9631, "Melbourne"),
    "Asia/Tokyo": (35.6762, 139.6503, "Tokyo"),
    "America/Los_Angeles": (34.0522, -118.2437, "Los Angeles"),
    "Asia/Kolkata": (22.5726, 88.3639, "Kolkata"),
}


def dung(ca, node_mode):
    nhan, y, mo, d, h, mi, tz, mien, ghi = ca
    cu = E.NODE_MODE
    E.NODE_MODE = node_mode
    try:
        lat, lon, noi = TOA_DO[tz]
        # miền Bắc dùng vùng khác, build_chart tự xử lý qua tham số mien
        c = E.build_chart(y, mo, d, h, mi, tz=tz, lat=lat, lon=lon,
                          noi_sinh=noi, mien=mien)
    finally:
        E.NODE_MODE = cu
    return c


def gon(c):
    return (c["type"], c["authority"], c["profile"], tuple(sorted(c["kenh"])))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", action="store_true", help="xuất thêm file CSV để điền tay")
    args = ap.parse_args()

    assert len(BO_50) == 50, f"phải đúng 50 ca, đang có {len(BO_50)}"

    # ── Phần 1: True Node so Mean Node ─────────────────────────────
    print("═" * 78)
    print("PHẦN 1 — TRUE NODE so MEAN NODE trên 50 ca")
    print("═" * 78)
    lech = []
    for ca in BO_50:
        t, m = dung(ca, "true"), dung(ca, "mean")
        if gon(t) != gon(m):
            lech.append((ca[0], gon(t), gon(m)))
    quyet, phu = [], []
    for nhan, t, m in lech:
        (quyet if (t[0], t[1]) != (m[0], m[1]) else phu).append((nhan, t, m))

    print(f"\n  {len(lech)}/50 ca cho kết quả khác nhau giữa hai chế độ.")
    print(f"  Trong đó {len(quyet)} ca khác cả Type hoặc Authority — CHỈ CẦN ĐỐI CHIẾU {len(quyet)} CA NÀY.\n")
    print("  ┌─ CA QUYẾT ĐỊNH — hỏi nguồn ngoài mấy ca này là chốt được node")
    for nhan, t, m in quyet:
        ca = next(c for c in BO_50 if c[0] == nhan)
        _, y, mo, d, h, mi, tz, mien, _ = ca
        print(f"  │ {nhan}  {d:02d}/{mo:02d}/{y} {h:02d}:{mi:02d}  {TOA_DO[tz][2]}"
              + (f" (miền {mien})" if mien else ""))
        print(f"  │     nếu nguồn ngoài ra  {t[0]:<22} {t[1]:<16} → chốt TRUE NODE")
        print(f"  │     nếu nguồn ngoài ra  {m[0]:<22} {m[1]:<16} → chốt MEAN NODE")
    print("  └─")
    if phu:
        print(f"\n  ({len(phu)} ca còn lại chỉ khác danh sách kênh, không đủ rõ để quyết:"
              f" {', '.join(n for n, _, _ in phu)})")
    if not lech:
        print("  → Hai chế độ cho kết quả y hệt trên bộ này. Cần thêm ca để phân biệt.")
    else:
        print(f"\n  → Chỉ cần đối chiếu {len(lech)} ca này với nguồn ngoài là chốt được node.")

    # ── Phần 2: bảng đối chiếu ─────────────────────────────────────
    print("\n" + "═" * 78)
    print("PHẦN 2 — BẢNG ĐỐI CHIẾU (chế độ hiện tại: %s NODE)" % E.NODE_MODE.upper())
    print("═" * 78)
    print(f"\n{'Mã':<7}{'Ngày sinh':<18}{'Nơi':<16}{'Type':<23}{'Auth':<12}{'Prof'}")
    print("-" * 78)
    hang = []
    for ca in BO_50:
        nhan, y, mo, d, h, mi, tz, mien, ghi = ca
        c = dung(ca, E.NODE_MODE)
        noi = TOA_DO[tz][2] + (f" ({mien})" if mien else "")
        print(f"{nhan:<7}{d:02d}/{mo:02d}/{y} {h:02d}:{mi:02d}  {noi:<16}"
              f"{c['type']:<23}{c['authority']:<12}{c['profile']}")
        hang.append({
            "ma": nhan, "ngay": f"{d:02d}/{mo:02d}/{y}", "gio": f"{h:02d}:{mi:02d}",
            "noi_sinh": TOA_DO[tz][2], "mui_gio": tz, "mien": mien or "",
            "engine_type": c["type"], "engine_authority": c["authority"],
            "engine_profile": c["profile"], "engine_kenh": " ".join(sorted(c["kenh"])),
            "nguon1_type": "", "nguon1_authority": "", "nguon1_profile": "",
            "nguon2_type": "", "nguon2_authority": "", "nguon2_profile": "",
            "khop": "", "ghi_chu": ghi,
        })

    if args.csv:
        ten = "doi-chieu-50-chart.csv"
        with open(ten, "w", newline="", encoding="utf-8-sig") as f:
            w = csv.DictWriter(f, fieldnames=list(hang[0].keys()))
            w.writeheader()
            w.writerows(hang)
        print(f"\n✅ Đã xuất {ten} — mở bằng Excel, điền cột nguon1 và nguon2.")
        print("   Cột 'khop' điền: OK nếu khớp cả ba, hoặc ghi rõ lệch chỗ nào.")


if __name__ == "__main__":
    main()
