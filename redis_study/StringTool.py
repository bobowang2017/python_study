import redis
import unittest


class StringTest(unittest.TestCase):
    def setUp(self) -> None:
        pool = redis.ConnectionPool(host='192.168.64.128', port=6379)
        self.client = redis.Redis(connection_pool=pool)
        self.key = "test_string"

    def test_get_key(self):
        """
        获取指定 key 的值
        :return:
        """
        return self.client.get(self.key)

    def test_set_key(self):
        """
        设置指定 key 的值
        :return:
        """
        return self.client.set(self.key, "value", ex=None, px=None, nx=False, xx=False)

    def test_get_range_key(self):
        """
        返回 key 中字符串值的子字符
        :return:
        """
        return self.client.getrange(self.key, start=0, end=1)

    def test_get_set_key(self):
        """
        将给定 key 的值设为 value ，并返回 key 的旧值(old value)
        :return:
        """

        return self.client.getset(self.key, "value")
