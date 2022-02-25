import pandas as pd

from Globals import ALERTS_FILE


def add_to_alert_file(home_team, guest_team, diff, status):
    df = pd.read_excel(ALERTS_FILE)
    df2 = pd.DataFrame([[home_team, guest_team, '', diff, status]],
                       columns=['Home_Team', 'Guest_Team', 'Date', 'diff', 'status'])
    df = pd.concat([df, df2])
    df.to_excel(ALERTS_FILE, index=False)


def remove_from_alert_file(home_team, guest_team):
    df = pd.read_excel(ALERTS_FILE)
    df = df[(df['Home_Team'] != home_team) & (df['Guest_Team'] != guest_team)]
    df.to_excel(ALERTS_FILE, index=False)
