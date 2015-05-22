#!/usr/bin/env python
# encoding: utf-8

import threading
import time
import Queue

# 构造一个不限制大小的队列
SHARE_Q = Queue.Queue()
# 设置线程个数
_WORKER_THREAD_NUM = 3


class MyThread(threading.Thread):

    def __init__(self, func):
        super(MyThread, self).__init__()
        self.func = func

    def run(self):
        self.func()


def worker():
    global SHARE_Q
    while not SHARE_Q.empty():
        item = SHARE_Q.get()
        print 'Processing: ', item
        time.sleep(1)


def main():
    global SHARE_Q
    threads = []

    # 向队列中放任务
    for task in xrange(1000):
        SHARE_Q.put(task)

    for i in xrange(_WORKER_THREAD_NUM):
        thread = MyThread(worker)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

if __name__ == '__main__':
    main()
