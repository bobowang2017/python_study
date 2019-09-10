# -*- coding: utf-8 -*-
template = {
    "name": "wangxiangbo",
    "number": 1,
    "meta_data": {
        "deploy": "k8s",
        "info": "hahah"
    },
    "owbe_data": [],
    "params": {
        "param_one": {
            "hello": "world",
            "juju": "i love you",
            "bobo": ["w", "h"]
        }
    }
}

result = {
    "name": "",
    "meta_data": {
        "info": ""
    },
    "params": {
        "param_one": {
            "hello": "",
            "bobo": ""
        }
    }
}


def display(data, template, key=""):
    for _k, _v in data.items():
        if isinstance(_v, dict):
            temp = template.get(_k)
            if not temp:
                return
            display(_v, temp, key=key + ":" + _k)
        else:
            print(key + ":" + _k + "->" + str(_v))
            data[_k] = template[_k]


print(result)
display(result, template)
print(result)
