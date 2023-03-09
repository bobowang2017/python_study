import redis
import unittest


class HashMapTest(unittest.TestCase):
    def setUp(self) -> None:
        pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
        self.client = redis.Redis(connection_pool=pool)
        self.key = "test_key"

    def test_hset(self):
        """
        将哈希表 key 中的字段name的值设为 value
        """
        keys = []
        return self.client.hset(self.key, "name", "value")

    def test_h_m_set(self):
        user = {"name":"wang", "age": 18, "address": "hubei"}
        return self.client.hmset(self.key, user)

    def test_hget(self):
        return self.client.hget(self.key, "name")

    def test_hkeys(self):
        return self.client.hkeys(self.key)

    def test_hgetall(self):
        return self.client.hgetall(self.key)

    def test_h_del(self):
        keys = ["age", "address"]
        return self.client.hdel(self.key, *keys)


