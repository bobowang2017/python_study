# -*- coding: utf-8 -*-
# 抽象工厂模式的主要目的是提供一个接口来创建一系列相关对象而无需指定具体的类。这个模式与与工厂方法模式的区别在于，它的一个
# 方法子类，可以创建一系列的对象。依然用可乐来举例，只喝普通的可乐还不足以让我们非常快乐，那么如果有一杯冰可乐，想必就能满
# 足我们了。于是我们的抽象产品类变为了两个，一个是冰可乐，一个是普通可乐，具体产品类有百事冰可乐、可口可乐冰可乐，普通百事
# ，普通可口可乐。抽象工厂类有生产冰可乐和生产普通可乐的抽象方法，具体工厂类有百事工厂，可口可乐工厂。
from abc import ABCMeta, abstractmethod


class IceCoke(metaclass=ABCMeta):
    @abstractmethod
    def drink(self):
        pass


class OrdinaryCoke(metaclass=ABCMeta):
    @abstractmethod
    def drink(self):
        pass


class CocaIce(IceCoke):
    def drink(self):
        print('drink  Coca-ice-Cola')


class PepsiIce(IceCoke):
    def drink(self):
        print('drink Pepsi-ice-Cola')


class CocaOrdinary(OrdinaryCoke):
    def drink(self):
        print('drink Coca-ordinary-Cola')


class PepsiOrdinary(OrdinaryCoke):
    def drink(self):
        print('drink Pepsi-ordinary-Cola')


class FastFoodRestaurant(metaclass=ABCMeta):
    @abstractmethod
    def make_ice_coke(self):
        pass

    @abstractmethod
    def make_ordinary_coke(self):
        pass


class CocaProduce(FastFoodRestaurant):
    def make_ice_coke(self):
        return CocaIce()

    def make_ordinary_coke(self):
        return CocaOrdinary()


class PepsiProduce(FastFoodRestaurant):
    def make_ice_coke(self):
        return PepsiIce()

    def make_ordinary_coke(self):
        return PepsiOrdinary()


KCD = CocaProduce()
coke = KCD.make_ice_coke()
coke.drink()
# drink  Coca-ice-Cola
