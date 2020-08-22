from celery_study.celery_task.celery_app import cel_app


def worker_start():
    from celery.bin import worker as celery_worker
    worker = celery_worker.worker(app=cel_app)
    worker.run(concurrency=4, traceback=False, loglevel='INFO', P="eventlet")


if __name__ == "__main__":
    worker_start()