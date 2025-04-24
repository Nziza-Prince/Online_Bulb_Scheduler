import asyncio
import websockets
import subprocess
import json

async def handler(websocket):
    async for message in websocket:
        print(f"Received from web: {message}")
        data = json.loads(message)

        # Simulate schedule by sending ON then OFF after delay
        subprocess.run(["mosquitto_pub", "-h", "localhost", "-t", "iot/light", "-m", "ON"])
        print("Published: ON")

        await asyncio.sleep(int(data['delay']))  # delay in seconds

        subprocess.run(["mosquitto_pub", "-h", "localhost", "-t", "iot/light", "-m", "OFF"])
        print("Published: OFF")

start_server = websockets.serve(handler, "localhost", 6789)

print("WebSocket server listening on ws://localhost:6789")
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
