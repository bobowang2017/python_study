## 出错步骤

1、通过命令celery -A tasks worker --loglevel=info启动celery服务。

2、直接通过delay方式执行任务中的方法。

3、提示错误信息如下：Task handler raised error: ValueError('not enough values to unpack (expected 3, got 0)',)

##说明
Linux环境下是不存在这个问题的，只有win10环境下会出现

##解决方法
1、虚拟环境中安装eventlet(pip install eventlet)

2、启动celery服务的时候加个参数(celery -A <mymodule> worker -l info -P eventlet)

##启动celery服务的其他方式

    from celery.bin import worker as celery_worker
    from celery import Celery
    
    BROKER_URL = 'redis://localhost:6379/0'
    BACKEND_URL = 'redis://localhost:6379/0'
    app = Celery('tasks', broker=BROKER_URL, backend=BACKEND_URL)
    
    @app.task(name='celery_study.tasks.add')
        def add(x, y):
            time.sleep(5)
            return x + y

    def worker_start():
        worker = celery_worker.worker(app=app)
        worker.run(broker=BROKER_URL, concurrency=4, traceback=False, loglevel='INFO')

    if __name__ == "__main__":
        worker_start()