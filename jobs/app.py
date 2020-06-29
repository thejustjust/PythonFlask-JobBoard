import sqlite3
from flask import g, Flask, render_template

app = Flask(__name__)
DATABASE = 'db/jobs.sqlite'

@app.route("/")
@app.route("/jobs")
def jobs():
    return render_template('index.html')
    
