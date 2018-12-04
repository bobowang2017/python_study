# coding: utf-8
import time

from celery_study.tasks import add

result = add.delay(4, 5)
print(result)
# while not result.ready():
#     time.sleep(1)
# print('task done: {0}'.format(result.get()))
