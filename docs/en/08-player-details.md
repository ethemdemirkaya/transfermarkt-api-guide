## 8. Get Player Details

* **Description:** Returns detailed profile information for one or more players via Transfermarkt's new-generation API (`tmapi.transfermarkt.technology`). The response includes birth details, nationality, height, preferred foot, position, contract expiry date, agency, current and highest market value, and club/national team assignments. Since multiple players can be queried in a single request, it is ideal for bulk data retrieval.
* **Method:** `GET`
* **Endpoint URL:** `/players?ids[]={player_id}&ids[]={player_id}...`
* **Full URL Example:** `https://tmapi.transfermarkt.technology/players?ids[]=74857&ids[]=658536`

> **Note:** For a single player, `https://tmapi.transfermarkt.technology/player/{player_id}` can also be used. In that case, the `data` field is a single player object instead of an array.

### Parameters

#### Path Parameters

This endpoint has no path parameters.

#### Query Parameters

| Parameter | Type     | Required     | Description                                                                          |
|:--------- |:-------- |:------------ |:------------------------------------------------------------------------------------ |
| `ids[]`   | `string` | **Required** | The Transfermarkt ID of the player. Repeat the parameter for multiple players.       |

### Sample Request (`cURL`)

Use the `-g` (`--globoff`) flag so that cURL does not interpret the `[]` characters.

```bash
curl -g -X GET "https://tmapi.transfermarkt.technology/players?ids[]=74857&ids[]=658536"
```

### Sample Successful Response (`200 OK`)

The response is an envelope object with `success`, `message` and `data` fields. Each element in the `data` array is a player. The sample response has been shortened.

```json
{
  "success": true,
  "message": "OK",
  "data": [
    {
      "id": "74857",
      "name": "Marc ter Stegen",
      "shortName": "M. ter Stegen",
      "lifeDates": {
        "age": 34,
        "dateOfBirth": "1992-04-30",
        "isDateOfBirthUnknown": false,
        "dateOfDeath": null
      },
      "birthPlaceDetails": {
        "placeOfBirth": "Mönchengladbach",
        "countryOfBirthId": 40,
        "gender": "male"
      },
      "nationalityDetails": {
        "passportName": "Marc-André ter Stegen",
        "nationalities": { "nationalityId": 40, "secondNationalityId": 0 }
      },
      "attributes": {
        "height": 1.87,
        "positionGroup": "GOALKEEPER",
        "positionId": 1,
        "contractUntil": "2027-06-30",
        "preferredFoot": { "id": 2, "name": "right" },
        "outfitter": { "id": 1, "name": "adidas" },
        "position": { "id": 1, "name": "Goalkeeper", "shortName": "GK", "category": "Goalkeeper" },
        "consultantAgency": { "id": 2295, "name": "ROOF", "relativeUrl": "/roof/beraterfirma/berater/2295" }
      },
      "relativeUrl": "/marc-ter-stegen/profil/spieler/74857",
      "ribbon": { "transferId": "6483707", "ribbonType": "ON_LOAN" },
      "portraitUrl": "https://img.a.transfermarkt.technology/portrait/big/74857-1674465246.jpg",
      "marketValueDetails": {
        "current": {
          "value": 3000000,
          "currency": "EUR",
          "compact": { "prefix": "€", "content": "3.00", "suffix": "M" },
          "determined": "2026-06-05"
        },
        "highest": {
          "value": 90000000,
          "currency": "EUR",
          "compact": { "prefix": "€", "content": "90.00", "suffix": "M" },
          "determined": "2019-12-20"
        }
      },
      "clubAssignments": [
        { "playerId": "74857", "clubId": "610", "shirtNumber": 1, "isCaptain": false, "type": "current", "debut": "2026-08-09", "start": "2026-08-04" },
        { "playerId": "74857", "clubId": "3262", "shirtNumber": null, "isCaptain": false, "type": "nationalTeam", "debut": "2012-05-26" }
      ]
    }
  ]
}
```

### Response Fields

#### Root Object Structure

| Field     | Type      | Description                           |
|:--------- |:--------- |:------------------------------------- |
| `success` | `boolean` | Whether the request succeeded.        |
| `message` | `string`  | Status message (`"OK"`).              |
| `data`    | `array`   | List of player objects.               |

---

#### Player Object

| Field                | Type     | Description                                                                                          | Example Value                             |
|:-------------------- |:-------- |:---------------------------------------------------------------------------------------------------- |:----------------------------------------- |
| `id`                 | `string` | The player's Transfermarkt ID.                                                                       | `"74857"`                                 |
| `name` / `shortName` | `string` | The player's full and short name.                                                                    | `"Marc ter Stegen"`                       |
| `lifeDates`          | `object` | Age (`age`), date of birth (`dateOfBirth`, `YYYY-MM-DD`) and date of death if applicable.            | `{ "age": 34, ... }`                      |
| `birthPlaceDetails`  | `object` | Place of birth (`placeOfBirth`), country of birth ID (`countryOfBirthId`) and gender.                | `{ "placeOfBirth": "Mönchengladbach" }`   |
| `nationalityDetails` | `object` | Full passport name and nationality country IDs (`nationalityId`, `secondNationalityId`; `0` if none). | `{ "passportName": "..." }`              |
| `attributes`         | `object` | Physical and contract information. Detailed below.                                                   | `{...}`                                   |
| `relativeUrl`        | `string` | Relative link to the player's profile page.                                                          | `"/marc-ter-stegen/profil/spieler/74857"` |
| `ribbon`             | `object` | Status label shown on the profile, e.g. `ribbonType: "ON_LOAN"`.                                     | `{ "ribbonType": "ON_LOAN" }`             |
| `portraitUrl`        | `string` | Full URL of the player's photo.                                                                      | `"https://img.a.transfermarkt..."`        |
| `marketValueDetails` | `object` | Market value information. Detailed below.                                                            | `{...}`                                   |
| `clubAssignments`    | `array`  | The player's club and national team assignments. Detailed below.                                     | `[...]`                                   |
| `nominees` / `participations` | `array` | Returned as empty arrays for the players examined; contents not yet documented.            | `[]`                                      |

---

#### `attributes` Object

| Field              | Type     | Description                                                          | Example Value            |
|:------------------ |:-------- |:-------------------------------------------------------------------- |:------------------------ |
| `height`           | `number` | Height (in metres).                                                  | `1.87`                   |
| `positionGroup`    | `string` | Position group (e.g. `GOALKEEPER`, `FORWARD`).                       | `"GOALKEEPER"`           |
| `positionId`       | `number` | Position ID.                                                         | `1`                      |
| `position`         | `object` | English name, abbreviation and category of the position.             | `{ "shortName": "GK" }`  |
| `preferredFoot`    | `object` | Preferred foot (e.g. `right`).                                       | `{ "name": "right" }`    |
| `contractUntil`    | `string` | Expiry date of the current contract (`YYYY-MM-DD`).                  | `"2027-06-30"`           |
| `outfitter`        | `object` | The player's kit supplier brand.                                     | `{ "name": "adidas" }`   |
| `consultantAgency` | `object` | The player's agency (ID, name, profile link).                        | `{ "name": "ROOF" }`     |
| `formerClubsNote`  | `string` | Additional info such as youth clubs.                                 | `"Borussia Mönchengladbach (1996-2010)"` |

---

#### `marketValueDetails` Object

The `current`, `previous` and `highest` (career high) fields all share the same structure:

| Field        | Type     | Description                                  | Example Value                                         |
|:------------ |:-------- |:-------------------------------------------- |:----------------------------------------------------- |
| `value`      | `number` | Market value (integer).                      | `3000000`                                             |
| `currency`   | `string` | Currency.                                    | `"EUR"`                                               |
| `compact`    | `object` | Shortened value for display.                 | `{ "prefix": "€", "content": "3.00", "suffix": "M" }` |
| `determined` | `string` | Date the value was determined.               | `"2026-06-05"`                                        |

In addition, the `delta` field contains the change compared to the previous value (`value`, `percentage`, `type`: e.g. `DECREASED`).

---

#### Object in the `clubAssignments` Array

| Field         | Type      | Description                                                                                 | Example Value  |
|:------------- |:--------- |:------------------------------------------------------------------------------------------- |:-------------- |
| `clubId`      | `string`  | Club or national team ID. Use the [Club Details](14-club-details.md) endpoint for details.   | `"610"`        |
| `type`        | `string`  | Assignment type: `current` (current club), `nationalTeam`, etc.                             | `"current"`    |
| `shirtNumber` | `number`  | Shirt number. `null` if unknown.                                                            | `1`            |
| `isCaptain`   | `boolean` | Whether the player is the team captain.                                                     | `false`        |
| `debut`       | `string`  | Date of the player's first match for this team.                                             | `"2026-08-09"` |
| `start`       | `string`  | Date the player joined the team (if available).                                             | `"2026-08-04"` |

### Data Access Example (JavaScript)

```javascript
async function getPlayersDetails(playerIds) {
  const query = playerIds.map(id => `ids[]=${id}`).join('&');
  const response = await fetch(`https://tmapi.transfermarkt.technology/players?${query}`);
  const { data } = await response.json();

  data.forEach(player => {
    const mv = player.marketValueDetails?.current?.compact;
    console.log(
      `${player.name} | Age ${player.lifeDates.age} | ${player.attributes.position.shortName} | ` +
      `Contract: ${player.attributes.contractUntil} | Value: ${mv ? mv.prefix + mv.content + mv.suffix : '-'}`
    );
  });
}

getPlayersDetails(['74857', '658536']);

// Expected Output Example:
// Marc ter Stegen | Age 34 | GK | Contract: 2027-06-30 | Value: €3.00M
// Simon Adingra | ...
```

### Error Response Example

Invalid IDs do not cause an error; they are simply omitted from the response. If none of the IDs are found, `data` is an empty array.

```json
{ "success": true, "message": "OK", "data": [] }
```
