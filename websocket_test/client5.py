# -*- coding: utf-8 -*-

import websocket

headers = {
    'Authorization': 'Bearer token123',
    'User-Agent': 'Custom Agent'
}

websocket_url = 'wss://example.com/websocket'


def on_message(ws, message):
    print(message)


def on_error(ws, error):
    print(error)


def on_close(ws):
    print("Connection closed")


def on_open(ws):
    print("Connection opened")
    ws.send()


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(websocket_url,
                                header=headers,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()
