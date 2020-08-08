# -*- coding: utf-8 -*-
from celery_study.celery_task.task01 import send_email
from celery_study.celery_task.task02 import send_msg

result = send_email.delay("hello")
print(result.id)
result = send_msg.delay("world")
print(result.id)
