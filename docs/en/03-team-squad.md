## 3. Get Players by Team

* **Description:** Returns the basic information (ID, name, shirt number, position ID, link) of all players in the current squad of the given team ID as a list. This endpoint is used to list all players of a team and obtain the `player ID`s required for player-specific queries.
* **Method:** `GET`
* **Endpoint URL:** `/quickselect/players/{club_id}`
* **Full URL Example:** `https://www.transfermarkt.com.tr/quickselect/players/36`

### Parameters

#### Path Parameters

| Parameter | Type     | Required     | Description                                                                          |
|:--------- |:-------- |:------------ |:------------------------------------------------------------------------------------ |
| `club_id` | `string` | **Required** | The Transfermarkt ID of the team whose squad will be listed. (e.g. `36` for Fenerbahçe). |

#### Query Parameters

This endpoint has no query parameters.

### Sample Request (`cURL`)

```bash
curl -X GET "https://www.transfermarkt.com.tr/quickselect/players/36"
```

### Sample Successful Response (`200 OK`)

On a successful request, the endpoint returns a JSON array. Each object in the array represents a player.

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

### Response Fields

Each object in the returned JSON array contains the following fields:

| Field         | Type     | Description                                                                                                                                  | Example Value                         |
|:------------- |:-------- |:-------------------------------------------------------------------------------------------------------------------------------------------- |:------------------------------------- |
| `id`          | `number` | The player's unique ID in the Transfermarkt system. This ID is used to fetch other player-specific data (profile, statistics, etc.).         | `649317`                              |
| `name`        | `string` | The player's full name.                                                                                                                      | `"Jhon Durán"`                        |
| `shirtNumber` | `string` | The player's shirt number. It is of type string.                                                                                             | `"10"`                                |
| `positionId`  | `number` | Numeric ID indicating the player's main position. See the table below.                                                                       | `4`                                   |
| `link`        | `string` | The relative URL path to the player's profile page on the Transfermarkt website.                                                             | `"/jhon-duran/profil/spieler/649317"` |

#### `positionId` Values

The `positionId` field indicates the player's main position group.

| ID  | Position   |
|:--- |:---------- |
| `1` | Goalkeeper |
| `2` | Defender   |
| `3` | Midfielder |
| `4` | Forward    |

### Data Access Example (JavaScript)

The following JavaScript code shows how to read player information from the response and convert `positionId` into meaningful text.

```javascript
const responseData = [
  { "id": 205927, "name": "Dominik Livakovic", "shirtNumber": "40", "positionId": 1 },
  { "id": 649317, "name": "Jhon Durán", "shirtNumber": "10", "positionId": 4 }
];

const positionMap = {
  1: 'Goalkeeper',
  2: 'Defender',
  3: 'Midfielder',
  4: 'Forward'
};

responseData.forEach(player => {
  const positionName = positionMap[player.positionId] || 'Unknown';
  console.log(
    `#${player.shirtNumber} - ${player.name} (ID: ${player.id}) - Position: ${positionName}`
  );
});

// Output:
// #40 - Dominik Livakovic (ID: 205927) - Position: Goalkeeper
// #10 - Jhon Durán (ID: 649317) - Position: Forward
```

### Error Response Example

When an invalid `club_id` is sent or the team has no players, the API usually returns an empty JSON array (`[]`) with a `200 OK` status code.
