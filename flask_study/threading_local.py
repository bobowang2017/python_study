# -*- coding: utf-8 -*-
import threading

try:
    from greenlet import getcurrent as get_ident
except ImportError:
    try:
        from threading import get_ident
    except ImportError:
        from _thread import get_ident


class Local(object):
    def __init__(self):
        object.__setattr__(self, '__storage__', {})
        object.__setattr__(self, '__ident_func__', get_ident)

    def __setattr__(self, key, value):
        ident = self.__ident_func__()
        storage = self.__storage__
        try:
            storage[ident][key] = value
        except KeyError:
            storage[ident] = {key: value}

    def __getattr__(self, name):
        try:
            return self.__storage__[self.__ident_func__()][name]
        except KeyError:
            raise AttributeError(name)


local_values = Local()


def task(num):
    local_values.name = num
    import time
    time.sleep(1)
    print(local_values.name, threading.current_thread().name)


for i in range(20):
    th = threading.Thread(target=task, args=(i,), name="线程%s" % i)
    th.start()
