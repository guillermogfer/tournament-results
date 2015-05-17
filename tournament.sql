-- Table definitions for the tournament project.

--
-- Table structure for table `players`
--

CREATE TABLE players(
    id serial PRIMARY KEY,
    name TEXT NOT NULL
);

--
-- Table structure for table `matches`
--

CREATE TABLE matches(
    id serial PRIMARY KEY,
    winner integer REFERENCES players (id),
    loser integer REFERENCES players (id)
);

--
-- Name: total_wins; Type: VIEW;
--

CREATE VIEW total_wins AS
 SELECT players.id,
    players.name,
    COUNT(matches.winner) AS wins
   FROM (matches
     RIGHT JOIN players ON ((matches.winner = players.id)))
  GROUP BY matches.winner, players.name, players.id
  ORDER BY COUNT(matches.winner) DESC;

--
-- Name: total_matches; Type: VIEW;
--

CREATE VIEW total_matches AS
 SELECT players.name,
    COUNT(matches.id) AS matches
   FROM (matches
     RIGHT JOIN players ON (((matches.winner = players.id) OR (matches.loser = players.id))))
  GROUP BY players.name;

--
-- Name: player_standings; Type: VIEW;
--

CREATE VIEW player_standings AS
 SELECT total_wins.id,
    total_wins.name,
    total_wins.wins,
    total_matches.matches
   FROM total_wins,
    total_matches
  WHERE (total_wins.name = total_matches.name)
  ORDER BY total_wins.wins DESC;
