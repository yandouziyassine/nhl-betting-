import requests

# Dictionnaire des équipes
teams = {
    17: "Detroit Red Wings",
    6: "Boston Bruins",
    52: "Winnipeg Jets",
    28: "San Jose Sharks",
    5: "Pittsburgh Penguins",
    14: "Tampa Bay Lightning",
    4: "Philadelphia Flyers",
    10: "Toronto Maple Leafs",
    12: "Carolina Hurricanes",
    53: "Arizona Coyotes",
    20: "Calgary Flames",
    8: "Montréal Canadiens",
    15: "Washington Capitals",
    23: "Vancouver Canucks",
    21: "Colorado Avalanche",
    18: "Nashville Predators",
    24: "Anaheim Ducks",
    54: "Vegas Golden Knights",
    55: "Seattle Kraken",
    25: "Dallas Stars",
    16: "Chicago Blackhawks",
    3: "New York Rangers",
    29: "Columbus Blue Jackets",
    13: "Florida Panthers",
    22: "Edmonton Oilers",
    30: "Minnesota Wild",
    9: "Ottawa Senators",
    2: "New York Islanders",
    26: "Los Angeles Kings",
    1: "New Jersey Devils",
    70: "To be determined",
    7: "Buffalo Sabres"
}

# Identifiants des équipes
team_id1 = 13  # Florida Panthers
team_id2 = 14  # Tampa Bay Lightning
team_name1 = teams.get(team_id1)
team_name2 = teams.get(team_id2)

print(f"Équipe 1 : {team_name1}")
print(f"Équipe 2 : {team_name2}")

# Function to calculate the % of victory
def calculate_victory_percentage(team_id, team_name):
    url = f"https://api.nhle.com/stats/rest/en/team/summary?cayenneExp=seasonId%3D{team_id}%20and%20teamFullName%3D%22{team_name}%22"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if 'data' in data and data['data']:
            team_stats = data['data'][0]
            games_played = team_stats.get('gamesPlayed', 0)
            wins = team_stats.get('wins', 0)
            if games_played > 0:
                return wins / games_played
    return None

# Function for other data
def get_team_stat(team_name, season_id, stat_key):
    url = f"https://api.nhle.com/stats/rest/en/team/summary?cayenneExp=teamFullName%3D%22{team_name}%22%20and%20seasonId%3D{season_id}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if 'data' in data and data['data']:
            return data['data'][0].get(stat_key, None)
    return None

# season data
season_id = "20232024"

#% of victories
a1 = calculate_victory_percentage(season_id, team_name1)
a2 = calculate_victory_percentage(season_id, team_name2)

#goal against
b1 = get_team_stat(team_name1, season_id, "goalsAgainstPerGame")
b2 = get_team_stat(team_name2, season_id, "goalsAgainstPerGame")

#goal for
c1 = get_team_stat(team_name1, season_id, "goalsForPerGame")
c2 = get_team_stat(team_name2, season_id, "goalsForPerGame")

#face off win
d1 = get_team_stat(team_name1, season_id, "faceoffWinPct")
d2 = get_team_stat(team_name2, season_id, "faceoffWinPct")

#shoot against
e1 = get_team_stat(team_name1, season_id, "shotsForPerGame")
e2 = get_team_stat(team_name2, season_id, "shotsForPerGame")

#shoot for
f1 = get_team_stat(team_name1, season_id, "shotsAgainstPerGame")
f2 = get_team_stat(team_name2, season_id, "shotsAgainstPerGame")

#power play
h1 = get_team_stat(team_name1, season_id, "powerPlayPct")
h2 = get_team_stat(team_name2, season_id, "powerPlayPct")

# Calculate % of bock by the goalkeeper
g1 = 1 - b1 / f1 if b1 and f1 else None
g2 = 1 - b2 / f2 if b2 and f2 else None

# Calculate the odds
cote = -10.67 + ((12.21844622716187 * g1) + (0.43665 * g2)) + \
       ((0.901 * d1) + (-0.1217 * d2)) + \
       ((-0.8187919 * c1) + (0.5263939 * c2)) + \
       ((0.9730232 * b1) + (-0.485 * b2)) + \
       ((0.756 * a1) + (0.196 * a2)) + \
       ((-0.197 * h1) + (0.0101 * h2))

# result
print("Cote calculée :", cote)
print(f"a1: {a1}, a2: {a2}")
print(f"b1: {b1}, b2: {b2}")
print(f"c1: {c1}, c2: {c2}")
print(f"d1: {d1}, d2: {d2}")
print(f"e1: {e1}, e2: {e2}")
print(f"f1: {f1}, f2: {f2}")
print(f"g1: {g1}, g2: {g2}")
print(f"h1: {h1}, h2: {h2}")
