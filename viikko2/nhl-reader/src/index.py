import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    response = requests.get(url).json()

    players = []

    for player_dict in response:
        player = Player(player_dict)
        players.append(player)

    players.sort(key=lambda player: player.goals + player.assists, reverse=True)

    print("Players from Finland:")

    for player in players:
        if player.nationality == "FIN":
            print(f"{player.name} {player.team} {player.goals} + {player.assists} = {player.goals + player.assists}")

if __name__ == "__main__":
    main()
    