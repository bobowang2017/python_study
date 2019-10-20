# -*- coding: utf-8 -*-
from itertools import chain

list1 = [1, 2, 3]

set1 = {'a', 'b'}

tun = (1, 4, 6,)

d = {'s': 'de', 'g': 123}

for i in chain(list1, set1, tun, d):
    print(i)
