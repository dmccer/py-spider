#!/usr/bin/env python
# encoding: utf-8

"""
多线程抓取豆瓣上海租房小组讨论信息
"""

import urllib2
import re
import threading
import Queue
import sys

reload(sys)
sys.setdefaultencoding('utf8')

SHARE_Q = Queue.Queue()
_WORKER_THREAD_NUM = 3
html_name = 1


class MyThread(threading.Thread):
    """
    自定义多线程模板
    """
    def __init__(self, func):
        super(MyThread, self).__init__()
        self.func = func

    def run(self):
        self.func()


def worker():
    global SHARE_Q

    while not SHARE_Q.empty():
        url = SHARE_Q.get()
        html = get_html(url)
        html_to_file(html)
        SHARE_Q.task_done()


def get_html(url):
    try:
        page = urllib2.urlopen(url).read().decode('utf-8')
        html = ''.join(re.findall(r'(<table class="olt">.*</table>)', page, re.S))
        html = re.sub(r'<script>[\s\S]*</script>', '', html)
    except urllib2.URLError, e:
        if hasattr(e, 'code'):
            print 'Error code: ', e.code
        elif hasattr(e, 'reason'):
            print 'Error reason: ', e.reason
        sys.exit()

    return html


def html_to_file(html):
    global html_name

    with open('zf_data/' + str(html_name), 'w+') as file:
        file.write(html)

    html_name += 1


def main():
    global SHARE_Q
    global HTML_Q

    db_threads = []
    douban_url = 'http://www.douban.com/group/shanghaizufang/discussion?start={start}'

    for start in xrange(10):
        SHARE_Q.put(douban_url.format(start=start))

    for i in xrange(_WORKER_THREAD_NUM):
        db_thread = MyThread(worker)
        db_thread.start()
        db_threads.append(db_thread)

    for thread in db_threads:
        thread.join()

    SHARE_Q.join()

if __name__ == '__main__':
    main()
