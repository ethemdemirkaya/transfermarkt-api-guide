## 5. Player Performance by Club

* **Description:** Based on the given player ID, returns the player's aggregated performance statistics (matches, goals, assists, etc.) at every club they played for during their career. The data is grouped separately for each club.
* **Method:** `GET`
* **Endpoint URL:** `/ceapi/player/{player_id}/performance`
* **Full URL Example:** `https://www.transfermarkt.com.tr/ceapi/player/433049/performance`

### Parameters

#### Path Parameters

| Parameter   | Type     | Required     | Description                                                                                            |
|:----------- |:-------- |:------------ |:------------------------------------------------------------------------------------------------------ |
| `player_id` | `string` | **Required** | The Transfermarkt ID of the player whose performance data will be fetched. (e.g. `433049` for Youssef En-Nesyri). |

#### Query Parameters

This endpoint has no query parameters.

### Sample Request (`cURL`)

```bash
curl -X GET "https://www.transfermarkt.com.tr/ceapi/player/433049/performance"
```

### Sample Successful Response (`200 OK`)

On a successful request, the endpoint returns a JSON object containing the player's information and a list of per-club performances.

```json
{
  "playerName": "Youssef En-Nesyri",
  "goalkeeper": false,
  "performances": [
    {
      "assists": 8,
      "gamesPlayed": 196,
      "goalsScored": 73,
      "entity": {
        "link": "/fc-sevilla/startseite/verein/368",
        "name": "Sevilla",
        "logo": "https://tmssl.akamaized.net//images/wappen/profil/368.png?lm=1730896593",
        "id": "368"
      }
    },
    {
      "assists": 8,
      "gamesPlayed": 54,
      "goalsScored": 31,
      "entity": {
        "link": "/fenerbahce-istanbul/startseite/verein/36",
        "name": "Fenerbahçe",
        "logo": "https://tmssl.akamaized.net//images/wappen/profil/36.png?lm=1753429185",
        "id": "36"
      }
    },
    {
      "assists": 4,
      "gamesPlayed": 53,
      "goalsScored": 15,
      "entity": {
        "link": "/cd-leganes/startseite/verein/1244",
        "name": "Leganés",
        "logo": "https://tmssl.akamaized.net//images/wappen/profil/1244.png?lm=1422972468",
        "id": "1244"
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

| Field          | Type      | Description                                                                                                                        |
|:-------------- |:--------- |:---------------------------------------------------------------------------------------------------------------------------------- |
| `playerName`   | `string`  | The player's full name.                                                                                                            |
| `goalkeeper`   | `boolean` | Indicates whether the player is a goalkeeper. `false` means an outfield player.                                                    |
| `performances` | `array`   | List of objects containing the player's performance at each club.                                                                  |
| `translations` | `object`  | Contains localized translations of the texts used in the UI (the `headline` field contains "Kulüplere göre performansı" / "Performance by club"). |

---

#### Performance Object in the `performances` Array

Each object in this array represents the aggregated statistics at a single club.

| Field                     | Type     | Description                                                             | Example Value       |
|:------------------------- |:-------- |:----------------------------------------------------------------------- |:------------------- |
| `assists`                 | `number` | Total number of assists at the club.                                    | `8`                 |
| `gamesPlayed`             | `number` | Total number of matches at the club.                                    | `196`               |
| `goalsScored`             | `number` | Total number of goals at the club.                                      | `73`                |
| `entity`                  | `object` | Object containing the club's own information. Detailed below.           | `{...}`             |
| `detailedPerformanceLink` | `string` | Relative link to the player's detailed statistics page for that club.   | `"/.../verein/368"` |

---

#### `entity` Object (Club Information)

| Field  | Type     | Description                                                   | Example Value           |
|:------ |:-------- |:------------------------------------------------------------- |:----------------------- |
| `id`   | `string` | The club's unique Transfermarkt ID. (e.g. `368`, `36`).       | `"368"`                 |
| `name` | `string` | The club's name.                                              | `"Sevilla"`             |
| `link` | `string` | Relative link to the club's Transfermarkt page.               | `"/fc-sevilla/.../368"` |
| `logo` | `string` | Full URL of the club logo.                                    | `"https://.../368.png"` |

### Data Access Example (JavaScript)

The following JavaScript code shows how to list all of a player's career statistics by club.

```javascript
async function getPlayerPerformanceByClub(playerId) {
  try {
    const response = await fetch(`https://www.transfermarkt.com.tr/ceapi/player/${playerId}/performance`);
    if (!response.ok) {
      throw new Error(`Player not found or an error occurred: ${response.status}`);
    }
    const data = await response.json();

    console.log(`--- ${data.playerName} | Club Performance ---`);

    data.performances.forEach(perf => {
      console.log(
        `${perf.entity.name} (ID: ${perf.entity.id}): ${perf.gamesPlayed} Matches, ${perf.goalsScored} Goals, ${perf.assists} Assists`
      );
    });

  } catch (error) {
    console.error("Error while fetching data:", error.message);
  }
}

// Run the function for Youssef En-Nesyri (ID: 433049)
getPlayerPerformanceByClub('433049');

// Expected Output Example:
// --- Youssef En-Nesyri | Club Performance ---
// Sevilla (ID: 368): 196 Matches, 73 Goals, 8 Assists
// Fenerbahçe (ID: 36): 54 Matches, 31 Goals, 8 Assists
// Leganés (ID: 1244): 53 Matches, 15 Goals, 4 Assists
// Málaga (ID: 1084): 41 Matches, 5 Goals, 1 Assists
```

### Error Response Example

When an invalid `player_id` is sent, the API usually responds with a `404 Not Found` status code and an error message.

**`404 Not Found` Response:**

```json
{
  "message": "No player found for id 99999999"
}
```
