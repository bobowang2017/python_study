# -*- coding: utf-8 -*-


class BuildParam(object):
    CALL_BACK_URL = "www.haop123.com"
    DOCKER_REGISTRY = {
        "URL": "www.hao123.com",
        "USER": "zhangsan",
        "PASSWORD": "#@#DEFE"
    }

    def __setattr__(self, key, value):
        if not key.isupper():
            raise TypeError("key %s is not all uppercase" % key)
        else:
            self.__dict__[key] = value


class JavaBuildParam(BuildParam):
    build_key = "java"
    DOCKERFILE_URL = "www.wangyi.com"
    HELLO = "wangfwef"
    WORLD = "bobowang"


class SpringBootBuildParam(BuildParam):
    build_key = "spring-boot"
    DEPLOYMENT_URL = "who am i "


def get_build_params(_type, **kwargs):
    build_params = None
    for _class in BuildParam.__subclasses__():
        print(_class.__name__)
        if hasattr(_class, "build_key"):
            if getattr(_class, "build_key") == _type:
                build_params = _class
                break
    if build_params:
        constant = build_params()
        for _k, _v in kwargs.items():
            constant.__dict__[_k.upper()] = _v
        return constant
    else:
        raise Exception("Not Found BuildParam {}".format(_type))


build_constant = get_build_params("javac", pipeline_id="woshiwangxiangbo")
params = {_property: getattr(build_constant, _property) for _property in dir(build_constant) if _property.isupper()}
for _k, _v in params.items():
    print(_k, _v)
