import flask
import pandas as pd
from flask import Flask, request, render_template, redirect

from Globals import ALERTS_FILE
from alarm_file import add_to_alert_file

app = Flask(__name__)


@app.route('/', methods=['GET'])
def redirect_to_home():
    return flask.redirect('/nba_alerts')


@app.route('/nba_alerts', methods=['Post', 'GET'])
def nba_alerts():
    if request.method == 'GET':
        return render_template('main.html')
    if request.method == 'POST':
        if request.form.get('submit_il') == 'my_alerts':
            return redirect('/my_alerts')
        elif request.form.get('submit_us') == 'new_alert':
            return redirect('/new_alert')
        else:
            return ''


@app.route('/my_alerts', methods=['GET'])
def my_alerts():
    df = pd.read_excel(ALERTS_FILE)
    return render_template('my_alerts.html', tables=[df.to_html(classes='data')], titles=df.columns.values)


@app.route('/new_alert', methods=['Post', 'GET'])
def new_alert():
    if request.method == 'GET':
        return render_template('new_alert.html')
    if request.method == 'POST':
        add_to_alert_file(home_team=request.form['home_team'], guest_team=request.form['guest_team'],
                          diff=request.form['diff'], status=request.form['status'])
        return render_template('new_alert.html')


if __name__ == '__main__':
    app.run(port=23000)
