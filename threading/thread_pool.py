import queue
import threading
import time

StopTask = object()


class ThreadPool(object):
    def __init__(self, max_num=5):
        #  一个不限长度的队列，用于放待处理的任务，一端存放，另一端由线程取任务执行，初始为空
        self.task = queue.Queue()
        #  线程的最大数量，默认为5
        self.max_num = max_num
        # 创建的线程存放在该列表中，初始为空，数量应小于self.max_num
        self.thread_list = []
        # 空闲的线程存放在该列表中，初始为空
        self.free_list = []
        # 一个标志位，表示进程是否终止，默认False：不终止；True：终止，不理解可以暂时先放一放
        self.isterminal = False

    def run(self, func, args, callback=None):
        """
        线程池启动函数
        :param func: 函数名称
        :param args: 函数参数
        :param callback: 回调函数
        :return:
        """
        task = (func, args, callback)
        self.task.put(task)

        if len(self.free_list) == 0 and len(self.thread_list) < self.max_num:
            self.generate_thread()

    def generate_thread(self):
        """创建线程"""
        t = threading.Thread(target=self.call)
        t.start()

    def call(self):
        """执行线程"""
        current_thread = threading.currentThread
        self.thread_list.append(current_thread)

        get_task = self.task.get()
        while get_task != StopTask:
            # 执行任务
            func, args, callback = get_task
            try:
                ret = func(*args)
                status = True
            except Exception as e:
                ret = e
                status = False
            # 执行回调函数
            if callback:
                try:
                    callback(status, ret)
                except Exception:
                    pass
            # 处理任务or立即终止
            if self.isterminal:
                # 立即终止
                get_task = StopTask
            else:
                # 空闲处理
                self.free_list.append(current_thread)
                get_task = self.task.get()
                self.free_list.remove(current_thread)
        else:
            # 销毁线程
            self.thread_list.remove(current_thread)

    def close(self):
        """
        等待任务全部完成后，清空所有线程
        :return:
        """
        num = len(self.thread_list)
        while num:
            self.task.put(StopTask)
            num -= 1

    def terminal(self):
        """
        立即终止所有的线程
        :return:
        """
        self.isterminal = True

        while self.thread_list:
            self.task.put(StopTask)

        self.task.empty()
