# -*- coding: utf-8 -*-
def singleton(cls, *args, **kwargs):
    instance = {}

    def _instance():
        if cls not in instance:
            instance[cls] = cls(*args, *kwargs)
        return instance[cls]

    return _instance


@singleton
class TestSingleton:
    def __init__(self):
        self.num = 0

    def add(self):
        self.num = 99


ts1 = TestSingleton()
ts2 = TestSingleton()
print(ts1)
print(ts2)
