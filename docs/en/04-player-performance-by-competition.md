## 4. Player Performance by Competition

* **Description:** Based on the given player ID, returns the player's aggregated performance statistics (matches, goals, assists, etc.) across all official competitions played during their career. The data is grouped separately for each competition.
* **Method:** `GET`
* **Endpoint URL:** `/ceapi/player/{player_id}/performancepercompetition`
* **Full URL Example:** `https://www.transfermarkt.com.tr/ceapi/player/433049/performancepercompetition`

### Parameters

#### Path Parameters

| Parameter   | Type     | Required     | Description                                                                                            |
|:----------- |:-------- |:------------ |:------------------------------------------------------------------------------------------------------ |
| `player_id` | `string` | **Required** | The Transfermarkt ID of the player whose performance data will be fetched. (e.g. `433049` for Youssef En-Nesyri). |

#### Query Parameters

This endpoint has no query parameters.

### Sample Request (`cURL`)

```bash
curl -X GET "https://www.transfermarkt.com.tr/ceapi/player/433049/performancepercompetition"
```

### Sample Successful Response (`200 OK`)

On a successful request, the endpoint returns a JSON object containing the player's information and a list of per-competition performances.

```json
{
  "playerName": "Youssef En-Nesyri",
  "goalkeeper": false,
  "performances": [
    {
      "assists": 6,
      "gamesPlayed": 34,
      "goalsScored": 20,
      "entity": {
        "link": "/super-lig/startseite/wettbewerb/TR1",
        "name": "Süper Lig",
        "logo": "https://tmssl.akamaized.net//images/logo/mediumsmall/tr1.png?lm=1723019495",
        "id": "TR1"
      }
    },
    {
      "assists": 1,
      "gamesPlayed": 31,
      "goalsScored": 12,
      "entity": {
        "link": "/uefa-avrupa-ligi/startseite/wettbewerb/EL",
        "name": "Avrupa Ligi",
        "logo": "https://tmssl.akamaized.net//images/logo/mediumsmall/el.png?lm=1721915137",
        "id": "EL"
      }
    },
    {
      "assists": 2,
      "gamesPlayed": 20,
      "goalsScored": 10,
      "entity": {
        "link": "/uefa-sampiyonlar-ligi/startseite/wettbewerb/CL",
        "name": "Şampiyonlar Ligi",
        "logo": "https://tmssl.akamaized.net//images/logo/mediumsmall/cl.png?lm=1626810555",
        "id": "CL"
      }
    }
  ],
  "translations": {
    /* ... UI translations ... */
  }
}
```

### Response Fields

#### Root Object Structure

| Field          | Type      | Description                                                                                                                                                  |
|:-------------- |:--------- |:------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `playerName`   | `string`  | The player's full name.                                                                                                                                      |
| `goalkeeper`   | `boolean` | Indicates whether the player is a goalkeeper. `false` means an outfield player. This field is important for interpreting fields such as `cleanSheets` and `concededGoals`. |
| `performances` | `array`   | List of objects containing the player's performance in each competition.                                                                                     |
| `translations` | `object`  | Contains localized translations of the texts used in the UI.                                                                                                 |

---

#### Performance Object in the `performances` Array

Each object in this array represents the aggregated statistics in a single competition.

| Field                     | Type     | Description                                                                    | Example Value           |
|:------------------------- |:-------- |:------------------------------------------------------------------------------ |:----------------------- |
| `assists`                 | `number` | Total number of assists in the competition.                                    | `6`                     |
| `cleanSheets`             | `number` | Number of matches without conceding a goal (meaningful for goalkeepers).       | `0`                     |
| `gamesPlayed`             | `number` | Total number of matches in the competition.                                    | `34`                    |
| `goalsScored`             | `number` | Total number of goals in the competition.                                      | `20`                    |
| `concededGoals`           | `number` | Total number of goals conceded (meaningful for goalkeepers).                   | `0`                     |
| `entity`                  | `object` | Object containing the competition's own information. Detailed below.           | `{...}`                 |
| `detailedPerformanceLink` | `string` | Relative link to the player's detailed statistics page for that competition.   | `"/.../wettbewerb/TR1"` |

---

#### `entity` Object (Competition Information)

| Field  | Type     | Description                                              | Example Value           |
|:------ |:-------- |:-------------------------------------------------------- |:----------------------- |
| `id`   | `string` | The competition's unique code. (e.g. `TR1`, `CL`).       | `"TR1"`                 |
| `name` | `string` | The competition's full name.                             | `"Süper Lig"`           |
| `link` | `string` | Relative link to the competition's Transfermarkt page.   | `"/super-lig/.../TR1"`  |
| `logo` | `string` | Full URL of the competition logo.                        | `"https://.../tr1.png"` |

### Data Access Example (JavaScript)

The following JavaScript code shows how to list all of a player's career statistics by competition.

```javascript
async function getPlayerPerformance(playerId) {
  try {
    const response = await fetch(`https://www.transfermarkt.com.tr/ceapi/player/${playerId}/performancepercompetition`);
    if (!response.ok) {
      throw new Error(`Player not found or an error occurred: ${response.status}`);
    }
    const data = await response.json();

    console.log(`--- ${data.playerName} | Career Performance ---`);

    data.performances.forEach(perf => {
      // Only show competitions with at least 1 appearance
      if (perf.gamesPlayed > 0) {
        console.log(
          `${perf.entity.name}: ${perf.gamesPlayed} Matches, ${perf.goalsScored} Goals, ${perf.assists} Assists`
        );
      }
    });

  } catch (error) {
    console.error("Error while fetching data:", error.message);
  }
}

// Run the function for Youssef En-Nesyri (ID: 433049)
getPlayerPerformance('433049');

// Expected Output Example:
// --- Youssef En-Nesyri | Career Performance ---
// LaLiga: 230 Matches, 69 Goals, 10 Assists
// Süper Lig: 34 Matches, 20 Goals, 6 Assists
// Avrupa Ligi: 31 Matches, 12 Goals, 1 Assists
// ...other competitions
```

### Error Response Example

When an invalid `player_id` is sent, the API usually responds with a `404 Not Found` status code and an error message.

**`404 Not Found` Response:**

```json
{
  "message": "No player found for id 99999999"
}
```
