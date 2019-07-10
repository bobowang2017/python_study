# 定义:不直接向客户暴露对象创建的实现细节,而是通过一个工厂类来负责创建产品类的实例。
# 角色:工厂角色,抽象产品角色,具体产品角色。
# 优点:隐藏了对象创建代码的细节,客户端不需要修改代码。
# 缺点:违反了单一职责原则,将创建逻辑集中到一个工厂里面,当要添加新产品时,违背了开闭原则。


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
