# -*- coding: utf-8 -*-
import sys

if len(sys.argv) == 0:
    print('No params input')

print(type(sys.argv[0]))
data = list(sys.argv[1])
for i in range(0, len(data)):
    print(data[i])
