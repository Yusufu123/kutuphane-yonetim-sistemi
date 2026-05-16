# Veritabanı Özeti

**Proje:** Kütüphane Yönetim Sistemi

---

## Veri Saklama Yaklaşımı

Bu proje **dosya tabanlı** bir veri saklama yöntemi kullanmaktadır.  
İlişkisel veritabanı (SQL) kullanılmamıştır; bunun yerine Python sözlükleri ve metin dosyaları tercih edilmiştir.

---

## Bellekteki Veri Yapıları

### `kitaplar` (dict)
```
Anahtar: isbn (str)
Değer  : Kitap nesnesi

Örnek:
{
  "978-1": Kitap(isbn="978-1", baslik="Tutunamayanlar", yazar="Oğuz Atay",
                 yil=1972, kopya_sayisi=2, mevcut_kopya=1)
}
```

### `uyeler` (dict)
```
Anahtar: uye_id (str, örn: "U001")
Değer  : Uye nesnesi

Örnek:
{
  "U001": Uye(uye_id="U001", ad="Ali", soyad="Yılmaz",
              email="ali@email.com", odunc_listesi=["978-1"])
}
```

### `odunc_kayitlari` (list)
```
Her eleman bir dict'tir:
{
  "tarih": "2025-05-10",
  "islem": "ÖDÜNÇ",
  "uye": "Ali Yılmaz",
  "kitap": "Tutunamayanlar"
}
```

---

## Dosya Tabanlı Kayıtlar

| Dosya | İçerik | Format |
|-------|--------|--------|
| `logs/islemler.log` | Tüm işlemlerin zaman damgalı kaydı | Düz metin |
| `outputs/rapor.txt` | Sistem anlık durum raporu | Düz metin |

---

## Veri İlişkileri

```
Kitap ←──────────── Uye
(isbn)               (odunc_listesi içinde isbn referansı)
```

Üye ile kitap arasındaki ilişki, üyenin `odunc_listesi` içindeki ISBN değerleri aracılığıyla kurulur.

---

## Sınırlılıklar

- Veriler program kapandığında silinir (kalıcı depolama yok).
- İleride `data/kitaplar.json` ve `data/uyeler.json` dosyalarına kayıt/yükleme eklenebilir.
