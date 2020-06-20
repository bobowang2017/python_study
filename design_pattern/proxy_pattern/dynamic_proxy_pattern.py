# -*- coding: utf-8 -*-
# python动态代理实现
from types import MethodType


class ProxyFactory:
    """
    类装饰器中的参数是需要在init方法定义的，实际执行是在__call__方法中
    """
    def __init__(self, hcls):
        if issubclass(hcls, InvocationHandler) or hcls is InvocationHandler:
            self.hcls = hcls
        else:
            raise HandlerException(hcls)

    def __call__(self, cls):
        """
        这里给类设置了一个代理对象Proxy，返回的是实例化的Proxy对象
        :param cls:
        :return:
        """
        return Proxy(cls, self.hcls)


class Proxy:
    def __init__(self, cls, hcls):
        self.cls = cls
        self.hcls = hcls
        self.handlers = dict()

    def __call__(self, *args, **kwargs):
        """
        通过代理完成被代理对象的初始化
        :param args:
        :param kwargs:
        :return:
        """
        self.obj = self.cls(*args, **kwargs)
        return self

    def __getattr__(self, attr):
        """
        访问任何被代理对象的属性都会调用该方法，可以在该方法中完成相关逻辑
        :param attr:
        :return:
        """
        print('get attr', attr)
        isExist = hasattr(self.obj, attr)
        res = None
        if isExist:
            res = getattr(self.obj, attr)
            if isinstance(res, MethodType):
                if self.handlers.get(res) is None:
                    self.handlers[res] = self.hcls(self.obj, res)
                return self.handlers[res]
            else:
                return res
        return res


class InvocationHandler:
    def __init__(self, obj, func):
        self.obj = obj
        self.func = func

    def __call__(self, *args, **kwargs):
        print('handler:', self.func, args, kwargs)
        return self.func(*args, **kwargs)


class HandlerException(Exception):
    def __init__(self, cls):
        super(HandlerException, self).__init__(cls, 'is not a hanlder class')


# 这里用类装饰器修饰了类Sample
@ProxyFactory(InvocationHandler)
class Sample:
    def __init__(self, age):
        self.age = age

    def foo(self):
        print('hello', self.age)

    def add(self, x, y):
        return x + y


s = Sample(12)
print(type(s))
s.foo()
s.add(1, 2)
s.add(2, 4)
print(s.age)
