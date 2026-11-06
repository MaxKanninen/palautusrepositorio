import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    for player in players:
        print(player)

class PlayerReader():
    def __init__(self, url):
        self.response = requests.get(url).json()

    def get_players(self):
        players = []

        for player_dict in self.response:
            player = Player(player_dict)
            players.append(player)

        return players

class PlayerStats:
    def __init__(self, reader): 
        self.players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        top_nat_players = []

        for player in self.players:
            if player.nationality == nationality:
               top_nat_players.append(player)

        top_nat_players.sort(key=lambda player: player.goals + player.assists, reverse=True)
        
        return top_nat_players

if __name__ == "__main__":
    main()
    