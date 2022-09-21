from core import app
from flask import render_template

@app.route('/')
def index():
    greeting="Hello there, ACE!"
    return render_template('index.html', greet=greeting)