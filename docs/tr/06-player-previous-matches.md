## 6. Oyuncunun Son Maçlarını Listeleme

* **Açıklama:** Belirtilen oyuncu ID'sine göre, oyuncunun (kulüp ve milli takım dahil) oynadığı son maçların bir listesini döndürür. Yanıt, maçlarda yer alan tüm takımların bilgilerini içeren bir "sözlük" (`teams`) ve maçların listesini (`matches`) olmak üzere iki ana bölümden oluşur. `limit` query parametresi ile döndürülecek maç sayısı ayarlanabilir.
* **Method:** `GET`
* **Endpoint URL:** `/ceapi/previousMatches/player/{player_id}`
* **Örnek Tam URL:** `https://www.transfermarkt.com.tr/ceapi/previousMatches/player/433049?limit=25`

### Parametreler

#### Path Parametreleri

| Parametre   | Tip      | Zorunluluk  | Açıklama                                                                                    |
|:----------- |:-------- |:----------- |:------------------------------------------------------------------------------------------- |
| `player_id` | `string` | **Zorunlu** | Maçları listelenecek oyuncunun Transfermarkt ID'si. (Örn: `433049` Youssef En-Nesyri için). |

#### Query Parametreleri

| Parametre | Tip      | Zorunluluk   | Açıklama                                                                                   |
|:--------- |:-------- |:------------ |:------------------------------------------------------------------------------------------ |
| `limit`   | `number` | İsteğe Bağlı | Döndürülecek maksimum maç sayısı. Belirtilmezse varsayılan bir değer kullanılır (örn: 25). |

### Örnek İstek (`cURL`)

```bash
curl -X GET "https://www.transfermarkt.com.tr/ceapi/previousMatches/player/433049?limit=5"
```

### Başarılı Yanıt Örneği (`200 OK`)

Endpoint, başarılı bir istek sonucunda `teams` ve `matches` anahtarlarına sahip bir JSON objesi döndürür.

```json
{
  "teams": {
    "36": {
      "name": "Fenerbahçe",
      "link": "/fenerbahce-istanbul/startseite/verein/36",
      "isNT": false
    },
    "234": {
      "name": "Feyenoord",
      "link": "/feyenoord-rotterdam/startseite/verein/234",
      "isNT": false
    },
    "3575": {
      "name": "Fas",
      "link": "/marokko/startseite/verein/3575",
      "isNT": true
    }
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
    },
    {
      "competition": { "id": "FS", "label": "Dostluk Maçları" },
      "id": 4619056,
      "match": {
        "away": 3955,
        "home": 3575,
        "result": "1:0",
        "state": "Played",
        "time": 1749499200
      }
    }
  ]
}
```

### Yanıt Verisi Açıklaması

#### Ana Obje Yapısı

| Değişken Adı | Tip      | Açıklama                                                                                                                                                                  |
|:------------ |:-------- |:------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `teams`      | `object` | Anahtar olarak takım ID'sini, değer olarak takım bilgilerini içeren bir arama tablosu (lookup table). `matches` listesindeki `home` ve `away` ID'leri bu tablodan okunur. |
| `matches`    | `array`  | Oyuncunun son maçlarını içeren objelerin listesi.                                                                                                                         |

---

#### `teams` Objesi

Bu obje, maç listesinde geçen tüm takımların bilgilerini barındırır. Objenin anahtarı takımın ID'sidir.

| Değişken Adı          | Tip       | Açıklama                                                                                       | Örnek Değer                  |
|:--------------------- |:--------- |:---------------------------------------------------------------------------------------------- |:---------------------------- |
| `name`                | `string`  | Takımın adı.                                                                                   | `"Fenerbahçe"`               |
| `link`                | `string`  | Takımın profil sayfasına giden göreceli link.                                                  | `"/fenerbahce-istanbul/..."` |
| `image1x` / `image2x` | `string`  | Takım logosunun farklı çözünürlükteki URL'leri.                                                | `"https://.../36.png"`       |
| `isNT`                | `boolean` | Takımın bir milli takım (`National Team`) olup olmadığını belirtir. `true` ise milli takımdır. | `false`                      |

---

#### `matches` Dizisindeki Maç Objesi

| Değişken Adı  | Tip      | Açıklama                                                       |
|:------------- |:-------- |:-------------------------------------------------------------- |
| `competition` | `object` | Maçın oynandığı müsabakanın bilgileri (`id`, `label`, `link`). |
| `id`          | `number` | Maç raporunun benzersiz Transfermarkt ID'si.                   |
| `match`       | `object` | Maçın detaylarını içeren asıl obje.                            |

---

#### `match` Objesi (Maç Detayları)

| Değişken Adı | Tip      | Açıklama                                                                                                                 | Örnek Değer           |
|:------------ |:-------- |:------------------------------------------------------------------------------------------------------------------------ |:--------------------- |
| `home`       | `number` | Ev sahibi takımın ID'si. Bu ID, `teams` objesinden takım adını bulmak için kullanılır.                                   | `36`                  |
| `away`       | `number` | Deplasman takımının ID'si.                                                                                               | `234`                 |
| `result`     | `string` | Maçın skoru. Oynanmamış maçlar için "-:-" olabilir.                                                                      | `"5:2"`               |
| `state`      | `string` | Maçın durumu. `Played` (Oynandı), `Postponed` (Ertelendi), `Scheduled` (Planlandı) gibi değerler alabilir.               | `"Played"`            |
| `time`       | `number` | Maçın başlangıç zamanını belirten **Unix timestamp** (saniye cinsinden). Bunu okunabilir bir tarihe dönüştürmek gerekir. | `1755018000`          |
| `link`       | `string` | Maçın detaylı rapor sayfasına giden göreceli link.                                                                       | `"/spielbericht/..."` |

### Veriye Erişim Örneği (JavaScript)

Aşağıdaki kod, maç listesini alıp `teams` objesini kullanarak takım isimlerini yazdırmayı ve Unix zaman damgasını normal tarihe çevirmeyi gösterir.

```javascript
async function getPlayerLastMatches(playerId, limit = 10) {
  try {
    const response = await fetch(`https://www.transfermarkt.com.tr/ceapi/previousMatches/player/${playerId}?limit=${limit}`);
    const data = await response.json();

    const teamsLookup = data.teams;
    const matches = data.matches;

    console.log("--- Son Maçlar ---");

    matches.forEach(m => {
      const homeTeam = teamsLookup[m.match.home].name;
      const awayTeam = teamsLookup[m.match.away].name;

      // Unix timestamp'i milisaniyeye çevirip Date objesi oluştur
      const matchDate = new Date(m.match.time * 1000).toLocaleDateString('tr-TR');

      console.log(
        `${matchDate} | ${m.competition.label} | ${homeTeam} ${m.match.result} ${awayTeam} (${m.match.state})`
      );
    });

  } catch (error) {
    console.error("Veri alınırken hata oluştu:", error);
  }
}

// Youssef En-Nesyri (ID: 433049) için son 5 maçı listele
getPlayerLastMatches('433049', 5);

// Beklenen Çıktı Örneği:
// --- Son Maçlar ---
// 12.08.2025 | Şampiyonlar Ligi Elemeleri | Fenerbahçe 5:2 Feyenoord (Played)
// 10.08.2025 | Süper Lig | Fenerbahçe -:- Alanyaspor (Postponed)
// 07.08.2025 | Şampiyonlar Ligi Elemeleri | Feyenoord 2:1 Fenerbahçe (Played)
// 06.06.2025 | Dostluk Maçları | Fas 1:0 Benin (Played)
// 03.06.2025 | Dostluk Maçları | Fas 2:0 Tunus (Played)
```

### Hata Yanıtı Örneği

Geçersiz bir `player_id` gönderildiğinde, API genellikle `404 Not Found` durum kodu ve bir hata mesajı ile yanıt verebilir.
