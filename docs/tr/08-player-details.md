## 8. Oyuncunun Detaylı Bilgilerini Getirme

* **Açıklama:** Transfermarkt'ın yeni nesil API'si (`tmapi.transfermarkt.technology`) üzerinden bir veya birden fazla oyuncunun detaylı profil bilgilerini döndürür. Yanıt; doğum bilgileri, uyruk, boy, tercih ettiği ayak, mevki, sözleşme bitiş tarihi, menajerlik şirketi, güncel ve en yüksek piyasa değeri ile kulüp/milli takım bağlantılarını içerir. Tek istekte birden fazla oyuncu sorgulanabildiği için toplu veri çekmek için idealdir.
* **Method:** `GET`
* **Endpoint URL:** `/players?ids[]={player_id}&ids[]={player_id}...`
* **Örnek Tam URL:** `https://tmapi.transfermarkt.technology/players?ids[]=74857&ids[]=658536`

> **Not:** Tek bir oyuncu için `https://tmapi.transfermarkt.technology/player/{player_id}` adresi de kullanılabilir. Bu durumda `data` alanı dizi yerine doğrudan tek bir oyuncu objesidir.

### Parametreler

#### Path Parametreleri

Bu endpoint için path parametresi bulunmamaktadır.

#### Query Parametreleri

| Parametre | Tip      | Zorunluluk  | Açıklama                                                                                         |
|:--------- |:-------- |:----------- |:------------------------------------------------------------------------------------------------ |
| `ids[]`   | `string` | **Zorunlu** | Bilgileri alınacak oyuncunun Transfermarkt ID'si. Birden fazla oyuncu için parametre tekrarlanır. |

### Örnek İstek (`cURL`)

`[]` karakterlerinin cURL tarafından yorumlanmaması için `-g` (`--globoff`) parametresi kullanılmalıdır.

```bash
curl -g -X GET "https://tmapi.transfermarkt.technology/players?ids[]=74857&ids[]=658536"
```

### Başarılı Yanıt Örneği (`200 OK`)

Yanıt, `success`, `message` ve `data` alanlarından oluşan bir zarf (envelope) objesidir. `data` dizisindeki her eleman bir oyuncudur. Örnek yanıt kısaltılmıştır.

```json
{
  "success": true,
  "message": "OK",
  "data": [
    {
      "id": "74857",
      "name": "Marc ter Stegen",
      "shortName": "M. ter Stegen",
      "lifeDates": {
        "age": 34,
        "dateOfBirth": "1992-04-30",
        "isDateOfBirthUnknown": false,
        "dateOfDeath": null
      },
      "birthPlaceDetails": {
        "placeOfBirth": "Mönchengladbach",
        "countryOfBirthId": 40,
        "gender": "male"
      },
      "nationalityDetails": {
        "passportName": "Marc-André ter Stegen",
        "nationalities": { "nationalityId": 40, "secondNationalityId": 0 }
      },
      "attributes": {
        "height": 1.87,
        "positionGroup": "GOALKEEPER",
        "positionId": 1,
        "contractUntil": "2027-06-30",
        "preferredFoot": { "id": 2, "name": "right" },
        "outfitter": { "id": 1, "name": "adidas" },
        "position": { "id": 1, "name": "Goalkeeper", "shortName": "GK", "category": "Goalkeeper" },
        "consultantAgency": { "id": 2295, "name": "ROOF", "relativeUrl": "/roof/beraterfirma/berater/2295" }
      },
      "relativeUrl": "/marc-ter-stegen/profil/spieler/74857",
      "ribbon": { "transferId": "6483707", "ribbonType": "ON_LOAN" },
      "portraitUrl": "https://img.a.transfermarkt.technology/portrait/big/74857-1674465246.jpg",
      "marketValueDetails": {
        "current": {
          "value": 3000000,
          "currency": "EUR",
          "compact": { "prefix": "€", "content": "3.00", "suffix": "M" },
          "determined": "2026-06-05"
        },
        "highest": {
          "value": 90000000,
          "currency": "EUR",
          "compact": { "prefix": "€", "content": "90.00", "suffix": "M" },
          "determined": "2019-12-20"
        }
      },
      "clubAssignments": [
        { "playerId": "74857", "clubId": "610", "shirtNumber": 1, "isCaptain": false, "type": "current", "debut": "2026-08-09", "start": "2026-08-04" },
        { "playerId": "74857", "clubId": "3262", "shirtNumber": null, "isCaptain": false, "type": "nationalTeam", "debut": "2012-05-26" }
      ]
    }
  ]
}
```

### Yanıt Verisi Açıklaması

#### Ana Obje Yapısı

| Değişken Adı | Tip       | Açıklama                                            |
|:------------ |:--------- |:--------------------------------------------------- |
| `success`    | `boolean` | İsteğin başarılı olup olmadığı.                     |
| `message`    | `string`  | Durum mesajı (`"OK"`).                              |
| `data`       | `array`   | Oyuncu objelerinin listesi.                         |

---

#### Oyuncu Objesi

| Değişken Adı         | Tip      | Açıklama                                                                                                  | Örnek Değer                               |
|:-------------------- |:-------- |:--------------------------------------------------------------------------------------------------------- |:----------------------------------------- |
| `id`                 | `string` | Oyuncunun Transfermarkt ID'si.                                                                            | `"74857"`                                 |
| `name` / `shortName` | `string` | Oyuncunun tam ve kısa adı.                                                                                | `"Marc ter Stegen"`                       |
| `lifeDates`          | `object` | Yaş (`age`), doğum tarihi (`dateOfBirth`, `YYYY-MM-DD`) ve varsa ölüm tarihi.                            | `{ "age": 34, ... }`                      |
| `birthPlaceDetails`  | `object` | Doğum yeri (`placeOfBirth`), doğduğu ülkenin ID'si (`countryOfBirthId`) ve cinsiyet.                      | `{ "placeOfBirth": "Mönchengladbach" }`   |
| `nationalityDetails` | `object` | Pasaporttaki tam adı ve uyruk ülke ID'leri (`nationalityId`, `secondNationalityId`; yoksa `0`).           | `{ "passportName": "..." }`               |
| `attributes`         | `object` | Fiziksel ve sözleşme bilgileri. Aşağıda detaylandırılmıştır.                                              | `{...}`                                   |
| `relativeUrl`        | `string` | Oyuncunun profil sayfasına giden göreceli link.                                                           | `"/marc-ter-stegen/profil/spieler/74857"` |
| `ribbon`             | `object` | Profilde gösterilen durum etiketi. Örn. `ribbonType: "ON_LOAN"` (kiralık). | `{ "ribbonType": "ON_LOAN" }`             |
| `portraitUrl`        | `string` | Oyuncu fotoğrafının tam URL'si.                                                                           | `"https://img.a.transfermarkt..."`        |
| `marketValueDetails` | `object` | Piyasa değeri bilgileri. Aşağıda detaylandırılmıştır.                                                     | `{...}`                                   |
| `clubAssignments`    | `array`  | Oyuncunun kulüp ve milli takım bağlantıları. Aşağıda detaylandırılmıştır.                                 | `[...]`                                   |
| `nominees` / `participations` | `array` | İncelenen oyuncularda boş dizi olarak döndü; içeriği henüz belgelenmedi.                                         | `[]`                                      |

---

#### `attributes` Objesi

| Değişken Adı       | Tip      | Açıklama                                                                                                  | Örnek Değer         |
|:------------------ |:-------- |:--------------------------------------------------------------------------------------------------------- |:------------------- |
| `height`           | `number` | Boy (metre cinsinden).                                                                                    | `1.87`              |
| `positionGroup`    | `string` | Mevki grubu (örn. `GOALKEEPER`, `FORWARD`).                                     | `"GOALKEEPER"`      |
| `positionId`       | `number` | Mevki ID'si.                                                                                              | `1`                 |
| `position`         | `object` | Mevkinin İngilizce adı, kısaltması ve kategorisi.                                                         | `{ "shortName": "GK" }` |
| `preferredFoot`    | `object` | Tercih ettiği ayak (örn. `right`).                                                             | `{ "name": "right" }` |
| `contractUntil`    | `string` | Mevcut sözleşmesinin bitiş tarihi (`YYYY-MM-DD`).                                                         | `"2027-06-30"`      |
| `outfitter`        | `object` | Oyuncunun kullandığı ekipman markası.                                                                     | `{ "name": "adidas" }` |
| `consultantAgency` | `object` | Oyuncunun menajerlik şirketi (ID, ad, profil linki).                                                      | `{ "name": "ROOF" }` |
| `formerClubsNote`  | `string` | Altyapı kulüpleri gibi ek bilgiler.                                                                       | `"Borussia Mönchengladbach (1996-2010)"` |

---

#### `marketValueDetails` Objesi

`current` (güncel), `previous` (bir önceki) ve `highest` (kariyerindeki en yüksek) alanlarının her biri aynı yapıdadır:

| Değişken Adı | Tip      | Açıklama                                                              | Örnek Değer                                    |
|:------------ |:-------- |:--------------------------------------------------------------------- |:---------------------------------------------- |
| `value`      | `number` | Piyasa değeri (tam sayı).                                             | `3000000`                                      |
| `currency`   | `string` | Para birimi.                                                          | `"EUR"`                                        |
| `compact`    | `object` | Gösterim için kısaltılmış değer.                                      | `{ "prefix": "€", "content": "3.00", "suffix": "M" }` |
| `determined` | `string` | Değerin belirlendiği tarih.                                           | `"2026-06-05"`                                 |

Ek olarak `delta` alanı, önceki değere göre değişimi (`value`, `percentage`, `type`: örn. `DECREASED`) içerir.

---

#### `clubAssignments` Dizisindeki Obje

| Değişken Adı  | Tip      | Açıklama                                                                          | Örnek Değer      |
|:------------- |:-------- |:--------------------------------------------------------------------------------- |:---------------- |
| `clubId`      | `string` | Kulüp veya milli takımın ID'si. Detaylar için [Kulüp Detayları](14-club-details.md) endpoint'i kullanılabilir. | `"610"` |
| `type`        | `string` | Bağlantı tipi: `current` (güncel kulüp), `nationalTeam` (milli takım) vb.        | `"current"`      |
| `shirtNumber` | `number` | Forma numarası. Bilinmiyorsa `null`.                                              | `1`              |
| `isCaptain`   | `boolean`| Takım kaptanı olup olmadığı.                                                      | `false`          |
| `debut`       | `string` | Bu takımdaki ilk maçının tarihi.                                                  | `"2026-08-09"`   |
| `start`       | `string` | Takıma katılış tarihi (varsa).                                                    | `"2026-08-04"`   |

### Veriye Erişim Örneği (JavaScript)

```javascript
async function getPlayersDetails(playerIds) {
  const query = playerIds.map(id => `ids[]=${id}`).join('&');
  const response = await fetch(`https://tmapi.transfermarkt.technology/players?${query}`);
  const { data } = await response.json();

  data.forEach(player => {
    const mv = player.marketValueDetails?.current?.compact;
    console.log(
      `${player.name} | ${player.lifeDates.age} yaş | ${player.attributes.position.shortName} | ` +
      `Sözleşme: ${player.attributes.contractUntil} | Değer: ${mv ? mv.prefix + mv.content + mv.suffix : '-'}`
    );
  });
}

getPlayersDetails(['74857', '658536']);

// Beklenen Çıktı Örneği:
// Marc ter Stegen | 34 yaş | GK | Sözleşme: 2027-06-30 | Değer: €3.00M
// Simon Adingra | ...
```

### Hata Yanıtı Örneği

Geçersiz ID'ler hata döndürmez, sadece yanıttan çıkarılır. Hiçbir ID bulunamazsa `data` boş bir dizi olur.

```json
{ "success": true, "message": "OK", "data": [] }
```
