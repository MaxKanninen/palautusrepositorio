class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality = dict['nationality']
        self.assists = dict['assists']
        self.goals = dict['goals']
        self.team = dict['team']
        self.games = dict['games']
        self.id = dict.get('id')

    @property
    def points(self):
        return self.goals + self.assists

    def __str__(self):
        return self.name
