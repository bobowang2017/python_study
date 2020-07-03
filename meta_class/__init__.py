# -*- coding: utf-8 -*-
class MyClass:
    data = 1


instance = MyClass()

MyClass = type('MyClass', (), {'data': 1})
instance = MyClass()
