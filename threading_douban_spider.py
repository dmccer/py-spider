#!/usr/bin/env python
# encoding: utf-8

"""
多线程 Python 爬虫，爬取豆瓣 Top 前 100 的所有电影

Author: Kane
Date: 2015-05-22
"""

import urllib2
import re
import threading
import Queue
import time
import sys

reload(sys)
sys.setdefaultencoding('utf8')
_DATA = []
FILE_LOCK = threading.Lock()

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
        url = SHARE_Q.get()
        my_page = get_page(url)
        find_title(my_page)
        time.sleep(1)
        SHARE_Q.task_done()


def get_page(url):
    """
    根据 url 爬取网页 HTML

    Args:
        url: 要爬取页面的 url

    Returns:
        返回整个页面的 HTML(Unicode 编码)

    Raises:
        URLError: 请求 url 引起的异常
    """
    try:
        html = urllib2.urlopen(url).read().decode('utf-8')
    except urllib2.URLError, e:
        if hasattr(e, 'code'):
            print 'The server could not fulfill the request.'
            print 'Error code: %s' % e.code
        elif hasattr(e, 'reason'):
            print 'We failed to reach a server. Please check your url and read the reason.'
            print 'Reason: %s' % e.reason
        sys.exit()

    return html


def find_title(page):
    """
    匹配 page 中前 100 的电影名称

    Args:
        page: html 文本用于正则匹配
    """
    temp_data = []
    movie_items = re.findall(r'<span.*?class="title">(.*?)</span>', page, re.S)

    for index, item in enumerate(movie_items):
        if item.find('&nbsp') == -1:
            # print item
            temp_data.append(item)

    _DATA.append(temp_data)


def main():
    global SHARE_Q
    start_time = time.time()
    threads = []
    douban_url = 'http://movie.douban.com/top250?start={page}&filter=&type='
    for index in xrange(10):
        SHARE_Q.put(douban_url.format(page=index * 25))

    for i in xrange(_WORKER_THREAD_NUM):
        thread = MyThread(worker)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    SHARE_Q.join()

    end_time = time.time()
    print '总耗时：%d' % (end_time - start_time)

    with open('movie.txt', 'w+') as f:
        for page in _DATA:
            for movie_name in page:
                f.write(movie_name + '\n')

    print 'Spider Successful!!!!!'

if __name__ == '__main__':
    main()
