## 11. Takımın Son Maçlarını Listeleme

* **Açıklama:** Belirtilen takım ID'sine göre, takımın oynadığı son maçların bir listesini döndürür. Yanıt yapısı, diğer maç listeleme endpoint'leri ile (oyuncu son/gelecek, takım gelecek) tamamen aynıdır.
* **Method:** `GET`
* **Endpoint URL:** `/ceapi/previousMatches/team/{team_id}`
* **Örnek Tam URL:** `https://www.transfermarkt.com.tr/ceapi/previousMatches/team/36?limit=25`

### Parametreler

#### Path Parametreleri

| Parametre | Tip      | Zorunluluk  | Açıklama                                                                       |
|:--------- |:-------- |:----------- |:------------------------------------------------------------------------------ |
| `team_id` | `string` | **Zorunlu** | Maçları listelenecek takımın Transfermarkt ID'si. (Örn: `36` Fenerbahçe için). |

#### Query Parametreleri

| Parametre | Tip      | Zorunluluk   | Açıklama                                                                                   |
|:--------- |:-------- |:------------ |:------------------------------------------------------------------------------------------ |
| `limit`   | `number` | İsteğe Bağlı | Döndürülecek maksimum maç sayısı. Belirtilmezse varsayılan bir değer kullanılır (örn: 25). |

### Örnek İstek (`cURL`)

```bash
curl -X GET "https://www.transfermarkt.com.tr/ceapi/previousMatches/team/36?limit=5"
```

### Başarılı Yanıt Örneği (`200 OK`)

Endpoint, başarılı bir istek sonucunda `teams` ve `matches` anahtarlarına sahip bir JSON objesi döndürür.

```json
{
  "teams": {
    "36": { "name": "Fenerbahçe", "link": "/fenerbahce-istanbul/startseite/verein/36" },
    "234": { "name": "Feyenoord", "link": "/feyenoord-rotterdam/startseite/verein/234" },
    "11282": { "name": "Alanyaspor", "link": "/alanyaspor/startseite/verein/11282" }
  },
  "matches": [
    {
      "competition": { "id": "CLQ", "label": "Şampiyonlar Ligi Elemeleri" },
      "id": 4676660,
      "match": {
        "away": 234,
        "home": 36,
        "link": "/spielbericht/index/spielbericht/4676660",
        "result": "5:2",
        "state": "Played",
        "time": 1755018000
      }
    },
    {
      "competition": { "id": "TR1", "label": "Süper Lig" },
      "id": 4646344,
      "match": {
        "away": 11282,
        "home": 36,
        "result": "-:-",
        "state": "Postponed",
        "time": 1754764200
      }
    }
  ]
}
```

### Yanıt Verisi Açıklaması

Bu endpoint'in yanıt yapısı, `10-takim-gelecek-maclari-listeleme.md` dökümanında açıklanan yapı ile tamamen aynıdır. Tek fark `match` objesi içindeki `state` ve `result` alanlarının değerleridir.

#### Ana Obje Yapısı

| Değişken Adı | Tip      | Açıklama                                                                               |
|:------------ |:-------- |:-------------------------------------------------------------------------------------- |
| `teams`      | `object` | Anahtar olarak takım ID'sini, değer olarak takım bilgilerini içeren bir arama tablosu. |
| `matches`    | `array`  | Takımın son maçlarını içeren objelerin listesi.                                        |

---

#### `match` Objesi (Maç Detayları)

| Değişken Adı      | Tip      | Açıklama                                                                          | Örnek Değer           |
|:----------------- |:-------- |:--------------------------------------------------------------------------------- |:--------------------- |
| `home` / `away`   | `number` | Takım ID'leri. `teams` objesinden detayları alınır.                               | `36`                  |
| `result`          | `string` | Maçın skoru. Ertelenmiş maçlar için `"-:-"` olabilir.                             | `"5:2"`               |
| `resultExtension` | `string` | Skorla ilgili ek bilgi, örn: `"PEN"` (penaltılar).                                | `"PEN"`               |
| `state`           | `string` | Maçın durumu. `Played` (Oynandı), `Postponed` (Ertelendi) gibi değerler alabilir. | `"Played"`            |
| `time`            | `number` | Maçın başlangıç zamanını belirten **Unix timestamp** (saniye cinsinden).          | `1755018000`          |
| `link`            | `string` | Maçın rapor sayfasına giden göreceli link.                                        | `"/spielbericht/..."` |

### Veriye Erişim Örneği (JavaScript)

Aşağıdaki kod, bir takımın son maçlarını nasıl alacağınızı gösterir.

```javascript
async function getTeamLastMatches(teamId, limit = 10) {
  try {
    const response = await fetch(`https://www.transfermarkt.com.tr/ceapi/previousMatches/team/${teamId}?limit=${limit}`);
    const data = await response.json();

    const teamsLookup = data.teams;
    const matches = data.matches;

    const teamName = teamsLookup[teamId].name;
    console.log(`--- ${teamName} | Son Maçlar ---`);

    matches.forEach(m => {
      const homeTeam = teamsLookup[m.match.home].name;
      const awayTeam = teamsLookup[m.match.away].name;

      const matchDate = new Date(m.match.time * 1000).toLocaleDateString('tr-TR');

      // Varsa penaltı gibi ek bilgiyi skora ekle
      const fullResult = m.match.resultExtension 
        ? `${m.match.result} (${m.match.resultExtension})` 
        : m.match.result;

      console.log(
        `${matchDate} | ${m.competition.label} | ${homeTeam} ${fullResult} ${awayTeam} (${m.match.state})`
      );
    });

  } catch (error) {
    console.error("Veri alınırken hata oluştu:", error);
  }
}

// Fenerbahçe (ID: 36) için son 5 maçı listele
getTeamLastMatches('36', 5);

// Beklenen Çıktı Örneği:
// --- Fenerbahçe | Son Maçlar ---
// 12.08.2025 | Şampiyonlar Ligi Elemeleri | Fenerbahçe 5:2 Feyenoord (Played)
// 10.08.2025 | Süper Lig | Fenerbahçe -:- Alanyaspor (Postponed)
// 07.08.2025 | Şampiyonlar Ligi Elemeleri | Feyenoord 2:1 Fenerbahçe (Played)
// 27.05.2025 | Süper Lig | Fenerbahçe 2:1 Konyaspor (Played)
// 22.05.2025 | Süper Lig | Hatayspor 4:2 Fenerbahçe (Played)
```

### Hata Yanıtı Örneği

Geçersiz bir `team_id` gönderildiğinde veya takımın geçmişte maçı olmadığında, API `404 Not Found` durumu veya boş bir `matches` dizisi döndürebilir.
