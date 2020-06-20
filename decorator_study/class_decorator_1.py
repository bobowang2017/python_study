# -*- coding: utf-8 -*-
class Logger(object):
    def __init__(self, level='INFO'):
        self.level = level

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print("[{level}]: the function {func}() is running...".format(level=self.level, func=func.__name__))
            func(*args, **kwargs)
        return wrapper


@Logger(level="WARNING")
def say(something):
    print("say {}!".format(something))


say("hello")