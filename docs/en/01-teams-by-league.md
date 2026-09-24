# Transfermarkt API Documentation

This document describes the unofficial API endpoints that can be used to fetch data from the Transfermarkt website.

---

## 1. Get Teams by League

* **Description:** Returns the basic information (ID, name, link) of the teams belonging to the given league code (such as `TR1`) as a list. This endpoint is typically used to list the teams in a league and obtain team IDs for other API calls.
* **Method:** `GET`
* **Endpoint URL:** `/quickselect/teams/{league_code}`
* **Full URL Example:** `https://www.transfermarkt.com.tr/quickselect/teams/TR1`

### Parameters

#### Path Parameters

| Parameter     | Type     | Required     | Description                                                                                         |
|:------------- |:-------- |:------------ |:--------------------------------------------------------------------------------------------------- |
| `league_code` | `string` | **Required** | The code of the league whose teams will be listed. Example: `TR1` (Turkish Süper Lig), `GB1` (English Premier League). |

#### Query Parameters

This endpoint has no query parameters.

### Sample Request (`cURL`)

```bash
curl -X GET "https://www.transfermarkt.com.tr/quickselect/teams/TR1"
```

### Sample Successful Response (`200 OK`)

On a successful request, the endpoint returns a JSON array. Each object in the array represents a team.

```json
[
  {
    "id": 141,
    "name": "Galatasaray SK",
    "link": "/galatasaray-sk/startseite/verein/141"
  },
  {
    "id": 36,
    "name": "Fenerbahçe SK",
    "link": "/fenerbahce-sk/startseite/verein/36"
  },
  {
    "id": 114,
    "name": "Beşiktaş JK",
    "link": "/besiktas-jk/startseite/verein/114"
  },
  {
    "id": 449,
    "name": "Trabzonspor",
    "link": "/trabzonspor/startseite/verein/449"
  }
]
```

### Response Fields

Each object in the returned JSON array contains the following fields:

| Field  | Type     | Description                                                                                                                                            | Example Value                             |
|:------ |:-------- |:------------------------------------------------------------------------------------------------------------------------------------------------------ |:----------------------------------------- |
| `id`   | `number` | The team's unique ID in the Transfermarkt system. This ID is used to fetch other team-specific data (squad, matches, etc.).                            | `141`                                     |
| `name` | `string` | The team's full name.                                                                                                                                  | `"Galatasaray SK"`                        |
| `link` | `string` | The relative URL path to the team's profile page on the Transfermarkt website. It can be combined with the main domain to build a full URL.            | `"/galatasaray-sk/startseite/verein/141"` |

#### Data Access Example (JavaScript)

The following JavaScript code shows how to get the name and ID of each team from the response.

```javascript
const responseData = [
  {
    "id": 141,
    "name": "Galatasaray SK",
    "link": "/galatasaray-sk/startseite/verein/141"
  },
  {
    "id": 36,
    "name": "Fenerbahçe SK",
    "link": "/fenerbahce-sk/startseite/verein/36"
  }
];

// Loop to list all teams
responseData.forEach(team => {
  console.log(`Team Name: ${team.name}, Team ID: ${team.id}`);
});

// Output:
// Team Name: Galatasaray SK, Team ID: 141
// Team Name: Fenerbahçe SK, Team ID: 36
```

### Error Response Example

When an invalid `league_code` is sent or there are no teams in the given league, the API usually returns an empty JSON array.

**Response for an invalid league code (`XYZ`):** `200 OK`

```json
[]
```
