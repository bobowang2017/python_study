# coding: utf-8
from elasticsearch import Elasticsearch
from elasticsearch import helpers


class ElasticSearchUtils(object):

    def __init__(self):
        self.es = Elasticsearch(hosts=[{'host': 'localhost', 'port': 9200}])

    def index(self, index, doc_type, body, id=None):
        """
        插入文档
        :param index: 索引名称
        :param doc_type: 文档名称
        :param body: 文档内容
        :param id: 序列号
        :return:
        """
        return self.es.index(index, doc_type, body, id=id)

    def count(self, index_name):
        """
        :param index_name:
        :return: 统计index总数
        """
        return self.es.count(index=index_name)

    def delete(self, index_name, doc_type, id):
        """
        :param index_name:
        :param doc_type:
        :param id:
        :return: 删除index中具体的一条
        """
        return self.es.delete(index=index_name, doc_type=doc_type, id=id)

    def get(self, index_name, doc_type, id):
        """
        根据文档编号索引数据
        :param index_name: 索引名称
        :param doc_type: 文档类型名称
        :param id: 编号
        :return:
        """
        return self.es.get(index_name, doc_type, id=id)

    def search(self, index_name, doc_type, body, size=10):
        """
        根据条件进行搜索
        :param index_name: 索引名称
        :param doc_type: 文档类型名称
        :param body: 查询条件
        :param size: 查询数据条目
        :return:
        """
        try:
            results = self.es.search(index=index_name, doc_type=doc_type, body=body)
            return results['hits']['hits'][:size]
        except Exception as err:
            pass

    def bulk(self, actions):
        return helpers.bulk(self.es, actions)

    def delete_by_query(self, index, body, doc_type=None, params=None):
        return self.es.delete_by_query(index, body, doc_type=doc_type)


es_utils = ElasticSearchUtils()
