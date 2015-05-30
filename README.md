# Tournament results (Swiss pairings system)

## Description
Database model and a bunch of methods which could be used to implemente a game tournament that uses the Swiss pairings system. This system is used for pairing up players in each round: players are not eliminated, and each player should be paired with another player with the same number of wins, or as close as possible.

## Requirements
* Postgresql
* [*psycopg2*](http://initd.org/psycopg/docs/install.html) python's postgresql library

## Installation
First of all, you will need to create a database called *tournament*.
Choose your preferred way to create such database in Postgres, for instance (UNIX based OS command line):

`$ createdb tournament`

Then, connect to the fresh created database:

`$ psql tournament`

And execute SQL's script:

`tournament=> \i tournament.sql `

Output should be:

```
CREATE TABLE
CREATE TABLE
CREATE VIEW
CREATE VIEW
CREATE VIEW
CREATE VIEW
CREATE VIEW
```

And you will end with a schema like this:

| Schema        | Name           | Type  |
| ------------- |:-------------| :-----|
| public      | matches | table |
| public      | matches_id_seq      |   sequence |
| public      | player_standings     |    view |
| public | player_standings_even | view  |
| public | player_standings_odd  | view    |
| public | players               | table   |
| public | players_id_seq        | sequence|
| public | total_matches         | view    |
| public | total_wins            | view    |

## Run tests
A set of tests is included, to launch them you need to type (from *project's root dir*):

`$ python tournament_test.py`

And if it everything goes well, output should be:

```
1. Old matches can be deleted.
2. Player records can be deleted.
3. After deleting, countPlayers() returns zero.
4. After registering a player, countPlayers() returns 1.
5. Players can be registered and deleted.
6. Newly registered players appear in the standings with no matches.
7. After a match, players have updated standings.
8. After one match, players with one win are paired.
Success!  All tests pass!
```