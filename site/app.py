
from flask import Flask, render_template, redirect
import os
from websocket import create_connection
import json

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/play/<event>')
def play(event):
    print("entered event")
    protocol = os.environ['PROTOCOL']
    url = os.environ['CONN_URL']
    port = os.environ['CONN_PORT']

    complete_url = f'{protocol}://{url}:{port}'
    
    request = {
            "event": event
    }

    ws = create_connection(complete_url)
    ws.send(json.dumps(request))
    ws.close()
    return redirect('/')
