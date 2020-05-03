from types import FunctionType


def t(_type):
    def test(func):
        def __wrapper(*args, **kwargs):
            print('111111111111')
            return func(*args, **kwargs)
        return __wrapper
    return test


class MetaPerson(type):
    def __new__(cls, *args, **kwargs):
        print('元类本身:', cls)
        print('类的命名空间词典:', args[2])
        class_dict = args[2]
        for attr, value in class_dict.items():
            if type(value) is FunctionType:
                class_dict[attr] = t()(value)
        print('类创建完成')


class Person(metaclass=MetaPerson):
    def __init__(self,name='0x',age = 1):
        self.name = name
        self.age = age

    def lastName(self):
        return self.name.split()[-1]


