# coding: utf-8
import redis


class RedisClient(object):
    @property
    def redis_client(self):
        pool = redis.ConnectionPool(host='localhost', port=6379)
        client = redis.Redis(connection_pool=pool)
        return client

    def lpush(self, name, *values):
        return self.redis_client.lpush(name, *values)

    def set_key(self, name, value):
        return self.redis_client.set(name, value)

    def exist_key(self, name):
        return self.redis_client.exists(name)

    def lrange(self, name, start, end):
        return self.redis_client.lrange(name, start, end)


redis_cli = RedisClient()
