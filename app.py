# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
from flask import redirect
from flask import request
# from flask_pymongo import PyMongo

import datetime



# -- Initialization section --
app = Flask(__name__)
app.jinja_env.globals['current_time'] = datetime.datetime.now()


events = [
        {"name":"First Day of Classes", "date":"2020-08-21"},
        {"name":"Winter Break", "date":"2020-12-20"},
        {"name":"Finals Begin", "date":"2020-12-01"}
    ]
#
# MONGO_DBNAME = ''
# MONGO_DB_USERNAME = ''
# MONGO_DB_PASSWORD = ''
#
# app.config['MONGO_DBNAME'] = MONGO_DBNAME
# app.config['MONGO_URI'] = f'mongodb+srv://{MONGO_DB_USERNAME}:{MONGO_DB_PASSWORD}@cluster0-kxrbn.mongodb.net/{MONGO_DBNAME}?retryWrites=true'

# mongo = PyMongo(app)

# -- Routes section --
# INDEX

@app.route('/')
@app.route('/index')
def index():
    data = {
    'events':events,
    }
    return render_template('index.html', data=data)

@app.route('/view')
def events_view():
    data = {
    'events':events,
    }
    return render_template('eventsView.html', data=data)

@app.route('/add', methods=['GET','POST'])
def events_add():
    if request.method == 'GET':
        data = {

        }
        return render_template('eventsAdd.html', data=data)
    else:
        ## Add event to events_list
        form = request.form

        event = {
        'name':form['eventName'],
        'date':form['eventDate'],
        }

        events.append(event)

        return redirect(url_for('events_view'))
