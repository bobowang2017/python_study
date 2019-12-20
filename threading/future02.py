from concurrent.futures import ThreadPoolExecutor  # 线程池模块
import os, time, random


def talk(name, p):
    # print(p * 100)
    print('name: %s  pis%s  run' % (name, os.getpid()))
    time.sleep(10)
    return p * 100


def call_back(fn):
    print(fn.result())
    print('Hello World')


if __name__ == '__main__':
    pool = ThreadPoolExecutor(4)
    for i in range(10):
        execute = pool.submit(talk, '线程%s' % i, i)  # 异步提交（只是提交需要运行的线程不等待）
        execute.add_done_callback(call_back)
    print('主进程')
