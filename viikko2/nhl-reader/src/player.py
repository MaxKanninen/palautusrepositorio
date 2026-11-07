class Player:
    def __init__(self, player_dict):
        self.name = player_dict['name']
        self.nationality = player_dict['nationality']
        self.assists = player_dict['assists']
        self.goals = player_dict['goals']
        self.team = player_dict['team']
        self.games = player_dict['games']
        self.id = player_dict.get('id')

    @property
    def points(self):
        return self.goals + self.assists

    def __str__(self):
        return self.name
