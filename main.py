from time import sleep

from playsound import playsound
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Server.server_functions import run_server
from NBA_Scrape.Game import create_games_from_web, create_games_from_csv
from Utils.Globals import WEB_ADDRESS, ALARM_FILE, ALERTS_FILE, LOG_FILE
from Utils.alarm_file import remove_from_alert_file
from Utils.Calendar import create_calndar_event_now, get_calendar_service
from threading import Thread

def active_alarm(alarm_file):
    playsound(alarm_file)

def run_scraper():
    n = 0
    while True:
        alert_games = create_games_from_csv(ALERTS_FILE)
        driver.get(WEB_ADDRESS)
        online_games = create_games_from_web(driver)
        for game in online_games:
            print(game)
            if game.check_if_alert_on_game(alert_games):
                remove_from_alert_file(game.home_team, game.guest_team)
                with open(LOG_FILE, 'a') as file:
                    file.write(str(game))
                    file.write('active alert')
                    file.write('\n')
                create_calndar_event_now(title='{} vs {}'.format(game.home_team, game.guest_team), description=game)
                print('done alert')
                active_alarm(ALARM_FILE)
        n += 1
        print(n)
        sleep(150)


if __name__ == '__main__':
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    service = get_calendar_service()
    t1 = Thread(target=run_server)
    t2 = Thread(target=run_scraper)
    t1.start()
    t2.start()
