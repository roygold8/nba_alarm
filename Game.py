import pandas as pd

from Scrape import get_status, get_teams, get_date, get_score


class Game:
    def calculate_dif(self):
        return abs(int(self.home_score) - int(self.guest_score))

    def __init__(self, status, home_team, guest_team, date, home_score, guest_score):
        self.status = status
        self.home_team = home_team
        self.guest_team = guest_team
        self.date = date
        self.home_score = home_score
        self.guest_score = guest_score
        self.score_diff = self.calculate_dif()

    def __str__(self):
        return '{} vs {} -> {} at {}, {} {} : {} , diff is {}'.format(self.home_team, self.guest_team, self.status,
                                                                      self.date,
                                                                      self.status, self.home_score,
                                                                      self.guest_score,
                                                                      self.score_diff)

    def to_list(self):
        return [self.home_team, self.guest_team, self.status, self.date, self.home_score, self.guest_score,
                self.score_diff]

    def check_if_alert_on_game(self, alert_games):
        for alert_game in alert_games:
            if self.home_team in alert_game.teams and self.guest_team in alert_game.teams:
                print(self.status)
                if alert_game.status in self.status.split() or alert_game.status == self.status:
                    print(self.score_diff)
                    if self.score_diff <= alert_game.score_diff:
                        return True
        return False


class Alert_Game:
    def __init__(self, status, teams, date, diff):
        self.status = status
        if type(self.status) != str:
            self.status = ''
        self.teams = teams
        self.date = date
        self.score_diff = diff

    def __str__(self):
        return 'Alert on {} game, Status - {}, diff - {}'.format(str(self.teams), self.status, self.score_diff)


def create_games_from_web(driver):
    status = get_status(driver)
    teams = get_teams(driver)
    date = get_date(driver)
    score = get_score(driver)
    games = []
    while teams:
        if len(status) < 1:
            status.append('')
        if len(score) < 1:
            score.append('0')
            score.append('0')
        games.append(Game(status[0], teams[1], teams[0], date, score[1], score[0]))
        status.pop(0)
        teams.pop(0)
        teams.pop(0)
        score.pop(0)
        score.pop(0)
    return games


def create_games_from_csv(path):
    df = pd.read_excel(path)
    games = []
    for i in range(len(df)):
        games.append(Alert_Game(status=df.iloc[i]['status'], teams=(df.iloc[i]['Home_Team'], df.iloc[i]['Guest_Team']),
                                date=df.iloc[i]['Date'], diff=df.iloc[i]['diff']))
    return games
