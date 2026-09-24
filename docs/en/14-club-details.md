## 14. Get Club Details

* **Description:** Returns detailed information about one or more clubs (or national teams) via Transfermarkt's new-generation API. The response includes short name, abbreviation, country, primary league, the parent organisation's address and colours, squad size, average age, total and average market value, and historical crest images. It is ideal for resolving club IDs obtained from other endpoints into names and logos.
* **Method:** `GET`
* **Endpoint URL:** `/clubs?ids[]={club_id}&ids[]={club_id}...`
* **Full URL Example:** `https://tmapi.transfermarkt.technology/clubs?ids[]=3262&ids[]=610`

### Parameters

#### Path Parameters

This endpoint has no path parameters.

#### Query Parameters

| Parameter | Type     | Required     | Description                                                                   |
|:--------- |:-------- |:------------ |:----------------------------------------------------------------------------- |
| `ids[]`   | `string` | **Required** | The club's Transfermarkt ID. Repeat the parameter for multiple clubs.         |

### Sample Request (`cURL`)

```bash
curl -g -X GET "https://tmapi.transfermarkt.technology/clubs?ids[]=3262&ids[]=610"
```

### Sample Successful Response (`200 OK`)

The sample response has been shortened.

```json
{
  "success": true,
  "message": "OK",
  "data": [
    {
      "id": "610",
      "name": "Ajax Amsterdam",
      "baseDetails": {
        "shortName": "Ajax",
        "abbreviation": "AJA",
        "isNationalTeam": false,
        "countryId": 122,
        "mainClubId": "610",
        "primaryCompetitionId": "NL1",
        "superiorClubId": 293,
        "superiorClub": {
          "id": "293",
          "name": "AFC Ajax Amsterdam",
          "location": {
            "countryId": 122,
            "street": "Johan Cruijff Boulevard 1",
            "postcode": "1100 DL",
            "city": "Amsterdam",
            "latitude": 52.373079696011,
            "longitude": 4.8924531787634
          },
          "colors": { "firstColor": "#FF0000", "secondColor": "#FFFFFF", "thirdColor": "" }
        }
      },
      "squadDetails": {
        "squadSize": 28,
        "averageAge": 26.32,
        "averageAgeDisplay": "26.3",
        "averageMarketValue": { "value": 8167857, "currency": "EUR", "compact": { "prefix": "€", "content": "8.17", "suffix": "M" }, "determined": "2026-09-24" },
        "acquisitionValue": { "value": 90650000, "currency": "EUR", "compact": { "prefix": "€", "content": "90.65", "suffix": "M" }, "determined": "2026-09-24" },
        "top18PlayersMarketValue": { "value": 205500000, "currency": "EUR", "compact": { "prefix": "€", "content": "205.50", "suffix": "M" }, "determined": "2026-09-24" },
        "top18SharePercentage": { "value": 89.86, "display": "89,9 %" },
        "currentMarketValue": { "value": 228700000, "currency": "EUR", "compact": { "prefix": "€", "content": "228.70", "suffix": "M" }, "determined": "2026-09-24" }
      },
      "preferences": { "themeId": 0, "clubCode": "AJX" },
      "relativeUrl": "/ajax-amsterdam/startseite/verein/610",
      "isSpecialClub": false,
      "historical": {
        "names": [],
        "images": [
          { "url": "https://img.a.transfermarkt.technology/wappen/big/610.png?lm=1789459204", "name": "610.png", "seasonId": 0 }
        ]
      },
      "identifier": "Ajax Amsterdam (610)",
      "crestUrl": "https://img.a.transfermarkt.technology/wappen/big/610.png?lm=1789459204"
    }
  ]
}
```

*(Note: Market values are updated continuously; the values in the example are as of 2026-09-24.)*

### Response Fields

#### Club Object

| Field          | Type      | Description                                                                 | Example Value                             |
|:-------------- |:--------- |:--------------------------------------------------------------------------- |:----------------------------------------- |
| `id`           | `string`  | The club's Transfermarkt ID.                                                | `"610"`                                   |
| `name`         | `string`  | The club's full name.                                                       | `"Ajax Amsterdam"`                        |
| `baseDetails`  | `object`  | Basic information. Detailed below.                                          | `{...}`                                   |
| `squadDetails` | `object`  | Squad statistics. Detailed below.                                           | `{...}`                                   |
| `relativeUrl`  | `string`  | Relative link to the club's profile page.                                   | `"/ajax-amsterdam/startseite/verein/610"` |
| `crestUrl`     | `string`  | Full URL of the current crest (the flag for national teams).                | `"https://img.a.transfermarkt..."`        |
| `historical`   | `object`  | Former names (`names`) and historical crests by season (`images`).          | `{...}`                                   |
| `identifier`   | `string`  | Identifier in `"Name (ID)"` format.                                         | `"Ajax Amsterdam (610)"`                  |
| `preferences`  | `object`  | Theme ID and club code.                                                     | `{ "clubCode": "AJX" }`                   |
| `metadata`     | `object`  | Record creation/update timestamps.                                          | `{ "updated": "2024-04-30T..." }`         |

---

#### `baseDetails` Object

| Field                  | Type      | Description                                                                                         | Example Value |
|:---------------------- |:--------- |:--------------------------------------------------------------------------------------------------- |:------------- |
| `shortName`            | `string`  | Short name.                                                                                         | `"Ajax"`      |
| `abbreviation`         | `string`  | Three-letter abbreviation.                                                                          | `"AJA"`       |
| `isNationalTeam`       | `boolean` | Whether it is a national team.                                                                      | `false`       |
| `countryId`            | `number`  | Country ID.                                                                                         | `122`         |
| `primaryCompetitionId` | `string`  | Code of the team's primary competition.                                                             | `"NL1"`       |
| `superiorClub`         | `object`  | Parent organisation (club association or federation) with address, coordinates and club colours (`colors`). | `{...}` |

---

#### `squadDetails` Object

| Field                     | Type     | Description                                                          |
|:------------------------- |:-------- |:-------------------------------------------------------------------- |
| `squadSize`               | `number` | Number of players in the squad.                                      |
| `averageAge`              | `number` | Average age of the squad.                                            |
| `currentMarketValue`      | `object` | Total market value of the squad.                                     |
| `averageMarketValue`      | `object` | Average market value per player.                                     |
| `top18PlayersMarketValue` | `object` | Total value of the 18 most valuable players.                         |
| `top18SharePercentage`    | `object` | Share of the 18 most valuable players in the total value (percent).  |
| `acquisitionValue`        | `object` | Total transfer cost of the squad.                                    |

Value objects share the same structure as `marketValueDetails` in the [Player Details](08-player-details.md) document (`value`, `currency`, `compact`, `determined`).

### Data Access Example (JavaScript)

```javascript
async function getClubs(clubIds) {
  const query = clubIds.map(id => `ids[]=${id}`).join('&');
  const response = await fetch(`https://tmapi.transfermarkt.technology/clubs?${query}`);
  const { data } = await response.json();

  data.forEach(club => {
    const mv = club.squadDetails.currentMarketValue.compact;
    console.log(
      `${club.name} (${club.baseDetails.abbreviation}) | League: ${club.baseDetails.primaryCompetitionId} | ` +
      `Squad: ${club.squadDetails.squadSize} | Avg. age: ${club.squadDetails.averageAgeDisplay} | ` +
      `Value: ${mv.prefix}${mv.content}${mv.suffix}`
    );
  });
}

// Germany national team (3262) and Ajax (610)
getClubs(['3262', '610']);
```

### Error Response Example

Invalid IDs do not cause an error; they are omitted from the response. If none of the IDs are found, `data` is an empty array:

```json
{ "success": true, "message": "OK", "data": [] }
```

> **Note:** There is no `/clubs/{club_id}` route for a single club (`404`). Use `ids[]` for a single club as well.
