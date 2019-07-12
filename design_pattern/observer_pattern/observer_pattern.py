# 需求：员工上班在偷偷看股票，拜托前台一旦老板进来，就通知他们，让他们停止看股票。这里有两类人，一类是观察者，即员工，一
# 类是通知者，即前台，员工在观察前台的状态，前台负责通知员工最新的动态。


# class Receptionist(object):
#     def __init__(self):
#         self.observes = []
#         self.status = ''
#
#     def attach(self, observe):
#         self.observes.append(observe)
#
#     def notify(self):
#         for observe in self.observes:
#             observe.update()
#
#
# class StockObserve(object):
#     def __init__(self, name, receptionist):
#         self.name = name
#         self.receptionist = receptionist
#
#     def update(self):
#         print('%s,%s停止看股票' % (self.receptionist.status, self.name))
#
#
# if __name__ == '__main__':
#     receptionist = Receptionist()
#     observe1 = StockObserve('张三', receptionist)
#     observe2 = StockObserve('李四', receptionist)
#     receptionist.attach(observe1)
#     receptionist.attach(observe2)
#
#     receptionist.status = '老板来了'
#     receptionist.notify()

# 这里的两个类的耦合是非常大的，它们是相互依赖的。一方面是前台类的notify方法会调用股票观察者类的update方法，另一方面，观
# 察者类会访问调用前台类的status属性来获取最新的动态。当需求变动时，例如现在老板也可以是通知者，员工除了看股票，还会看nba
# ，如果增加一个Boss类和NBAObserver类，这样这四个类的耦合就会非常紧密，后期维护将非常困难，所以当遇到这种紧耦合的情况时，
# 就需要将它们耦合的部分抽象成一个父类，这样后期维护就会轻松很多。

from abc import ABCMeta, abstractmethod


class Subject(metaclass=ABCMeta):
    observers = []
    status = ''

    @abstractmethod
    def attach(self, observer):
        pass

    @abstractmethod
    def detach(self, observer):
        pass

    @abstractmethod
    def notify(self):
        pass


class Observer(object):
    __metaclass__ = ABCMeta

    def __init__(self, name, sub):
        self.name = name
        self.sub = sub

    @abstractmethod
    def update(self):
        pass


class Boss(Subject):
    def __init__(self):
        pass

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update()


class StockObserver(Observer):
    def update(self):
        print('%s,%s停止看股票' % (self.sub.status, self.name))


class NBAObserver(Observer):
    def update(self):
        print('%s,%s停止看NBA' % (self.sub.status, self.name))


if __name__ == '__main__':
    boss = Boss()
    observe1 = StockObserver('张三', boss)
    observe2 = NBAObserver('李四', boss)
    boss.attach(observe1)
    boss.attach(observe2)
    boss.detach(observe2)
    boss.status = '我是老板，我来了'
    boss.notify()
