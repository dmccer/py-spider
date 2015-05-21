#!/usr/bin/env python
# encoding: utf-8

import urllib2

# 获取 HTTP 的返回码


def get_code():
    try:
        res = urllib2.urlopen('http://www.baidu.com')
    except urllib2.HTTPError, e:
        print e.code

    print res.getcode()

def debug_log():
    http_handler = urllib2.HTTPHandler(debuglevel = 1)
    https_handler = urllib2.HTTPSHandler(debuglevel = 1)
    opener = urllib2.build_opener(http_handler, https_handler)
    urllib2.install_opener(opener)
    res = urllib2.urlopen('http://www.baidu.com')


get_code()
debug_log()
