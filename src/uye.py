"""
Üye veri modeli
"""
from datetime import date


class Uye:
    def __init__(self, uye_id, ad, soyad, email):
        self.uye_id = uye_id
        self.ad = ad
        self.soyad = soyad
        self.email = email
        self.kayit_tarihi = date.today().isoformat()
        self.odunc_listesi = []  # isbn listesi

    def tam_ad(self):
        return f"{self.ad} {self.soyad}"

    def kitap_odunc_al(self, isbn):
        self.odunc_listesi.append(isbn)

    def kitap_iade_et(self, isbn):
        if isbn in self.odunc_listesi:
            self.odunc_listesi.remove(isbn)
            return True
        return False

    def __str__(self):
        return (f"[{self.uye_id}] {self.tam_ad()} | {self.email} "
                f"| Kayıt: {self.kayit_tarihi} | Ödünç: {len(self.odunc_listesi)} kitap")
