## 7. List a Player's Upcoming Matches

* **Description:** Based on the given player ID, returns a list of the player's upcoming matches (including club and national team). Just like the "Previous Matches" endpoint, the response consists of a `teams` object containing information about all teams appearing in the matches and a `matches` array containing the list of matches.
* **Method:** `GET`
* **Endpoint URL:** `/ceapi/nextMatches/player/{player_id}`
* **Full URL Example:** `https://www.transfermarkt.com.tr/ceapi/nextMatches/player/433049?limit=25`

### Parameters

#### Path Parameters

| Parameter   | Type     | Required     | Description                                                                                      |
|:----------- |:-------- |:------------ |:------------------------------------------------------------------------------------------------ |
| `player_id` | `string` | **Required** | The Transfermarkt ID of the player whose fixtures will be listed. (e.g. `433049` for Youssef En-Nesyri). |

#### Query Parameters

| Parameter | Type     | Required | Description                                                                          |
|:--------- |:-------- |:-------- |:------------------------------------------------------------------------------------ |
| `limit`   | `number` | Optional | Maximum number of matches to return. If not specified, a default value is used (e.g. 25). |

### Sample Request (`cURL`)

```bash
curl -X GET "https://www.transfermarkt.com.tr/ceapi/nextMatches/player/433049?limit=5"
```

### Sample Successful Response (`200 OK`)

On a successful request, the endpoint returns a JSON object with `teams` and `matches` keys.

```json
{
  "teams": {
    "1467": { "name": "Göztepe", "link": "/goztepe/startseite/verein/1467", "isNT": false },
    "36": { "name": "Fenerbahçe", "link": "/fenerbahce-istanbul/startseite/verein/36", "isNT": false },
    "294": { "name": "Benfica", "link": "/benfica-lissabon/startseite/verein/294", "isNT": false }
  },
  "matches": [
    {
      "competition": { "id": "TR1", "label": "Süper Lig" },
      "id": 4646352,
      "match": {
        "away": 36,
        "home": 1467,
        "link": "/spielbericht/index/spielbericht/4646352",
        "result": "-:-",
        "state": "Fixture",
        "time": 1755369000
      }
    },
    {
      "competition": { "id": "CLQ", "label": "Şampiyonlar Ligi Elemeleri" },
      "id": 4697252,
      "match": {
        "away": 294,
        "home": 36,
        "link": "/spielbericht/index/spielbericht/4697252",
        "result": "-:-",
        "state": "Fixture",
        "time": 1755716400
      }
    }
  ]
}
```

### Response Fields

The response structure of this endpoint is exactly the same as the one described in [`06-player-previous-matches.md`](06-player-previous-matches.md). The only difference is the values of the `state` and `result` fields inside the `match` object.

#### Root Object Structure

| Field     | Type     | Description                                                                          |
|:--------- |:-------- |:------------------------------------------------------------------------------------ |
| `teams`   | `object` | A lookup table with team IDs as keys and team information as values.                 |
| `matches` | `array`  | List of objects containing the player's upcoming matches.                            |

---

#### `teams` Object

Contains team information (`name`, `link`, `isNT`, etc.) keyed by team ID. This structure is the same as in the `previousMatches` endpoint.

---

#### `match` Object (Match Details)

| Field           | Type     | Description                                                                          | Example Value         |
|:--------------- |:-------- |:------------------------------------------------------------------------------------ |:--------------------- |
| `home` / `away` | `number` | Team IDs. Details are read from the `teams` object.                                  | `36`                  |
| `result`        | `string` | Always `"-:-"` since the match has not been played yet.                              | `"-:-"`               |
| `state`         | `string` | The match state. For upcoming matches it is usually `"Fixture"` (scheduled).         | `"Fixture"`           |
| `time`          | `number` | **Unix timestamp** (in seconds) indicating the match kick-off time.                  | `1755369000`          |
| `link`          | `string` | Relative link to the match report page.                                              | `"/spielbericht/..."` |

### Data Access Example (JavaScript)

The following code shows how to fetch the upcoming matches list and print team names using the `teams` object.

```javascript
async function getPlayerNextMatches(playerId, limit = 10) {
  try {
    const response = await fetch(`https://www.transfermarkt.com.tr/ceapi/nextMatches/player/${playerId}?limit=${limit}`);
    const data = await response.json();

    const teamsLookup = data.teams;
    const matches = data.matches;

    console.log("--- Upcoming Matches ---");

    matches.forEach(m => {
      const homeTeam = teamsLookup[m.match.home].name;
      const awayTeam = teamsLookup[m.match.away].name;

      const matchDate = new Date(m.match.time * 1000).toLocaleString('en-GB', {
        year: 'numeric', month: 'long', day: 'numeric', hour: '2-digit', minute: '2-digit'
      });

      console.log(
        `${matchDate} | ${m.competition.label} | ${homeTeam} vs ${awayTeam}`
      );
    });

  } catch (error) {
    console.error("Error while fetching data:", error);
  }
}

// List the next 5 matches of Youssef En-Nesyri (ID: 433049)
getPlayerNextMatches('433049', 5);

// Expected Output Example:
// --- Upcoming Matches ---
// 16 August 2025 at 21:30 | Süper Lig | Göztepe vs Fenerbahçe
// 20 August 2025 at 22:00 | Şampiyonlar Ligi Elemeleri | Fenerbahçe vs Benfica
// 24 August 2025 at 22:00 | Süper Lig | Fenerbahçe vs Kocaelispor
// 27 August 2025 at 22:00 | Şampiyonlar Ligi Elemeleri | Benfica vs Fenerbahçe
// 31 August 2025 at 22:00 | Süper Lig | Gençlerbirliği vs Fenerbahçe
```

### Error Response Example

When an invalid `player_id` is sent or the player has no scheduled matches, the API may return a `404 Not Found` status or an empty `matches` array.
