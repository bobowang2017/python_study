from es.elastic_search_server import es_utils
import unittest


class Example(unittest.TestCase):

    def setUp(self):
        self.client = es_utils
        self.index = "school"
        self.doc_type = "name_detail"

    # def test_index(self):
    #     data = {
    #         "c_name": "米勒中学",
    #         "e_name": "Miller School of Albemarle",
    #         "country": "美国",
    #         "education": "高中"
    #     }
    #     result = self.client.index(self.index, self.doc_type, data)
    #     print(result)

    # def test_delete(self):
    #     id = 123
    #     result = self.client.delete(self.index, self.doc_type, id)
    #     print(result)

    # def test_search(self):
    #     query = {
    #         "query": {
    #             "match_all": {}
    #         }
    #     }
    #     result = self.client.search(self.index, self.doc_type, query, size=10)
    #     print(result)

    def test_bulk(self):
        with open('school.json', encoding='utf-8') as f:
            schools = eval(f.read())
            action = [
                {
                    "_index": self.index,
                    "_type": self.doc_type,
                    "_source": {
                        "c_name": school['c_name'],
                        "e_name": school['e_name'],
                        "country": school['country'],
                        "education": school['education']}
                } for school in schools
            ]
            return self.client.bulk(action)

    # def test_mutil_delete(self):
    #     query = {
    #         "query": {
    #             "match_all": {}
    #         }
    #     }
    #     return self.client.delete_by_query(self.index, query, doc_type=self.doc_type, params=None)


if __name__ == '__main__':
    unittest.main()
