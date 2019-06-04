class CoffeeLatte(object):
    def show_taste(self):
        print("这是拿铁咖啡")


class MochaCoffee(object):
    def show_taste(self):
        print("这是摩卡咖啡")


class MilkTea(object):
    def show_taste(self):
        print("这是奶茶")


class CoffeeFactory(object):
    coffee_type = {
        'coffee_latte': CoffeeLatte,
        'mocha_coffee': MochaCoffee,
        'milk_tea': MilkTea
    }

    @classmethod
    def create_coffee(cls, _type):
        if _type not in cls.coffee_type.keys():
            raise Exception('类型不存在')
        return cls.coffee_type.get(_type)()


class App(object):
    factory = CoffeeFactory

    def coffee_make(self, coffee_type):
        unit = self.factory.create_coffee(coffee_type)
        unit.show_taste()


if __name__ == '__main__':
    app = App()
    app.coffee_make('coffee_latte')
    app.coffee_make('milk_tea')
