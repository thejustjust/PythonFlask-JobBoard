import sqlite3
from flask import g, Flask, render_template

app = Flask(__name__)

DATABASE = 'db/jobs.sqlite'
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row
    return db

@app.route("/")
@app.route("/jobs")
def jobs():
    return render_template('index.html')
    
