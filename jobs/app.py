from flask import Flask, render_template

app = Flask(__name__)

jobs = render_template('index.html')

@app.route('/')
@app.route('/jobs')
