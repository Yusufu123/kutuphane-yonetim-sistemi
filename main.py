"""
Kütüphane Yönetim Sistemi - Ana Giriş Noktası
Yazar: Yusuf Kıvrık
Tarih: 2025
"""

from src.kutuphane import Kutuphane
from src.arayuz import menu_goster


def main():
    print("=" * 50)
    print("   KÜTÜPHANE YÖNETİM SİSTEMİ")
    print("=" * 50)

    kutuphane = Kutuphane()
    kutuphane.ornek_veri_yukle()

    menu_goster(kutuphane)


if __name__ == "__main__":
    main()
