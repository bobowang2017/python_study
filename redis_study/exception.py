# -*- coding: utf-8 -*-
import types


class RedisException(Exception):

    def __init__(self, *args):
        super().__init__(*args)


class ExceptionListener(object):

    def __init__(self, ignore_method):
        self.ignore_method = ignore_method

    def run_with_try(self, func):
        def ware(*args, **kwargs):
            try:
                res = func(*args, **kwargs)
            except Exception as e:
                res = None
            else:
                return res
        return ware

    def __call__(self, cls):
        for k, v in cls.__dict__.items():
            if isinstance(type(v), types.FunctionType) and k not in self.ignore_method:
                setattr(cls, k, self.run_with_try(v))
        return cls
