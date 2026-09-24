## 13. Oyuncunun Maç Bazında Performansı

* **Açıklama:** Transfermarkt'ın yeni nesil API'si üzerinden bir oyuncunun kariyeri boyunca kadroda yer aldığı **her bir maç** için ayrıntılı istatistikleri döndürür. Her kayıt; maç bilgileri (müsabaka, sezon, tarih, skor), kulüp/rakip bilgileri ve oyuncunun o maçtaki istatistiklerini (dakika, gol, asist, kart, şut, pas, ikili mücadele, penaltı vb.) içerir. Oynamadığı maçlar da (yedek kulübesi, sakatlık, kadro dışı) listede yer alır. Maçlar en yeniden en eskiye sıralıdır.
* **Method:** `GET`
* **Endpoint URL:** `/player/{player_id}/performance-game`
* **Örnek Tam URL:** `https://tmapi.transfermarkt.technology/player/74857/performance-game`

> ⚠️ **Yanıt boyutu:** Uzun kariyerli oyuncularda yanıt birkaç MB olabilir (örnekteki oyuncu için ~1250 maç, ~2.7 MB). Sonucu mutlaka önbelleğe alın. Sezon filtresi (`seasonId` vb.) denendi ancak yanıtı değiştirmediği görüldü; filtrelemeyi istemci tarafında yapın.

### Parametreler

#### Path Parametreleri

| Parametre   | Tip      | Zorunluluk  | Açıklama                                                                       |
|:----------- |:-------- |:----------- |:------------------------------------------------------------------------------ |
| `player_id` | `string` | **Zorunlu** | Oyuncunun Transfermarkt ID'si. (Örn: `74857` Marc ter Stegen için).            |

#### Query Parametreleri

Bu endpoint için bilinen bir query parametresi bulunmamaktadır.

### Örnek İstek (`cURL`)

```bash
curl -X GET "https://tmapi.transfermarkt.technology/player/74857/performance-game"
```

### Başarılı Yanıt Örneği (`200 OK`)

Örnek yanıt kısaltılmıştır; `performance` dizisinde yalnızca bir maç gösterilmiştir.

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

### Yanıt Verisi Açıklaması

#### `data` Objesi

| Değişken Adı     | Tip      | Açıklama                                                                                         |
|:---------------- |:-------- |:------------------------------------------------------------------------------------------------ |
| `playerId`       | `string` | Oyuncunun ID'si.                                                                                 |
| `performance`    | `array`  | Her bir maç için bir kayıt. En yeni maç ilk sıradadır.                                           |
| `clubIds`        | `array`  | Yanıttaki maçlarda geçen tüm kulüp ID'leri. [Kulüp Detayları](14-club-details.md) ile toplu sorgulanabilir. |
| `coachIds`       | `array`  | Yanıtta geçen tüm teknik direktör ID'leri.                                                       |
| `competitionIds` | `array`  | Yanıtta geçen tüm müsabaka kodları.                                                              |
| `gameIds`        | `array`  | Yanıttaki tüm maç ID'leri.                                                                       |

---

#### `gameInformation` Objesi

| Değişken Adı       | Tip       | Açıklama                                                                                          | Örnek Değer                |
|:------------------ |:--------- |:------------------------------------------------------------------------------------------------- |:-------------------------- |
| `gameId`           | `string`  | Maç ID'si. Maç raporu linki: `/spielbericht/index/spielbericht/{gameId}`.                         | `"4824829"`                |
| `competitionId`    | `string`  | Müsabaka kodu.                                                                                    | `"UNLA"`                   |
| `seasonId`         | `number`  | Sezonun başladığı yıl.                                                                            | `2026`                     |
| `season`           | `object`  | Sezonun görüntülenecek adı (`display`: `"26/27"`).                                                | `{...}`                    |
| `gameDay`          | `number`  | Hafta / tur numarası.                                                                             | `1`                        |
| `gameDuration`     | `number`  | Maçın süresi (dakika).                                                                            | `90`                       |
| `isNationalGame`   | `boolean` | Milli takım maçı olup olmadığı.                                                                   | `true`                     |
| `isGamePostponed`  | `boolean` | Maçın ertelenip ertelenmediği.                                                                    | `false`                    |
| `gameState`        | `string`  | Maçın nasıl bittiği: `regularly_terminated` (normal süre), `extra_time` (uzatma), `penalty_shootout` (penaltılar). | `"regularly_terminated"` |
| `date.dateTimeUTC` | `string`  | Maçın başlangıç zamanı (ISO 8601, UTC).                                                           | `"2026-09-24T18:45:00+00:00"` |
| `refereeId` / `stadiumId` | `number` | Hakem ve stadyum ID'leri.                                                                | `1651`                     |

---

#### `clubsInformation` Objesi

`club` (oyuncunun takımı) ve `opponent` (rakip) aynı yapıdadır:

| Değişken Adı         | Tip      | Açıklama                                                    | Örnek Değer |
|:-------------------- |:-------- |:----------------------------------------------------------- |:----------- |
| `clubId`             | `string` | Takım ID'si.                                                | `"3262"`    |
| `venue`              | `string` | `home` (ev sahibi) veya `away` (deplasman).                 | `"away"`    |
| `goalsTotal`         | `number` | Takımın attığı gol.                                         | `1`         |
| `opponentGoalsTotal` | `number` | Takımın yediği gol.                                         | `1`         |
| `points`             | `number` | Maçtan alınan puan (3 / 1 / 0).                             | `1`         |
| `coachId`            | `string` | Teknik direktör ID'si.                                      | `"118"`     |
| `tacticId`           | `number` | Dizilişin ID'si.                                            | `10`        |
| `clubRank`           | `number` | Takımın sıralaması (varsa, yoksa `null`).                   | `null`      |

---

#### `statistics` Objesi

Oyuncu maçta forma giymediyse sayısal alanların çoğu `null` olur.

| Alt Obje                 | Önemli Alanlar                                                                                                                                              |
|:------------------------ |:----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `generalStatistics`      | `participationState` (`played`, `in squad`, `injured`, `not in squad`), `shirtNumber`, `isCaptain`, `positionId`, `age`, `primaryClubId`, `injuryId`, `absenceId` |
| `goalStatistics`         | `goalsScoredTotal`, `assists`, `ownGoalsScored`, `scoringAttempts`, `scoringAttemptsOnGoal`, `scoringAttemptsOffGoal`, `scoringAttemptsBlocked`, `scoringGoalkeeperSaves` (kaleci kurtarışı), `penaltyShooter*` (penaltı kullanan), `penaltyGoalkeeper*` (penaltıda kaleci), `teamGoalsOnThePitch` / `opponentGoalsOnThePitch` (sahadayken atılan/yenen goller) |
| `cardStatistics`         | `yellowCardNet`, `yellowCardGross`, `fairPlayPoints`, `redCardsRescinded`                                                                                  |
| `playingTimeStatistics`  | `playedMinutes`, `isStarting` (ilk 11'de başladı mı)                                                                                                        |
| `duelStatistics`         | `tackles`, `tacklesWon`, `tacklesLost`, `tacklesWonRatio`, `foulsCommitted`, `foulsGained`, `offsides`                                                      |
| `distributionStatistics` | `passes`, `passesReached`, `passesFailed`, `passesReachedRatio` (yüzde), `corners`, `throwIns`, `goalKicks`                                                 |

### Veriye Erişim Örneği (JavaScript)

Aşağıdaki kod, oyuncunun belirli bir sezondaki maçlarını filtreleyip özet istatistik çıkarır.

```javascript
async function getSeasonSummary(playerId, seasonId) {
  const response = await fetch(`https://tmapi.transfermarkt.technology/player/${playerId}/performance-game`);
  const { data } = await response.json();

  const games = data.performance.filter(p => p.gameInformation.seasonId === seasonId);
  const played = games.filter(p => p.statistics.generalStatistics.participationState === 'played');

  const sum = (fn) => played.reduce((total, p) => total + (fn(p) ?? 0), 0);

  console.log(`Sezon ${games[0]?.gameInformation.season.display ?? seasonId}`);
  console.log(`Kadroda: ${games.length} | Oynadı: ${played.length}`);
  console.log(`Dakika: ${sum(p => p.statistics.playingTimeStatistics.playedMinutes)}`);
  console.log(`Gol: ${sum(p => p.statistics.goalStatistics.goalsScoredTotal)} | Asist: ${sum(p => p.statistics.goalStatistics.assists)}`);
}

// Marc ter Stegen (ID: 74857), 2025/26 sezonu
getSeasonSummary('74857', 2025);
```

### Hata Yanıtı Örneği

Geçersiz bir `player_id` için API `404 Not Found` döndürür:

```json
{ "success": false, "message": "Playerperformancegame not found" }
```
