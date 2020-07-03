# -*- coding: utf-8 -*-
class MyMeta(type):
    def __init__(self, name, bases, dic):
        super().__init__(name, bases, dic)
        print('===>MyMeta.__init__')
        print(self.__name__)
        print(dic)
        print(self.yaml_tag)

    def __new__(cls, *args, **kwargs):
        print('===>MyMeta.__new__')
        print(cls.__name__)
        return type.__new__(cls, *args, **kwargs)

    def __call__(cls, *args, **kwargs):
        print('===>MyMeta.__call__')
        obj = cls.__new__(cls)
        cls.__init__(cls, *args, **kwargs)
        return obj


class Foo(metaclass=MyMeta):
    yaml_tag = '!Foo'

    def __init__(self, name):
        print('Foo.__init__')
        self.name = name

    def __new__(cls, *args, **kwargs):
        print('Foo.__new__')
        return object.__new__(cls)


foo = Foo('foo')


# 从上面的运行结果可以发现在定义 class Foo() 定义时，会依次调用 MyMeta 的 __new__ 和 __init__ 方法构建 Foo 类，然后在调
# 用 foo = Foo() 创建类的实例对象时，才会调用 MyMeta 的 __call__ 方法来调用 Foo 类的 __new__ 和 __init__ 方法。
