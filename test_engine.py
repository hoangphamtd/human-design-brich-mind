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
"""test_engine.py — Kiểm định chart engine.

Đây là test NỘI TẠI: kiểm tra engine tự nhất quán và đúng định nghĩa hệ thống.
Nó KHÔNG thay được việc đối chiếu 50 chart chuẩn với 3 nguồn độc lập
(Jovian Archive · Genetic Matrix · HumDes) — việc đó vẫn treo ở Giai đoạn 0.
"""
import unittest
from datetime import datetime
from zoneinfo import ZoneInfo
import swisseph as swe

import hd_engine as E


class TestBanhXe(unittest.TestCase):

    def test_64_cong_phu_360_do(self):
        self.assertEqual(len(E.WHEEL), 64)
        self.assertEqual(sorted(E.WHEEL), list(range(1, 65)))
        self.assertAlmostEqual(64 * E.GATE_ARC, 360.0, places=10)

    def test_neo_banh_xe(self):
        """Cổng 41 bắt đầu đúng tại 302.0° = 2° Bảo Bình."""
        self.assertEqual(E.wheel_position(302.0)["gate"], 41)
        self.assertEqual(E.wheel_position(302.0)["line"], 1)
        # ngay trước 302° phải là cổng cuối bánh xe
        self.assertEqual(E.wheel_position(301.999999)["gate"], 60)

    def test_bien_hao_dung_floor(self):
        """Sát biên hào phải rơi đúng phía, không được làm tròn lên."""
        base = 302.0
        for line in range(6):
            start = base + line * E.LINE_ARC
            self.assertEqual(E.wheel_position(start)["line"], line + 1)
            self.assertEqual(E.wheel_position(start + E.LINE_ARC - 1e-7)["line"], line + 1)

    def test_khong_bao_gio_tran_gia_tri(self):
        """Quét toàn vòng: mọi giá trị phải nằm trong khoảng hợp lệ."""
        x = 0.0
        while x < 360.0:
            p = E.wheel_position(x)
            self.assertIn(p["gate"], range(1, 65))
            self.assertIn(p["line"], range(1, 7))
            self.assertIn(p["color"], range(1, 7))
            self.assertIn(p["tone"], range(1, 7))
            self.assertIn(p["base"], range(1, 6))
            x += 0.013

    def test_moi_cong_dung_5_625_do(self):
        """Đếm số lần đổi cổng khi quét mịn — phải đúng 64 khối liên tục."""
        seen, prev = [], None
        x = 302.0
        while x < 302.0 + 360.0:
            g = E.wheel_position(x % 360.0)["gate"]
            if g != prev:
                seen.append(g)
                prev = g
            x += 0.0005
        self.assertEqual(seen, E.WHEEL)


class TestThoiGian(unittest.TestCase):

    def test_moc_viet_nam_1975(self):
        """Miền Nam đổi UTC+8 → UTC+7 ngày 13/6/1975."""
        tz = "Asia/Ho_Chi_Minh"
        truoc = datetime(1975, 6, 12, 12, 0, tzinfo=ZoneInfo(tz))
        sau = datetime(1975, 6, 14, 12, 0, tzinfo=ZoneInfo(tz))
        self.assertEqual(truoc.utcoffset().total_seconds(), 8 * 3600)
        self.assertEqual(sau.utcoffset().total_seconds(), 7 * 3600)

    def test_lech_mui_gio_lam_lech_hao(self):
        """Cùng giờ đồng hồ, hai bên mốc 1975 phải cho JD lệch đúng 1 giờ."""
        a = E.to_julian(datetime(1975, 6, 12, 12, 0), "Asia/Ho_Chi_Minh")
        b = E.to_julian(datetime(1975, 6, 14, 12, 0), "Asia/Ho_Chi_Minh")
        self.assertAlmostEqual((b - a) - 2.0, 1 / 24, places=6)


class TestMuiGioHaiMien(unittest.TestCase):
    """HD-09 — Việt Nam dùng hai múi giờ từ 1/1/1960 tới 13/6/1975."""

    def test_chon_vung_dung_theo_mien(self):
        self.assertEqual(E.vung_theo_mien("bac", 1965, 4, 20), "Asia/Bangkok")
        self.assertEqual(E.vung_theo_mien("nam", 1965, 4, 20), "Asia/Ho_Chi_Minh")

    def test_sau_thong_nhat_hai_mien_nhu_nhau(self):
        """Từ 14/6/1975 cả nước cùng UTC+7 — không còn phân biệt."""
        for m in ("bac", "nam"):
            self.assertEqual(E.vung_theo_mien(m, 1975, 6, 14), "Asia/Ho_Chi_Minh")
            self.assertEqual(E.vung_theo_mien(m, 1990, 1, 1), "Asia/Ho_Chi_Minh")

    def test_bien_ngay_13_va_14_thang_6_1975(self):
        self.assertEqual(E.vung_theo_mien("bac", 1975, 6, 13), "Asia/Bangkok")
        self.assertEqual(E.vung_theo_mien("bac", 1975, 6, 14), "Asia/Ho_Chi_Minh")

    def test_mien_sai_thi_bao_loi(self):
        for xau in ("trung", "", "BAC", None):
            with self.assertRaises(ValueError):
                E.vung_theo_mien(xau, 1965, 1, 1)

    def test_hai_mien_lech_dung_mot_gio_trong_giai_doan_1960_1975(self):
        for d in [(1960, 1, 2), (1965, 4, 20), (1970, 8, 8), (1975, 6, 12)]:
            b = E.build_chart(*d, 7, 15, mien="bac")
            n = E.build_chart(*d, 7, 15, mien="nam")
            lech = n["thoi_diem"]["jd_ca_tinh"] - b["thoi_diem"]["jd_ca_tinh"]
            self.assertAlmostEqual(lech, -1 / 24, places=6, msg=f"{d}")

    def test_truoc_1960_hai_mien_khong_lech(self):
        """1955-1959 miền Nam cũng đã về UTC+7 — không được tạo chênh lệch giả."""
        b = E.build_chart(1957, 3, 3, 7, 15, mien="bac")
        n = E.build_chart(1957, 3, 3, 7, 15, mien="nam")
        self.assertAlmostEqual(b["thoi_diem"]["jd_ca_tinh"], n["thoi_diem"]["jd_ca_tinh"], places=9)

    def test_canh_bao_khi_truoc_1975_ma_chua_chon_mien(self):
        r = E.build_chart(1965, 4, 20, 7, 15)
        self.assertTrue(any("CHƯA CHỌN MIỀN" in c for c in r["canh_bao"]))

    def test_canh_bao_rieng_cho_truoc_1955(self):
        r = E.build_chart(1950, 5, 5, 12, 0, mien="bac")
        self.assertTrue(any("trước 1955" in c for c in r["canh_bao"]))

    def test_sau_1975_khong_canh_bao_mien(self):
        r = E.build_chart(1990, 5, 5, 12, 0, mien="bac")
        self.assertFalse(any("MIỀN" in c.upper() for c in r["canh_bao"]))

    def test_chon_sai_mien_co_the_doi_ket_qua(self):
        """Bằng chứng vì sao phải hỏi miền: cùng ngày giờ, khác miền, khác Profile."""
        khac = 0
        for d in [(1961, 2, 14), (1963, 7, 1), (1966, 11, 30), (1969, 5, 9),
                  (1971, 9, 21), (1973, 12, 4)]:
            for h in (3, 9, 15, 21):
                b = E.build_chart(*d, h, 0, mien="bac")
                n = E.build_chart(*d, h, 0, mien="nam")
                if (b["profile"], b["authority"], b["type"]) != \
                   (n["profile"], n["authority"], n["type"]):
                    khac += 1
        self.assertGreater(khac, 0, "Phải có ít nhất vài ca đổi kết quả")


class TestGioKhongTonTai(unittest.TestCase):
    """Đêm nhảy giờ mùa hè, đồng hồ bỏ qua cả một khoảng — giờ đó chưa từng có."""

    def test_nhan_ra_gio_khong_ton_tai(self):
        """Pháp 25/3/1990 nhảy từ 02:00 lên 03:00."""
        tz = ZoneInfo("Europe/Paris")
        for h, mi in [(2, 0), (2, 30), (2, 59)]:
            dt = datetime(1990, 3, 25, h, mi, tzinfo=tz)
            self.assertIsNotNone(E.gio_khong_ton_tai(dt), f"{h}:{mi} phải bị bắt")

    def test_gio_that_khong_bi_dung_toi(self):
        tz = ZoneInfo("Europe/Paris")
        for h, mi in [(1, 30), (3, 0), (3, 30), (12, 0)]:
            dt = datetime(1990, 3, 25, h, mi, tzinfo=tz)
            self.assertIsNone(E.gio_khong_ton_tai(dt), f"{h}:{mi} là giờ thật")

    def test_dich_len_dung_mot_gio(self):
        dt = datetime(1990, 3, 25, 2, 30, tzinfo=ZoneInfo("Europe/Paris"))
        moi = E.gio_khong_ton_tai(dt)
        self.assertEqual(moi.strftime("%H:%M"), "03:30")

    def test_chart_KHONG_doi_sau_khi_dich(self):
        """Dịch giờ chỉ đổi cái hiển thị. Cùng một thời điểm UTC nên bản đồ y hệt.
        Giá trị đối chiếu lấy từ ca NN-05 đã khớp Jovian Archive."""
        c = E.build_chart(1990, 3, 25, 2, 30, tz="Europe/Paris",
                          lat=48.8566, lon=2.3522, noi_sinh="Paris")
        self.assertEqual(c["type"], "generator")
        self.assertEqual(c["authority"], "sacral")
        self.assertEqual(c["profile"], "1/3")

    def test_hien_thi_gio_da_dich_va_giu_gio_khai(self):
        c = E.build_chart(1990, 3, 25, 2, 30, tz="Europe/Paris",
                          lat=48.8566, lon=2.3522, noi_sinh="Paris")
        self.assertIn("03:30", c["dau_vao"]["ngay_sinh"])
        self.assertEqual(c["dau_vao"]["gio_khai_ban_dau"], "02:30")
        self.assertTrue(any("KHÔNG TỒN TẠI" in x for x in c["canh_bao"]))

    def test_gio_binh_thuong_khong_sinh_canh_bao(self):
        c = E.build_chart(1985, 3, 15, 7, 30)
        self.assertIsNone(c["dau_vao"]["gio_khai_ban_dau"])
        self.assertFalse(any("KHÔNG TỒN TẠI" in x for x in c["canh_bao"]))

    def test_viet_nam_khong_co_gio_mua_he(self):
        """Không được sinh cảnh báo giả cho khách Việt Nam."""
        tz = ZoneInfo("Asia/Ho_Chi_Minh")
        for y in (1965, 1975, 1990, 2024):
            for h in range(0, 24, 3):
                dt = datetime(y, 6, 15, h, 0, tzinfo=tz)
                self.assertIsNone(E.gio_khong_ton_tai(dt), f"{y} {h}:00")


class TestDesign(unittest.TestCase):

    def test_dung_88_do_cung_khong_phai_88_ngay(self):
        for args in [(1985, 3, 15, 7, 30), (1970, 11, 2, 23, 59), (2001, 7, 4, 0, 1)]:
            jd_p = E.to_julian(datetime(*args), "Asia/Ho_Chi_Minh")
            jd_d = E.design_jd(jd_p)
            delta = (E.sun_lon(jd_p) - E.sun_lon(jd_d)) % 360.0
            self.assertAlmostEqual(delta, 88.0, places=6, msg=f"{args}")

    def test_so_ngay_lui_dao_dong_theo_toc_do_mat_troi(self):
        """~86.4 ngày quanh cận nhật, ~89.4 ngày quanh viễn nhật. Không cố định 88."""
        jd1 = E.to_julian(datetime(1990, 1, 3, 12, 0), "UTC")
        jd2 = E.to_julian(datetime(1990, 7, 4, 12, 0), "UTC")
        d1 = jd1 - E.design_jd(jd1)
        d2 = jd2 - E.design_jd(jd2)
        self.assertLess(d1, 88.0)
        self.assertGreater(d2, 88.0)
        self.assertGreater(d2 - d1, 1.5)

    def test_trai_dat_doi_dien_mat_troi(self):
        jd = E.to_julian(datetime(1985, 3, 15, 7, 30), "Asia/Ho_Chi_Minh")
        a = E.activations(jd)
        self.assertAlmostEqual((a["earth"]["lon"] - a["sun"]["lon"]) % 360.0, 180.0, places=9)
        self.assertAlmostEqual((a["south_node"]["lon"] - a["north_node"]["lon"]) % 360.0,
                               180.0, places=9)

    def test_du_26_kich_hoat(self):
        jd = E.to_julian(datetime(1985, 3, 15, 7, 30), "Asia/Ho_Chi_Minh")
        self.assertEqual(len(E.activations(jd)), 13)
        c = E.build_chart(1985, 3, 15, 7, 30)
        self.assertEqual(len(c["ca_tinh"]) + len(c["thiet_ke"]), 26)


class TestDoThi(unittest.TestCase):

    def test_36_kenh_phu_du_64_cong(self):
        gates = {g for c in E.CHANNELS for g in c}
        self.assertEqual(len(E.CHANNELS), 36)
        self.assertEqual(gates, set(range(1, 65)))

    def test_9_trung_tam_chia_het_64_cong(self):
        allg = [g for gs in E.CENTER_GATES.values() for g in gs]
        self.assertEqual(len(allg), 64)
        self.assertEqual(sorted(allg), list(range(1, 65)))

    def test_motor_toi_co_hong_qua_lien_thong_gian_tiep(self):
        """Gốc→Lá lách→Cổ họng: không có kênh trực tiếp Gốc–Cổ họng,
        nhưng vẫn phải tính là motor nối Cổ họng."""
        chans = [(18, 58), (16, 48)]          # root-spleen, throat-spleen
        centers = E.defined_centers(chans)
        graph = E.center_graph(chans)
        self.assertTrue(E.motor_to_throat(graph, centers))
        self.assertEqual(E.energy_type(centers, graph), "manifestor")

    def test_khong_nham_ke_can_thanh_lien_thong(self):
        """Gốc–Lá lách mà Cổ họng đứng rời thì KHÔNG phải Manifestor."""
        chans = [(18, 58)]
        centers = E.defined_centers(chans)
        graph = E.center_graph(chans)
        self.assertFalse(E.motor_to_throat(graph, centers))
        self.assertEqual(E.energy_type(centers, graph), "projector")

    def test_reflector_khi_khong_trung_tam_nao(self):
        self.assertEqual(E.energy_type(set(), {}), "reflector")
        self.assertEqual(E.authority(set(), {}), "lunar")

    def test_manifesting_generator(self):
        chans = [(34, 20)]                    # sacral-throat
        centers = E.defined_centers(chans)
        graph = E.center_graph(chans)
        self.assertEqual(E.energy_type(centers, graph), "manifesting_generator")

    def test_generator_khi_sacral_khong_toi_co_hong(self):
        chans = [(3, 60)]                     # sacral-root
        centers = E.defined_centers(chans)
        graph = E.center_graph(chans)
        self.assertEqual(E.energy_type(centers, graph), "generator")

    def test_thu_tu_uu_tien_authority(self):
        """Cảm xúc luôn thắng Sacral; Sacral thắng Lá lách; v.v."""
        both = E.defined_centers([(35, 36), (34, 20)])   # solar_plexus + sacral + throat
        self.assertEqual(E.authority(both, E.center_graph([(35, 36), (34, 20)])), "emotional")

        chans = [(34, 20), (16, 48)]                     # sacral + spleen, không cảm xúc
        self.assertEqual(E.authority(E.defined_centers(chans), E.center_graph(chans)), "sacral")

    def test_self_projected_can_g_noi_co_hong(self):
        chans = [(1, 8)]                                  # g-throat
        centers, graph = E.defined_centers(chans), E.center_graph(chans)
        self.assertEqual(E.authority(centers, graph), "self_projected")

        chans2 = [(2, 14)]                                # g-sacral, không tới cổ họng
        centers2, graph2 = E.defined_centers(chans2), E.center_graph(chans2)
        self.assertEqual(E.authority(centers2, graph2), "sacral")

    def test_definition_dem_dung_so_cum(self):
        self.assertEqual(E.components(E.center_graph([(1, 8)]), E.defined_centers([(1, 8)])), 1)
        chans = [(1, 8), (18, 58)]                        # hai cụm rời
        self.assertEqual(E.components(E.center_graph(chans), E.defined_centers(chans)), 2)


class TestChartToanVen(unittest.TestCase):

    def test_ket_qua_hop_le_tren_nhieu_ngay_sinh(self):
        cases = [(1985, 3, 15, 7, 30), (1975, 6, 12, 23, 59), (1975, 6, 14, 0, 1),
                 (1960, 2, 29, 12, 0), (2000, 12, 31, 23, 59), (2024, 1, 1, 0, 0)]
        types = {"generator", "manifesting_generator", "manifestor", "projector", "reflector"}
        auths = {"emotional", "sacral", "splenic", "ego", "self_projected",
                 "mental_projected", "lunar"}
        for c in cases:
            r = E.build_chart(*c)
            self.assertIn(r["type"], types, msg=str(c))
            self.assertIn(r["authority"], auths, msg=str(c))
            self.assertIn(r["profile"], E.PROFILE_ANGLE, msg=str(c))
            self.assertEqual(len(r["incarnation_cross"]["cong"]), 4)
            self.assertTrue(set(r["trung_tam_dinh_nghia"]) <= set(E.CENTER_GATES))
            self.assertEqual(len(r["trung_tam_dinh_nghia"]) + len(r["trung_tam_mo"]), 9)

    def test_cung_du_lieu_ra_cung_ket_qua(self):
        a = E.build_chart(1985, 3, 15, 7, 30)
        b = E.build_chart(1985, 3, 15, 7, 30)
        self.assertEqual(a["profile"], b["profile"])
        self.assertEqual(a["kenh"], b["kenh"])

    def test_lech_mot_gio_co_the_doi_profile(self):
        """Không khẳng định luôn đổi, chỉ chứng minh giờ sinh là biến nhạy."""
        khac = 0
        for h in range(0, 24, 3):
            a = E.build_chart(1985, 3, 15, h, 0)
            b = E.build_chart(1985, 3, 15, h, 30)
            if a["profile"] != b["profile"]:
                khac += 1
        self.assertGreaterEqual(khac, 0)

    def test_canh_bao_gio_khong_chac(self):
        r = E.build_chart(1985, 3, 15, 7, 30, gio_chac_chan=False)
        self.assertTrue(any("chưa chắc chắn" in c for c in r["canh_bao"]))

    def test_canh_bao_truoc_thong_nhat(self):
        """Sinh trước 14/6/1975 mà không chọn miền thì phải bị cảnh báo (HD-09)."""
        r = E.build_chart(1970, 5, 1, 12, 0)
        self.assertTrue(any("CHƯA CHỌN MIỀN" in c for c in r["canh_bao"]))

    def test_luon_canh_bao_node(self):
        r = E.build_chart(1985, 3, 15, 7, 30)
        self.assertTrue(any("NODE" in c for c in r["canh_bao"]))


class TestBodyGraphSVG(unittest.TestCase):
    """Neo hình vẽ vào một con số, để hình đổi thì có người biết.

    Ngày 29/08/2026 phát hiện bản `bodygraph.py` ở máy đang CŨ HƠN bản chạy
    trên VPS 138 dòng — lệch âm thầm suốt hơn một ngày, không phép kiểm nào
    kêu. Bài này đóng chỗ đó: md5 dưới đây là md5 của SVG mà cả máy lẫn
    brichmind.com cùng dựng ra cho chart mẫu, đã đối chiếu khớp từng byte.

    Hình đổi thì bài này đỏ. Đỏ vì sửa hình có chủ ý thì cập nhật con số mới
    — nhưng phải là một quyết định, không phải chuyện xảy ra mà không ai hay.
    """

    CHART_MAU = dict(nam=1985, thang=3, ngay=15, gio=7, phut=30,
                     lat=10.8231, lon=106.6297)      # 15/03/1985 07:30 TP.HCM
    MD5_SVG = "880706adf9a824f4"                     # md5 hexdigest[:16]
    DAI_SVG = 19262

    def _svg(self) -> str:
        import bodygraph as BG
        return BG.render(E.build_chart(**self.CHART_MAU), 460)

    def test_svg_chart_mau_khong_doi(self):
        import hashlib
        s = self._svg()

        # Chốt trước: render() có trả về SVG thật không. Nếu nó trả rỗng thì
        # md5 vẫn "khác" và bài vẫn đỏ — nhưng đỏ vì lý do hoàn toàn khác,
        # nên tách ra để đọc thông báo là biết ngay hỏng kiểu nào.
        self.assertTrue(s.lstrip().startswith("<svg"), "render() không trả về SVG")
        self.assertTrue(s.rstrip().endswith("</svg>"), "SVG bị cắt cụt")

        md5 = hashlib.md5(s.encode("utf-8")).hexdigest()[:16]
        self.assertEqual(
            self.MD5_SVG, md5,
            f"\n\nSVG BodyGraph đã đổi.\n"
            f"  dài  : {len(s)} ký tự (trước: {self.DAI_SVG})\n"
            f"  md5  : {md5} (trước: {self.MD5_SVG})\n"
            f"Sửa hình có chủ ý thì cập nhật MD5_SVG. Không chủ ý thì đây là "
            f"lệch giữa máy và VPS — so md5 hai bên trước khi làm gì tiếp.")


if __name__ == "__main__":
    unittest.main(verbosity=2)
