# -*- coding: utf-8 -*-
from importlib import import_module

from import_study import msg_list

for msg in msg_list:
    m, c = msg.rsplit('.', maxsplit=1)
    print(m, c)
    _module = import_module(m)
    _obj = getattr(_module, c)()
    getattr(_obj, 'send_msg')()
