## 4. Oyuncunun Müsabakalara Göre Performansı

* **Açıklama:** Belirtilen oyuncu ID'sine göre, oyuncunun kariyeri boyunca oynadığı tüm resmi müsabakalardaki toplam performans istatistiklerini (maç, gol, asist vb.) döndürür. Veriler, her bir müsabaka için ayrı gruplandırılmıştır.
* **Method:** `GET`
* **Endpoint URL:** `/ceapi/player/{player_id}/performancepercompetition`
* **Örnek Tam URL:** `https://www.transfermarkt.com.tr/ceapi/player/433049/performancepercompetition`

### Parametreler

#### Path Parametreleri

| Parametre   | Tip      | Zorunluluk  | Açıklama                                                                                            |
|:----------- |:-------- |:----------- |:--------------------------------------------------------------------------------------------------- |
| `player_id` | `string` | **Zorunlu** | Performans verileri alınacak oyuncunun Transfermarkt ID'si. (Örn: `433049` Youssef En-Nesyri için). |

#### Query Parametreleri

Bu endpoint için query parametresi bulunmamaktadır.

### Örnek İstek (`cURL`)

```bash
curl -X GET "https://www.transfermarkt.com.tr/ceapi/player/433049/performancepercompetition"
```

### Başarılı Yanıt Örneği (`200 OK`)

Endpoint, başarılı bir istek sonucunda oyuncunun bilgilerini ve müsabaka bazlı performans listesini içeren bir JSON objesi döndürür.

```json
{
  "playerName": "Youssef En-Nesyri",
  "goalkeeper": false,
  "performances": [
    {
      "assists": 6,
      "gamesPlayed": 34,
      "goalsScored": 20,
      "entity": {
        "link": "/super-lig/startseite/wettbewerb/TR1",
        "name": "Süper Lig",
        "logo": "https://tmssl.akamaized.net//images/logo/mediumsmall/tr1.png?lm=1723019495",
        "id": "TR1"
      }
    },
    {
      "assists": 1,
      "gamesPlayed": 31,
      "goalsScored": 12,
      "entity": {
        "link": "/uefa-avrupa-ligi/startseite/wettbewerb/EL",
        "name": "Avrupa Ligi",
        "logo": "https://tmssl.akamaized.net//images/logo/mediumsmall/el.png?lm=1721915137",
        "id": "EL"
      }
    },
    {
      "assists": 2,
      "gamesPlayed": 20,
      "goalsScored": 10,
      "entity": {
        "link": "/uefa-sampiyonlar-ligi/startseite/wettbewerb/CL",
        "name": "Şampiyonlar Ligi",
        "logo": "https://tmssl.akamaized.net//images/logo/mediumsmall/cl.png?lm=1626810555",
        "id": "CL"
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

| Değişken Adı   | Tip       | Açıklama                                                                                                                                                       |
|:-------------- |:--------- |:-------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `playerName`   | `string`  | Oyuncunun tam adı.                                                                                                                                             |
| `goalkeeper`   | `boolean` | Oyuncunun kaleci olup olmadığını belirtir. `false` ise saha oyuncusudur. Bu alan, `cleanSheets` ve `concededGoals` gibi alanların yorumlanması için önemlidir. |
| `performances` | `array`   | Oyuncunun her bir müsabakadaki performansını içeren objelerin listesi.                                                                                         |
| `translations` | `object`  | Arayüzde kullanılan metinlerin Türkçe çevirilerini içerir.                                                                                                     |

---

#### `performances` Dizisindeki Performans Objesi

Bu dizideki her bir obje, tek bir müsabakadaki toplam istatistikleri temsil eder.

| Değişken Adı              | Tip      | Açıklama                                                                   | Örnek Değer             |
|:------------------------- |:-------- |:-------------------------------------------------------------------------- |:----------------------- |
| `assists`                 | `number` | Müsabakadaki toplam asist sayısı.                                          | `6`                     |
| `cleanSheets`             | `number` | Gol yenilmeyen maç sayısı (kaleciler için anlamlıdır).                     | `0`                     |
| `gamesPlayed`             | `number` | Müsabakadaki toplam maç sayısı.                                            | `34`                    |
| `goalsScored`             | `number` | Müsabakadaki toplam gol sayısı.                                            | `20`                    |
| `concededGoals`           | `number` | Yenilen toplam gol sayısı (kaleciler için anlamlıdır).                     | `0`                     |
| `entity`                  | `object` | Müsabakanın kendi bilgilerini içeren obje. Aşağıda detaylandırılmıştır.    | `{...}`                 |
| `detailedPerformanceLink` | `string` | Oyuncunun o müsabakadaki detaylı istatistik sayfasına giden göreceli link. | `"/.../wettbewerb/TR1"` |

---

#### `entity` Objesi (Müsabaka Bilgileri)

| Değişken Adı | Tip      | Açıklama                                                 | Örnek Değer             |
|:------------ |:-------- |:-------------------------------------------------------- |:----------------------- |
| `id`         | `string` | Müsabakanın benzersiz kodu. (Örn: `TR1`, `CL`).          | `"TR1"`                 |
| `name`       | `string` | Müsabakanın tam adı.                                     | `"Süper Lig"`           |
| `link`       | `string` | Müsabakanın Transfermarkt sayfasına giden göreceli link. | `"/super-lig/.../TR1"`  |
| `logo`       | `string` | Müsabaka logosunun tam URL'si.                           | `"https://.../tr1.png"` |

### Veriye Erişim Örneği (JavaScript)

Aşağıdaki JavaScript kodu, bir oyuncunun tüm kariyer istatistiklerini müsabaka bazında nasıl listeleyeceğinizi gösterir.

```javascript
async function getPlayerPerformance(playerId) {
  try {
    const response = await fetch(`https://www.transfermarkt.com.tr/ceapi/player/${playerId}/performancepercompetition`);
    if (!response.ok) {
      throw new Error(`Oyuncu bulunamadı veya bir hata oluştu: ${response.status}`);
    }
    const data = await response.json();

    console.log(`--- ${data.playerName} | Kariyer Performansı ---`);

    data.performances.forEach(perf => {
      // Sadece en az 1 maça çıktığı turnuvaları göster
      if (perf.gamesPlayed > 0) {
        console.log(
          `${perf.entity.name}: ${perf.gamesPlayed} Maç, ${perf.goalsScored} Gol, ${perf.assists} Asist`
        );
      }
    });

  } catch (error) {
    console.error("Veri çekilirken hata:", error.message);
  }
}

// Youssef En-Nesyri (ID: 433049) için fonksiyonu çalıştır
getPlayerPerformance('433049');

// Beklenen Çıktı Örneği:
// --- Youssef En-Nesyri | Kariyer Performansı ---
// LaLiga: 230 Maç, 69 Gol, 10 Asist
// Süper Lig: 34 Maç, 20 Gol, 6 Asist
// Avrupa Ligi: 31 Maç, 12 Gol, 1 Asist
// ...diğer müsabakalar
```

### Hata Yanıtı Örneği

Geçersiz bir `player_id` gönderildiğinde, API genellikle `404 Not Found` durum kodu ve bir hata mesajı ile yanıt verebilir.

**`404 Not Found` Yanıtı:**

```json
{
  "message": "No player found for id 99999999"
}
```
