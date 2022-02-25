from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import time
from flask import Flask,request,render_template,redirect, url_for
app = Flask(__name__)

#login functions
def enter_metiav_us(driver):
    driver.get(r'https://meitav.viewtrade.com')
    user_name = driver.find_element_by_name("username")
    password = driver.find_element_by_name("password")
    enter = driver.find_element_by_name("processLogin")
    le = driver.find_element_by_name("language")
    user_name.send_keys('90481')
    password.send_keys('Hakfar4591')
    time.sleep(1)
    le.click()
    time.sleep
    enter.click()

def enter_metiav_is(driver):
    driver.get(r'https://sparkmeitav.ordernet.co.il')
    user_name = driver.find_element_by_name("username")
    password = driver.find_element_by_name("password")
    #enter = driver.find_element_by_id("btnSubmit")
    user_name.send_keys('1320214294')
    password.send_keys('Roygold5')
    #enter.click()

#END

#web functions
@app.route('/meitav', methods=['POST','GET'])
def meitav():
    if request.method == 'GET':
        return render_template('form1.html')
    if request.method == 'POST':
        if request.form.get('submit_il') == 'IL':
            print('im here')
            return redirect('/il')
        elif request.form.get('submit_us') == 'US':
            print('im here')
            return redirect('/us')
        else:
            return ''


@app.route('/il', methods=['POST','GET'])
def il():
    driver = webdriver.Chrome()
    enter_metiav_is(driver)
    return ''

@app.route('/us', methods=['POST','GET'])
def us():
    driver = webdriver.Chrome()
    enter_metiav_us(driver)
    return ''

if __name__ == '__main__':
    app.run()

