# -*- coding: utf-8 -*-
def quick_sort(r, low, high):
    if low > high:
        return
    i, j = low, high
    temp = r[low]
    while i != j:
        while i < j and r[j] >= temp:
            j -= 1
        while i < j and r[i] <= temp:
            i += 1
        if i < j:
            r[i], r[j] = r[j], r[i]
        print(data)
    r[low], r[i] = r[i], temp
    quick_sort(r, low, i - 1)
    quick_sort(r, i + 1, high)
data = [7, 6, 9, 8, 5, 10, 3]
print(data)
quick_sort(data, 0, data.__len__() - 1)
print(data)
