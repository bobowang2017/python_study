# -*- coding: utf-8 -*-
# 原型模式(Prototype Pattern):用原型实例指定创建对象的种类,并且通过拷贝这些原型创建新的对象。
"""
    设计模式——原型模式
    原型模式(Prototype Pattern):用原型实例指定创建对象的种类,并且通过拷贝这些原型创建新的对象。
    原型模式是用场景:需要大量的基于某个基础原型进行微量修改而得到新原型时使用。
    优点：原型模式关注的是大量相同对象或相似对象的创建问题，意图在于通过复制一个已经存在的实例来获得一个新的实例，以避免
    重复创建此类实例带来的开销。被复制的实例就是这个“原型”，这个原型是可定制的。
"""
from copy import copy, deepcopy


# 原型抽象类
class Prototype(object):

    def clone(self):
        pass

    def deep_clone(self):
        pass


# 工作经历类
class WorkExperience(object):

    def __init__(self):
        self.time_area = ''
        self.company = ''

    def set_work_experience(self, time_area, company):
        self.time_area = time_area
        self.company = company


# 简历类
class Resume(Prototype):

    def __init__(self, name):
        self.name = name
        self.work_experience = WorkExperience()

    def set_person_info(self, sex, age):
        self.sex = sex
        self.age = age

    def set_work_experience(self, time_area, company):
        self.work_experience.set_work_experience(time_area, company)

    def display(self):
        print(self.name)
        print(self.sex, self.age)
        print('工作经历', self.work_experience.time_area, self.work_experience.company)

    def clone(self):
        return copy(self)

    def deep_clone(self):
        return deepcopy(self)


if __name__ == '__main__':
    obj1 = Resume('andy')
    obj2 = obj1.clone()  # 浅拷贝对象
    obj3 = obj1.deep_clone()  # 深拷贝对象

    obj1.set_person_info('男', 28)
    obj1.set_work_experience('2010-2015', 'AA')
    obj2.set_person_info('男', 27)
    obj2.set_work_experience('2011-2017', 'AA')  # 修改浅拷贝的对象工作经历
    obj3.set_person_info('男', 29)
    obj3.set_work_experience('2016-2017', 'AA')  # 修改深拷贝的对象的工作经历

    obj1.display()
    obj2.display()
    obj3.display()
