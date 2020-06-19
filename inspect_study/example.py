# -*- coding: utf-8 -*-
import functools
import inspect
import unittest

#
# class InspectTest(unittest.TestCase):
#
#     def setUp(self) -> None:
#         pass
#
#     def get_runtime_param(self):
#         pass


def check_is_admin(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        func_args = inspect.getcallargs(f, *args, **kwargs)
        print(func_args)
        res = f(*args, **kwargs)
        print(inspect.stack())
        return res
    return wrapper


@check_is_admin
def get_food(age, name='wangxiangbo'):
    print(age)


get_food(18)
