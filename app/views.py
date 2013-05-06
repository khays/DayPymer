from flask import render_template
from entries import getEntries
from app import app

entryLocation = '/Users/kellyhays/Dropbox/Notes/work/'

@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': 'Miguel' } # fake user
    notes = getEntries(entryLocation)
    return render_template("index.html",
        title = 'Home',
        user = user,
        notes = notes)

@app.route('/life')
def life():
    user = { 'nickname': 'John' } # fake user
    return render_template("index.html",
        title = 'Home',
        user = user)
