# coding: utf-8
class Constant(object):

    def __setattr__(self, key, value):
        if key in self.__dict__.keys():
            raise TypeError("Can't change const.%s" % key)
        if not key.isupper():
            raise TypeError("const name %s is not all uppercase" % key)
        self.__dict__[key] = value


const = Constant()
const.MY_CONSTANT = "CHINA"
const.MY_SECOND_CONSTANT = "RUSSIA"
