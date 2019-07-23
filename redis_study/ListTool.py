import json

import redis
import unittest


class ListTest(unittest.TestCase):
    def setUp(self) -> None:
        pool = redis.ConnectionPool(host='192.168.64.128', port=6379)
        self.client = redis.Redis(connection_pool=pool)
        self.key = "test_list"

    def test_lpush(self):
        """
        将一个或多个值插入到列表头部
        :return:
        """
        return self.client.lpush(self.key, *tuple("Python Java C++ C Go Html JavaScript".split(" ")))

    def test_rpush(self):
        return self.client.rpush(self.key, *tuple("Django SpringCloud Css NodeJs".split(" ")))

    def test_lrange(self):
        """
        获取列表指定范围内的元素
        :return:
        """
        data = self.client.lrange(name=self.key, start=0, end=100)
        print([json.loads(_data)for _data in data])
        return [json.loads(_data)for _data in data]

    def test_blpop(self):
        pass

    def test_brpop(self):
        pass

    def test_lindex(self):
        """
        通过索引获取列表中的元素
        :return:
        """
        return self.client.lindex(self.key, index=10)

    def test_llen(self):
        """
        获取列表长度
        :return:
        """
        return self.client.llen(self.key)

    def test_lpop(self):
        """
        移出并获取列表的第一个元素
        :return:
        """
        return self.client.lpop(self.key)

    def test_rpop(self):
        """
        移除列表的最后一个元素，返回值为移除的元素。
        :return:
        """
        return self.client.rpop(self.key)

    def test_lrem(self):
        pass

    def test_lset(self):
        pass
