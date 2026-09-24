## 13. Player Performance per Match

* **Description:** Returns detailed statistics for **every single match** in which a player was part of the matchday squad throughout their career, via Transfermarkt's new-generation API. Each entry contains match information (competition, season, date, score), club/opponent information and the player's statistics for that match (minutes, goals, assists, cards, shots, passes, duels, penalties, etc.). Matches the player did not play in (on the bench, injured, not in squad) are also listed. Matches are sorted from newest to oldest.
* **Method:** `GET`
* **Endpoint URL:** `/player/{player_id}/performance-game`
* **Full URL Example:** `https://tmapi.transfermarkt.technology/player/74857/performance-game`

> ⚠️ **Response size:** For players with long careers the response can be several MB (~1250 matches, ~2.7 MB for the example player). Always cache the result. A season filter (`seasonId` etc.) was tried but did not change the response; filter on the client side.

### Parameters

#### Path Parameters

| Parameter   | Type     | Required     | Description                                                             |
|:----------- |:-------- |:------------ |:----------------------------------------------------------------------- |
| `player_id` | `string` | **Required** | The player's Transfermarkt ID. (e.g. `74857` for Marc ter Stegen).      |

#### Query Parameters

This endpoint has no known query parameters.

### Sample Request (`cURL`)

```bash
curl -X GET "https://tmapi.transfermarkt.technology/player/74857/performance-game"
```

### Sample Successful Response (`200 OK`)

The sample response has been shortened; only one match is shown in the `performance` array.

```json
{
  "success": true,
  "message": "OK",
  "data": {
    "playerId": "74857",
    "performance": [
      {
        "gameInformation": {
          "gameId": "4824829",
          "competitionId": "UNLA",
          "competitionTypeId": 11,
          "competitionGroupId": "2",
          "refereeId": 1651,
          "stadiumId": 159,
          "seasonId": 2026,
          "gameDay": 1,
          "gameDuration": 90,
          "isNationalGame": true,
          "isLiveGame": false,
          "isGameReportCreated": true,
          "isGamePostponed": false,
          "gameState": "regularly_terminated",
          "date": { "dateTimeUTC": "2026-09-24T18:45:00+00:00", "isTimeDefined": true },
          "season": { "id": 2026, "display": "26/27", "cyclicalName": "2027", "nonCyclicalName": "26/27" }
        },
        "clubsInformation": {
          "club": { "venue": "away", "clubId": "3262", "coachId": "118", "goalsTotal": 1, "opponentGoalsTotal": 1, "clubRank": null, "tacticId": 10, "points": 1 },
          "opponent": { "venue": "home", "clubId": "3379", "coachId": "59876", "goalsTotal": 1, "opponentGoalsTotal": 1, "clubRank": null, "tacticId": 16, "points": 1 }
        },
        "statistics": {
          "generalStatistics": { "shirtNumber": 1, "isCaptain": false, "participationState": "played", "positionId": 1, "primaryClubId": 610, "age": 34, "pointsOnThePitch": 1 },
          "goalStatistics": { "goalsScoredTotal": 0, "assists": 0, "ownGoalsScored": 0, "teamGoalsOnThePitch": 1, "opponentGoalsOnThePitch": 1, "scoringAttempts": 0, "scoringGoalkeeperSaves": 9 },
          "cardStatistics": { "yellowCardNet": 0, "yellowCardGross": 0, "fairPlayPoints": 0, "redCardsRescinded": 0 },
          "playingTimeStatistics": { "playedMinutes": 90, "isStarting": true },
          "duelStatistics": { "tackles": 0, "tacklesWon": 0, "foulsCommitted": 0, "foulsGained": 1, "offsides": 0 },
          "distributionStatistics": { "passes": 38, "passesReached": 18, "passesFailed": 20, "passesReachedRatio": 47.4, "goalKicks": 6 }
        }
      }
    ],
    "clubIds": ["2", "3", "4", "..."],
    "coachIds": ["..."],
    "competitionIds": ["17EU", "17WC", "CL", "..."],
    "gameIds": ["..."]
  }
}
```

### Response Fields

#### `data` Object

| Field            | Type     | Description                                                                                          |
|:---------------- |:-------- |:---------------------------------------------------------------------------------------------------- |
| `playerId`       | `string` | The player's ID.                                                                                     |
| `performance`    | `array`  | One entry per match. The most recent match comes first.                                              |
| `clubIds`        | `array`  | All club IDs appearing in the response. Can be resolved in bulk via [Club Details](14-club-details.md). |
| `coachIds`       | `array`  | All coach IDs appearing in the response.                                                             |
| `competitionIds` | `array`  | All competition codes appearing in the response.                                                     |
| `gameIds`        | `array`  | All match IDs in the response.                                                                       |

---

#### `gameInformation` Object

| Field              | Type      | Description                                                                                         | Example Value                 |
|:------------------ |:--------- |:--------------------------------------------------------------------------------------------------- |:----------------------------- |
| `gameId`           | `string`  | Match ID. Match report link: `/spielbericht/index/spielbericht/{gameId}`.                           | `"4824829"`                   |
| `competitionId`    | `string`  | Competition code.                                                                                   | `"UNLA"`                      |
| `seasonId`         | `number`  | The year the season started.                                                                        | `2026`                        |
| `season`           | `object`  | Display name of the season (`display`: `"26/27"`).                                                  | `{...}`                       |
| `gameDay`          | `number`  | Matchday / round number.                                                                            | `1`                           |
| `gameDuration`     | `number`  | Match duration (minutes).                                                                           | `90`                          |
| `isNationalGame`   | `boolean` | Whether it is a national team match.                                                                | `true`                        |
| `isGamePostponed`  | `boolean` | Whether the match was postponed.                                                                    | `false`                       |
| `gameState`        | `string`  | How the match ended: `regularly_terminated` (regular time), `extra_time`, `penalty_shootout`.       | `"regularly_terminated"`      |
| `date.dateTimeUTC` | `string`  | Kick-off time (ISO 8601, UTC).                                                                      | `"2026-09-24T18:45:00+00:00"` |
| `refereeId` / `stadiumId` | `number` | Referee and stadium IDs.                                                                     | `1651`                        |

---

#### `clubsInformation` Object

`club` (the player's team) and `opponent` share the same structure:

| Field                | Type     | Description                                         | Example Value |
|:-------------------- |:-------- |:--------------------------------------------------- |:------------- |
| `clubId`             | `string` | Team ID.                                            | `"3262"`      |
| `venue`              | `string` | `home` or `away`.                                   | `"away"`      |
| `goalsTotal`         | `number` | Goals scored by the team.                           | `1`           |
| `opponentGoalsTotal` | `number` | Goals conceded by the team.                         | `1`           |
| `points`             | `number` | Points earned from the match (3 / 1 / 0).           | `1`           |
| `coachId`            | `string` | Coach ID.                                           | `"118"`       |
| `tacticId`           | `number` | Formation ID.                                       | `10`          |
| `clubRank`           | `number` | The team's rank (if available, otherwise `null`).   | `null`        |

---

#### `statistics` Object

If the player did not play in the match, most numeric fields are `null`.

| Sub-object               | Key Fields                                                                                                                                                  |
|:------------------------ |:----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `generalStatistics`      | `participationState` (`played`, `in squad`, `injured`, `not in squad`), `shirtNumber`, `isCaptain`, `positionId`, `age`, `primaryClubId`, `injuryId`, `absenceId` |
| `goalStatistics`         | `goalsScoredTotal`, `assists`, `ownGoalsScored`, `scoringAttempts`, `scoringAttemptsOnGoal`, `scoringAttemptsOffGoal`, `scoringAttemptsBlocked`, `scoringGoalkeeperSaves` (goalkeeper saves), `penaltyShooter*` (penalty taker), `penaltyGoalkeeper*` (goalkeeper facing penalties), `teamGoalsOnThePitch` / `opponentGoalsOnThePitch` (goals scored/conceded while on the pitch) |
| `cardStatistics`         | `yellowCardNet`, `yellowCardGross`, `fairPlayPoints`, `redCardsRescinded`                                                                                  |
| `playingTimeStatistics`  | `playedMinutes`, `isStarting` (started in the starting XI)                                                                                                  |
| `duelStatistics`         | `tackles`, `tacklesWon`, `tacklesLost`, `tacklesWonRatio`, `foulsCommitted`, `foulsGained`, `offsides`                                                      |
| `distributionStatistics` | `passes`, `passesReached`, `passesFailed`, `passesReachedRatio` (percentage), `corners`, `throwIns`, `goalKicks`                                            |

### Data Access Example (JavaScript)

The following code filters a player's matches for a given season and prints summary statistics.

```javascript
async function getSeasonSummary(playerId, seasonId) {
  const response = await fetch(`https://tmapi.transfermarkt.technology/player/${playerId}/performance-game`);
  const { data } = await response.json();

  const games = data.performance.filter(p => p.gameInformation.seasonId === seasonId);
  const played = games.filter(p => p.statistics.generalStatistics.participationState === 'played');

  const sum = (fn) => played.reduce((total, p) => total + (fn(p) ?? 0), 0);

  console.log(`Season ${games[0]?.gameInformation.season.display ?? seasonId}`);
  console.log(`In squad: ${games.length} | Played: ${played.length}`);
  console.log(`Minutes: ${sum(p => p.statistics.playingTimeStatistics.playedMinutes)}`);
  console.log(`Goals: ${sum(p => p.statistics.goalStatistics.goalsScoredTotal)} | Assists: ${sum(p => p.statistics.goalStatistics.assists)}`);
}

// Marc ter Stegen (ID: 74857), 2025/26 season
getSeasonSummary('74857', 2025);
```

### Error Response Example

For an invalid `player_id`, the API returns `404 Not Found`:

```json
{ "success": false, "message": "Playerperformancegame not found" }
```
