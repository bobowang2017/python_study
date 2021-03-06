# coding: utf-8
import redis

from redis_study.exception import ExceptionListener


@ExceptionListener(["redis_client"])
class RedisClient(object):
    @property
    def redis_client(self):
        pool = redis.ConnectionPool(
            host='127.0.0.1', port=6379,
            max_connections=300, decode_responses=True)
        client = redis.Redis(connection_pool=pool,  socket_connect_timeout=1)
        return client

    def get(self, key):
        return self.redis_client.get('bobo')

    def lpush(self, name, *values):
        return self.redis_client.lpush(name, *values)

    def set_key(self, name, value):
        return self.redis_client.set(name, value)

    def exist_key(self, name):
        return self.redis_client.exists(name)

    def lrange(self, name, start, end):
        return self.redis_client.lrange(name, start, end)


redis_cli = RedisClient()

res = redis_cli.get('hello')
print(res)