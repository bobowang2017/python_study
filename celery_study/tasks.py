# coding: utf-8
from celery import Celery

app = Celery('tasks', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')
app.config_from_object()

@app.task
def add(x, y):
    return x + y
