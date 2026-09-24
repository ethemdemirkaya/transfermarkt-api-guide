## 14. Kulüp Detaylarını Getirme

* **Açıklama:** Transfermarkt'ın yeni nesil API'si üzerinden bir veya birden fazla kulübün (veya milli takımın) detaylı bilgilerini döndürür. Yanıt; kısa ad, kısaltma, ülke, ana lig, bağlı olduğu kuruluşun adresi ve renkleri, kadro büyüklüğü, yaş ortalaması, toplam ve ortalama piyasa değeri ile geçmiş logo görsellerini içerir. Diğer endpoint'lerden elde edilen kulüp ID'lerini isim ve logoya dönüştürmek için idealdir.
* **Method:** `GET`
* **Endpoint URL:** `/clubs?ids[]={club_id}&ids[]={club_id}...`
* **Örnek Tam URL:** `https://tmapi.transfermarkt.technology/clubs?ids[]=3262&ids[]=610`

### Parametreler

#### Path Parametreleri

Bu endpoint için path parametresi bulunmamaktadır.

#### Query Parametreleri

| Parametre | Tip      | Zorunluluk  | Açıklama                                                                                    |
|:--------- |:-------- |:----------- |:------------------------------------------------------------------------------------------- |
| `ids[]`   | `string` | **Zorunlu** | Kulübün Transfermarkt ID'si. Birden fazla kulüp için parametre tekrarlanır.                 |

### Örnek İstek (`cURL`)

```bash
curl -g -X GET "https://tmapi.transfermarkt.technology/clubs?ids[]=3262&ids[]=610"
```

### Başarılı Yanıt Örneği (`200 OK`)

Örnek yanıt kısaltılmıştır.

```json
{
  "success": true,
  "message": "OK",
  "data": [
    {
      "id": "610",
      "name": "Ajax Amsterdam",
      "baseDetails": {
        "shortName": "Ajax",
        "abbreviation": "AJA",
        "isNationalTeam": false,
        "countryId": 122,
        "mainClubId": "610",
        "primaryCompetitionId": "NL1",
        "superiorClubId": 293,
        "superiorClub": {
          "id": "293",
          "name": "AFC Ajax Amsterdam",
          "location": {
            "countryId": 122,
            "street": "Johan Cruijff Boulevard 1",
            "postcode": "1100 DL",
            "city": "Amsterdam",
            "latitude": 52.373079696011,
            "longitude": 4.8924531787634
          },
          "colors": { "firstColor": "#FF0000", "secondColor": "#FFFFFF", "thirdColor": "" }
        }
      },
      "squadDetails": {
        "squadSize": 28,
        "averageAge": 26.32,
        "averageAgeDisplay": "26.3",
        "averageMarketValue": { "value": 8167857, "currency": "EUR", "compact": { "prefix": "€", "content": "8.17", "suffix": "M" }, "determined": "2026-09-24" },
        "acquisitionValue": { "value": 90650000, "currency": "EUR", "compact": { "prefix": "€", "content": "90.65", "suffix": "M" }, "determined": "2026-09-24" },
        "top18PlayersMarketValue": { "value": 205500000, "currency": "EUR", "compact": { "prefix": "€", "content": "205.50", "suffix": "M" }, "determined": "2026-09-24" },
        "top18SharePercentage": { "value": 89.86, "display": "89,9 %" },
        "currentMarketValue": { "value": 228700000, "currency": "EUR", "compact": { "prefix": "€", "content": "228.70", "suffix": "M" }, "determined": "2026-09-24" }
      },
      "preferences": { "themeId": 0, "clubCode": "AJX" },
      "relativeUrl": "/ajax-amsterdam/startseite/verein/610",
      "isSpecialClub": false,
      "historical": {
        "names": [],
        "images": [
          { "url": "https://img.a.transfermarkt.technology/wappen/big/610.png?lm=1789459204", "name": "610.png", "seasonId": 0 }
        ]
      },
      "identifier": "Ajax Amsterdam (610)",
      "crestUrl": "https://img.a.transfermarkt.technology/wappen/big/610.png?lm=1789459204"
    }
  ]
}
```

*(Not: Piyasa değerleri sürekli güncellenir; örnekteki değerler 24.09.2026 tarihlidir.)*

### Yanıt Verisi Açıklaması

#### Kulüp Objesi

| Değişken Adı    | Tip       | Açıklama                                                                          | Örnek Değer                               |
|:--------------- |:--------- |:--------------------------------------------------------------------------------- |:----------------------------------------- |
| `id`            | `string`  | Kulübün Transfermarkt ID'si.                                                      | `"610"`                                   |
| `name`          | `string`  | Kulübün tam adı.                                                                  | `"Ajax Amsterdam"`                        |
| `baseDetails`   | `object`  | Temel bilgiler. Aşağıda detaylandırılmıştır.                                      | `{...}`                                   |
| `squadDetails`  | `object`  | Kadro istatistikleri. Aşağıda detaylandırılmıştır.                                | `{...}`                                   |
| `relativeUrl`   | `string`  | Kulübün profil sayfasına giden göreceli link.                                     | `"/ajax-amsterdam/startseite/verein/610"` |
| `crestUrl`      | `string`  | Güncel logonun (milli takımlarda bayrağın) tam URL'si.                            | `"https://img.a.transfermarkt..."`        |
| `historical`    | `object`  | Geçmiş isimler (`names`) ve sezonlara göre geçmiş logolar (`images`).             | `{...}`                                   |
| `identifier`    | `string`  | `"Ad (ID)"` formatında tanımlayıcı.                                               | `"Ajax Amsterdam (610)"`                  |
| `preferences`   | `object`  | Tema ID'si ve kulüp kodu.                                                         | `{ "clubCode": "AJX" }`                   |
| `metadata`      | `object`  | Kaydın oluşturulma/güncellenme zamanı.                                            | `{ "updated": "2024-04-30T..." }`         |

---

#### `baseDetails` Objesi

| Değişken Adı           | Tip       | Açıklama                                                                                  | Örnek Değer   |
|:---------------------- |:--------- |:----------------------------------------------------------------------------------------- |:------------- |
| `shortName`            | `string`  | Kısa ad.                                                                                  | `"Ajax"`      |
| `abbreviation`         | `string`  | Üç harfli kısaltma.                                                                       | `"AJA"`       |
| `isNationalTeam`       | `boolean` | Milli takım olup olmadığı.                                                                | `false`       |
| `countryId`            | `number`  | Ülke ID'si.                                                                               | `122`         |
| `primaryCompetitionId` | `string`  | Takımın ana müsabakasının kodu.                                                           | `"NL1"`       |
| `superiorClub`         | `object`  | Bağlı olduğu üst kuruluş (kulüp derneği veya federasyon); adres, koordinat ve kulüp renkleri (`colors`). | `{...}` |

---

#### `squadDetails` Objesi

| Değişken Adı              | Tip      | Açıklama                                                                 |
|:------------------------- |:-------- |:------------------------------------------------------------------------ |
| `squadSize`               | `number` | Kadrodaki oyuncu sayısı.                                                 |
| `averageAge`              | `number` | Kadronun yaş ortalaması.                                                 |
| `currentMarketValue`      | `object` | Kadronun toplam piyasa değeri.                                           |
| `averageMarketValue`      | `object` | Oyuncu başına ortalama piyasa değeri.                                    |
| `top18PlayersMarketValue` | `object` | En değerli 18 oyuncunun toplam değeri.                                   |
| `top18SharePercentage`    | `object` | En değerli 18 oyuncunun toplam değer içindeki payı (yüzde).              |
| `acquisitionValue`        | `object` | Kadronun toplam transfer maliyeti.                                       |

Değer objeleri [Oyuncu Detayları](08-player-details.md) dökümanındaki `marketValueDetails` ile aynı yapıdadır (`value`, `currency`, `compact`, `determined`).

### Veriye Erişim Örneği (JavaScript)

```javascript
async function getClubs(clubIds) {
  const query = clubIds.map(id => `ids[]=${id}`).join('&');
  const response = await fetch(`https://tmapi.transfermarkt.technology/clubs?${query}`);
  const { data } = await response.json();

  data.forEach(club => {
    const mv = club.squadDetails.currentMarketValue.compact;
    console.log(
      `${club.name} (${club.baseDetails.abbreviation}) | Lig: ${club.baseDetails.primaryCompetitionId} | ` +
      `Kadro: ${club.squadDetails.squadSize} | Yaş ort.: ${club.squadDetails.averageAgeDisplay} | ` +
      `Değer: ${mv.prefix}${mv.content}${mv.suffix}`
    );
  });
}

// Almanya Milli Takımı (3262) ve Ajax (610)
getClubs(['3262', '610']);
```

### Hata Yanıtı Örneği

Geçersiz ID'ler hata döndürmez, yanıttan çıkarılır. Hiçbir ID bulunamazsa `data` boş dizi olur:

```json
{ "success": true, "message": "OK", "data": [] }
```

> **Not:** Tek kulüp için `/clubs/{club_id}` adresi mevcut değildir (`404`). Tek kulüp için de `ids[]` kullanın.
