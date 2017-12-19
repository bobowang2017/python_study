# -*- coding: utf-8 -*-
from sys import getrefcount

a = 1
b = 1
print(id(a))
print(id(b))

l = [1, 2, 3]
print(getrefcount(l))

import gc
print(gc.get_threshold())
