import datetime

import redis
import unittest


class KeyTest(unittest.TestCase):
    def setUp(self) -> None:
        pool = redis.ConnectionPool(host='192.168.64.128', port=6379)
        self.client = redis.Redis(connection_pool=pool)
        self.key = "test_key"

    def test_del_key(self):
        """
        该命令用于在 key 存在时删除 key
        :return:
        """
        return self.client.delete(self.key)

    def test_exist_key(self):
        """
        检查给定 key 是否存在
        :return:
        """
        return self.client.exists(self.key)

    def test_expire_key(self):
        """
        为给定 key 设置过期时间，以秒计
        :return:
        """
        return self.client.expire(self.key, time=10)

    def test_expire_at_key(self):
        """
        EXPIREAT 的作用和 EXPIRE 类似，都用于为 key 设置过期时间。
        不同在于 EXPIREAT 命令接受的时间参数是 UNIX 时间戳(unix timestamp)。
        :return:
        """
        return self.client.expireat(self.key, when=datetime.datetime.now())

    def test_p_expire_key(self):
        """
        设置 key 的过期时间以毫秒计。
        :return:
        """
        return self.client.pexpire(self.key, time=10)

    def test_p_expire_at_key(self):
        """
        设置 key 过期时间的时间戳(unix timestamp) 以毫秒计
        :return:
        """
        pass

    def test_keys(self):
        """
        查找所有符合给定模式( pattern)的 key
        :return:
        """
        return self.client.keys()

    def test_move_key_db(self):
        pass

    def test_persist_key(self):
        """
        移除 key 的过期时间，key 将持久保持
        :return:
        """
        return self.client.persist(self.key)

    def test_ttl_key(self):
        """
        以秒为单位，返回给定 key 的剩余生存时间
        :return:
        """
        return self.client.ttl(self.key)

    def test_p_ttl_key(self):
        """
        以毫秒为单位，返回给定 key 的剩余生存时间
        :return:
        """
        return self.client.pttl(self.key)

    def test_random_key(self):
        """
        从当前数据库中随机返回一个 key
        :return:
        """
        return self.client.randomkey()

    def test_rename_key(self):
        """
        修改 key 的名称
        :return:
        """
        return self.client.rename(self.key, "new_name")

    def test_type_key(self):
        """
        返回 key 所储存的值的类型
        :return:
        """
        return self.client.type(self.key)

    def test_renamenx_key(self):
        """
        仅当 newkey 不存在时，将 key 改名为 newkey
        :return:
        """
        return self.client.renamenx(self.key, "new_name")
