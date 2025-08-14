## 10. Takımın Gelecek Maçlarını Listeleme

* **Açıklama:** Belirtilen takım ID'sine göre, takımın sıradaki maçlarının (fikstürünün) bir listesini döndürür. Yanıt yapısı, oyuncu bazlı "son/gelecek maçlar" endpoint'leri ile tamamen aynıdır: maçlarda yer alan tüm takımların bilgilerini içeren bir `teams` objesi ve maçların listesini içeren bir `matches` dizisinden oluşur.
* **Method:** `GET`
* **Endpoint URL:** `/ceapi/nextMatches/team/{team_id}`
* **Örnek Tam URL:** `https://www.transfermarkt.com.tr/ceapi/nextMatches/team/36?limit=25`

### Parametreler

#### Path Parametreleri

| Parametre | Tip      | Zorunluluk  | Açıklama                                                                        |
|:--------- |:-------- |:----------- |:------------------------------------------------------------------------------- |
| `team_id` | `string` | **Zorunlu** | Fikstürü listelenecek takımın Transfermarkt ID'si. (Örn: `36` Fenerbahçe için). |

#### Query Parametreleri

| Parametre | Tip      | Zorunluluk   | Açıklama                                                                                   |
|:--------- |:-------- |:------------ |:------------------------------------------------------------------------------------------ |
| `limit`   | `number` | İsteğe Bağlı | Döndürülecek maksimum maç sayısı. Belirtilmezse varsayılan bir değer kullanılır (örn: 25). |

### Örnek İstek (`cURL`)

```bash
curl -X GET "https://www.transfermarkt.com.tr/ceapi/nextMatches/team/36?limit=5"
```

### Başarılı Yanıt Örneği (`200 OK`)

Endpoint, başarılı bir istek sonucunda `teams` ve `matches` anahtarlarına sahip bir JSON objesi döndürür.

```json
{
  "teams": {
    "1467": { "name": "Göztepe", "link": "/goztepe/startseite/verein/1467" },
    "36": { "name": "Fenerbahçe", "link": "/fenerbahce-istanbul/startseite/verein/36" },
    "294": { "name": "Benfica", "link": "/benfica-lissabon/startseite/verein/294" }
  },
  "matches": [
    {
      "competition": { "id": "TR1", "label": "Süper Lig" },
      "id": 4646352,
      "match": {
        "away": 36,
        "home": 1467,
        "link": "/spielbericht/index/spielbericht/4646352",
        "result": "-:-",
        "state": "Fixture",
        "time": 1755369000
      }
    },
    {
      "competition": { "id": "CLQ", "label": "Şampiyonlar Ligi Elemeleri" },
      "id": 4697252,
      "match": {
        "away": 294,
        "home": 36,
        "link": "/spielbericht/index/spielbericht/4697252",
        "result": "-:-",
        "state": "Fixture",
        "time": 1755716400
      }
    }
  ]
}
```

### Yanıt Verisi Açıklaması

Bu endpoint'in yanıt yapısı, `07-oyuncu-gelecek-maclari-listeleme.md` dökümanında açıklanan yapı ile tamamen aynıdır.

#### Ana Obje Yapısı

| Değişken Adı | Tip      | Açıklama                                                                               |
|:------------ |:-------- |:-------------------------------------------------------------------------------------- |
| `teams`      | `object` | Anahtar olarak takım ID'sini, değer olarak takım bilgilerini içeren bir arama tablosu. |
| `matches`    | `array`  | Takımın gelecek maçlarını içeren objelerin listesi.                                    |

---

#### `match` Objesi (Maç Detayları)

| Değişken Adı    | Tip      | Açıklama                                                                            | Örnek Değer               |
|:--------------- |:-------- |:----------------------------------------------------------------------------------- |:------------------------- |
| `home` / `away` | `number` | Takım ID'leri. `teams` objesinden detayları alınır.                                 | `36`                      |
| `result`        | `string` | Maç henüz oynanmadığı için her zaman `"-:-"` değerini alır.                         | `"-:-"`                   |
| `state`         | `string` | Maçın durumu. Gelecek maçlar için genellikle `"Fixture"` (Planlandı) değerini alır. | `"Fixture"`               |
| `time`          | `number` | Maçın başlangıç zamanını belirten **Unix timestamp** (saniye cinsinden).            | `1755369000`              |
| `link`          | `string` | Maçın rapor sayfasına giden göreceli link.                                          | `"/spielbericht/..."`     |
| `group`         | `string` | Maçın hangi turda veya grupta olduğunu belirtir. (örn: "Play-Off turu ilk maç")     | `"Play-Off turu ilk maç"` |

### Veriye Erişim Örneği (JavaScript)

Aşağıdaki kod, bir takımın fikstürünü nasıl alacağınızı gösterir.

```javascript
async function getTeamFixture(teamId, limit = 10) {
  try {
    const response = await fetch(`https://www.transfermarkt.com.tr/ceapi/nextMatches/team/${teamId}?limit=${limit}`);
    const data = await response.json();

    const teamsLookup = data.teams;
    const matches = data.matches;

    const teamName = teamsLookup[teamId].name;
    console.log(`--- ${teamName} | Gelecek Maçlar ---`);

    matches.forEach(m => {
      const homeTeam = teamsLookup[m.match.home].name;
      const awayTeam = teamsLookup[m.match.away].name;

      const matchDate = new Date(m.match.time * 1000).toLocaleString('tr-TR', {
        year: 'numeric', month: 'long', day: 'numeric', hour: '2-digit', minute: '2-digit'
      });

      console.log(
        `${matchDate} | ${m.competition.label} | ${homeTeam} vs ${awayTeam}`
      );
    });

  } catch (error) {
    console.error("Veri alınırken hata oluştu:", error);
  }
}

// Fenerbahçe (ID: 36) için gelecek 5 maçı listele
getTeamFixture('36', 5);

// Beklenen Çıktı Örneği:
// --- Fenerbahçe | Gelecek Maçlar ---
// 16 Ağustos 2025 21:30 | Süper Lig | Göztepe vs Fenerbahçe
// 20 Ağustos 2025 22:00 | Şampiyonlar Ligi Elemeleri | Fenerbahçe vs Benfica
// 24 Ağustos 2025 22:00 | Süper Lig | Fenerbahçe vs Kocaelispor
// 27 Ağustos 2025 22:00 | Şampiyonlar Ligi Elemeleri | Benfica vs Fenerbahçe
// 31 Ağustos 2025 22:00 | Süper Lig | Gençlerbirliği vs Fenerbahçe
```

### Hata Yanıtı Örneği

Geçersiz bir `team_id` gönderildiğinde veya takımın planlanmış bir maçı olmadığında, API `404 Not Found` durumu veya boş bir `matches` dizisi döndürebilir.
