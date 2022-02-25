from time import sleep

from playsound import playsound
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from Game import create_games_from_web, create_games_from_csv
from Globals import WEB_ADDRESS, ALARM_FILE, ALERTS_FILE, LOG_FILE
from alarm_file import remove_from_alert_file


def active_alarm(alarm_file):
    playsound(alarm_file)


if __name__ == '__main__':
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    n = 0
    while True:
        alert_games = create_games_from_csv(ALERTS_FILE)
        driver.get(WEB_ADDRESS)
        online_games = create_games_from_web(driver)
        for game in online_games:
            if game.check_if_alert_on_game(alert_games):
                print('!')
                remove_from_alert_file(game.home_team, game.guest_team)
                with open(LOG_FILE, 'a') as file:
                    file.write(str(game))
                active_alarm(ALARM_FILE)
        n += 1
        print(n)
        sleep(300)
