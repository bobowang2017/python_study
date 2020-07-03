# -*- coding: utf-8 -*-
class Singleton(type):
    def __init__(self, *args, **kwargs):
        self.__instance = None
        super(Singleton, self).__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super(Singleton, self).__call__(*args, **kwargs)
        return self.__instance


class Foo(metaclass=Singleton):
    pass


f1 = Foo()
f2 = Foo()
print(f1 is f2)
