# coding: utf-8
def heap_adjust(L, start, end):
    temp = L[start]
    i, j = start, 2 * start + 1
    while i <= end:
        if j < end and L[j] < L[j + 1]:
            j += 1
        if j < end and temp < L[j]:
            L[i] = L[j]
            i = j
            j = 2 * i + 1
        else:
            break
    L[i] = temp


data = [7, 6, 9, 8, 5, 10, 3, 7, 1, 4, 2]
print("初始数据")
print(data)
len_data = len(data)
first_sort_count = int(len_data / 2 - 1)
# 构造初始堆
print("初始堆的构造")
for i in range(first_sort_count + 1):
    heap_adjust(data, first_sort_count - i, len_data - 1)
    print(data)

while len_data - 1 >= 0:
    data[0], data[len_data - 1] = data[len_data - 1], data[0]
    print("调整后的堆")
    heap_adjust(data, 0, len_data - 1)
    print(data)
    len_data -= 1
print("最终数据")
print(data)
