# -*- coding: utf-8 -*-
import inspect

import objgraph


class Dict(dict):
    def __init__(self, args={}):
        dict.__init__(self, args)


class List(list):
    def __init__(self, args=()):
        list.__init__(self, args)


class MyClass:
    def __init__(self):
        self.a = []
        d1 = Dict({1: 1})
        d2 = Dict({2: 2})
        l = List((1, 2, 3))
        self.a.append(d1)
        self.a.append(d2)


c = MyClass()

print 'objgraph.by_type:', objgraph.by_type('Dict')
chain = objgraph.find_backref_chain(objgraph.by_type('Dict')[-1], inspect.ismodule)
objgraph.show_chain(chain, filename='chain.png')
