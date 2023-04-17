import argparse
import asyncio
import websockets
import pyperclip


async def send_clipboard_data(websocket, path, poll_interval):
    last_clipboard_contents = ""
    last_send_status = True
    print(f"Connected...")
    while True:
        clipboard_contents = pyperclip.paste()
        if clipboard_contents != last_clipboard_contents and last_send_status:
            try:
                await websocket.send(clipboard_contents)
                last_clipboard_contents = clipboard_contents
                last_send_status = True
            except Exception as e:
                last_send_status = False
                with open("error.log", "r") as f:
                    last_error = f.readline().strip()
                if str(e) != last_error:
                    with open("error.log", "w") as f:
                        f.write(str(e) + "\n")
        elif clipboard_contents != last_clipboard_contents and not last_send_status:
            last_send_status = True
        await asyncio.sleep(poll_interval)


async def ws_handler(websocket, path):
    await send_clipboard_data(websocket, path, args.poll_interval)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Expose clipboard data to a WebSocket server.')
    parser.add_argument('--host', type=str, default='localhost', help='WebSocket server host (default: localhost)')
    parser.add_argument('--port', type=int, default=6678, help='WebSocket server port (default: 6678)')
    parser.add_argument('--poll-interval', type=float, default=0.1, help='Poll interval for clipboard data (default: 0.1)')
    args = parser.parse_args()

    websocket_path = f"{args.host}:{args.port}"
    start_server = websockets.serve(ws_handler, args.host, args.port)
    print(f"Starting {'ws://' + websocket_path}")
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
