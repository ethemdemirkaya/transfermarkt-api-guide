## 9. Oyuncunun Sezonluk Performans Detayları

* **Açıklama:** Belirtilen oyuncu ID'sine göre, oyuncunun kariyerindeki her bir sezon ve o sezonda oynadığı her bir müsabaka için ayrı ayrı performans istatistiklerini döndürür. Yanıt, her sezon/müsabaka kombinasyonu için maç, gol, asist, kartlar ve yüzde bazlı istatistikler gibi detaylı veriler içeren bir dizi (array) olarak gelir. Bu endpoint, bir oyuncunun belirli bir sezondaki formunu analiz etmek için idealdir.
* **Method:** `GET`
* **Endpoint URL:** `/ceapi/player/{player_id}/performance`
* **Örnek Tam URL:** `https://www.transfermarkt.com.tr/ceapi/player/433049/performance`

### Parametreler

#### Path Parametreleri

| Parametre   | Tip      | Zorunluluk  | Açıklama                                                                                            |
|:----------- |:-------- |:----------- |:--------------------------------------------------------------------------------------------------- |
| `player_id` | `string` | **Zorunlu** | Performans verileri alınacak oyuncunun Transfermarkt ID'si. (Örn: `433049` Youssef En-Nesyri için). |

#### Query Parametreleri

Bu endpoint'in görünen bir query parametresi yoktur, ancak sunucu tarafında sezon filtresi gibi ek parametreler alıyor olabilir.

### Örnek İstek (`cURL`)

```bash
curl -X GET "https://www.transfermarkt.com.tr/ceapi/player/433049/performance"
```

### Başarılı Yanıt Örneği (`200 OK`)

Endpoint, başarılı bir istek sonucunda her bir elemanı belirli bir sezon ve müsabakadaki performansı temsil eden bir JSON dizisi döndürür.

```json
[
  {
    "detailedStatsLink": "/youssef-en-nesyri/leistungsdatendetails/spieler/433049/wettbewerb/CLQ/saison/2025",
    "competitionDescription": "Şampiyonlar Ligi Elemeleri",
    "logo": "https://tmssl.akamaized.net//images/logo/normal/clq.png?lm=1626812672",
    "nameSeason": "25/26",
    "possibleGames": 2,
    "gamesPlayed": 2,
    "goalsScored": 1,
    "assists": 1,
    "yellowCards": 0,
    "secondYellowCards": 0,
    "redCards": 0,
    "startElevenPercent": 100,
    "minutesPlayedPercent": 96.67,
    "goalsContributedPercent": 33.33,
    "goalkeeper": false,
    "minutesPlayed": 174
  },
  {
    "detailedStatsLink": "/youssef-en-nesyri/leistungsdatendetails/spieler/433049/wettbewerb/TR1/saison/2024",
    "competitionDescription": "Süper Lig",
    "logo": "https://tmssl.akamaized.net//images/logo/normal/tr1.png",
    "nameSeason": "24/25",
    "possibleGames": 38,
    "gamesPlayed": 34,
    "goalsScored": 20,
    "assists": 6,
    "yellowCards": 3,
    "secondYellowCards": 0,
    "redCards": 0,
    "startElevenPercent": 95,
    "minutesPlayedPercent": 88.5,
    "goalsContributedPercent": 76.47,
    "goalkeeper": false,
    "minutesPlayed": 3005
  }
]
```

*(Not: Örnek yanıta ikinci bir sezon verisi eklenerek dizinin yapısı daha net gösterilmiştir.)*

### Yanıt Verisi Açıklaması

Dönen JSON dizisindeki her bir obje, bir sezon-müsabaka performansını temsil eder ve aşağıdaki alanları içerir:

| Değişken Adı              | Tip       | Açıklama                                                                                  | Örnek Değer                    |
|:------------------------- |:--------- |:----------------------------------------------------------------------------------------- |:------------------------------ |
| `detailedStatsLink`       | `string`  | Bu performansa ait detaylı istatistik sayfasına giden göreceli link.                      | `"/.../saison/2025"`           |
| `competitionDescription`  | `string`  | Müsabakanın tam adı.                                                                      | `"Şampiyonlar Ligi Elemeleri"` |
| `logo`                    | `string`  | Müsabaka logosunun tam URL'si.                                                            | `"https://.../clq.png"`        |
| `nameSeason`              | `string`  | Performansın ait olduğu sezon (örn: 25/26).                                               | `"25/26"`                      |
| `possibleGames`           | `number`  | O sezon o müsabakada oynanabilecek maksimum maç sayısı.                                   | `2`                            |
| `gamesPlayed`             | `number`  | Oyuncunun oynadığı maç sayısı.                                                            | `2`                            |
| `goalsScored`             | `number`  | Atılan gol sayısı.                                                                        | `1`                            |
| `assists`                 | `number`  | Yapılan asist sayısı.                                                                     | `1`                            |
| `yellowCards`             | `number`  | Görülen sarı kart sayısı.                                                                 | `0`                            |
| `secondYellowCards`       | `number`  | İkinci sarıdan kırmızı kart sayısı.                                                       | `0`                            |
| `redCards`                | `number`  | Direkt kırmızı kart sayısı.                                                               | `0`                            |
| `startElevenPercent`      | `number`  | Oyuncunun oynadığı maçlara yüzde kaç oranında ilk 11'de başladığı.                        | `100`                          |
| `minutesPlayedPercent`    | `number`  | Oynanması mümkün olan toplam dakikaların yüzde kaçında sahada kaldığı.                    | `96.67`                        |
| `goalsContributedPercent` | `number`  | Takımın attığı gollere oyuncunun (gol veya asist ile) yüzde kaç oranında katkı sağladığı. | `33.33`                        |
| `goalkeeper`              | `boolean` | Oyuncunun kaleci olup olmadığı.                                                           | `false`                        |
| `minutesPlayed`           | `number`  | O sezon o müsabakada oynadığı toplam dakika.                                              | `174`                          |

### Veriye Erişim Örneği (JavaScript)

Aşağıdaki JavaScript kodu, bir oyuncunun sezonluk performans dökümünü nasıl alıp işleyeceğinizi gösterir.

```javascript
async function getPlayerSeasonalPerformance(playerId) {
  try {
    const response = await fetch(`https://www.transfermarkt.com.tr/ceapi/player/${playerId}/performance`);
    const data = await response.json();

    if (data && data.length > 0) {
      console.log(`--- Sezonluk Performans Dökümü ---`);
      data.forEach(perf => {
        console.log(`\n> Sezon: ${perf.nameSeason} | Müsabaka: ${perf.competitionDescription}`);
        console.log(`  Maç: ${perf.gamesPlayed}/${perf.possibleGames} | Dakika: ${perf.minutesPlayed}'`);
        console.log(`  Gol: ${perf.goalsScored} | Asist: ${perf.assists}`);
        console.log(`  Kartlar (S/S-K/K): ${perf.yellowCards}/${perf.secondYellowCards}/${perf.redCards}`);
      });
    } else {
      console.log("Oyuncunun sezonluk performans verisi bulunamadı.");
    }

  } catch (error) {
    console.error("Veri alınırken hata oluştu:", error);
  }
}

// Youssef En-Nesyri (ID: 433049) için fonksiyonu çalıştır
getPlayerSeasonalPerformance('433049');
```

### Hata Yanıtı Örneği

Geçersiz bir `player_id` gönderildiğinde veya oyuncunun hiç maçı olmadığında, API `404 Not Found` durumu veya boş bir JSON dizisi (`[]`) döndürebilir.
