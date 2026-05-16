# Kullanım Senaryoları

**Proje:** Kütüphane Yönetim Sistemi

---

## Senaryo 1: Yeni Kitap Ekleme

**Aktör:** Kütüphane Görevlisi (Yönetici)  
**Amaç:** Sisteme yeni bir kitap kaydı açmak

**Adımlar:**
1. Ana menüden "1. Kitap İşlemleri" seçilir.
2. Alt menüden "1. Kitap Ekle" seçilir.
3. ISBN, başlık, yazar adı, yayın yılı ve kopya sayısı girilir.
4. Sistem kitabı kaydeder ve onay mesajı gösterir.

**Başarı Koşulu:** Kitap `kitaplar` sözlüğüne eklenir, log kaydı oluşur.  
**Hata Koşulu:** Aynı ISBN zaten varsa "zaten kayıtlı" hatası verilir.

---

## Senaryo 2: Kitap Ödünç Verme

**Aktör:** Kütüphane Görevlisi  
**Amaç:** Kayıtlı bir üyeye kitap ödünç vermek

**Adımlar:**
1. Ana menüden "3. Ödünç / İade" seçilir.
2. "1. Kitap Ödünç Ver" seçilir.
3. Üye ID ve kitap ISBN girilir.
4. Sistem üyeyi ve kitabı doğrular, stok kontrolü yapar.
5. Ödünç işlemi gerçekleştirilir.

**Başarı Koşulu:** Kitabın mevcut kopyası azalır, üyenin ödünç listesine eklenir.  
**Hata Koşulu:** Üye yoksa, kitap yoksa veya mevcut kopya sıfırsa işlem reddedilir.

---

## Senaryo 3: Kitap İade Alma

**Aktör:** Kütüphane Görevlisi  
**Amaç:** Üyeden ödünç kitabı geri almak

**Adımlar:**
1. "3. Ödünç / İade" → "2. Kitap İade Al" seçilir.
2. Üye ID ve kitap ISBN girilir.
3. Sistem üyenin ödünç listesinde bu kitabın olduğunu doğrular.
4. İade işlemi gerçekleştirilir.

**Başarı Koşulu:** Kitabın mevcut kopyası artar, üyenin ödünç listesinden çıkarılır.  
**Hata Koşulu:** Üyede bu kitap kayıtlı değilse işlem reddedilir.

---

## Senaryo 4: Kitap Arama

**Aktör:** Kütüphane Görevlisi  
**Amaç:** Başlık veya yazar adına göre kitap bulmak

**Adımlar:**
1. "1. Kitap İşlemleri" → "3. Kitap Ara" seçilir.
2. Arama terimi girilir (örn: "Atay" veya "Tutunamayanlar").
3. Sistem eşleşen kitapları listeler.

**Başarı Koşulu:** Eşleşen kitaplar ekranda gösterilir.  
**Hata Koşulu:** Eşleşme yoksa "Sonuç bulunamadı" mesajı verilir.

---

## Senaryo 5: Rapor Oluşturma

**Aktör:** Kütüphane Görevlisi  
**Amaç:** Sistemin anlık durumunu dosyaya kaydetmek

**Adımlar:**
1. Ana menüden "4. Rapor Oluştur" seçilir.
2. Sistem toplam kitap, üye ve ödünçteki kitap sayısını hesaplar.
3. `outputs/rapor.txt` dosyasına yazar.

**Başarı Koşulu:** Rapor dosyası oluşturulur ve yolu ekranda gösterilir.
