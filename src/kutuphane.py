"""
Kütüphane iş mantığı - tüm işlemler burada yönetilir
"""

import json
import os
from datetime import date
from src.kitap import Kitap
from src.uye import Uye
from src.logger import islem_kaydet


class Kutuphane:
    def __init__(self):
        self.kitaplar = {}   # isbn -> Kitap
        self.uyeler = {}     # uye_id -> Uye
        self.odunc_kayitlari = []  # tüm işlem geçmişi

    # ─── KİTAP İŞLEMLERİ ───────────────────────────────────────

    def kitap_ekle(self, isbn, baslik, yazar, yil, kopya=1):
        if isbn in self.kitaplar:
            print(f"HATA: {isbn} ISBN'li kitap zaten kayıtlı.")
            return False
        self.kitaplar[isbn] = Kitap(isbn, baslik, yazar, yil, kopya)
        islem_kaydet(f"KİTAP EKLENDİ | {baslik} | ISBN:{isbn}")
        print(f"✓ '{baslik}' kitabı sisteme eklendi.")
        return True

    def kitap_sil(self, isbn):
        if isbn not in self.kitaplar:
            print("HATA: Kitap bulunamadı.")
            return False
        baslik = self.kitaplar[isbn].baslik
        del self.kitaplar[isbn]
        islem_kaydet(f"KİTAP SİLİNDİ | {baslik} | ISBN:{isbn}")
        print(f"✓ '{baslik}' kitabı sistemden silindi.")
        return True

    def kitap_ara(self, arama):
        arama = arama.lower()
        sonuclar = [k for k in self.kitaplar.values()
                    if arama in k.baslik.lower() or arama in k.yazar.lower()]
        return sonuclar

    def tum_kitaplari_listele(self):
        return list(self.kitaplar.values())

    # ─── ÜYE İŞLEMLERİ ─────────────────────────────────────────

    def uye_ekle(self, ad, soyad, email):
        uye_id = f"U{len(self.uyeler) + 1:03d}"
        self.uyeler[uye_id] = Uye(uye_id, ad, soyad, email)
        islem_kaydet(f"ÜYE EKLENDİ | {ad} {soyad} | ID:{uye_id}")
        print(f"✓ Üye eklendi. ID: {uye_id}")
        return uye_id

    def uye_sil(self, uye_id):
        if uye_id not in self.uyeler:
            print("HATA: Üye bulunamadı.")
            return False
        uye = self.uyeler[uye_id]
        if uye.odunc_listesi:
            print("HATA: Üyenin iade etmediği kitaplar var.")
            return False
        del self.uyeler[uye_id]
        islem_kaydet(f"ÜYE SİLİNDİ | {uye.tam_ad()} | ID:{uye_id}")
        print(f"✓ {uye.tam_ad()} üyelikten silindi.")
        return True

    def tum_uyeleri_listele(self):
        return list(self.uyeler.values())

    # ─── ÖDÜNÇ İŞLEMLERİ ───────────────────────────────────────

    def odunc_ver(self, uye_id, isbn):
        if uye_id not in self.uyeler:
            print("HATA: Üye bulunamadı.")
            return False
        if isbn not in self.kitaplar:
            print("HATA: Kitap bulunamadı.")
            return False

        kitap = self.kitaplar[isbn]
        uye = self.uyeler[uye_id]

        if not kitap.musait_mi():
            print(f"HATA: '{kitap.baslik}' şu anda mevcut değil.")
            return False

        kitap.odunc_ver()
        uye.kitap_odunc_al(isbn)

        kayit = {
            "tarih": date.today().isoformat(),
            "islem": "ÖDÜNÇ",
            "uye": uye.tam_ad(),
            "kitap": kitap.baslik
        }
        self.odunc_kayitlari.append(kayit)
        islem_kaydet(f"ÖDÜNÇ | {uye.tam_ad()} -> '{kitap.baslik}'")
        print(f"✓ '{kitap.baslik}' kitabı {uye.tam_ad()} adına ödünç verildi.")
        return True

    def iade_al(self, uye_id, isbn):
        if uye_id not in self.uyeler:
            print("HATA: Üye bulunamadı.")
            return False
        if isbn not in self.kitaplar:
            print("HATA: Kitap bulunamadı.")
            return False

        kitap = self.kitaplar[isbn]
        uye = self.uyeler[uye_id]

        if isbn not in uye.odunc_listesi:
            print("HATA: Bu üyede bu kitap kayıtlı değil.")
            return False

        kitap.iade_al()
        uye.kitap_iade_et(isbn)

        kayit = {
            "tarih": date.today().isoformat(),
            "islem": "İADE",
            "uye": uye.tam_ad(),
            "kitap": kitap.baslik
        }
        self.odunc_kayitlari.append(kayit)
        islem_kaydet(f"İADE | {uye.tam_ad()} -> '{kitap.baslik}'")
        print(f"✓ '{kitap.baslik}' kitabı iade alındı.")
        return True

    # ─── RAPOR ──────────────────────────────────────────────────

    def rapor_olustur(self):
        toplam_kitap = len(self.kitaplar)
        toplam_uye = len(self.uyeler)
        oduncteki = sum(1 for k in self.kitaplar.values() if not k.musait_mi())

        rapor_yolu = "outputs/rapor.txt"
        os.makedirs("outputs", exist_ok=True)
        with open(rapor_yolu, "w", encoding="utf-8") as f:
            f.write(f"KÜTÜPHANE RAPORU - {date.today()}\n")
            f.write("=" * 40 + "\n")
            f.write(f"Toplam Kitap : {toplam_kitap}\n")
            f.write(f"Toplam Üye  : {toplam_uye}\n")
            f.write(f"Ödünçteki   : {oduncteki}\n")
            f.write("\n--- Kitap Listesi ---\n")
            for k in self.kitaplar.values():
                f.write(str(k) + "\n")
            f.write("\n--- Üye Listesi ---\n")
            for u in self.uyeler.values():
                f.write(str(u) + "\n")
        print(f"✓ Rapor '{rapor_yolu}' dosyasına kaydedildi.")

    # ─── ÖRNEK VERİ ─────────────────────────────────────────────

    def ornek_veri_yukle(self):
        kitaplar = [
            ("978-1", "Tutunamayanlar", "Oğuz Atay", 1972, 2),
            ("978-2", "İnce Memed", "Yaşar Kemal", 1955, 3),
            ("978-3", "Kürk Mantolu Madonna", "Sabahattin Ali", 1943, 2),
            ("978-4", "Sinekli Bakkal", "Halide Edib Adıvar", 1936, 1),
            ("978-5", "Yaprak Dökümü", "Reşat Nuri Güntekin", 1930, 2),
        ]
        uyeler = [
            ("Ali", "Yılmaz", "ali@email.com"),
            ("Ayşe", "Kaya", "ayse@email.com"),
            ("Mehmet", "Demir", "mehmet@email.com"),
        ]
        for isbn, baslik, yazar, yil, kopya in kitaplar:
            self.kitaplar[isbn] = Kitap(isbn, baslik, yazar, yil, kopya)
        for ad, soyad, email in uyeler:
            uye_id = f"U{len(self.uyeler) + 1:03d}"
            self.uyeler[uye_id] = Uye(uye_id, ad, soyad, email)
