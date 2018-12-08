# coding: utf-8
from pymongo import MongoClient


class MongodbClient:

    @property
    def mongodb_client(self):
        client = MongoClient(host='47.92.27.75', port=27017)
        db = client['on_app_location']
        db['test'].ensure_index([('location', '2dsphere')])
        return db['test']

    def insert(self, data):
        try:
            res = self.mongodb_client.insert(data)
        except Exception as e:
            res = 'Mongodb异常'
        return res

    def update(self, old_data, new_data):
        try:
            res = self.mongodb_client.update(old_data, new_data)
        except Exception as e:
            res = 'Mongodb异常'
        return res

    def find_all(self, condition=None, max_length=100):
        try:
            res = self.mongodb_client.find(condition).limit(max_length)
        except Exception as e:
            res = 'Mongodb异常'
        return res

    def delete(self, data):
        try:
            res = self.mongodb_client.remove(data)
        except Exception as e:
            res = 'Mongodb异常'
        return res

    def aggregate(self, condition=None):
        try:
            res = self.mongodb_client.aggregate(condition)
        except Exception as e:
            res = 'Mongodb异常'
        return res


mongodb_cli = MongodbClient()
