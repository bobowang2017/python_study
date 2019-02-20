# coding: utf-8
import time

from celery_study.tasks import add

# add.delay(4, 5)
print('7'*88)
add.apply_async((2, 8))
# add.delay(4, 5)
print('8'*88)

