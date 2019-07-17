import consul


class ConsulClient(object):

    def __init__(self, host=None, port=None, token=None):
        self.host = host
        self.port = port
        self.token = token
        self.consul = consul.Consul("192.168.64.128", 8500, "http")

    # 注册服务 注册服务的服务名  端口  以及 健康监测端口
    def register(self, name, service_id, address, port, tags, interval):
        check = consul.Check.tcp(address, port, "10s")
        self.consul.agent.service.register(name, service_id=service_id, address=address, port=port, tags=tags,
                                           interval=interval, check=check)

    def deregister(self, service_id):
        # 此处有坑，源代码用的get方法是不对的，改成put,两个方法都得改
        self.consul.agent.service.deregister(service_id)
        self.consul.agent.check.deregister(service_id)

    def set_kv(self, key, value):
        return self.consul.kv.put(key, value)

    def get_kv(self, key):
        return self.consul.kv.get(key)


consul_cli = ConsulClient()

