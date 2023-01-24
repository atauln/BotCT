
from flask import Flask, render_template, redirect
import os
import asyncio
import websockets


app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html', url=os.environ['CONN_URL'], port=os.environ['CONN_PORT'], protocol=os.environ['PROTOCOL'])

@app.route('/play')
async def play():
    async with websockets.connect('{os.environ["PROTOCOL"]}://{os.environ["CONN_URL"]}:{os.environ["CONN_PORT"]}') as websocket:
        await websocket.send('{"event":"gunshot"}')
        await websocket.close()
    return redirect('/')
