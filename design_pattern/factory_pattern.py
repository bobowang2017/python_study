# 简单工厂模式已经帮我们做到我们需要某种对象时，可以不关心对象是怎么创建的，只需要向工厂类要对象即可，但是如果我们又多了
# 一种对象，例如又出现了一个可乐品牌，嗯，我们叫它sfencs可乐吧，那么我们快餐店也得新添加这种可乐，也就是工厂类也得能够创
# 建sfencs可乐对象了，但是这样就得在工厂类中加入新的逻辑判断来根据用户需求制造新添加的这个对象，显然是不恰当的，因为这样
# 每当有一个新的类型的可乐增加的时候，我们都得修改工厂类的逻辑代码，使之能够判断出新的类型。这个问题使用工厂方法模式可以
# 得到解决。

# 工厂方法模式将原来的工厂类变为了抽象类，不同类型的可乐通过不同的子类生产，也就是工厂方法模式定义了一个创建对象的接口，但
# 具体创建哪个类的对象由子类来决定，这种方式的逻辑判断相当于交给了客户端，也就是KCD=Sfencs_produce()来选择使用哪个子类，这
# 样如果有新可乐产品出现的话，只需要再写一个子类继承工厂抽象类。这里的类中，快餐店抽象类也叫做抽象工厂类，它的子类称为具体
# 工厂类。可乐也一样，Coke为抽象产品类，它的子类为具体产品类。
from abc import ABCMeta, abstractmethod


class Coke(metaclass=ABCMeta):
    @abstractmethod
    def drink(self):
        pass


class Coca(Coke):
    def drink(self):
        print('drink Coca-Cola')


class Pepsi(Coke):
    def drink(self):
        print('drink Pepsi-Cola')


class Sfencs(Coke):
    def drink(self):
        print('drink Sfencs-Cola')


class FastFoodRestaurant(metaclass=ABCMeta):
    @abstractmethod
    def make_coke(self):
        pass


class CocaProduce(FastFoodRestaurant):
    def make_coke(self):
        return Coca()


class PepsiProduce(FastFoodRestaurant):
    def make_coke(self):
        return Pepsi()


class SfencsProduce(FastFoodRestaurant):
    def make_coke(self):
        return Sfencs()


KCD = SfencsProduce()
coke = KCD.make_coke()
coke.drink()

