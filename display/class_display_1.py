# -*- coding: utf-8 -*-
from types import MethodType


class BuildParam(object):
    allow_type = ["java", "spring_boot", "spring_cloud"]

    def __init__(self):
        self.CALL_BACK_URL = "www.callback.com"
        self.DOCKER_REGISTRY = {
            "USER": "bobo",
            "PASSWORD": "1233!@##"
        }

    def reset(self, **kwargs):
        for _k, _v in kwargs.items():
            self.__dict__[_k] = _v

    def java(self, **kwargs):
        self.__dict__['TEST_WHO'] = "java"
        self.reset(**kwargs)
        return self.__dict__

    def spring_boot(self, **kwargs):
        self.__dict__['TEST'] = "spring"
        self.reset(**kwargs)
        return self.__dict__

    def get_build_param(self, _type, **kwargs):
        if _type not in self.allow_type:
            raise Exception("Method {} Not Found".format(_type))
        if not hasattr(self, _type):
            raise Exception("Class BuildParam has no property {}".format(_type))
        func = getattr(self, _type)
        if not type(func) is MethodType:
            raise Exception("Method {} is not callable".format(_type))
        return func(**kwargs)


build_param = BuildParam()
res = build_param.get_build_param("javac", PIPELINE_ID="213")
print(res)
