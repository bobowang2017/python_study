import unittest

import redis


class HashMapTest(unittest.TestCase):
    def setUp(self) -> None:
        pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
        self.client = redis.Redis(connection_pool=pool)
        self.key = "test_key"

    def test_hset(self):
        """
        将哈希表 key 中的字段name的值设为 value
        """
        r = redis.StrictRedis()
        pub = r.pubsub()
        pub.subscribe('__keyevent@0__:expired')

        for msg in pub.listen():
            print(msg['type'])
            print(msg['channel'])
            print(msg['data'])
            if msg['type'] == 'message':
                print('监听到啦')