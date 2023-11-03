from socket import *
import json, time, threading
from websocket import create_connection

from websocket_test.function import random_loc


class Client():
    def __init__(self):
        # 调用create_connection方法，建立一个websocket链接,链接是自己的链接
        self.ws = create_connection("ws://127.0.0.1:8080/api/v1/rooms?title=Room&ownerId=11111&maxMember=10")
        # 建一个线程，监听服务器发送给客户端的数据
        self.trecv = threading.Thread(target=self.recv)
        self.trecv.start()

    # 发送方法，聊天输入语句时调用，此处默认为群聊ALL
    def send(self, content):
        # 这里的msg要根据实际需要自己写
        msg = {
            "MsgType": 2,
            "UserId": "2482762655",
            "UserName": "xxxxxxxx",
            "Latitude": content.get("latitude"),
            "Longitude": content.get("longtitude")
        }
        msg = json.dumps(msg)
        self.ws.send(msg)

    # 接收服务端发送给客户的数据，只要ws处于连接状态，则一直接收数据
    def recv(self):
        try:
            while self.ws.connected:
                result = self.ws.recv()
                print("received msg:" + str(result))
        except Exception as e:
            print(e)


if __name__ == '__main__':
    c = Client()
    # 建立链接后，就可以按照需要自己send了
    x = 500
    y = 500
    print(f"-->({x}, {y})", end="")
    for i in range(2000):
        x1, y1 = random_loc(x, y)
        c.send({"longtitude": x1, "latitude": y1})
        time.sleep(1)
        x, y = random_loc(x1, y1)
        c.send({"longtitude": x, "latitude": y})
        time.sleep(1)

