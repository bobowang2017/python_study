# coding: utf-8
# 计数排序
# 计数排序的思想类似于哈希表中的直接定址法，在给定的一组序列中，先找出该序列中的最大值和最小值，从而确定需要开辟多大的
# 辅助空间，每一个数在对应的辅助空间中都有唯一的下标。
# 1、找出序列中最大值和最小值，开辟Max-Min+1的辅助空间。
# 2、最小的数对应下标为0的位置，遇到一个数就给对应下标处的值+1。
# 3、遍历一遍辅助空间，就可以得到有序的一组序列


def count_sort(data):
    min, max = 0, 0
    for i in range(len(data)):
        # 找出数组中最大值的下标
        if data[i] > data[max]:
            max = i
        if data[i] <= data[min]:
            min = i
    print('max=%s,min=%s' % (data[max], data[min]))
    temp = [0] * (data[max] - data[min] + 1)
    print(temp)
    for index, val in enumerate(data):
        temp[val - data[min]] += 1
    print(temp)


data = [4, 6, 6, 7, 9, 9, 9, 1, 1, 3, 5, 8]

count_sort(data)
