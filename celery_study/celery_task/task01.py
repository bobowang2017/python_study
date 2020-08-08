# -*- coding: utf-8 -*-
import time
from celery_study.celery_task.celery_app import cel_app


@cel_app.task
def send_email(res):
    time.sleep(5)
    print(res)
    return "Send Email Finished"
