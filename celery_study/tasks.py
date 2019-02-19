# coding: utf-8
import time
from celery.bin import worker as celery_worker

from celery import Celery

BROKER_URL = 'redis://localhost:6379/0'
BACKEND_URL = 'redis://localhost:6379/0'

app = Celery('tasks', broker=BROKER_URL, backend=BACKEND_URL)


# app.config_from_object()


@app.task(name='celery_study.tasks.add')
def add(x, y):
    time.sleep(5)
    return x + y


def worker_start():
    worker = celery_worker.worker(app=app)
    worker.run(broker=BROKER_URL, concurrency=4, traceback=False, loglevel='INFO')


if __name__ == "__main__":
    worker_start()
