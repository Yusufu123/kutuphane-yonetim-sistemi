# Rol ve Yetki Matrisi

**Proje:** Kütüphane Yönetim Sistemi

---

## Kullanıcı Rolleri

Bu sistemde şu an için tek bir aktif rol vardır: **Yönetici**.  
İleride geliştirme yapılırsa "Üye" rolü de aktif hale getirilebilir.

---

## Yetki Tablosu

| İşlem | Yönetici | Üye (Planlı) |
|-------|----------|--------------|
| Kitap ekleme | ✅ | ❌ |
| Kitap silme | ✅ | ❌ |
| Kitap arama | ✅ | ✅ |
| Tüm kitapları listeleme | ✅ | ✅ |
| Üye ekleme | ✅ | ❌ |
| Üye silme | ✅ | ❌ |
| Tüm üyeleri listeleme | ✅ | ❌ |
| Ödünç verme | ✅ | ❌ |
| İade alma | ✅ | ❌ |
| Kendi ödünç geçmişini görme | ✅ | ✅ |
| Rapor oluşturma | ✅ | ❌ |

---

## Yetki Kısıtı Uygulama Biçimi

Mevcut sürümde sistem **tek kullanıcılı** çalıştığından giriş doğrulaması yoktur.  
Gelecekte kullanıcı adı/şifre ile giriş eklenerek bu matris uygulamaya geçirilecektir.
