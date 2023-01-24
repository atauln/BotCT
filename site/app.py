
from flask import Flask, render_template, redirect
import os
from websocket import create_connection


app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/play')
def play():
    protocol = os.environ['PROTOCOL']
    url = os.environ['CONN_URL']
    port = os.environ['CONN_PORT']

    complete_url = f'{protocol}://{url}:{port}'

    ws = create_connection(complete_url)
    ws.send('{"event":"gunshot"}')
    ws.close()
    return redirect('/')
