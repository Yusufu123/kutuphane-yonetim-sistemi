# Yapay Zeka Kullanım Yöntemleri ve Senaryoları

**Proje:** Kütüphane Yönetim Sistemi

---

## 1. Kullanılan Yöntemler

### 1.1 Kod İskeleti Oluşturma
Sınıfların (`Kitap`, `Uye`, `Kutuphane`) temel metod iskeletleri için Claude'a şu türde istemler verilmiştir:

> "Python'da bir kütüphane yönetim sistemi için Kitap sınıfı yaz. ISBN, başlık, yazar, yıl ve kopya sayısı olsun. Ödünç verme ve iade metodları da ekle."

### 1.2 Belge Taslakları
`docs/` klasöründeki belgeler için şablon başlıkları ve içerik taslakları yapay zeka yardımıyla oluşturulmuştur.

### 1.3 Hata Ayıklama
`src/` paketinin tanınmaması gibi teknik sorunların çözümünde yapay zekadan öneri alınmıştır.

---

## 2. Örnek İstem–Yanıt Senaryoları

### Senaryo A: Üye silme kısıtı

**İstem:**
> "Üye silme işleminde, üyenin iade etmediği kitapları varsa silme işlemini engelle."

**Yapay zekanın önerisi:**
```python
def uye_sil(self, uye_id):
    uye = self.uyeler[uye_id]
    if uye.odunc_listesi:
        print("HATA: Üyenin iade etmediği kitaplar var.")
        return False
    ...
```

**Kullanım:** Bu öneri incelendi, projeye uyarlandı ve `kutuphane.py` içinde kullanıldı.

---

### Senaryo B: Log modülü

**İstem:**
> "Her işlemi tarih ve saatle birlikte bir log dosyasına yazan basit bir Python fonksiyonu yaz."

**Yapay zekanın önerisi:** `datetime.now()` ve dosyaya yazma örneği verildi.

**Kullanım:** `src/logger.py` dosyasına entegre edildi.

---

## 3. Değerlendirme

Yapay zeka araçları, geliştirme sürecini hızlandırmak ve olası hataları önceden görmek açısından faydalı olmuştur. Ancak tüm çıktılar eleştirel bir bakışla değerlendirilmiş; projeye uymayan öneriler alınmamıştır.
