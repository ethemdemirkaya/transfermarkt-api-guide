## 12. Get a Player's Sorare Card Info

> ⚠️ **This endpoint no longer works.** It returned `404 Not Found` when tested on 2026-09-24.

* **Description:** Based on the given player ID, returns statistics about the player's fantasy football card via Transfermarkt's [Sorare](https://sorare.com) integration. Rather than general football statistics, this endpoint includes performance-based scores used in the Sorare game (e.g. `score_so5`), special metrics such as duels won, and the player's Sorare card image.
* **Method:** `GET`
* **Endpoint URL:** `/ceapi/sorare/fetchPlayersCard/{player_id}`
* **Full URL Example:** `https://www.transfermarkt.com.tr/ceapi/sorare/fetchPlayersCard/396638`

### Parameters

#### Path Parameters

| Parameter   | Type     | Required     | Description                                                                                          |
|:----------- |:-------- |:------------ |:---------------------------------------------------------------------------------------------------- |
| `player_id` | `string` | **Required** | The Transfermarkt ID of the player whose Sorare card info will be fetched. (e.g. `396638` for Manor Solomon). |

#### Query Parameters

This endpoint has no query parameters.

### Sample Request (`cURL`)

```bash
curl -X GET "https://www.transfermarkt.com.tr/ceapi/sorare/fetchPlayersCard/396638"
```

### Sample Successful Response (`200 OK`)

On a successful request, the endpoint returns a JSON object containing the player's Sorare statistics.

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
  "translations": { /* ... UI translations ... */ }
}
```

### Response Fields

The returned JSON object contains the following fields:

| Field                      | Type     | Description                                                                                         | Example Value                     |
|:-------------------------- |:-------- |:--------------------------------------------------------------------------------------------------- |:--------------------------------- |
| `tmv4_player_id`           | `number` | The player's Transfermarkt ID.                                                                      | `396638`                          |
| `score_so5`                | `number` | Sorare's average fantasy score over the last 5 matches. This is one of the game's core metrics.     | `83`                              |
| `matches_played_total`     | `number` | Total number of matches taken into account by Sorare.                                               | `15`                              |
| `matches_played_quota_so5` | `number` | Number of matches played within the last 5-match period.                                            | `1`                               |
| `goals` / `assists`        | `number` | Number of goals and assists in the evaluated period.                                                | `3` / `7`                         |
| `duels_won`                | `number` | Number of duels won.                                                                                | `59`                              |
| `clean_sheet`              | `number` | Number of matches without conceding (only meaningful for defenders and goalkeepers).               | `5`                               |
| `pass_accuracy_quota`      | `number` | Pass accuracy ratio (as a decimal, out of 1.0).                                                     | `0.886051`                        |
| `card_image_url`           | `string` | Full URL of the player's card image on Sorare.                                                      | `"https://assets.sorare.com/..."` |
| `target_url`               | `string` | Full URL to the player's profile page on Sorare.                                                    | `"https://sorare.com/..."`        |
| `last_update_timestamp`    | `string` | When the data was last updated.                                                                     | `"2025-08-14 19:51:41"`           |
| `position`                 | `string` | Abbreviation of the player's position (localized, e.g. SOK = left winger).                          | `"SOK"`                           |
| `translations`             | `object` | Contains localized translations of the texts used in the UI.                                        | `{...}`                           |

### Data Access Example (JavaScript)

The following code shows how to fetch a player's Sorare card info and print it in a meaningful format.

```javascript
async function getSorareCardInfo(playerId) {
  try {
    const response = await fetch(`https://www.transfermarkt.com.tr/ceapi/sorare/fetchPlayersCard/${playerId}`);
    const data = await response.json();

    if (data && data.tmv4_player_id) {
      const passAccuracy = (data.pass_accuracy_quota * 100).toFixed(1);

      console.log(`--- Sorare Card Info (ID: ${data.tmv4_player_id}) ---`);
      console.log(`Sorare Score (Last 5 Matches): ${data.score_so5}`);
      console.log(`Pass Accuracy: ${passAccuracy}%`);
      console.log(`Duels Won: ${data.duels_won}`);
      console.log(`\nCard Image: ${data.card_image_url}`);
      console.log(`Sorare Profile: ${data.target_url}`);
      console.log(`Last Updated: ${data.last_update_timestamp}`);

    } else {
      console.log("Player not found or no Sorare data is available for this player.");
    }

  } catch (error) {
    console.error("Error while fetching data:", error);
  }
}

// Run the function for Manor Solomon (ID: 396638)
getSorareCardInfo('396638');
```

### Error Response Example

If the player ID is invalid or the player has no Sorare card/data, the API may return a `404 Not Found` status or an empty JSON object (`{}`).
