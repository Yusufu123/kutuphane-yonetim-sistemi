# Kütüphane Yönetim Sistemi

Python Final Projesi — Yusuf Kıvrık — 2025

---

## Proje Hakkında

Bu proje, terminal üzerinden çalışan bir kütüphane yönetim sistemidir.  
Kitap ve üye kaydı, ödünç verme/iade alma ve rapor oluşturma işlemlerini destekler.

## Kurulum

```bash
pip install -r requirements.txt
```

> Ekstra kütüphane gerekmez; yalnızca Python standart kütüphanesi kullanılmıştır.

## Çalıştırma

```bash
python main.py
```

## Özellikler

- Kitap ekle, sil, ara, listele
- Üye ekle, sil, listele
- Kitap ödünç ver ve iade al (stok kontrolü ile)
- Tüm işlemler `logs/islemler.log` dosyasına kaydedilir
- `outputs/rapor.txt` ile anlık sistem raporu oluşturulabilir

## Klasör Yapısı

```
.
├── main.py
├── requirements.txt
├── src/
│   ├── kitap.py
│   ├── uye.py
│   ├── kutuphane.py
│   ├── arayuz.py
│   └── logger.py
├── docs/
│   ├── proje_onerisi.md
│   ├── ilerleme_raporu.md
│   ├── teknik_rapor.md
│   ├── rol_yetki_matrisi.md
│   ├── veritabani_ozeti.md
│   ├── senaryolar.md
│   ├── yapay_zeka_kullanim_beyani.md
│   └── yapay_zeka_kullanim_yontemleri_ve_senaryolari.md
├── data/
├── logs/
└── outputs/
```
