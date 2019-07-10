import unittest


class DictTool(unittest.TestCase):
    def setUp(self):
        self.data = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}

    def test_display_key(self):
        for _k in self.data:
            print(_k)

    def test_display(self):
        for _k, _v in self.data.items():
            print(_k, _v)

    def test_sort(self):
        print(sorted(self.data, key=lambda x: x, reverse=True))


if __name__ == "__main__":
    unittest.main()
