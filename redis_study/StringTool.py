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

    def test_get_bit(self):
        """
        对 key 所储存的字符串值，获取指定偏移量上的位(bit)
        :return:
        """
        return self.client.getbit(name="", offset=0)

    def test_mget(self):
        """
        获取所有(一个或多个)给定 key 的值
        :return:
        """
        return self.client.mget(keys=["key1", "key2"])

    def test_set_bit_key(self):
        pass

    def test_setex(self):
        """
        将值 value 关联到 key ，并将 key 的过期时间设为 seconds (以秒为单位)
        :return:
        """
        return self.client.setex(self.key, "value", 10)

    def test_setnx(self):
        """
        只有在 key 不存在时设置 key 的值
        :return:
        """
        return self.client.setnx(self.key, "value")

    def test_setrange(self):
        pass

    def test_strlen(self):
        """
        返回 key 所储存的字符串值的长度
        :return:
        """
        return self.client.strlen(self.key)

    def test_sget(self):
        """
        同时设置一个或多个 key-value 对
        :return:
        """
        # return self.client.mset(*args, **kwargs)
        pass

    def test_msetnx(self):
        pass

    def test_incr_key(self):
        """
        将 key 中储存的数字值增一
        :return:
        """
        return self.client.incr(self.key)

    def test_incr_by_key(self):
        """
        将 key 所储存的值加上给定的增量值（increment）
        :return:
        """
        return self.client.incrby(self.key, 10)

    def test_decr_key(self):
        """
        将 key 中储存的数字值减一
        :return:
        """
        return self.client.decr(self.key)

    def test_append_key(self):
        """
        如果 key 已经存在并且是一个字符串， APPEND 命令将指定的 value 追加到该 key 原来值（value）的末尾
        :return:
        """
        return self.client.append(self.key, "value")
