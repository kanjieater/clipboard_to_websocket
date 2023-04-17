# Clipboard_to_WebSocket

A simple Python script that exposes your clipboard data to a WebSocket server.

## Usage

- Clone the repository
- Install dependencies with `pip install -r requirements.txt`
- Start the WebSocket server with `python __init__.py`
- Connect to the server using the WebSocket protocol. The clipboard data will be sent to the client as soon as it changes.

## Configuration
You can configure the WebSocket server host, port, and clipboard poll interval by passing command line arguments when starting the script:

```bash
Copy code
usage: clip_to_ws.py [-h] [--host HOST] [--port PORT] [--poll-interval POLL_INTERVAL]
```

Expose clipboard data to a WebSocket server.

```bash
optional arguments:
  -h, --help            show this help message and exit
  --host HOST           WebSocket server host (default: localhost)
  --port PORT           WebSocket server port (default: 6678)
  --poll-interval POLL_INTERVAL
                        Poll interval for clipboard data (default: 0.1)
```

Example:

```python
python __init__.py --host localhost --port 6678 --poll-interval 0.1
```
## License

This software is released under the MIT License. See LICENSE for more information.