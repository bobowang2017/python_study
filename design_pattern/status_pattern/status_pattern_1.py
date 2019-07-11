# -*- coding: utf-8 -*-
class State(object):
    """
    状态父类，用于抽象状态方法，每增加一种状态，只需要增加一个子类，并修改相关状态的跳转

    """

    def __init__(self):
        pass

    def write_program(self, w):
        pass


class NoonState(State):
    def write_program(self, w):
        if w.get_hour() < 12:
            print('当前时间：%d, 精神百倍' % w.GetHour())
        else:
            w.set_state(AfterState())
            w.write_program()


class AfterState(State):
    def write_program(self, w):
        if w.get_hour() < 14:
            print('当前时间：%d, 吃午饭' % w.GetHour())
        else:
            w.set_state(EveningState())
            w.write_program()


class EveningState(State):
    def write_program(self, w):
        if w.get_finish():
            print('当前时间：%d, 睡觉' % w.GetHour())
        else:
            print('当前时间：%d，当日事，当日毕。加班吧' % w.GetHour())


class Work(object):
    def __init__(self):
        self.__hour = None
        self.__state = NoonState()
        self.__finish = False

    def get_hour(self):
        return self.__hour

    def set_hour(self, h):
        self.__hour = h

    def set_state(self, s):
        self.__state = s

    def get_finish(self):
        return self.__finish

    def set_finish(self, f):
        self.__finish = f

    def write_program(self):
        self.__state.write_program(self)


if __name__ == '__main__':
    work = Work()

    work.set_hour(10)
    work.write_program()

    work.set_hour(13)
    work.write_program()

    work.set_hour(19)
    work.write_program()

    work.set_hour(21)
    work.set_finish(True)
    work.write_program()
