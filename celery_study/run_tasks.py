# coding: utf-8
import time

from celery_study.tasks import add

result = add.delay(4, 5)
# result = add.apply_async((2, 8))
print(result)

