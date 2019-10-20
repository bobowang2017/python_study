# -*- coding: utf-8 -*-
# itemgetter用来去dict中的key，省去了使用lambda函数
from operator import itemgetter
# itertool还包含有其他很多函数，比如将多个list联合起来
from itertools import groupby

lst = [{'name': 'zhangsan', 'age': 20, 'country': 'China'},
       {'name': 'wangwu', 'age': 19, 'country': 'USA'},
       {'name': 'lisi', 'age': 22, 'country': 'JP'},
       {'name': 'zhaoliu', 'age': 22, 'country': 'USA'},
       {'name': 'pengqi', 'age': 22, 'country': 'USA'},
       {'name': 'lijiu', 'age': 22, 'country': 'China'}
       ]

# 通过country进行分组：
# 需要先排序，然后才能groupby。lst排序后自身被改变
lst.sort(key=itemgetter('country'))
lstg = groupby(lst, itemgetter('country'))

res = {}
for key, group in lstg:
    for g in group:
        if key in res:
            res[key].append(g)
        else:
            res[key] = [g]

print(res)
