import unittest
from kubernetes import client, config


class TestK8s(unittest.TestCase):
    def setUp(self) -> None:
        config.kube_config.load_kube_config("config")
        self.v1 = client.CoreV1Api()

    def test_list_all_namespace(self):
        for ns in self.v1.list_namespace().items:
            print(ns.metadata.name)

    def test_list_pod_by_namespace(self):
        ns = "ccpow-zqdev01"
        ret = self.v1.list_namespaced_pod(ns)
        for i in ret.items:
            print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))