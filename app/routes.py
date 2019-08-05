import os
from app import app
from flask import render_template, request, redirect, session, url_for

app.secret_key = b'A{\xf2?p7,U\xc2\x96\xf0k\xd2\r\x9f\xf5'

accounts = [
        {"Name":"Catherine Uwakwe", "Email":"cuwakwe@exeter.edu", "Name of School": "Phillips Exeter Academy"},
        {"Name":"Maria Millette", "Email":"millette_maria@theharveyschool.com", "Name of School": "The Harvey School"},
    ]


from flask_pymongo import PyMongo

# name of database
app.config['MONGO_DBNAME'] = 'UniDROP' 

# URI of database
app.config['MONGO_URI'] = 'mongodb+srv://admin:Barbie0904@cluster0-ueken.mongodb.net/UniDROP?retryWrites=true&w=majority' 

mongo = PyMongo(app)

# INDEX

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', account = accounts)

@app.route('/elements')

def elements():
    return render_template('elements.html', accounts = accounts)


# CONNECT TO DB, ADD DATA

@app.route('/add')

def add():
    # connect to the database
    account = mongo.db.accounts
    # insert new data
    account.insert({"Name": "Catherine Uwakwe", "Email": "cuwakwe@exeter.edu", "Name of School": "Phillips Exeter Academy"})
    # return a message to the user
    return "Account Successfully Created"


@app.route("/accounts_new", methods = ["POST", "GET"])
def accounts_new():
    userdata = dict(request.form)
    accounts = mongo.db.accounts
    accounts.insert(userdata)
    return redirect('/index')
  
def accountmade():
    print('Account Created!')
    return redirect
    
    