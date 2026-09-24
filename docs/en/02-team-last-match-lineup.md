## 2. Get a Team's Last Match Lineup

* **Description:** Based on the given team ID, returns detailed information about the last official match the team played. This includes the match's starting XI, substitutes, tactical formation, head coach and in-match events (goals, cards, substitutions).
* **Method:** `GET`
* **Endpoint URL:** `/ceapi/FinalFormation/ClubId/{club_id}`
* **Full URL Example:** `https://www.transfermarkt.com.tr/ceapi/FinalFormation/ClubId/36`

### Parameters

#### Path Parameters

| Parameter | Type     | Required     | Description                                                                 |
|:--------- |:-------- |:------------ |:--------------------------------------------------------------------------- |
| `club_id` | `string` | **Required** | The Transfermarkt ID of the team to fetch data for. (e.g. `36` for Fenerbahçe). |

#### Query Parameters

This endpoint has no query parameters.

### Sample Request (`cURL`)

```bash
curl -X GET "https://www.transfermarkt.com.tr/ceapi/FinalFormation/ClubId/36"
```

### Sample Successful Response (`200 OK`)

On a successful request, the endpoint returns a complex JSON object. The sample response has been shortened for readability.

```json
{
  "list": {
    "players": [
      {
        "id": "322873",
        "name": "İrfan Can Eğribayat",
        "positionMain": "Kaleci",
        "actions": { "substitution": [], "cards": [], "goals": [] }
      },
      {
        "id": "191614",
        "name": "Fred",
        "positionMain": "Orta saha",
        "actions": {
          "substitution": { "description": "Değişim", /* ... */ },
          "cards": [],
          "goals": [
            {
              "description": "GOL!",
              "score": "3:1",
              "assistByPlayer": "Brown",
              "time": { "minute": "55", "addedTime": "0" }
            }
          ]
        }
      },
      {
        "id": "287579",
        "name": "Sofyan Amrabat",
        "positionMain": "Orta saha",
        "actions": {
          "substitution": [],
          "cards": [
            {
              "description": "Sarı kart",
              "reason": "Faul",
              "type": "gelb",
              "time": { "minute": "21", "addedTime": "0" }
            }
          ],
          "goals": []
        }
      }
    ],
    "substitutes": [ /* ... List of substitute players ... */ ]
  },
  "matchInfo": {
    "competition": { "id": "CLQ", "name": "UEFA Şampiyonlar Ligi Elemeleri" },
    "date": "Sal, 12 Ağu 2025 - 20:00  Saat",
    "tactic": "3-4-1-2"
  },
  "matchReport": {
    "id": "4676660",
    "result": "5:2 "
  },
  "teams": {
    "team1": { "id": "36", "name": "Fenerbahçe" },
    "team2": { "id": "234", "name": "Feyenoord" }
  },
  "trainer": {
    "id": "781",
    "name": "José Mourinho"
  }
}
```

> **Note:** Text values (positions, card descriptions, dates, etc.) are returned in the language of the domain you query. The examples above come from `transfermarkt.com.tr`, so they are in Turkish.

### Response Fields

The returned JSON object contains many sub-objects. The key structures are described below.

#### Root Object Structure

| Field          | Type     | Description                                                           |
|:-------------- |:-------- |:--------------------------------------------------------------------- |
| `list`         | `object` | The main list containing the starting XI (`players`) and substitutes (`substitutes`). |
| `translations` | `object` | Contains translations of the texts used in the UI.                    |
| `matchInfo`    | `object` | General match info such as competition, date and tactic.              |
| `matchReport`  | `object` | Match report ID, link and result.                                     |
| `teams`        | `object` | Information about the two teams that played the match.                |
| `trainer`      | `object` | The team's head coach information.                                    |

---

#### Player Object in `list.players` and `list.substitutes`

| Field                    | Type     | Description                                                               | Example Value                   |
|:------------------------ |:-------- |:------------------------------------------------------------------------- |:------------------------------- |
| `id`                     | `string` | The player's Transfermarkt ID.                                            | `"191614"`                      |
| `name`                   | `string` | The player's full name.                                                   | `"Fred"`                        |
| `shortName`              | `string` | The player's short name.                                                  | `"Fred"`                        |
| `captain`                | `string` | `"x"` if the player is the captain, otherwise empty.                      | `""`                            |
| `number`                 | `string` | Shirt number.                                                             | `"7"`                           |
| `profileUrl`             | `string` | Relative link to the player's profile page.                               | `"/fred/profil/spieler/191614"` |
| `positionMain`           | `string` | The player's position (localized, Turkish on `.com.tr`).                  | `"Orta saha"`                   |
| `positionShort`          | `string` | Abbreviation of the player's position (localized).                        | `"MOS"`                         |
| `styleTop` / `styleLeft` | `number` | CSS values for the player's position in the pitch formation graphic.      | `43`                            |
| `actions`                | `object` | Contains the player's in-match actions (goals, cards, substitutions).     | `{...}`                         |

---

#### `actions` Object

This object holds the player's key moments in the match.

| Field          | Type                 | Description                                                                                                              |
|:-------------- |:-------------------- |:------------------------------------------------------------------------------------------------------------------------ |
| `substitution` | `object` or `array`  | Substitution info. It is an object if the player was subbed off, and also an object if they came on as a substitute. `[]` if empty. |
| `cards`        | `array`              | List of cards the player received. May be empty.                                                                         |
| `goals`        | `array`              | List of goals the player scored. May be empty.                                                                           |

##### `actions.goals` Object

| Field            | Type     | Description                                           | Example Value        |
|:---------------- |:-------- |:----------------------------------------------------- |:-------------------- |
| `description`    | `string` | Description of the event.                             | `"GOL!"`             |
| `score`          | `string` | The score after the goal.                             | `"3:1"`              |
| `goalType`       | `string` | How the goal came about (e.g. corner, pass).          | `"Pas"`              |
| `action`         | `string` | Type of shot (e.g. long-range shot, header).          | `"Uzaktan şut"`      |
| `assistByPlayer` | `string` | Short name of the assisting player. May be empty.     | `"Brown"`            |
| `time`           | `object` | When the goal was scored (`minute`, `addedTime`).     | `{ "minute": "55" }` |

##### `actions.cards` Object

| Field         | Type     | Description                                              | Example Value        |
|:------------- |:-------- |:-------------------------------------------------------- |:-------------------- |
| `description` | `string` | Card type.                                               | `"Sarı kart"`        |
| `reason`      | `string` | Reason for the card.                                     | `"Faul"`             |
| `type`        | `string` | Programmatic name of the card type (`gelb`: yellow).     | `"gelb"`             |
| `time`        | `object` | When the card was shown (`minute`, `addedTime`).         | `{ "minute": "21" }` |

##### `actions.substitution` Object

| Field         | Type     | Description                                  | Example Value        |
|:------------- |:-------- |:-------------------------------------------- |:-------------------- |
| `description` | `string` | Description of the event.                    | `"Değişim"`          |
| `playerIn`    | `string` | Short name of the player coming on.          | `"Yüksek"`           |
| `playerOut`   | `string` | Short name of the player coming off.         | `"Fred"`             |
| `reason`      | `string` | Reason for the substitution.                 | `"Taktik"`           |
| `time`        | `object` | When the substitution was made.              | `{ "minute": "87" }` |

### Data Access Example (JavaScript)

```javascript
async function getMatchDetails(clubId) {
  const response = await fetch(`https://www.transfermarkt.com.tr/ceapi/FinalFormation/ClubId/${clubId}`);
  const data = await response.json();

  console.log(`Head Coach: ${data.trainer.name}`);
  console.log(`Last Match Tactic: ${data.matchInfo.tactic}`);
  console.log(`Opponent: ${data.teams.team2.name}, Score: ${data.matchReport.result}`);

  console.log("\n--- Goal Scorers ---");
  // Check both the starting XI and the substitutes
  const allPlayers = [...data.list.players, ...data.list.substitutes];

  allPlayers.forEach(player => {
    if (player.actions.goals.length > 0) {
      player.actions.goals.forEach(goal => {
        console.log(`- ${player.shortName} (${goal.time.minute}') - Score: ${goal.score}`);
      });
    }
  });
}

// Run the function for Fenerbahçe (ID: 36)
getMatchDetails('36');
```

### Error Response Example

When an invalid `club_id` is sent, the API usually returns an empty response or a `200 OK` status with no content. If a server-side error occurs, a status code such as `500` may also be returned.
