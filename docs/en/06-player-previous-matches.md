## 6. List a Player's Previous Matches

* **Description:** Based on the given player ID, returns a list of the most recent matches the player has played (including club and national team). The response consists of two main parts: a "dictionary" (`teams`) containing information about all teams appearing in the matches, and the list of matches (`matches`). The number of matches returned can be adjusted with the `limit` query parameter.
* **Method:** `GET`
* **Endpoint URL:** `/ceapi/previousMatches/player/{player_id}`
* **Full URL Example:** `https://www.transfermarkt.com.tr/ceapi/previousMatches/player/433049?limit=25`

### Parameters

#### Path Parameters

| Parameter   | Type     | Required     | Description                                                                                     |
|:----------- |:-------- |:------------ |:----------------------------------------------------------------------------------------------- |
| `player_id` | `string` | **Required** | The Transfermarkt ID of the player whose matches will be listed. (e.g. `433049` for Youssef En-Nesyri). |

#### Query Parameters

| Parameter | Type     | Required | Description                                                                          |
|:--------- |:-------- |:-------- |:------------------------------------------------------------------------------------ |
| `limit`   | `number` | Optional | Maximum number of matches to return. If not specified, a default value is used (e.g. 25). |

### Sample Request (`cURL`)

```bash
curl -X GET "https://www.transfermarkt.com.tr/ceapi/previousMatches/player/433049?limit=5"
```

### Sample Successful Response (`200 OK`)

On a successful request, the endpoint returns a JSON object with `teams` and `matches` keys.

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

### Response Fields

#### Root Object Structure

| Field     | Type     | Description                                                                                                                                                  |
|:--------- |:-------- |:------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `teams`   | `object` | A lookup table with team IDs as keys and team information as values. The `home` and `away` IDs in the `matches` list are resolved from this table.          |
| `matches` | `array`  | List of objects containing the player's previous matches.                                                                                                    |

---

#### `teams` Object

This object holds information about all teams appearing in the match list. The object's key is the team's ID.

| Field                 | Type      | Description                                                                               | Example Value                |
|:--------------------- |:--------- |:----------------------------------------------------------------------------------------- |:---------------------------- |
| `name`                | `string`  | The team's name.                                                                          | `"Fenerbahçe"`               |
| `link`                | `string`  | Relative link to the team's profile page.                                                 | `"/fenerbahce-istanbul/..."` |
| `image1x` / `image2x` | `string`  | URLs of the team logo in different resolutions.                                           | `"https://.../36.png"`       |
| `isNT`                | `boolean` | Indicates whether the team is a national team (`National Team`). `true` means it is.      | `false`                      |
| `image`               | `string`  | Full URL of the team crest (the flag for national teams). In current responses `image1x` / `image2x` are `null`, so use this field instead. | `"https://img.a.transfermarkt.technology/..."` |

---

#### Match Object in the `matches` Array

| Field         | Type     | Description                                                          |
|:------------- |:-------- |:-------------------------------------------------------------------- |
| `competition` | `object` | Information about the competition the match was played in (`id`, `label`, `link`). `link` is a full URL. |
| `id`          | `number` | The unique Transfermarkt ID of the match report.                     |
| `match`       | `object` | The actual object containing the match details.                      |
| `integrations` | `array` | External integration data. Returned as an empty array (`[]`) in the responses examined. |

---

#### `match` Object (Match Details)

| Field    | Type     | Description                                                                                                         | Example Value         |
|:-------- |:-------- |:------------------------------------------------------------------------------------------------------------------- |:--------------------- |
| `home`   | `number` | ID of the home team. This ID is used to look up the team name in the `teams` object.                                | `36`                  |
| `away`   | `number` | ID of the away team.                                                                                                | `234`                 |
| `result` | `string` | The match score. May be "-:-" for matches not yet played.                                                           | `"5:2"`               |
| `state`  | `string` | The match state. Can take values such as `Played`, `Postponed`, `Fixture` (scheduled).                                        | `"Played"`            |
| `time`   | `number` | **Unix timestamp** (in seconds) indicating the match kick-off time. It needs to be converted to a readable date.    | `1755018000`          |
| `link`   | `string` | Relative link to the match's detailed report page.                                                                  | `"/spielbericht/..."` |
| `resultExtension` | `string` | Additional score info, e.g. `"PEN"` (decided on penalties). Empty string if none. | `"PEN"` |
| `day`    | `string` | Matchday / round number. | `"7"` |
| `dayLink` | `string` | Relative link to that matchday's fixtures page. | `"/wettbewerb/spieltag/..."` |
| `group`  | `string` | Group or round name (localized, e.g. `"Grup 2"`). `null` if none. | `"Grup 2"` |
| `injury` | `object` | Injury info (`reason`, `link`) if the player missed the match due to injury. Otherwise `null`. | `{ "reason": "Uyluk sakatlığı" }` |
| `suspension` | `object` | Suspension info if the player missed the match due to a suspension. Otherwise `null`. | `null` |

### Data Access Example (JavaScript)

The following code shows how to fetch the match list, print team names using the `teams` object and convert the Unix timestamp to a regular date.

```javascript
async function getPlayerLastMatches(playerId, limit = 10) {
  try {
    const response = await fetch(`https://www.transfermarkt.com.tr/ceapi/previousMatches/player/${playerId}?limit=${limit}`);
    const data = await response.json();

    const teamsLookup = data.teams;
    const matches = data.matches;

    console.log("--- Previous Matches ---");

    matches.forEach(m => {
      const homeTeam = teamsLookup[m.match.home].name;
      const awayTeam = teamsLookup[m.match.away].name;

      // Convert the Unix timestamp to milliseconds and create a Date object
      const matchDate = new Date(m.match.time * 1000).toLocaleDateString('en-GB');

      console.log(
        `${matchDate} | ${m.competition.label} | ${homeTeam} ${m.match.result} ${awayTeam} (${m.match.state})`
      );
    });

  } catch (error) {
    console.error("Error while fetching data:", error);
  }
}

// List the last 5 matches of Youssef En-Nesyri (ID: 433049)
getPlayerLastMatches('433049', 5);

// Expected Output Example:
// --- Previous Matches ---
// 12/08/2025 | Şampiyonlar Ligi Elemeleri | Fenerbahçe 5:2 Feyenoord (Played)
// 10/08/2025 | Süper Lig | Fenerbahçe -:- Alanyaspor (Postponed)
// 07/08/2025 | Şampiyonlar Ligi Elemeleri | Feyenoord 2:1 Fenerbahçe (Played)
// 06/06/2025 | Dostluk Maçları | Fas 1:0 Benin (Played)
// 03/06/2025 | Dostluk Maçları | Fas 2:0 Tunus (Played)
```

### Error Response Example

When an invalid `player_id` is sent, the API usually responds with a `404 Not Found` status code and an error message.
