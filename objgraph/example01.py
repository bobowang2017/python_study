# -*- coding: utf-8 -*-
import gc
import objgraph

gc.collect()
objgraph.show_growth()
a = []
objgraph.show_growth()
a.append([1, 2, 3])
objgraph.show_growth()
b = ['a', 'b', 'c']
del b
objgraph.show_growth()
