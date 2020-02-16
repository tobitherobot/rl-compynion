class Player(object):
    score = 0
    goals = 0
    assists = 0
    saves = 0
    shots = 0
    team = 0
    platform = ''

    def __init__(self, actor_id, username, online_id):
        self.actor_id = actor_id
        self.username = username
        self.online_id = online_id

    def __repr__(self):
        return self.username + ': ' + str(self.actor_id)

    def __str__(self):
        string = self.get_username().ljust(25) + \
                 str(self.score).rjust(5) + \
                 str(self.get_goals()).rjust(3) + \
                 str(self.get_assists()).rjust(3) + \
                 str(self.get_saves()).rjust(3) + \
                 str(self.get_shots()).rjust(3)
        return string

    def __get__(self, instance, owner):
        return self

    def get_actor_id(self):
        return self.actor_id

    def get_username(self):
        return self.username

    def get_online_id(self):
        return self.online_id

    def get_team(self):
        return self.team

    def get_platform(self):
        return self.platform

    def get_score(self):
        return self.score

    def get_goals(self):
        return self.goals

    def get_assists(self):
        return self.assists

    def get_saves(self):
        return self.saves

    def get_shots(self):
        return self.shots

    def set_team(self, value):
        self.team = value

    def set_platform(self, value):
        self.platform = value

    def set_score(self, value):
        self.score = value

    def set_goals(self, value):
        self.goals = value

    def set_assists(self, value):
        self.assists = value

    def set_saves(self, value):
        self.saves = value

    def set_shots(self, value):
        self.shots = value
