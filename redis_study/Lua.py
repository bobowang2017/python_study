import redis
import unittest


class LuaTest(unittest.TestCase):
    def setUp(self) -> None:
        pool = redis.ConnectionPool(host='10.176.139.10', port=6379)
        self.client = redis.Redis(connection_pool=pool)

    def test_lua(self):
        lua = """      
                if  redis.call('get', KEYS[1]) == ARGV[1] 
                    then
                        return redis.call('del', KEYS[1])
                    else
                        return 0           
                end
                """
        try:
            cmd = self.client.register_script(lua)
            return cmd(keys='keys', args='args')
        except Exception as e:
            print(e)
