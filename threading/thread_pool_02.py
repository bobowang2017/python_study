import queue
from threading import Thread


class ThreadPoolManager(object):

    def __init__(self, thread_num):
        # 这里定义的是一个线程安全的队列
        self.work_queue = queue.Queue()
        # 定义线程池最大线程数量
        self.thread_num = thread_num
        # 初始化工作线程
        self.__init_threading_pool()

    def __init_threading_pool(self):
        for i in range(self.thread_num):
            thread = WorkThread(self.work_queue)
            thread.start()

    def add_jobs(self, func, *args):
        self.work_queue.put((func, args))


class WorkThread(Thread):

    def __init__(self, work_queue):
        Thread.__init__(self)
        self.work_queue = work_queue

    def run(self):
        while True:
            # 从队列里取元素，如果block=True,则一直阻塞到有可用元素为止。
            target, args = self.work_queue.get(block=False)
            target(*args)
            self.work_queue.task_done()

# thread_pool = ThreadPoolManager(4)
# thread_pool.add_jobs()
