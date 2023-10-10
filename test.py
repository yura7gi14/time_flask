from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    #current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    current_day = datetime.datetime.now().strftime('%Y-%m-%d')
    current_time = datetime.datetime.now().strftime('%H:%M:%S')
    return render_template('index.html', current_day = current_day, current_time=current_time)

