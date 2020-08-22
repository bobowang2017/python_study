# -*- coding: utf-8 -*-
import unittest

from elasticsearch_study.es_api import es_client


class TestElasticSearch(unittest.TestCase):

    def setUp(self) -> None:
        self.client = es_client
        self.index_name = 'chengyu'
        self.doc_type = 'cy'

    def test_ping(self):
        print(self.client.ping())

    def test_create_index(self):
        mappings = {
            "mappings": {
                self.doc_type: {
                    "properties": {
                        "id": {
                            "type": "long",
                            "index": "false"
                        },
                        "name": {
                            "type": "text",  # keyword不会进行分词,text会分词
                            "index": True  # 不建索引
                        },
                        "spell": {
                            "type": "text",
                            "index": True
                        },
                        "content": {
                            "type": "text",
                            "index": True
                        },
                        "derivation": {
                            "type": "text",
                            "index": True
                        },
                        "sample": {
                            "type": "text",
                            "index": True
                        }
                    }
                }
            }
        }
        self.client.create_index(self.index_name, self.doc_type, mappings)

    def test_get_all_index(self):
        res = self.client.get_all_index()
        for _r in res:
            print(_r)

    def test_delete_index(self):
        _id = 'io5693MB4620cLqTniZA'
        self.client.delete(self.index_name, self.doc_type, _id)

    def test_delete_index_all(self):
        self.client.delete(self.index_name, self.doc_type)

    def test_index(self):
        body = {
            'name': '陂湖禀量',
            'spell': 'bēi  hú  bǐng  liáng',
            'content': '比喻度量宽广恢弘。',
            'derivation': '《后汉书·黄宪传》：“叔度汪汪若千顷陂，澄之不清，淆之不浊，不可量也。”',
            'samples': ''
        }
        self.client.insert(self.index_name, self.doc_type, body)

    def test_bulk_insert(self):
        index_name, doc_type = self.index_name, self.doc_type

        def bulk_es(chunk_data):
            response = self.client.insert(index_name, doc_type, chunk_data)
            print(response['result'])
            print(response['_shards'])

        with open('cy.json', encoding='utf-8') as f:
            data = eval(f.read())
            for index, _data in enumerate(data):
                print('index=%s' % str(index))
                _data['id'] = _data['ID']
                bulk_es(_data)

    def test_search(self):
        res = self.client.search('chengyu', 'cy', {'query': {'match': {'name': '陂湖禀'}}})
        print(res)

    def test_count(self):
        res = self.client.count(self.index_name)
        print(res)