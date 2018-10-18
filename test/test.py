# -*- coding: utf-8 -*-
def get_constellation(month, day):
    """
    根据生日计算星座
    :param month: 月份
    :param day: 天数
    :return:
    """
    dates = (21, 20, 21, 21, 22, 22, 23, 24, 24, 24, 23, 22)
    constellations = ("摩羯座", "水瓶座", "双鱼座", "白羊座", "金牛座", "双子座", "巨蟹座", "狮子座", "处女座", "天秤座", "天蝎座", "射手座", "摩羯座")
    if day < dates[month - 1]:
        return constellations[month - 1]
    else:
        return constellations[month]


def zodiac(month, day):
    constellations = ('摩羯座', '水瓶座', '双鱼座', '白羊座', '金牛座', '双子座',
                      '巨蟹座', u'狮子座', '处女座', '天秤座', '天蝎座', '射手座')

    d = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22), (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))
    return constellations[len(tuple(filter(lambda y: y <= (month, day), d))) % 12]


print(get_constellation(2, 19))
print(zodiac(2, 19))
