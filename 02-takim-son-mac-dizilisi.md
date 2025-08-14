## 2. Takımın Son Maç Dizilişini Getirme

* **Açıklama:** Belirtilen takım ID'sine göre, takımın oynadığı son resmi maça ait detaylı bilgileri döndürür. Bu bilgiler arasında maçın ilk 11'i, yedekler, taktik diziliş, teknik direktör ve maç içerisinde gerçekleşen olaylar (gol, kart, oyuncu değişikliği) yer alır.
* **Method:** `GET`
* **Endpoint URL:** `/ceapi/FinalFormation/ClubId/{club_id}`
* **Örnek Tam URL:** `https://www.transfermarkt.com.tr/ceapi/FinalFormation/ClubId/36`

### Parametreler

#### Path Parametreleri

| Parametre | Tip      | Zorunluluk  | Açıklama                                                                     |
|:--------- |:-------- |:----------- |:---------------------------------------------------------------------------- |
| `club_id` | `string` | **Zorunlu** | Bilgileri alınacak takımın Transfermarkt ID'si. (Örn: `36` Fenerbahçe için). |

#### Query Parametreleri

Bu endpoint için query parametresi bulunmamaktadır.

### Örnek İstek (`cURL`)

```bash
curl -X GET "https://www.transfermarkt.com.tr/ceapi/FinalFormation/ClubId/36"
```

### Başarılı Yanıt Örneği (`200 OK`)

Endpoint, başarılı bir istek sonucunda karmaşık bir JSON objesi döndürür. Örnek yanıt, okunabilirliği artırmak için kısaltılmıştır.

```json
{
  "list": {
    "players": [
      {
        "id": "322873",
        "name": "İrfan Can Eğribayat",
        "positionMain": "Kaleci",
        "actions": { "substitution": [], "cards": [], "goals": [] }
      },
      {
        "id": "191614",
        "name": "Fred",
        "positionMain": "Orta saha",
        "actions": {
          "substitution": { "description": "Değişim", /* ... */ },
          "cards": [],
          "goals": [
            {
              "description": "GOL!",
              "score": "3:1",
              "assistByPlayer": "Brown",
              "time": { "minute": "55", "addedTime": "0" }
            }
          ]
        }
      },
      {
        "id": "287579",
        "name": "Sofyan Amrabat",
        "positionMain": "Orta saha",
        "actions": {
          "substitution": [],
          "cards": [
            {
              "description": "Sarı kart",
              "reason": "Faul",
              "type": "gelb",
              "time": { "minute": "21", "addedTime": "0" }
            }
          ],
          "goals": []
        }
      }
    ],
    "substitutes": [ /* ... Yedek oyuncular listesi ... */ ]
  },
  "matchInfo": {
    "competition": { "id": "CLQ", "name": "UEFA Şampiyonlar Ligi Elemeleri" },
    "date": "Sal, 12 Ağu 2025 - 20:00  Saat",
    "tactic": "3-4-1-2"
  },
  "matchReport": {
    "id": "4676660",
    "result": "5:2 "
  },
  "teams": {
    "team1": { "id": "36", "name": "Fenerbahçe" },
    "team2": { "id": "234", "name": "Feyenoord" }
  },
  "trainer": {
    "id": "781",
    "name": "José Mourinho"
  }
}
```

### Yanıt Verisi Açıklaması

Dönen JSON objesi birçok alt obje içerir. Anahtar yapılar aşağıda açıklanmıştır.

#### Ana Obje Yapısı

| Değişken Adı   | Tip      | Açıklama                                                          |
|:-------------- |:-------- |:----------------------------------------------------------------- |
| `list`         | `object` | İlk 11 (`players`) ve yedekleri (`substitutes`) içeren ana liste. |
| `translations` | `object` | Arayüzde kullanılan metinlerin çevirilerini içerir.               |
| `matchInfo`    | `object` | Maçın turnuva, tarih ve taktik gibi genel bilgileri.              |
| `matchReport`  | `object` | Maç raporu ID'si, linki ve sonucu.                                |
| `teams`        | `object` | Maçı oynayan iki takımın bilgileri.                               |
| `trainer`      | `object` | Takımın teknik direktör bilgileri.                                |

---

#### `list.players` ve `list.substitutes` içindeki Oyuncu Objesi

| Değişken Adı             | Tip      | Açıklama                                                             | Örnek Değer                     |
|:------------------------ |:-------- |:-------------------------------------------------------------------- |:------------------------------- |
| `id`                     | `string` | Oyuncunun Transfermarkt ID'si.                                       | `"191614"`                      |
| `name`                   | `string` | Oyuncunun tam adı.                                                   | `"Fred"`                        |
| `shortName`              | `string` | Oyuncunun kısa adı.                                                  | `"Fred"`                        |
| `captain`                | `string` | Oyuncu kaptansa `"x"` değeri alır, değilse boştur.                   | `""`                            |
| `number`                 | `string` | Forma numarası.                                                      | `"7"`                           |
| `profileUrl`             | `string` | Oyuncunun profil sayfasına giden göreceli link.                      | `"/fred/profil/spieler/191614"` |
| `positionMain`           | `string` | Oyuncunun Türkçe mevkisi.                                            | `"Orta saha"`                   |
| `positionShort`          | `string` | Oyuncunun mevki kısaltması (ÖL, STO, S vb.).                         | `"MOS"`                         |
| `styleTop` / `styleLeft` | `number` | Saha dizilişi görselinde oyuncunun pozisyonu için CSS değerleri.     | `43`                            |
| `actions`                | `object` | Oyuncunun maç içindeki aksiyonlarını (gol, kart, değişiklik) içerir. | `{...}`                         |

---

#### `actions` Objesi

Bu obje, oyuncunun maçtaki önemli anlarını barındırır.

| Değişken Adı   | Tip                   | Açıklama                                                                                                          |
|:-------------- |:--------------------- |:----------------------------------------------------------------------------------------------------------------- |
| `substitution` | `object` veya `array` | Oyuncu değişikliği bilgisi. Oyuncu oyundan çıktıysa obje, yedekse ve oyuna girdiyse yine obje olur. Boş ise `[]`. |
| `cards`        | `array`               | Oyuncunun gördüğü kartların listesi. Boş olabilir.                                                                |
| `goals`        | `array`               | Oyuncunun attığı gollerin listesi. Boş olabilir.                                                                  |

##### `actions.goals` Objesi

| Değişken Adı     | Tip      | Açıklama                                       | Örnek Değer          |
|:---------------- |:-------- |:---------------------------------------------- |:-------------------- |
| `description`    | `string` | Olayın açıklaması.                             | `"GOL!"`             |
| `score`          | `string` | Golden sonraki skor.                           | `"3:1"`              |
| `goalType`       | `string` | Golün nasıl olduğu (örn: Korner, Pas).         | `"Pas"`              |
| `action`         | `string` | Vuruş şekli (örn: Uzaktan şut, Kafa vuruşu).   | `"Uzaktan şut"`      |
| `assistByPlayer` | `string` | Asisti yapan oyuncunun kısa adı. Boş olabilir. | `"Brown"`            |
| `time`           | `object` | Golün atıldığı zaman (`minute`, `addedTime`).  | `{ "minute": "55" }` |

##### `actions.cards` Objesi

| Değişken Adı  | Tip      | Açıklama                                           | Örnek Değer          |
|:------------- |:-------- |:-------------------------------------------------- |:-------------------- |
| `description` | `string` | Kart türü.                                         | `"Sarı kart"`        |
| `reason`      | `string` | Kartın sebebi.                                     | `"Faul"`             |
| `type`        | `string` | Kart tipinin programatik adı (`gelb`: sarı).       | `"gelb"`             |
| `time`        | `object` | Kartın gösterildiği zaman (`minute`, `addedTime`). | `{ "minute": "21" }` |

##### `actions.substitution` Objesi

| Değişken Adı  | Tip      | Açıklama                          | Örnek Değer          |
|:------------- |:-------- |:--------------------------------- |:-------------------- |
| `description` | `string` | Olayın açıklaması.                | `"Değişim"`          |
| `playerIn`    | `string` | Oyuna giren oyuncunun kısa adı.   | `"Yüksek"`           |
| `playerOut`   | `string` | Oyundan çıkan oyuncunun kısa adı. | `"Fred"`             |
| `reason`      | `string` | Değişiklik sebebi.                | `"Taktik"`           |
| `time`        | `object` | Değişikliğin yapıldığı zaman.     | `{ "minute": "87" }` |

### Veriye Erişim Örneği (JavaScript)

```javascript
async function getMatchDetails(clubId) {
  const response = await fetch(`https://www.transfermarkt.com.tr/ceapi/FinalFormation/ClubId/${clubId}`);
  const data = await response.json();

  console.log(`Teknik Direktör: ${data.trainer.name}`);
  console.log(`Son Maç Taktiği: ${data.matchInfo.tactic}`);
  console.log(`Rakip: ${data.teams.team2.name}, Skor: ${data.matchReport.result}`);

  console.log("\n--- Gol Atanlar ---");
  // Hem ilk 11 hem de yedeklerdeki oyuncuları kontrol et
  const allPlayers = [...data.list.players, ...data.list.substitutes];

  allPlayers.forEach(player => {
    if (player.actions.goals.length > 0) {
      player.actions.goals.forEach(goal => {
        console.log(`- ${player.shortName} (${goal.time.minute}') - Skor: ${goal.score}`);
      });
    }
  });
}

// Fenerbahçe (ID: 36) için fonksiyonu çalıştır
getMatchDetails('36');
```

### Hata Yanıtı Örneği

Geçersiz bir `club_id` gönderildiğinde, API genellikle boş bir yanıt veya içeriği olmayan bir `200 OK` durumu döndürebilir. Sunucu tarafında hata oluşursa `500` gibi bir durum kodu da beklenebilir.
