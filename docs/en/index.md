# Unofficial Transfermarkt API Documentation

This project aims to document the non-public (private) API endpoints used by the [Transfermarkt](https://www.transfermarkt.com.tr) website.

This documentation was created **for educational and research purposes** to help developers and data enthusiasts understand how Transfermarkt data can be accessed programmatically.

---

## 🚨 IMPORTANT WARNING AND DISCLAIMER 🚨

> It is very important that you carefully read and understand the following points before using this project.

* **UNOFFICIAL PROJECT:** This project has **no official affiliation** with Transfermarkt GmbH & Co. KG. It is a community-driven project.
* **TERMS OF USE VIOLATION:** Using these APIs **may violate** Transfermarkt's [Terms of Use](https://www.transfermarkt.com.tr/mvc/main/index/datenschutz). Crawling the site by automated means (scraping) or using APIs without permission is generally against service agreements.
* **ALL RESPONSIBILITY LIES WITH THE USER:** Any legal, ethical or technical liability arising from the use of these APIs rests entirely with you. By using this project, you accept this condition.
* **RISK OF CHANGE:** Since these are private APIs, Transfermarkt may **change or completely shut down** their URL structures, response formats or access methods **at any time, without notice.** Projects relying on this documentation may suddenly stop working.
* **SERVER LOAD:** Please **do not overload** Transfermarkt's servers. Irresponsible and heavy usage can degrade the site's quality of service. Always follow responsible usage principles.
* **DATA OWNERSHIP:** Ownership and copyright of all data, logos and names accessed through these APIs **belong entirely to Transfermarkt.**

---

## Table of Contents

1. [Teams by League](01-teams-by-league.md)
2. [Team's Last Match Lineup](02-team-last-match-lineup.md)
3. [Team Squad](03-team-squad.md)
4. [Player Performance by Competition](04-player-performance-by-competition.md)
5. [Player Performance by Club](05-player-performance-by-club.md)
6. [Player's Previous Matches](06-player-previous-matches.md)
7. [Player's Upcoming Matches](07-player-upcoming-matches.md)
8. Player Details *(not yet documented)*
9. [Player Seasonal Performance Details](09-player-seasonal-performance.md)
10. [Team's Upcoming Matches](10-team-upcoming-matches.md)
11. [Team's Previous Matches](11-team-previous-matches.md)
12. [Player's Sorare Card Info](12-player-sorare-card.md)

## Responsible Usage Principles

To show respect for Transfermarkt and the community, please follow these rules:

* **Rate Limiting:** Never send too many requests in a short period of time. Add reasonable delays between your requests (for example, at most 1 request per second).
* **Caching:** Instead of fetching the same data over and over, cache the results locally (on your device or server) for a certain period. This is especially important for data that rarely changes, such as team lists or player profiles.
* **Set a User-Agent:** Send a `User-Agent` in your request `header` that identifies you or your project. This provides transparency and makes it easier to contact you in case of a problem. Example: `User-Agent: MyAwesomeFootballApp/1.0 (https://github.com/your-username/your-project)`.
* **Fetch Only What You Need:** Avoid sending requests to endpoints or data you don't need.

## API Documentation

The detailed description, parameters, sample responses and usage scenarios of each endpoint can be found in the corresponding markdown files.

### 1. Get Teams by League

This endpoint returns basic information about all teams in a league.

> See [`01-teams-by-league.md`](01-teams-by-league.md) for details.

### 2. Get a Team's Last Match Lineup

Returns the lineup, tactics and in-match events of the last match a team played.

> See [`02-team-last-match-lineup.md`](02-team-last-match-lineup.md) for details.

### 3. Get Players by Team

Lists all players in a team's current squad.

> See [`03-team-squad.md`](03-team-squad.md) for details.

### 4. Player Performance by Competition

Presents all of a player's career statistics grouped by competition.

> See [`04-player-performance-by-competition.md`](04-player-performance-by-competition.md) for details.

### 5. Player Performance by Club

Presents all of a player's career statistics grouped by club.

> See [`05-player-performance-by-club.md`](05-player-performance-by-club.md) for details.

### 6. List a Player's Previous Matches

Lists the most recent matches a player has played.

> See [`06-player-previous-matches.md`](06-player-previous-matches.md) for details.

### 7. List a Player's Upcoming Matches

Lists a player's upcoming matches (fixtures).

> See [`07-player-upcoming-matches.md`](07-player-upcoming-matches.md) for details.

### 8. Get Player Details

Returns detailed profile information for one or more players via a modern API.

> Documentation for this endpoint is not yet available.

### 9. Player Seasonal Performance Details

Lists a player's performance in detail, broken down by season and competition.

> See [`09-player-seasonal-performance.md`](09-player-seasonal-performance.md) for details.

### 10. List a Team's Upcoming Matches

Lists a team's upcoming matches (fixtures).

> See [`10-team-upcoming-matches.md`](10-team-upcoming-matches.md) for details.

### 11. List a Team's Previous Matches

Lists the most recent matches a team has played.

> See [`11-team-previous-matches.md`](11-team-previous-matches.md) for details.

### 12. Get a Player's Sorare Card Info

Returns a player's card information and special statistics on the [Sorare](https://sorare.com) fantasy football platform.

> See [`12-player-sorare-card.md`](12-player-sorare-card.md) for details.

## Contributing

If you discover new endpoints, find an error in the existing documentation or would like to suggest improvements, please open an "Issue" or send a "Pull Request". Your contributions are welcome.

## License

This project is licensed under the [MIT License](https://github.com/ethemdemirkaya/transfermarkt-api-guide/blob/main/LICENSE). This means you can use the code as you wish, but the project comes with no warranty and its authors cannot be held liable for any damages.
