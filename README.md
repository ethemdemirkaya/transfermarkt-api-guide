# Gayriresmi Transfermarkt API Dökümantasyonu

Bu proje, [Transfermarkt](https://www.transfermarkt.com.tr) web sitesi tarafından kullanılan ve herkese açık olmayan (private) API endpoint'lerini dökümante etmeyi amaçlamaktadır.

Bu dökümantasyon, geliştiricilerin ve veri meraklılarının Transfermarkt verilerine programatik olarak nasıl erişebileceğini anlamalarına yardımcı olmak için **eğitim ve araştırma amacıyla** oluşturulmuştur.

---

## 🚨 ÖNEMLİ UYARI VE SORUMLULUK REDDİ 🚨

> Bu projeyi kullanmadan önce aşağıdaki maddeleri dikkatlice okumanız ve anlamanız çok önemlidir.

* **GAYRİRESMİ PROJE:** Bu projenin Transfermarkt GmbH & Co. KG ile **hiçbir resmi ilişkisi yoktur.** Bu, topluluk tarafından yürütülen bir projedir.
* **KULLANIM KOŞULLARI İHLALİ:** Bu API'ların kullanılması, Transfermarkt'ın [Kullanım Koşulları](https://www.transfermarkt.com.tr/mvc/main/index/datenschutz)'nı **ihlal edebilir.** Siteyi otomatik yöntemlerle taramak (scraping) veya izinsiz API kullanmak genellikle hizmet sözleşmelerine aykırıdır.
* **TÜM SORUMLULUK KULLANICIYA AİTTİR:** Bu API'ları kullanmaktan doğabilecek her türlü yasal, etik veya teknik sorumluluk tamamen size aittir. Bu projeyi kullanarak bu şartı kabul etmiş olursunuz.
* **DEĞİŞKENLİK RİSKİ:** Bunlar özel API'lar olduğu için, Transfermarkt URL yapılarını, yanıt formatlarını veya erişim yöntemlerini **herhangi bir zamanda, haber vermeksizin değiştirebilir veya tamamen kapatabilir.** Bu dökümantasyona dayalı projeleriniz aniden çalışmayı durdurabilir.
* **SUNUCU YÜKÜ:** Lütfen Transfermarkt sunucularına **aşırı yük bindirmeyin.** Sorumsuz ve yoğun kullanım, sitenin hizmet kalitesini düşürebilir. Her zaman sorumlu kullanım ilkelerine uyun.
* **VERİ MÜLKİYETİ:** Bu API'lar aracılığıyla erişilen tüm verilerin, logoların ve isimlerin mülkiyeti ve telif hakları **tamamen Transfermarkt'a aittir.**

---

## İçindekiler

1. [Lige Göre Takım Listesi](#1-lige-göre-takım-listesi-getirme)
2. [Takımın Son Maç Dizilişi](#2-takımın-son-maç-dizilişini-getirme)
3. [Takım Kadrosu Listeleme](#3-takıma-göre-oyuncu-listesi-getirme)
4. [Oyuncunun Müsabakalara Göre Performansı](#4-oyuncunun-müsabakalara-göre-performansı)
5. [Oyuncunun Kulüplere Göre Performansı](#5-oyuncunun-kulüplere-göre-performansı)
6. [Oyuncunun Son Maçlarını Listeleme](#6-oyuncunun-son-maçlarını-listeleme)
7. [Oyuncunun Gelecek Maçlarını Listeleme](#7-oyuncunun-gelecek-maçlarını-listeleme)
8. [Oyuncunun Detaylı Bilgilerini Getirme](#8-oyuncunun-detaylı-bilgilerini-getirme)
9. [Oyuncunun Sezonluk Performans Detayları](#9-oyuncunun-sezonluk-performans-detayları)
10. [Takımın Gelecek Maçlarını Listeleme](#10-takımın-gelecek-maçlarını-listeleme)
11. [Takımın Son Maçlarını Listeleme](#11-takımın-son-maçlarını-listeleme)
12. [Oyuncunun Sorare Kart Bilgileri](#12-oyuncunun-sorare-kart-bilgilerini-getirme)

## Sorumlu Kullanım İlkeleri

Transfermarkt'a ve topluluğa saygı göstermek için lütfen aşağıdaki kurallara uyun:

* **Rate Limiting (İstek Sınırı):** Asla çok kısa sürede çok fazla istek göndermeyin. İstekleriniz arasına makul bekleme süreleri ekleyin (örneğin saniyede en fazla 1 istek).
* **Caching (Önbellekleme):** Aynı veriyi tekrar tekrar çekmek yerine, sonuçları belirli bir süre için yerel olarak (cihazınızda veya sunucunuzda) önbelleğe alın. Özellikle takım listesi veya oyuncu profili gibi sık değişmeyen veriler için bu çok önemlidir.
* **User-Agent Belirtin:** İsteklerinizin `header` kısmında kim olduğunuzu veya projenizi belirten bir `User-Agent` gönderin. Bu, şeffaflık sağlar ve olası bir sorunda sizinle iletişime geçilmesini kolaylaştırır. Örnek: `User-Agent: MyAwesomeFootballApp/1.0 (https://github.com/kullanici-adiniz/proje-adiniz)`.
* **Sadece Gerekli Veriyi Çekin:** İhtiyacınız olmayan endpoint'lere veya verilere istek atmaktan kaçının.

## API Dökümantasyonu

Her bir endpoint'in detaylı açıklaması, parametreleri, örnek yanıtları ve kullanım senaryoları ilgili markdown dosyalarında bulunmaktadır.

### 1. Lige Göre Takım Listesi Getirme

Bu endpoint, bir ligdeki tüm takımların temel bilgilerini döndürür.

> Detaylar için `01-lig-gore-takim-listesi.md` dosyasına bakınız.

### 2. Takımın Son Maç Dizilişini Getirme

Bir takımın oynadığı son maçın kadrosunu, taktiğini ve maç içi olaylarını döndürür.

> Detaylar için `02-takim-son-mac-dizilisi.md` dosyasına bakınız.

### 3. Takıma Göre Oyuncu Listesi Getirme

Bir takımın güncel kadrosundaki tüm oyuncuları listeler.

> Detaylar için `03-takim-kadrosu-listeleme.md` dosyasına bakınız.

### 4. Oyuncunun Müsabakalara Göre Performansı

Bir oyuncunun kariyerindeki tüm istatistiklerini turnuva bazında gruplayarak sunar.

> Detaylar için `04-oyuncu-performansi-musabakaya-gore.md` dosyasına bakınız.

### 5. Oyuncunun Kulüplere Göre Performansı

Bir oyuncunun kariyerindeki tüm istatistiklerini kulüp bazında gruplayarak sunar.

> Detaylar için `05-oyuncu-performansi-kuluplere-gore.md` dosyasına bakınız.

### 6. Oyuncunun Son Maçlarını Listeleme

Bir oyuncunun oynadığı son maçları listeler.

> Detaylar için `06-oyuncu-son-maclari-listeleme.md` dosyasına bakınız.

### 7. Oyuncunun Gelecek Maçlarını Listeleme

Bir oyuncunun sıradaki maçlarını (fikstürünü) listeler.

> Detaylar için `07-oyuncu-gelecek-maclari-listeleme.md` dosyasına bakınız.

### 8. Oyuncunun Detaylı Bilgilerini Getirme

Bir veya daha fazla oyuncunun modern bir API üzerinden detaylı profil bilgilerini döndürür.

> Detaylar için `08-oyuncu-detayli-bilgileri-getirme.md` dosyasına bakınız.

### 9. Oyuncunun Sezonluk Performans Detayları

Bir oyuncunun performansını sezon ve müsabaka bazında ayrıntılı olarak listeler.

> Detaylar için `09-oyuncu-sezonluk-performans-detaylari.md` dosyasına bakınız.

### 10. Takımın Gelecek Maçlarını Listeleme

Bir takımın sıradaki maçlarını (fikstürünü) listeler.

> Detaylar için `10-takim-gelecek-maclari-listeleme.md` dosyasına bakınız.

### 11. Takımın Son Maçlarını Listeleme

Bir takımın oynadığı son maçları listeler.

> Detaylar için `11-takim-son-maclari-listeleme.md` dosyasına bakınız.

### 12. Oyuncunun Sorare Kart Bilgilerini Getirme

Bir oyuncunun [Sorare](https://sorare.com) fantazi futbol platformundaki kart bilgilerini ve özel istatistiklerini döndürür.

> Detaylar için `12-oyuncu-sorare-kart-bilgileri.md` dosyasına bakınız.

## Katkıda Bulunma

Yeni endpoint'ler keşfederseniz, mevcut dökümanda bir hata bulursanız veya iyileştirmeler önermek isterseniz lütfen bir "Issue" açın veya "Pull Request" gönderin. Katkılarınız memnuniyetle karşılanır.

## Lisans

Bu proje [MIT Lisansı](LICENSE) altında lisanslanmıştır. Bu, kodu istediğiniz gibi kullanabileceğiniz anlamına gelir ancak proje hiçbir garanti sunmaz ve yazarları herhangi bir zarardan sorumlu tutulamaz.
