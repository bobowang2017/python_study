# -*- coding: utf-8 -*-
import gc
import objgraph

gc.collect()
print'==============================================='
objgraph.show_growth()
a = []
print'==============================================='
objgraph.show_growth()
a.append([1, 2, 3])
print'==============================================='
objgraph.show_growth()
b = ['a', 'b', 'c']
del b
print'==============================================='
objgraph.show_growth()
