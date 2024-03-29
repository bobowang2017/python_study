from collections import namedtuple

# 创建一个具名元组
Customer = namedtuple('Customer', 'name fidelity')


class LineItem:

    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


# 上下文
class Order:

    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())


# 第一个具体策略
def fidelity_promo(order):
    """ 为积分为１０００或以上的顾客提供５％的折扣 """

    return order.total() * .05 if order.customer.fidelity >= 1000 else 0


# 第二个具体策略
def bulk_item_promo(order):
    """ 单个商品为２０个或以上时提供１０％折扣"""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount = item.total() * .1
    return discount


# 第三个具体策略
def large_order_promo(order):
    """ 订单中的不同商品达到１０个或以上时提供％７的折扣"""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07
    return 0


promos = [fidelity_promo, bulk_item_promo, large_order_promo]


def best_promo(order):
    """  选择可用的最佳折扣　"""
    return max(promo(order) for promo in promos)


promos = [globals()[name] for name in globals()
          if name.endswith('_promo')
          and name != 'best_promo']
