
from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html', url=os.getenv('CONN_URL'), port=os.getenv('CONN_PORT'))
