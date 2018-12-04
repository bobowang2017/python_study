# coding: utf-8
def heap_sort(L, start, end):
    temp = L[start]
    i, j = start, 2 * start
    while i <= end:
        if j < end and L[j] < L[j + 1]:
            j += 1
        if temp < L[j]:
            L[i] = L[j]
            i = j
            j = 2 * i
        else:
            break
    L[i] = temp


def heap_adjust():
    pass


data = [0, 7, 6, 9, 8, 5, 10, 3, 7, 1, 4, 2]
# data = [0, 90, 50, 80, 16, 30, 60, 70, 10, 2]
print(data)
len_data = len(data)
first_sort_count = int(len_data / 2 -1)
for i in range(first_sort_count-1):
    heap_sort(data, first_sort_count - i, len_data - 1)
print(data)
# heap_sort()
