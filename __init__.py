import asyncio
import websockets
import pyperclip

async def send_clipboard_data(websocket, path):
    last_clipboard_contents = ""
    last_send_status = True
    while True:
        clipboard_contents = pyperclip.paste()
        if clipboard_contents != last_clipboard_contents and last_send_status:
            try:
                await websocket.send(clipboard_contents)
                last_clipboard_contents = clipboard_contents
                last_send_status = True
            except Exception as e:
                last_send_status = False
                with open("error.log", "a") as f:
                    f.write(str(e) + "\n")
        elif clipboard_contents != last_clipboard_contents and not last_send_status:
            last_send_status = True
        await asyncio.sleep(0.3)

start_server = websockets.serve(send_clipboard_data, "localhost", 6678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()