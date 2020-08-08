# -*- coding: utf-8 -*-
from celery import Celery

cel_app = Celery(
    "celery_app_a",
    broker="redis://127.0.0.1:6379/1",
    backend="redis://127.0.0.1:6379/2",
    # 包含以下两个任务文件，去相应的py文件中寻找任务，对多个任务做分类。
    # 需要注意的是如果task定义的路径是在app同级别，则不需要include，否则需要include来指定任务的路径
    include=['celery_study.celery_task.task01', 'celery_study.celery_task.task02']
)

cel_app.conf.timezone = "Asia/Shanghai"
cel_app.conf.enable_utc = False
