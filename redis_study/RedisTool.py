import json

import redis
import unittest


class ListTest(unittest.TestCase):
    def setUp(self) -> None:
        pool = redis.ConnectionPool(host='192.168.64.128', port=6379)
        self.client = redis.Redis(connection_pool=pool)

    def test_lpush(self):
        self.client.lpush("list", ("wang", "xiang", "bo"))

    def test_lrange(self):
        data = self.client.lrange(name="logstash", start=0, end=100)
        print([json.loads(_data)for _data in data])
        return

    def test_blpop(self):
        pass

    def test_brpop(self):
        pass

    def test_lindex(self):
        return self.client.lindex("list", index=10)

    def test_llen(self):
        return self.client.llen("list")

    def test_lpop(self):
        return self.client.lpop("list")
