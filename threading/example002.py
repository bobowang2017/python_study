# -*- coding: utf-8 -*-
# ===================================================================================================================
# 线程锁模拟获取共享资源
# ===================================================================================================================
import threading
import time

globals_num = 0

lock = threading.RLock()


def func():
    lock.acquire()  # 获得锁
    global globals_num
    globals_num += 1
    time.sleep(0.001)
    print(globals_num)
    lock.release()  # 释放锁


for i in range(100):
    t = threading.Thread(target=func)
    t.start()
