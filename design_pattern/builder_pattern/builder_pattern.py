# 建造者模式（Builder Pattern）使用多个简单的对象一步一步构建成一个复杂的对象。这种类型的设计模式属于创建型模式，它提供了一
# 种创建对象的最佳方式。一个 Builder 类会一步一步构造最终的对象。该 Builder 类是独立于其他对象的。

"""
今天的例子，还是上一次谈到的快餐点餐系统。只不过，今天我们从订单的角度来构造这个系统。
"""


class Burger(object):
    """
    主餐
    """
    name = ""
    price = 0.0

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_name(self):
        return self.name


class CheeseBurger(Burger):
    def __init__(self):
        self.name = "cheese burger"
        self.price = 10.0


class SpicyChickenBurger(Burger):
    def __init__(self):
        self.name = "spicy chicken burger"
        self.price = 15.0


class Snack(object):
    """
    小食
    """
    name = ""
    price = 0.0
    type = "SNACK"

    def get_price(self):
        return self.price

    def set_pice(self, price):
        self.price = price

    def get_name(self):
        return self.name


class Chips(Snack):
    def __init__(self):
        self.name = "chips"
        self.price = 6.0


class ChickenWings(Snack):
    def __init__(self):
        self.name = "chicken wings"
        self.price = 12.0


class Beverage(object):
    """
    饮料
    """
    name = ""
    price = 0.0
    type = "BEVERAGE"

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_name(self):
        return self.name


class Coke(Beverage):
    def __init__(self):
        self.name = "coke"
        self.price = 4.0


class Milk(Beverage):
    def __init__(self):
        self.name = "milk"
        self.price = 5.0


"""
最终，我们是要建造一个订单，因而，需要一个订单类。假设，一个订单，包括一份主食，一份小食，一种饮料。
"""


class Order(object):
    burger = ""
    snack = ""
    beverage = ""

    def __init__(self, order_builder):
        self.burger = order_builder.bBurger
        self.snack = order_builder.bSnack
        self.beverage = order_builder.bBeverage

    def show(self):
        print("Burger:%s" % self.burger.getName())
        print("Snack:%s" % self.snack.getName())
        print("Beverage:%s" % self.beverage.getName())


class OrderBuilder(object):
    bBurger = ""
    bSnack = ""
    bBeverage = ""

    def add_burger(self, x_burger):
        self.bBurger = x_burger

    def add_snack(self, x_snack):
        self.bSnack = x_snack

    def add_beverage(self, x_beverage):
        self.bBeverage = x_beverage

    def build(self):
        return Order(self)


if __name__ == "__main__":
    order_builder = OrderBuilder()
    order_builder.add_burger(SpicyChickenBurger())
    order_builder.add_snack(Chips())
    order_builder.add_beverage(Milk())
    order_1 = order_builder.build()
    order_1.show()
