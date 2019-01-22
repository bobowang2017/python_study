# -*- coding: utf-8 -*-
import threading
import time


def worker(num):
    """
    thread worker function
    :return:
    """
    time.sleep(1)
    print("Thread %d" % num)
    return


for i in range(5):
    t = threading.Thread(target=worker, args=(i,), name="t. % d" % i)
    t.start()
