from consul_study.consul_server import consul_cli
import unittest


class ConsulTest(unittest.TestCase):
    def setUp(self) -> None:
        # consul_cli.register("test", "123", "0.0.0.0", "8500")
        pass

    def test_set_key(self):
        _k, _v = "key1", "value1"
        print(consul_cli.set_kv(_k, _v))

    def test_get_key(self):
        print(consul_cli.get_kv("key1"))

    def test_register_service(self):
        return consul_cli.register("zhang", "123", "192.168.64.128", 8500, ["tag"], "10s")


if __name__ == '__main__':
    unittest.main()
