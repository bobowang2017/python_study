# -*- coding: utf-8 -*-
from import_study.message.base import Msg


class Message(Msg):
    def __init__(self):
        pass

    def send_msg(self, msg):
        print(msg)
        print("Send Message")
