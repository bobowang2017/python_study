# -*- coding: utf-8 -*-
import unittest


class TestSet(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_init_set(self):
        """
        set初始化
        :return:
        """
        s1 = [1, 2, 3, 4, 5]
        print(set(s1))
        s2 = {'a': 1, 'b': 2}
        print(set(s2))
        s3 = 'wang'
        print(set(s3))

    def test_add_and_remove(self):
        """
        set添加和移除元素
        :return:
        """
        s = set('hello wrold')
        print(s)
        s.add('b')
        print(s)
        s.remove('w')
        print(s)
        s.update('hs')
        print(s)

    def test_set_operation(self):
        """
        set的操作
        :return:
        """
        s1 = set([1, 2, 3, 4, 5])
        s2 = set([6, 7, 8, 4, 5])
        print(s1 | s2)
        print(s1.union(s2))
        print(s1 & s2)
        print(s1.intersection(s2))
        print(s1 ^ s2)
        print(s1.symmetric_difference(s2))
        print(s1 - s2)
        print(s1.difference(s2))
        print(s1 <= s2)
        print(s1.issubset(s2))
        print(s1 >= s2)
        print(s1.issuperset(s2))
