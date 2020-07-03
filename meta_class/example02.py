# -*- coding: utf-8 -*-
class MyClass(object):
    pass


instance = MyClass()

print(type(instance))

print(type(MyClass))


# 所有的 Python 的用户定义类，都是 type 这个类的实例
# 可能会让你惊讶，事实上，类本身不过是一个名为 type 类的实例。在 Python 的类型世界里，type 这个类就是造物的上帝。
# 以上在代码可以验证。
# instance 是 MyClass 的实例，而 MyClass 不过是“上帝” type 的实例。
