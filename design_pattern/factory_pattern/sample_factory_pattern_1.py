from abc import ABCMeta, abstractmethod


class Coffee(metaclass=ABCMeta):
    @abstractmethod
    def show_taste(self):
        pass


class CoffeeLatte(Coffee):
    def show_taste(self):
        print("这是拿铁咖啡")


class MochaCoffee(Coffee):
    def show_taste(self):
        print("这是摩卡咖啡")


class MilkTea(Coffee):
    def show_taste(self):
        print("这是奶茶")


class CoffeeFactory(object):
    factory_type = ["CoffeeLatte", "MochaCoffee", "MilkTea"]

    @classmethod
    def create_coffee(cls, _type):
        if _type not in cls.factory_type:
            raise Exception('{}类型不存在'.format(_type))
        # eval（类名）返回的是一个class类型的对象
        return eval(_type)()


class App(object):
    factory = CoffeeFactory

    def coffee_make(self, coffee_type):
        unit = self.factory.create_coffee(coffee_type)
        unit.show_taste()


if __name__ == '__main__':
    app = App()
    app.coffee_make('MochaCoffee')
    app.coffee_make('MilkTea')
