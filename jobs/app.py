from flask import Flask, render_template

app = Flask(__name__)

def jobs():
    @app.route('/')
    @app.route('/jobs')
    return render_template('index.html')
    
