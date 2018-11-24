# coding: utf-8
import datetime
import random
import string

import pymysql

connection = pymysql.Connect(host='localhost', port=3306, user='root', passwd='root', db='study', charset='utf8mb4')

cursor = connection.cursor()

sql = """insert into message (from_user, to_user, content, create_at) values('%s','%s','%s','%s')"""

for i in range(1, 1000000):
    from_user = str(random.randint(1, 10))
    to_user = str(random.randint(1, 10))
    content = ''.join(random.sample(string.ascii_letters + string.digits, 30))
    now_time = datetime.datetime.now()
    params = (from_user, to_user, content, now_time)
    print(sql % params)
    cursor.execute(sql % params)

connection.commit()
cursor.close()
connection.close()
