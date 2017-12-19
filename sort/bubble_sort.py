# -*- coding: utf-8 -*-
def bubble_sort(lists):
    count = len(lists)
    for i in range(0, count):
        for j in range(i + 1, count):
            if lists[i] > lists[j]:
                lists[i], lists[j] = lists[j], lists[i]
                print(lists)
    return lists

data = [7, 6, 9, 8, 5, 10, 3]
print(data)
print(bubble_sort(data))