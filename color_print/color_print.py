# -*- coding: utf-8 -*-
# 格式："\033[显示方式;前景色;背景色m 需要变颜色的字符串 \033[显示方式m"
# 例子："\033[1;31;47m 需要变颜色的字符串 \033[0m"
# <1-高亮显示 31前景色红色 47背景色黑色--需要变颜色的字符串--0-取消颜色设置>
#
# 说明：
# 前景色   背景色   颜色
# ---------------------------------------
#     40    黑色
#     41    红色
#     42    绿色
#     43    黃色
#     44    蓝色
#     45    紫红色
#     46    青蓝色
#     47    白色
# 显示方式   意义
# -------------------------
#     终端默认设置(即取消颜色设置)
#     高亮显示
#     使用下划线
#     闪烁
#     反白显示
#     不可见
test_str = 'Hello World'
print('\033[1;31;43m%s\033[0m' % test_str)


def color_print(str):
    print('\033[1;31;43m%s\033[0m' % str)
color_print('zhangsan')

