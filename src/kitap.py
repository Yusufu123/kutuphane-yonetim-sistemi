"""
Kitap veri modeli
"""


class Kitap:
    def __init__(self, isbn, baslik, yazar, yil, kopya_sayisi=1):
        self.isbn = isbn
        self.baslik = baslik
        self.yazar = yazar
        self.yil = yil
        self.kopya_sayisi = kopya_sayisi
        self.mevcut_kopya = kopya_sayisi

    def odunc_ver(self):
        if self.mevcut_kopya > 0:
            self.mevcut_kopya -= 1
            return True
        return False

    def iade_al(self):
        if self.mevcut_kopya < self.kopya_sayisi:
            self.mevcut_kopya += 1
            return True
        return False

    def musait_mi(self):
        return self.mevcut_kopya > 0

    def __str__(self):
        durum = "Mevcut" if self.musait_mi() else "Ödünçte"
        return (f"[{self.isbn}] {self.baslik} - {self.yazar} ({self.yil}) "
                f"| {self.mevcut_kopya}/{self.kopya_sayisi} kopya | {durum}")
