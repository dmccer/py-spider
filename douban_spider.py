#!/usr/bin/env python
# encoding: utf-8

"""
一个简单地 Python 爬虫，用于抓取豆瓣电影 TOP 100 的电影
"""

import re
import urllib2
import time


class DouBanSpider(object):
    """类说明

    本类主要用于抓取豆瓣前 100 的电影

    """

    def __init__(self):
        self.page = 1
        self.cur_url = 'http://movie.douban.com/top250?start={page}&filter=&type='
        self.datas = []
        self._top_num = 1
        print '豆瓣电影爬虫准备就绪，准备爬取数据...'

    def get_page(self, cur_page):
        """

        根据当前页码爬取网页 HTML

        Args:
          cur_page: 表示当前抓取的网站页码

        Returns:
          返回抓取到整个页码的 HTML(unicode 编码)

        Raises:
          URLError: url 引发的异常

        """
        url = self.cur_url

        try:
            my_page = urllib2.urlopen(url.format(page=(cur_page - 1) * 25)).read().decode('utf-8')
        except urllib2.URLError, e:
            if hasattr(e, 'code'):
                print 'The server couldn\'t fulfill the request.'
                print 'Error code: %s' % e.code

            elif hasattr(e, 'reason'):
                print 'We failed to reach a server. Please check your url and read the reason'
                print 'Reason: %s' % e.reason

        return my_page

    def find_title(self, my_page):
        """

        通过返回的整个网页 HTML，正则匹配前 100 的电影

        Args:
          my_page: 传入页面的 HTML 文本用于正则匹配

        """

        temp_data = []
        movie_items = re.findall(r'<span.*?class="title">(.*?)</span>', my_page, re.S)

        for index, item in enumerate(movie_items):
            if item.find("&nbsp") == -1:
                temp_data.append('Top' + str(self._top_num) + ' ' + item)
                self._top_num += 1

        self.datas.extend(temp_data)

    def start_spider(self):
        """

        爬虫入口，并控制爬虫抓取页面的范围

        """
        while self.page <= 10:
            my_page = self.get_page(self.page)
            self.find_title(my_page)
            self.page += 1


def main():
    print """
        ###################################
           一个简单地豆瓣电影前 100 爬虫
           Author: Kane
           Version: 0.0.1
           Date: 2015-05-21
        ###################################
    """
    start_time = time.time()

    my_spider = DouBanSpider()
    my_spider.start_spider()

    for item in my_spider.datas:
        print item

    end_time = time.time()

    print '豆瓣爬虫爬取结束'
    print '总耗时：%d' % (end_time - start_time)

if __name__ == '__main__':
    main()
