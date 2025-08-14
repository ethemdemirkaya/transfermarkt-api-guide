    ## 12. Oyuncunun Sorare Kart Bilgilerini Getirme

* **Açıklama:** Belirtilen oyuncu ID'sine göre, Transfermarkt'ın [Sorare](https://sorare.com) entegrasyonu aracılığıyla oyuncunun fantazi futbol kartı ile ilgili istatistiklerini döndürür. Bu endpoint, genel futbol istatistiklerinden ziyade, Sorare oyununda kullanılan performansa dayalı puanları (örn: `score_so5`), ikili mücadele kazanma gibi özel metrikleri ve oyuncunun Sorare kart görselini içerir.
* **Method:** `GET`
* **Endpoint URL:** `/ceapi/sorare/fetchPlayersCard/{player_id}`
* **Örnek Tam URL:** `https://www.transfermarkt.com.tr/ceapi/sorare/fetchPlayersCard/396638`

### Parametreler

#### Path Parametreleri

| Parametre   | Tip      | Zorunluluk  | Açıklama                                                                                          |
|:----------- |:-------- |:----------- |:------------------------------------------------------------------------------------------------- |
| `player_id` | `string` | **Zorunlu** | Sorare kart bilgileri alınacak oyuncunun Transfermarkt ID'si. (Örn: `396638` Manor Solomon için). |

#### Query Parametreleri

Bu endpoint için query parametresi bulunmamaktadır.

### Örnek İstek (`cURL`)

```bash
curl -X GET "https://www.transfermarkt.com.tr/ceapi/sorare/fetchPlayersCard/396638"
```

### Başarılı Yanıt Örneği (`200 OK`)

Endpoint, başarılı bir istek sonucunda oyuncunun Sorare istatistiklerini içeren bir JSON objesi döndürür.

```json
{
  "tmv4_player_id": 396638,
  "score_so5": 83,
  "matches_played_total": 15,
  "matches_played_quota_so5": 1,
  "goals": 3,
  "assists": 7,
  "duels_won": 59,
  "clean_sheet": 5,
  "pass_accuracy_quota": 0.886051,
  "card_image_url": "https://assets.sorare.com/card/...",
  "target_url": "https://sorare.com/football/players/manor-solomon",
  "last_update_timestamp": "2025-08-14 19:51:41",
  "position": "SOK",
  "translations": { /* ... Arayüz çevirileri ... */ }
}
```

### Yanıt Verisi Açıklaması

Dönen JSON objesi aşağıdaki alanları içerir:

| Değişken Adı               | Tip      | Açıklama                                                                                             | Örnek Değer                       |
|:-------------------------- |:-------- |:---------------------------------------------------------------------------------------------------- |:--------------------------------- |
| `tmv4_player_id`           | `number` | Oyuncunun Transfermarkt ID'si.                                                                       | `396638`                          |
| `score_so5`                | `number` | Sorare'nin son 5 maçlık periyottaki ortalama fantazi puanı. Bu, oyunun temel metriklerinden biridir. | `83`                              |
| `matches_played_total`     | `number` | Sorare kapsamında değerlendirilen toplam maç sayısı.                                                 | `15`                              |
| `matches_played_quota_so5` | `number` | Son 5 maçlık periyotta oynadığı maç sayısı.                                                          | `1`                               |
| `goals` / `assists`        | `number` | Değerlendirilen periyottaki gol ve asist sayısı.                                                     | `3` / `7`                         |
| `duels_won`                | `number` | Kazanılan ikili mücadele sayısı.                                                                     | `59`                              |
| `clean_sheet`              | `number` | Gol yenilmeyen maç sayısı (Sadece defansif oyuncular ve kaleciler için anlamlıdır).                  | `5`                               |
| `pass_accuracy_quota`      | `number` | Pas isabet oranı (ondalık formatta, 1.0 üzerinden).                                                  | `0.886051`                        |
| `card_image_url`           | `string` | Oyuncunun Sorare üzerindeki kart görselinin tam URL'si.                                              | `"https://assets.sorare.com/..."` |
| `target_url`               | `string` | Oyuncunun Sorare'deki profil sayfasına yönlendiren tam URL.                                          | `"https://sorare.com/..."`        |
| `last_update_timestamp`    | `string` | Verinin son güncellenme zamanı.                                                                      | `"2025-08-14 19:51:41"`           |
| `position`                 | `string` | Oyuncunun mevki kısaltması (örn: SOK - Sol Kanat).                                                   | `"SOK"`                           |
| `translations`             | `object` | Arayüzde kullanılan metinlerin Türkçe çevirilerini içerir.                                           | `{...}`                           |

### Veriye Erişim Örneği (JavaScript)

Aşağıdaki kod, bir oyuncunun Sorare kart bilgilerini alıp anlamlı bir formatta nasıl yazdıracağınızı gösterir.

```javascript
async function getSorareCardInfo(playerId) {
  try {
    const response = await fetch(`https://www.transfermarkt.com.tr/ceapi/sorare/fetchPlayersCard/${playerId}`);
    const data = await response.json();

    if (data && data.tmv4_player_id) {
      const passAccuracy = (data.pass_accuracy_quota * 100).toFixed(1);

      console.log(`--- Sorare Kart Bilgileri (ID: ${data.tmv4_player_id}) ---`);
      console.log(`Sorare Puanı (Son 5 Maç): ${data.score_so5}`);
      console.log(`Pas İsabeti: %${passAccuracy}`);
      console.log(`İkili Mücadele Kazanma: ${data.duels_won}`);
      console.log(`\nKart Görseli: ${data.card_image_url}`);
      console.log(`Sorare Profili: ${data.target_url}`);
      console.log(`Son Güncelleme: ${data.last_update_timestamp}`);

    } else {
      console.log("Oyuncu bulunamadı veya oyuncunun Sorare verisi mevcut değil.");
    }

  } catch (error) {
    console.error("Veri alınırken hata oluştu:", error);
  }
}

// Manor Solomon (ID: 396638) için fonksiyonu çalıştır
getSorareCardInfo('396638');
```

### Hata Yanıtı Örneği

İlgili oyuncu ID'si geçersizse veya oyuncunun Sorare'de bir kartı/verisi bulunmuyorsa, API `404 Not Found` durumu veya boş bir JSON objesi (`{}`) döndürebilir.
