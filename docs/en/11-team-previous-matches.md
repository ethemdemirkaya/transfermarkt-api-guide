## 11. List a Team's Previous Matches

* **Description:** Based on the given team ID, returns a list of the most recent matches the team has played. The response structure is exactly the same as the other match listing endpoints (player previous/upcoming, team upcoming).
* **Method:** `GET`
* **Endpoint URL:** `/ceapi/previousMatches/team/{team_id}`
* **Full URL Example:** `https://www.transfermarkt.com.tr/ceapi/previousMatches/team/36?limit=25`

### Parameters

#### Path Parameters

| Parameter | Type     | Required     | Description                                                                         |
|:--------- |:-------- |:------------ |:----------------------------------------------------------------------------------- |
| `team_id` | `string` | **Required** | The Transfermarkt ID of the team whose matches will be listed. (e.g. `36` for Fenerbahçe). |

#### Query Parameters

| Parameter | Type     | Required | Description                                                                          |
|:--------- |:-------- |:-------- |:------------------------------------------------------------------------------------ |
| `limit`   | `number` | Optional | Maximum number of matches to return. If not specified, a default value is used (e.g. 25). |

### Sample Request (`cURL`)

```bash
curl -X GET "https://www.transfermarkt.com.tr/ceapi/previousMatches/team/36?limit=5"
```

### Sample Successful Response (`200 OK`)

On a successful request, the endpoint returns a JSON object with `teams` and `matches` keys.

```json
{
  "teams": {
    "36": { "name": "Fenerbahçe", "link": "/fenerbahce-istanbul/startseite/verein/36" },
    "234": { "name": "Feyenoord", "link": "/feyenoord-rotterdam/startseite/verein/234" },
    "11282": { "name": "Alanyaspor", "link": "/alanyaspor/startseite/verein/11282" }
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
    }
  ]
}
```

### Response Fields

The response structure of this endpoint is exactly the same as the one described in [`10-team-upcoming-matches.md`](10-team-upcoming-matches.md). The only difference is the values of the `state` and `result` fields inside the `match` object.

#### Root Object Structure

| Field     | Type     | Description                                                                          |
|:--------- |:-------- |:------------------------------------------------------------------------------------ |
| `teams`   | `object` | A lookup table with team IDs as keys and team information as values.                 |
| `matches` | `array`  | List of objects containing the team's previous matches.                              |

---

#### `match` Object (Match Details)

| Field             | Type     | Description                                                                     | Example Value         |
|:----------------- |:-------- |:------------------------------------------------------------------------------- |:--------------------- |
| `home` / `away`   | `number` | Team IDs. Details are read from the `teams` object.                             | `36`                  |
| `result`          | `string` | The match score. May be `"-:-"` for postponed matches.                          | `"5:2"`               |
| `resultExtension` | `string` | Additional information about the score, e.g. `"PEN"` (penalties).               | `"PEN"`               |
| `state`           | `string` | The match state. Can take values such as `Played`, `Postponed`.                 | `"Played"`            |
| `time`            | `number` | **Unix timestamp** (in seconds) indicating the match kick-off time.             | `1755018000`          |
| `link`            | `string` | Relative link to the match report page.                                         | `"/spielbericht/..."` |

### Data Access Example (JavaScript)

The following code shows how to fetch a team's previous matches.

```javascript
async function getTeamLastMatches(teamId, limit = 10) {
  try {
    const response = await fetch(`https://www.transfermarkt.com.tr/ceapi/previousMatches/team/${teamId}?limit=${limit}`);
    const data = await response.json();

    const teamsLookup = data.teams;
    const matches = data.matches;

    const teamName = teamsLookup[teamId].name;
    console.log(`--- ${teamName} | Previous Matches ---`);

    matches.forEach(m => {
      const homeTeam = teamsLookup[m.match.home].name;
      const awayTeam = teamsLookup[m.match.away].name;

      const matchDate = new Date(m.match.time * 1000).toLocaleDateString('en-GB');

      // Append extra info such as penalties to the score if present
      const fullResult = m.match.resultExtension
        ? `${m.match.result} (${m.match.resultExtension})`
        : m.match.result;

      console.log(
        `${matchDate} | ${m.competition.label} | ${homeTeam} ${fullResult} ${awayTeam} (${m.match.state})`
      );
    });

  } catch (error) {
    console.error("Error while fetching data:", error);
  }
}

// List the last 5 matches of Fenerbahçe (ID: 36)
getTeamLastMatches('36', 5);

// Expected Output Example:
// --- Fenerbahçe | Previous Matches ---
// 12/08/2025 | Şampiyonlar Ligi Elemeleri | Fenerbahçe 5:2 Feyenoord (Played)
// 10/08/2025 | Süper Lig | Fenerbahçe -:- Alanyaspor (Postponed)
// 07/08/2025 | Şampiyonlar Ligi Elemeleri | Feyenoord 2:1 Fenerbahçe (Played)
// 27/05/2025 | Süper Lig | Fenerbahçe 2:1 Konyaspor (Played)
// 22/05/2025 | Süper Lig | Hatayspor 4:2 Fenerbahçe (Played)
```

### Error Response Example

When an invalid `team_id` is sent or the team has no past matches, the API may return a `404 Not Found` status or an empty `matches` array.
