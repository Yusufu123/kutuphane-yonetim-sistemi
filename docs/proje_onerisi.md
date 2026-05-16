# Proje Önerisi

## Proje Adı
Kütüphane Yönetim Sistemi

## Geliştirici
**Ad Soyad:** Yusuf Kıvrık  
**Öğrenci No:** 202407105021  
**Tarih:** 2025

---

## Proje Fikri

Bu proje, küçük bir kütüphanenin kitap ve üye yönetimini terminal üzerinden gerçekleştirmesini sağlayan bir Python uygulamasıdır. Sistem; kitap ekleme/silme/arama, üye kaydı ve ödünç/iade işlemlerini destekler.

## Hedef Kullanıcılar
- Kütüphane görevlileri (yönetici rolü)
- Kayıtlı kütüphane üyeleri

## Kullanıcı Rolleri ve Yetkileri

| Rol | Yetkiler |
|-----|----------|
| Yönetici | Kitap ekle/sil, üye ekle/sil, ödünç ver, iade al, rapor oluştur |
| Üye | (Gelecekte) kendi ödünç geçmişini görüntüleme |

> Mevcut sürümde sistem tek kullanıcılı (yönetici) olarak çalışmaktadır.

## Temel Gereksinimler

1. **Kitap yönetimi:** Sisteme kitap eklenebilmeli, silinebilmeli ve aranabilmelidir.
2. **Üye yönetimi:** Üye kaydı oluşturulabilmeli ve silinebilmelidir.
3. **Ödünç/iade:** Bir üye kitap ödünç alabilmeli ve iade edebilmelidir.
4. **Stok takibi:** Her kitabın kaç kopyasının mevcut olduğu takip edilmelidir.
5. **Log kaydı:** Tüm işlemler tarih ve saat bilgisiyle `logs/islemler.log` dosyasına yazılmalıdır.
6. **Rapor:** Sistem durumu `outputs/rapor.txt` dosyasına aktarılabilmelidir.

## Kullanılacak Python Özellikleri

- Sınıflar (OOP): `Kitap`, `Uye`, `Kutuphane`
- Modüler yapı: `src/` klasörü altında ayrı dosyalar
- Dosya işlemleri: log ve rapor yazma
- Listeler ve sözlükler: veri saklama
- Tarih modülü (`datetime`): işlem tarihleri

## Proje Hedefi

Dönem sonunda; çalışan, hatasız, modüler ve belgelenmiş bir Python uygulaması teslim etmek.
