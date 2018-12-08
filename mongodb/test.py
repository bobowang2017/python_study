# coding: utf-8
from mongodb.client import mongodb_cli

# mongodb_cli.insert([
#     {'user_id': 10, 'location': [114.355617, 30.526148]},
#     {'user_id': 9, 'location': [114.355617, 30.526148]
#      }])

datas = mongodb_cli.find_all()
result = [data for data in datas]
print(result)

mongodb_cli.delete({"user_id": {"$in": [7, 8, 9, 10]}})
