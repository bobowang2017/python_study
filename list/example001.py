import unittest


class ListTool(unittest.TestCase):
    def setUp(self):
        self.a = [0, 1, 2, 3, 4, 5, 6]
        self.b = [7, 8, 9]

    def test_reverse_list(self):
        print(self.a[::-1])

    def test_add_list(self):
        self.a.extend(self.b)
        print(self.a)

    def test_counter(self):
        self.a.append(5)
        print(self.a.count(5))


if __name__ == "__main__":
    unittest.main()
