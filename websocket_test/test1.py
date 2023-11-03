import websocket


class WebSocketClient(object):
    def __init__(self, url, headers):
        self.ws = websocket.WebSocketApp(url, header=headers, on_message=self.on_message, on_error=self.on_error,
                                         on_close=self.on_close)
        websocket.enableTrace(True)

    def on_message(self, ws, message):
        print(ws)
        print(message)

    def on_error(self, ws, error):
        print(ws)
        print(error)

    def on_close(self, ws):
        print(ws)
        print("### closed ###")

    def run(self):
        self.ws.run_forever()


if __name__ == "__main__":
    ws_url = "ws://127.0.0.1:8080/api/v1/rooms?title=Room&ownerId=11111&maxMember=10"
    ws_headers = {"token": ""}
    WebSocketClient(ws_url, ws_headers).run()
