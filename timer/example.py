# -*- coding: utf-8 -*-
from threading import Timer


def talk(name):
    print("%s is talking." % name)


if __name__ == '__main__':
    '''Timer(等待多少秒, 执行的函数, args给函数传参数)'''
    timer = Timer(3, talk, args=("lily",))
    timer.start()