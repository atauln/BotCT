#!/usr/bin/env python

import asyncio
import websockets
import json

from pydub import AudioSegment
from pydub.playback import play

async def handler(websocket):
    while True:
        try:
            message = json.loads(await websocket.recv())
        except websockets.ConnectionClosedOK:
            break
        match message['event']:
            case "gunshot":
                print("received message")
                song = AudioSegment.from_wav("gunshot.wav")
                play(song)


async def main():
    print("websocket opening...")
    async with websockets.serve(handler, "0.0.0.0", 8001):
        print("websocket is now open, hosted on 0.0.0.0:8001")
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())

