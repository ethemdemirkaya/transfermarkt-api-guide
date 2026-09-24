## 5. Oyuncunun Kulüplere Göre Performansı

* **Açıklama:** Belirtilen oyuncu ID'sine göre, oyuncunun kariyeri boyunca oynadığı tüm kulüplerdeki toplam performans istatistiklerini (maç, gol, asist vb.) döndürür. Veriler, her bir kulüp için ayrı gruplandırılmıştır.
* **Method:** `GET`
* **Endpoint URL:** `/ceapi/player/{player_id}/performance`
* **Örnek Tam URL:** `https://www.transfermarkt.com.tr/ceapi/player/433049/performance`

### Parametreler

#### Path Parametreleri

| Parametre   | Tip      | Zorunluluk  | Açıklama                                                                                            |
|:----------- |:-------- |:----------- |:--------------------------------------------------------------------------------------------------- |
| `player_id` | `string` | **Zorunlu** | Performans verileri alınacak oyuncunun Transfermarkt ID'si. (Örn: `433049` Youssef En-Nesyri için). |

#### Query Parametreleri

Bu endpoint için query parametresi bulunmamaktadır.

### Örnek İstek (`cURL`)

```bash
curl -X GET "https://www.transfermarkt.com.tr/ceapi/player/433049/performance"
```

### Başarılı Yanıt Örneği (`200 OK`)

Endpoint, başarılı bir istek sonucunda oyuncunun bilgilerini ve kulüp bazlı performans listesini içeren bir JSON objesi döndürür.

```json
{
  "playerName": "Youssef En-Nesyri",
  "goalkeeper": false,
  "performances": [
    {
      "assists": 8,
      "gamesPlayed": 196,
      "goalsScored": 73,
      "entity": {
        "link": "/fc-sevilla/startseite/verein/368",
        "name": "Sevilla",
        "logo": "https://tmssl.akamaized.net//images/wappen/profil/368.png?lm=1730896593",
        "id": "368"
      }
    },
    {
      "assists": 8,
      "gamesPlayed": 54,
      "goalsScored": 31,
      "entity": {
        "link": "/fenerbahce-istanbul/startseite/verein/36",
        "name": "Fenerbahçe",
        "logo": "https://tmssl.akamaized.net//images/wappen/profil/36.png?lm=1753429185",
        "id": "36"
      }
    },
    {
      "assists": 4,
      "gamesPlayed": 53,
      "goalsScored": 15,
      "entity": {
        "link": "/cd-leganes/startseite/verein/1244",
        "name": "Leganés",
        "logo": "https://tmssl.akamaized.net//images/wappen/profil/1244.png?lm=1422972468",
        "id": "1244"
      }
    }
  ],
  "translations": {
    /* ... Arayüz çevirileri ... */
  }
}
```

### Yanıt Verisi Açıklaması

#### Ana Obje Yapısı

| Değişken Adı   | Tip       | Açıklama                                                                                                                   |
|:-------------- |:--------- |:-------------------------------------------------------------------------------------------------------------------------- |
| `playerName`   | `string`  | Oyuncunun tam adı.                                                                                                         |
| `goalkeeper`   | `boolean` | Oyuncunun kaleci olup olmadığını belirtir. `false` ise saha oyuncusudur.                                                   |
| `performances` | `array`   | Oyuncunun her bir kulüpteki performansını içeren objelerin listesi.                                                        |
| `translations` | `object`  | Arayüzde kullanılan metinlerin Türkçe çevirilerini içerir (`headline` alanı "Kulüplere göre performansı" değerini içerir). |

---

#### `performances` Dizisindeki Performans Objesi

Bu dizideki her bir obje, tek bir kulüpteki toplam istatistikleri temsil eder.

| Değişken Adı              | Tip      | Açıklama                                                                | Örnek Değer         |
|:------------------------- |:-------- |:----------------------------------------------------------------------- |:------------------- |
| `assists`                 | `number` | Kulüpteki toplam asist sayısı.                                          | `8`                 |
| `gamesPlayed`             | `number` | Kulüpteki toplam maç sayısı.                                            | `196`               |
| `goalsScored`             | `number` | Kulüpteki toplam gol sayısı.                                            | `73`                |
| `entity`                  | `object` | Kulübün kendi bilgilerini içeren obje. Aşağıda detaylandırılmıştır.     | `{...}`             |
| `detailedPerformanceLink` | `string` | Oyuncunun o kulüpteki detaylı istatistik sayfasına giden göreceli link. | `"/.../verein/368"` |

---

#### `entity` Objesi (Kulüp Bilgileri)

| Değişken Adı | Tip      | Açıklama                                                   | Örnek Değer             |
|:------------ |:-------- |:---------------------------------------------------------- |:----------------------- |
| `id`         | `string` | Kulübün benzersiz Transfermarkt ID'si. (Örn: `368`, `36`). | `"368"`                 |
| `name`       | `string` | Kulübün adı.                                               | `"Sevilla"`             |
| `link`       | `string` | Kulübün Transfermarkt sayfasına giden göreceli link.       | `"/fc-sevilla/.../368"` |
| `logo`       | `string` | Kulüp logosunun tam URL'si.                                | `"https://.../368.png"` |

### Veriye Erişim Örneği (JavaScript)

Aşağıdaki JavaScript kodu, bir oyuncunun tüm kariyer istatistiklerini kulüp bazında nasıl listeleyeceğinizi gösterir.

```javascript
async function getPlayerPerformanceByClub(playerId) {
  try {
    const response = await fetch(`https://www.transfermarkt.com.tr/ceapi/player/${playerId}/performance`);
    if (!response.ok) {
      throw new Error(`Oyuncu bulunamadı veya bir hata oluştu: ${response.status}`);
    }
    const data = await response.json();

    console.log(`--- ${data.playerName} | Kulüp Performansı ---`);

    data.performances.forEach(perf => {
      console.log(
        `${perf.entity.name} (ID: ${perf.entity.id}): ${perf.gamesPlayed} Maç, ${perf.goalsScored} Gol, ${perf.assists} Asist`
      );
    });

  } catch (error) {
    console.error("Veri çekilirken hata:", error.message);
  }
}

// Youssef En-Nesyri (ID: 433049) için fonksiyonu çalıştır
getPlayerPerformanceByClub('433049');

// Beklenen Çıktı Örneği:
// --- Youssef En-Nesyri | Kulüp Performansı ---
// Sevilla (ID: 368): 196 Maç, 73 Gol, 8 Asist
// Fenerbahçe (ID: 36): 54 Maç, 31 Gol, 8 Asist
// Leganés (ID: 1244): 53 Maç, 15 Gol, 4 Asist
// Málaga (ID: 1084): 41 Maç, 5 Gol, 1 Asist
```

### Hata Yanıtı Örneği

Geçersiz bir `player_id` gönderildiğinde, API genellikle `404 Not Found` durum kodu ve bir hata mesajı ile yanıt verir.

**`404 Not Found` Yanıtı:**

```json
{
  "message": "No player found for id 99999999"
}
```
