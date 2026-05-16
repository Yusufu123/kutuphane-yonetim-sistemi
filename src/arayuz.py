"""
Kullanıcı menüsü ve terminal arayüzü
"""


def menu_goster(kutuphane):
    while True:
        print("\n--- ANA MENÜ ---")
        print("1. Kitap İşlemleri")
        print("2. Üye İşlemleri")
        print("3. Ödünç / İade")
        print("4. Rapor Oluştur")
        print("0. Çıkış")

        secim = input("\nSeçiminiz: ").strip()

        if secim == "1":
            kitap_menu(kutuphane)
        elif secim == "2":
            uye_menu(kutuphane)
        elif secim == "3":
            odunc_menu(kutuphane)
        elif secim == "4":
            kutuphane.rapor_olustur()
        elif secim == "0":
            print("Güle güle!")
            break
        else:
            print("Geçersiz seçim.")


def kitap_menu(kutuphane):
    print("\n--- KİTAP İŞLEMLERİ ---")
    print("1. Kitap Ekle")
    print("2. Kitap Sil")
    print("3. Kitap Ara")
    print("4. Tüm Kitapları Listele")
    print("0. Geri")

    secim = input("Seçiminiz: ").strip()

    if secim == "1":
        isbn = input("ISBN: ").strip()
        baslik = input("Başlık: ").strip()
        yazar = input("Yazar: ").strip()
        yil = int(input("Yıl: ").strip())
        kopya = int(input("Kopya Sayısı: ").strip())
        kutuphane.kitap_ekle(isbn, baslik, yazar, yil, kopya)

    elif secim == "2":
        isbn = input("Silinecek kitabın ISBN'i: ").strip()
        kutuphane.kitap_sil(isbn)

    elif secim == "3":
        arama = input("Arama (başlık veya yazar): ").strip()
        sonuclar = kutuphane.kitap_ara(arama)
        if sonuclar:
            for k in sonuclar:
                print(" ", k)
        else:
            print("Sonuç bulunamadı.")

    elif secim == "4":
        kitaplar = kutuphane.tum_kitaplari_listele()
        if kitaplar:
            for k in kitaplar:
                print(" ", k)
        else:
            print("Sistemde kitap yok.")


def uye_menu(kutuphane):
    print("\n--- ÜYE İŞLEMLERİ ---")
    print("1. Üye Ekle")
    print("2. Üye Sil")
    print("3. Tüm Üyeleri Listele")
    print("0. Geri")

    secim = input("Seçiminiz: ").strip()

    if secim == "1":
        ad = input("Ad: ").strip()
        soyad = input("Soyad: ").strip()
        email = input("E-posta: ").strip()
        kutuphane.uye_ekle(ad, soyad, email)

    elif secim == "2":
        uye_id = input("Silinecek üye ID: ").strip()
        kutuphane.uye_sil(uye_id)

    elif secim == "3":
        uyeler = kutuphane.tum_uyeleri_listele()
        if uyeler:
            for u in uyeler:
                print(" ", u)
        else:
            print("Sistemde üye yok.")


def odunc_menu(kutuphane):
    print("\n--- ÖDÜNÇ / İADE ---")
    print("1. Kitap Ödünç Ver")
    print("2. Kitap İade Al")
    print("0. Geri")

    secim = input("Seçiminiz: ").strip()

    if secim == "1":
        uye_id = input("Üye ID: ").strip()
        isbn = input("Kitap ISBN: ").strip()
        kutuphane.odunc_ver(uye_id, isbn)

    elif secim == "2":
        uye_id = input("Üye ID: ").strip()
        isbn = input("Kitap ISBN: ").strip()
        kutuphane.iade_al(uye_id, isbn)
