import requests
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
from player import Player

SEASONS = [
    "2018-19", "2019-20", "2020-21", "2021-22", "2022-23",
    "2023-24", "2024-25", "2025-26", "2026-27",
]

def main():
    console = Console()
    season = Prompt.ask("Season", choices=SEASONS, default="2024-25")
    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    stats = PlayerStats(PlayerReader(url))

    while True:
        nationality = Prompt.ask("Nationality", choices=stats.nationalities(), default="")
        if not nationality:
            break

        players = stats.top_scorers_by_nationality(nationality)
        console.print(players_table(players, f"Season {season} players from {nationality}"))

def players_table(players, title):
    table = Table(title=title)
    table.add_column("name", style="cyan")
    table.add_column("teams", style="magenta")
    table.add_column("goals", justify="right", style="green")
    table.add_column("assists", justify="right", style="green")
    table.add_column("points", justify="right", style="green")

    for player in players:
        table.add_row(
            player.name, player.team,
            str(player.goals), str(player.assists), str(player.points),
        )

    return table

class PlayerReader:  # pylint: disable=too-few-public-methods
    def __init__(self, url):
        self.response = requests.get(url, timeout=10).json()

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

        top_nat_players.sort(key=lambda player: player.points, reverse=True)

        return top_nat_players

    def nationalities(self):
        return sorted({player.nationality for player in self.players})

if __name__ == "__main__":
    main()
