import re
from datetime import datetime


def get_date(driver):
    """
    check the date of current games in nba.com
    args
    driver - driver to do the html query on
    return
    date time object of day-month-year
    """
    day = driver.find_element_by_xpath('//span[@class="DatePickerWeek_dateText__2SoNU"]').text
    date = re.findall('(.*) (.*)',
                      driver.find_element_by_xpath('//p[@class="text-center text-sm font-black flex-auto"]').text)[0]
    month = date[0]
    year = date[1]
    date_string = '{}-{}-{}'.format(day, month, year)
    return datetime.strptime(date_string, '%d-%B-%Y')


def get_status(driver):
    """
    check the status of each game in nba.com
    args
    driver - driver to do the html query on
    return
    list of all the status of all games
    """
    game_status = []
    for element in driver.find_elements_by_xpath('//p[@class="text-xs uppercase"]'):
        game_status.append(element.text)
    return game_status


def get_teams(driver):
    """
    check the status of each game in nba.com
    args
    driver - driver to do the html query on
    return
    list of all the status of all games
    """
    teams = []
    for element in driver.find_elements_by_xpath('//span[@class="MatchupCardTeamName_teamName__3i23P"]'):
        teams.append(element.text)
    return teams


def get_score(driver):
    """
    check the scores of each game in nba.com
    args
    driver - driver to do the html query on
    return
    list of all the status of all games
    """
    game_scores = []
    for element in driver.find_elements_by_xpath('//p[@class="h9 relative inline-block leading-none"]'):
        game_scores.append(element.text)
    return game_scores
