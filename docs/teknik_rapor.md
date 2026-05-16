# Teknik Rapor

**Proje:** Kütüphane Yönetim Sistemi  
**Geliştirici:** Yusuf Kıvrık  
**Tarih:** 2025

---

## 1. Genel Bakış

Bu proje, Python ile geliştirilmiş bir terminal tabanlı kütüphane yönetim sistemidir. Sistem; kitap ve üye bilgilerini bellekte tutar, tüm işlemleri log dosyasına kaydeder ve rapor oluşturabilir.

## 2. Mimari Yapı

Proje modüler bir yapıda tasarlanmıştır:

```
main.py           → Giriş noktası
src/
  kitap.py        → Kitap veri modeli
  uye.py          → Üye veri modeli
  kutuphane.py    → İş mantığı (kitap, üye, ödünç işlemleri)
  arayuz.py       → Terminal menüsü
  logger.py       → Log kaydı
docs/             → Proje belgeleri
logs/             → İşlem kayıtları
outputs/          → Rapor çıktıları
data/             → Veri dosyaları (opsiyonel)
```

## 3. Sınıflar ve Sorumlulukları

### `Kitap`
- Kitabın ISBN, başlık, yazar, yıl ve kopya sayısı bilgilerini tutar.
- `odunc_ver()`: mevcut kopya sayısını 1 azaltır.
- `iade_al()`: mevcut kopya sayısını 1 artırır.
- `musait_mi()`: kitabın ödünç verilebilir olup olmadığını döner.

### `Uye`
- Üye ID, ad, soyad, e-posta ve kayıt tarihi bilgilerini tutar.
- `odunc_listesi`: üyenin elindeki kitapların ISBN listesi.
- `kitap_odunc_al()` / `kitap_iade_et()` metodları listeyi günceller.

### `Kutuphane`
- `kitaplar` (dict) ve `uyeler` (dict) veri yapılarını yönetir.
- Tüm iş kurallarını uygular: stok kontrolü, üye kontrolü, iade kontrolü.
- `odunc_kayitlari` listesi işlem geçmişini tutar.

## 4. Veri Saklama

Mevcut sürümde veriler **bellekte** (RAM) tutulmaktadır. Program kapatıldığında veriler kaybolur; ancak tüm işlemler `logs/islemler.log` dosyasına yazılmaktadır.

## 5. İş Akışı: Ödünç Verme

```
Kullanıcı → üye_id ve isbn girer
    ↓
Üye sistemde var mı? → HAYIR → Hata mesajı
    ↓
Kitap sistemde var mı? → HAYIR → Hata mesajı
    ↓
Kitapta mevcut kopya var mı? → HAYIR → Hata mesajı
    ↓
kitap.odunc_ver() → mevcut_kopya azalır
uye.kitap_odunc_al(isbn) → listeye eklenir
islem_kaydet() → log dosyasına yazılır
    ↓
Başarı mesajı
```

## 6. Log Sistemi

Her işlem `logs/islemler.log` dosyasına şu formatta yazılır:
```
[2025-05-10 14:32:01] ÖDÜNÇ | Ali Yılmaz -> 'Tutunamayanlar'
[2025-05-10 14:35:22] İADE | Ali Yılmaz -> 'Tutunamayanlar'
```

## 7. Kullanılan Python Modülleri

| Modül | Kullanım Amacı |
|-------|----------------|
| `datetime` | İşlem tarihi ve saati |
| `os` | Klasör oluşturma, dosya yolu |
| `json` | (Hazır; opsiyonel veri kalıcılığı için) |

## 8. Test Senaryoları

| Senaryo | Beklenen Sonuç | Sonuç |
|---------|----------------|-------|
| Var olan ISBN ile kitap ekleme | Hata mesajı | ✓ |
| Mevcut olmayan kitabı ödünç verme | Hata mesajı | ✓ |
| Stoku sıfır kitabı ödünç verme | Hata mesajı | ✓ |
| Kitabı olmayan üyeden iade alma | Hata mesajı | ✓ |
| Ödünç kitabı olan üyeyi silme | Hata mesajı | ✓ |
| Normal ödünç ve iade | Başarılı | ✓ |

## 9. Geliştirme Ortamı

- **Python sürümü:** 3.10+
- **İşletim Sistemi:** Windows / Linux / macOS
- **Ekstra kütüphane:** Yok (yalnızca standart kütüphane)
