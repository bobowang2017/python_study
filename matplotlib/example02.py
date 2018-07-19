# -*- coding: utf-8 -*-
import pymysql
from matplotlib import pyplot as plt

db = pymysql.connect(host="47.105.104.233", user="root",
                     password="root", db="cp_backend", port=3306)

cur = db.cursor()
time_range = '2018-07-22 23:59:59'
sql1 = "select count(1) from user_info where create_at <'%s';" % time_range
sql3 = "SELECT count(1) from user_info_detail where create_at <'%s';" % time_range
sql4 = "SELECT count(1) from user_info_detail where nickname !='' and  create_at <'%s';" % time_range
try:
    cur.execute(sql1)
    result1 = cur.fetchall()
    cur.execute(sql3)
    result3 = cur.fetchall()
    cur.execute(sql4)
    result4 = cur.fetchall()
    print(result1[0][0], result3[0][0], result4[0][0])
    y_value_list = [result1[0][0], result3[0][0], result4[0][0]]
except Exception as e:
    raise e

# 点状图
# plt.plot([1, 2, 3, 4, 5], [result1[0][0], result2[0][0], result3[0][0], result4[0][0], result5[0][0]], 'ro')
x_name_list = ['Login', 'Allowed', 'Success']
# 柱状图
x_value_list = [1, 3, 5]
plt.bar(x_value_list, y_value_list, color='rgb', tick_label=x_name_list)
# 指定Y轴标签
plt.ylabel('Statics')
# 并指定轴域的可视区域
plt.axis([0, 12, 0, 5000])

tag = 'Time Range (%s -- %s)' % ('2018-06-08 14:00:00', time_range)
plt.text(2, 4800, tag, fontsize=10, color='blue')

for a, b in zip(x_value_list, y_value_list):
    plt.text(a, b + 0.1, '%.0f' % b, ha='center', va='bottom', fontsize=10)
plt.show()
