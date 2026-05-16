# İlerleme Raporu

**Proje:** Kütüphane Yönetim Sistemi  
**Tarih:** 2025  
**Geliştirici:** Yusuf Kıvrık

---

## Tamamlanan İşler

- [x] Proje klasör yapısı oluşturuldu (`src/`, `docs/`, `data/`, `logs/`, `outputs/`)
- [x] `Kitap` sınıfı yazıldı (ödünç verme, iade, stok takibi)
- [x] `Uye` sınıfı yazıldı (üye bilgileri, ödünç listesi)
- [x] `Kutuphane` sınıfı yazıldı (tüm iş mantığı)
- [x] `arayuz.py` modülü yazıldı (terminal menüsü)
- [x] `logger.py` modülü yazıldı (log dosyası)
- [x] `main.py` giriş noktası hazırlandı
- [x] Örnek verilerle sistem test edildi
- [x] Rapor oluşturma özelliği eklendi
- [x] Tüm belgeler hazırlandı

## Devam Eden / Planlanan İşler

- [ ] Veri kalıcılığı: JSON dosyasına kayıt/yükleme (opsiyonel iyileştirme)
- [ ] Gecikmiş iade uyarısı (opsiyonel iyileştirme)

## Karşılaşılan Problemler

- Üye silme işleminde, üyenin iade etmediği kitapların kontrolü gerekiyordu. Bu durum `uye_sil()` metoduna eklendi.
- `src/` klasörünün paket olarak tanınması için `__init__.py` dosyası eklenmesi gerekti.

## Sonraki Adımlar

- Proje belgeleri tamamlandı.
- Final teslimi için `outputs/rapor.txt` oluşturulacak.
