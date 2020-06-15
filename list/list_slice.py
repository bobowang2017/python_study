import unittest


class ListSliceTest(unittest.TestCase):
    """
    step：正负数均可，其绝对值大小决定了切取数据时的‘‘步长”，而正负号决定了“切取方向”，
    正表示“从左往右”取值，
    负表示“从右往左”取值。
    当step省略时，默认为1，即从左往右以步长1取值。
    需要注意的是：如果方向与start-end构成的方向不一致，则为空。arr[6:3:1]
    """

    def setUp(self):
        self.arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    def test_range(self):
        """
        切片运算符s[i:j]代表的是从s中取一个子序列，它包含的元素索引k的范围是i<=k<j，默认移动步长为1
        """
        print(self.arr[3:9])

    def test_range_dis(self):
        """
        切片运算符s[i:j:stride]代表的是从s中取一个子序列，它包含的元素索引k的范围是i<=k<j，且移动步长为stride
        """
        print(self.arr[3:9:2])
        print(self.arr[6:3:-1])
        print(self.arr[6:3:1])

    def test_reverse_list(self):
        print(self.arr[::-1])


if __name__ == "__main__":
    unittest.main()
