import redis
import unittest


class HashMapTest(unittest.TestCase):
    def setUp(self) -> None:
        pool = redis.ConnectionPool(host='192.168.64.128', port=6379)
        self.client = redis.Redis(connection_pool=pool)
        self.key = "test_key"

    def test_hset(self):
        """
        将哈希表 key 中的字段name的值设为 value
        """
        return self.client.hset(self.key, "name", "value")

    def test_hget(self):
        return self.client.hget(self.key, "name")

    def test_hkeys(self):
        return self.client.hkeys(self.key)

    def test_hgetall(self):
        return self.client.hgetall(self.key)

