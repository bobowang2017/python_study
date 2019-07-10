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

    @classmethod
    def create_coffee(cls, _type):
        if _type == "coffee_latte":
            return CoffeeLatte()
        elif _type == "mocha_coffee":
            return MochaCoffee()
        elif _type == "milk_tea":
            return MilkTea()
        else:
            raise Exception('{}类型不存在'.format(_type))


class App(object):
    factory = CoffeeFactory

    def coffee_make(self, coffee_type):
        unit = self.factory.create_coffee(coffee_type)
        unit.show_taste()


if __name__ == '__main__':
    app = App()
    app.coffee_make('coffee_latte')
    app.coffee_make('milk_tea')
