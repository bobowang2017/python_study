# 项目地址：https://github.com/cool-RR/pysnooper

import pysnooper


@pysnooper.snoop()
def number_to_bits(number):
    number += 3
    data_ = [i_ ** 2 for i_ in range(number)]
    return data_


number_to_bits(1)
