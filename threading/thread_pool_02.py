import queue
from threading import Thread


class ThreadPoolManager(object):

    def __init__(self, thread_num):
        self.work_queue = queue.Queue()
        self.thread_num = thread_num

    def __init_threading_pool(self):
        for i in range(self.thread_num):
            thread = ThreadManager(self.work_queue)
            thread.start()

    def add_jobs(self, func, *args):
        self.work_queue.put((func, args))


class ThreadManager(Thread):

    def __init__(self, work_queue):
        Thread.__init__(self)
        self.work_queue = work_queue

    def run(self):
        while True:
            target, args = self.work_queue.get()
            target(*args)
            self.work_queue.task_done()

# thread_pool = ThreadPoolManager(4)
# thread_pool.add_jobs()
