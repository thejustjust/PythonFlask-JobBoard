from flask import Flask
from flask import render_template

app = Flask(__name__)

jobs = render_template('index.html')

@app.route('/')
@app.route('/jobs')
