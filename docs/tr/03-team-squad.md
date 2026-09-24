## 3. Takıma Göre Oyuncu Listesi Getirme

* **Açıklama:** Belirtilen takım ID'sine ait güncel kadrodaki tüm oyuncuların temel bilgilerini (ID, isim, forma numarası, mevki ID'si, link) bir liste olarak döndürür. Bu endpoint, bir takımın tüm oyuncularını listeleyip, oyuncu bazlı detay sorguları için gerekli olan `oyuncu ID`'lerini elde etmek amacıyla kullanılır.
* **Method:** `GET`
* **Endpoint URL:** `/quickselect/players/{club_id}`
* **Örnek Tam URL:** `https://www.transfermarkt.com.tr/quickselect/players/36`

### Parametreler

#### Path Parametreleri

| Parametre | Tip      | Zorunluluk  | Açıklama                                                                       |
|:--------- |:-------- |:----------- |:------------------------------------------------------------------------------ |
| `club_id` | `string` | **Zorunlu** | Kadrosu listelenecek takımın Transfermarkt ID'si. (Örn: `36` Fenerbahçe için). |

#### Query Parametreleri

Bu endpoint için query parametresi bulunmamaktadır.

### Örnek İstek (`cURL`)

```bash
curl -X GET "https://www.transfermarkt.com.tr/quickselect/players/36"
```

### Başarılı Yanıt Örneği (`200 OK`)

Endpoint, başarılı bir istek sonucunda bir JSON dizisi (array) döndürür. Dizideki her bir obje bir oyuncuyu temsil eder.

```json
[
  {
    "id": 205927,
    "name": "Dominik Livakovic",
    "shirtNumber": "40",
    "positionId": 1,
    "link": "/dominik-livakovic/profil/spieler/205927"
  },
  {
    "id": 204069,
    "name": "Milan Škriniar",
    "shirtNumber": "37",
    "positionId": 2,
    "link": "/milan-skriniar/profil/spieler/204069"
  },
  {
    "id": 287579,
    "name": "Sofyan Amrabat",
    "shirtNumber": "34",
    "positionId": 3,
    "link": "/sofyan-amrabat/profil/spieler/287579"
  },
  {
    "id": 649317,
    "name": "Jhon Durán",
    "shirtNumber": "10",
    "positionId": 4,
    "link": "/jhon-duran/profil/spieler/649317"
  }
]
```

### Yanıt Verisi Açıklaması

Dönen JSON dizisindeki her bir obje aşağıdaki alanları içerir:

| Değişken Adı  | Tip      | Açıklama                                                                                                                                         | Örnek Değer                           |
|:------------- |:-------- |:------------------------------------------------------------------------------------------------------------------------------------------------ |:------------------------------------- |
| `id`          | `number` | Oyuncunun Transfermarkt sistemindeki benzersiz ID'sidir. Bu ID, oyuncuya özel diğer verileri (profil, istatistikler vb.) çekmek için kullanılır. | `649317`                              |
| `name`        | `string` | Oyuncunun tam adıdır.                                                                                                                            | `"Jhon Durán"`                        |
| `shirtNumber` | `string` | Oyuncunun forma numarası. String tipindedir.                                                                                                     | `"10"`                                |
| `positionId`  | `number` | Oyuncunun ana mevkisini belirten sayısal ID. Aşağıdaki tabloya bakınız.                                                                          | `4`                                   |
| `link`        | `string` | Oyuncunun Transfermarkt web sitesindeki profil sayfasına yönlendiren göreceli URL yoludur.                                                       | `"/jhon-duran/profil/spieler/649317"` |

#### `positionId` Açıklaması

`positionId` alanı, oyuncunun ana mevki grubunu belirtir.

| ID  | Mevki     |
|:--- |:--------- |
| `1` | Kaleci    |
| `2` | Defans    |
| `3` | Orta Saha |
| `4` | Forvet    |

### Veriye Erişim Örneği (JavaScript)

Aşağıdaki JavaScript kodu, dönen yanıt içerisinden oyuncu bilgilerini almayı ve `positionId`'yi anlamlı bir metne çevirmeyi gösterir.

```javascript
const responseData = [
  { "id": 205927, "name": "Dominik Livakovic", "shirtNumber": "40", "positionId": 1 },
  { "id": 649317, "name": "Jhon Durán", "shirtNumber": "10", "positionId": 4 }
];

const positionMap = {
  1: 'Kaleci',
  2: 'Defans',
  3: 'Orta Saha',
  4: 'Forvet'
};

responseData.forEach(player => {
  const positionName = positionMap[player.positionId] || 'Bilinmiyor';
  console.log(
    `#${player.shirtNumber} - ${player.name} (ID: ${player.id}) - Mevki: ${positionName}`
  );
});

// Çıktı:
// #40 - Dominik Livakovic (ID: 205927) - Mevki: Kaleci
// #10 - Jhon Durán (ID: 649317) - Mevki: Forvet
```

### Hata Yanıtı Örneği

Geçersiz bir `club_id` gönderildiğinde veya ilgili takımda oyuncu bulunmadığında, API genellikle boş bir JSON dizisi (`[]`) ve `200 OK` durum kodu döndürür.
