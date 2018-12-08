# coding: utf-8
from celery import Celery

# app = Celery('tasks', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')
app = Celery('tasks', broker='amqp://admin:admin@47.105.104.233:5672/myvhost')
# app.config_from_object()


@app.task
def add(x, y):
    return x + y
