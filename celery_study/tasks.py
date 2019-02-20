# coding: utf-8
import time
from celery.bin import worker as celery_worker
from celery import Celery, Task
from celery.utils.log import get_task_logger

BROKER_URL = 'redis://localhost:6379/0'
BACKEND_URL = 'redis://localhost:6379/0'

app = Celery('tasks', broker=BROKER_URL, backend=BACKEND_URL)

app.config_from_object('celery_study.celery_config')
logger = get_task_logger(__name__)


class MyTask(Task):
    def on_success(self, retval, task_id, args, kwargs):
        print('task done: {0}'.format(retval))
        return super(MyTask, self).on_success(retval, task_id, args, kwargs)

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        print('task fail, reason: {0}'.format(exc))
        return super(MyTask, self).on_failure(exc, task_id, args, kwargs, einfo)


@app.task(name='celery_study.tasks.add', base=MyTask, bind=True)
def add(self, x, y):
    time.sleep(10)
    logger.info(x + y)
    if x + y == 10:
        print("*"*20)
        print(self.max_retries)
        print("*" * 20)
        raise self.retry(max_retries=3, countdown=10)


def worker_start():
    worker = celery_worker.worker(app=app)
    worker.run(broker=BROKER_URL, concurrency=4, traceback=False, loglevel='INFO')


if __name__ == "__main__":
    worker_start()
