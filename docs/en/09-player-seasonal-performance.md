## 9. Player Seasonal Performance Details

* **Description:** Based on the given player ID, returns separate performance statistics for each season of the player's career and each competition played in that season. The response is an array with detailed data for each season/competition combination, such as matches, goals, assists, cards and percentage-based statistics. This endpoint is ideal for analysing a player's form in a specific season.
* **Method:** `GET`
* **Endpoint URL:** `/ceapi/player/{player_id}/performance`
* **Full URL Example:** `https://www.transfermarkt.com.tr/ceapi/player/433049/performance`

### Parameters

#### Path Parameters

| Parameter   | Type     | Required     | Description                                                                                            |
|:----------- |:-------- |:------------ |:------------------------------------------------------------------------------------------------------ |
| `player_id` | `string` | **Required** | The Transfermarkt ID of the player whose performance data will be fetched. (e.g. `433049` for Youssef En-Nesyri). |

#### Query Parameters

This endpoint has no visible query parameters, but it may accept additional parameters on the server side, such as a season filter.

### Sample Request (`cURL`)

```bash
curl -X GET "https://www.transfermarkt.com.tr/ceapi/player/433049/performance"
```

### Sample Successful Response (`200 OK`)

On a successful request, the endpoint returns a JSON array in which each element represents the performance in a specific season and competition.

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

*(Note: A second season entry was added to the sample response to show the structure of the array more clearly.)*

### Response Fields

Each object in the returned JSON array represents one season-competition performance and contains the following fields:

| Field                     | Type      | Description                                                                                         | Example Value                  |
|:------------------------- |:--------- |:--------------------------------------------------------------------------------------------------- |:------------------------------ |
| `detailedStatsLink`       | `string`  | Relative link to the detailed statistics page for this performance.                                 | `"/.../saison/2025"`           |
| `competitionDescription`  | `string`  | The competition's full name.                                                                        | `"Şampiyonlar Ligi Elemeleri"` |
| `logo`                    | `string`  | Full URL of the competition logo.                                                                   | `"https://.../clq.png"`        |
| `nameSeason`              | `string`  | The season the performance belongs to (e.g. 25/26).                                                 | `"25/26"`                      |
| `possibleGames`           | `number`  | Maximum number of matches that could be played in that competition that season.                    | `2`                            |
| `gamesPlayed`             | `number`  | Number of matches the player played.                                                                | `2`                            |
| `goalsScored`             | `number`  | Number of goals scored.                                                                             | `1`                            |
| `assists`                 | `number`  | Number of assists.                                                                                  | `1`                            |
| `yellowCards`             | `number`  | Number of yellow cards received.                                                                    | `0`                            |
| `secondYellowCards`       | `number`  | Number of second-yellow (yellow-red) cards.                                                         | `0`                            |
| `redCards`                | `number`  | Number of straight red cards.                                                                       | `0`                            |
| `startElevenPercent`      | `number`  | Percentage of the player's appearances in which they started in the starting XI.                    | `100`                          |
| `minutesPlayedPercent`    | `number`  | Percentage of the total possible minutes the player spent on the pitch.                             | `96.67`                        |
| `goalsContributedPercent` | `number`  | Percentage of the team's goals the player contributed to (via a goal or an assist).                 | `33.33`                        |
| `goalkeeper`              | `boolean` | Whether the player is a goalkeeper.                                                                 | `false`                        |
| `minutesPlayed`           | `number`  | Total minutes played in that competition that season.                                              | `174`                          |

### Data Access Example (JavaScript)

The following JavaScript code shows how to fetch and process a player's season-by-season performance breakdown.

```javascript
async function getPlayerSeasonalPerformance(playerId) {
  try {
    const response = await fetch(`https://www.transfermarkt.com.tr/ceapi/player/${playerId}/performance`);
    const data = await response.json();

    if (data && data.length > 0) {
      console.log(`--- Seasonal Performance Breakdown ---`);
      data.forEach(perf => {
        console.log(`\n> Season: ${perf.nameSeason} | Competition: ${perf.competitionDescription}`);
        console.log(`  Matches: ${perf.gamesPlayed}/${perf.possibleGames} | Minutes: ${perf.minutesPlayed}'`);
        console.log(`  Goals: ${perf.goalsScored} | Assists: ${perf.assists}`);
        console.log(`  Cards (Y/Y-R/R): ${perf.yellowCards}/${perf.secondYellowCards}/${perf.redCards}`);
      });
    } else {
      console.log("No seasonal performance data found for the player.");
    }

  } catch (error) {
    console.error("Error while fetching data:", error);
  }
}

// Run the function for Youssef En-Nesyri (ID: 433049)
getPlayerSeasonalPerformance('433049');
```

### Error Response Example

When an invalid `player_id` is sent or the player has no matches, the API may return a `404 Not Found` status or an empty JSON array (`[]`).
