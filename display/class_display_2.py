# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
import functools
from types import MethodType


def dynamic_param(func):
    @functools.wraps(func)
    def _wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        for _k, _v in kwargs.items():
            result[_k] = _v
        return result

    return _wrapper


class Param(metaclass=ABCMeta):
    allow_type = ["java", "spring_boot", "spring_cloud", "vue", "react", "angular", "socket", "hap"]

    @abstractmethod
    def java(self, **kwargs):
        pass

    @abstractmethod
    def spring_boot(self, **kwargs):
        pass

    def get_build_param(self, _type, **kwargs):
        if _type not in self.allow_type:
            raise Exception("Method {} Not Found".format(_type))
        if not hasattr(self, _type):
            raise Exception("Class BuildParam has no property {}".format(_type))
        func = getattr(self, _type)
        if not type(func) is MethodType:
            raise Exception("Method {} is not callable".format(_type))
        return func(**kwargs)


class BuildParam(Param):

    def __init__(self):
        self.CALL_BACK_URL = "www.callback.com"
        self.DOCKER_REGISTRY = {
            "USER": "bobo",
            "PASSWORD": "1233!@##"
        }

    @dynamic_param
    def java(self, **kwargs):
        self.__dict__['TEST_WHO'] = "java"
        return self.__dict__

    @dynamic_param
    def spring_boot(self, **kwargs):
        self.__dict__['TEST'] = "spring-boot"
        return self.__dict__


build_param = BuildParam()
res = build_param.get_build_param("java", PIPELINE_ID=123)
print(res)
