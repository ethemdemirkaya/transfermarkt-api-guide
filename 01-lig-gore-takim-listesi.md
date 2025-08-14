# Transfermarkt API Dökümantasyonu

Bu döküman, Transfermarkt web sitesi üzerinden veri çekmek için kullanılabilecek gayriresmi (unofficial) API endpoint'lerini açıklamaktadır.

---

## 1. Lige Göre Takım Listesi Getirme

* **Açıklama:** Belirtilen lig koduna (`TR1` gibi) ait takımların temel bilgilerini (ID, isim, link) bir liste olarak döndürür. Bu endpoint, genellikle bir ligdeki takımları listeleyip başka API çağrıları için takım ID'si elde etmek amacıyla kullanılır.
* **Method:** `GET`
* **Endpoint URL:** `/quickselect/teams/{lig_kodu}`
* **Örnek Tam URL:** `https://www.transfermarkt.com.tr/quickselect/teams/TR1`

### Parametreler

#### Path Parametreleri

| Parametre  | Tip      | Zorunluluk  | Açıklama                                                                                                    |
|:---------- |:-------- |:----------- |:----------------------------------------------------------------------------------------------------------- |
| `lig_kodu` | `string` | **Zorunlu** | Takımları listelenecek olan ligin kodu. Örnek: `TR1` (Türkiye Süper Lig), `GB1` (İngiltere Premier League). |

#### Query Parametreleri

Bu endpoint için query parametresi bulunmamaktadır.

### Örnek İstek (`cURL`)

```bash
curl -X GET "https://www.transfermarkt.com.tr/quickselect/teams/TR1"
```

### Başarılı Yanıt Örneği (`200 OK`)

Endpoint, başarılı bir istek sonucunda bir JSON dizisi (array) döndürür. Dizideki her bir obje bir takımı temsil eder.

```json
[
  {
    "id": 141,
    "name": "Galatasaray SK",
    "link": "/galatasaray-sk/startseite/verein/141"
  },
  {
    "id": 36,
    "name": "Fenerbahçe SK",
    "link": "/fenerbahce-sk/startseite/verein/36"
  },
  {
    "id": 114,
    "name": "Beşiktaş JK",
    "link": "/besiktas-jk/startseite/verein/114"
  },
  {
    "id": 449,
    "name": "Trabzonspor",
    "link": "/trabzonspor/startseite/verein/449"
  }
]
```

### Yanıt Verisi Açıklaması

Dönen JSON dizisindeki her bir obje aşağıdaki alanları içerir:

| Değişken Adı | Tip      | Açıklama                                                                                                                                                    | Örnek Değer                               |
|:------------ |:-------- |:----------------------------------------------------------------------------------------------------------------------------------------------------------- |:----------------------------------------- |
| `id`         | `number` | Takımın Transfermarkt sistemindeki benzersiz ID'sidir. Bu ID, takıma özel diğer verileri (kadro, maçlar vb.) çekmek için kullanılır.                        | `141`                                     |
| `name`       | `string` | Takımın tam adıdır.                                                                                                                                         | `"Galatasaray SK"`                        |
| `link`       | `string` | Takımın Transfermarkt web sitesindeki profil sayfasına yönlendiren göreceli (relative) URL yoludur. Ana domain ile birleştirilerek tam URL oluşturulabilir. | `"/galatasaray-sk/startseite/verein/141"` |

#### Veriye Erişim Örneği (JavaScript)

Aşağıdaki JavaScript kodu, dönen yanıt içerisinden ilk takımın adını ve ID'sini nasıl alacağınızı gösterir.

```javascript
const responseData = [
  {
    "id": 141,
    "name": "Galatasaray SK",
    "link": "/galatasaray-sk/startseite/verein/141"
  },
  {
    "id": 36,
    "name": "Fenerbahçe SK",
    "link": "/fenerbahce-sk/startseite/verein/36"
  }
];

// Tüm takımları listelemek için döngü
responseData.forEach(team => {
  console.log(`Takım Adı: ${team.name}, Takım ID: ${team.id}`);
});

// Çıktı:
// Takım Adı: Galatasaray SK, Takım ID: 141
// Takım Adı: Fenerbahçe SK, Takım ID: 36
```

### Hata Yanıtı Örneği

Geçersiz bir `lig_kodu` gönderildiğinde veya ilgili ligde takım bulunmadığında, API genellikle boş bir JSON dizisi döndürür.

**Geçersiz lig kodu (`XYZ`) için yanıt:** `200 OK`

```json
[]
```
