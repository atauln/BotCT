
from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html', url=os.environ['CONN_URL'], port=os.environ['CONN_PORT'])
