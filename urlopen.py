#!/usr/bin/env python
# encoding: utf-8

import urllib2

# urlopen 返回应答对象 response
# 1. urlopen 接收 url 字符串
# 2. urlopen 接收 Reqeust 对象

# 1
response = urllib2.urlopen('http://www.baidu.com')
html = response.read()
print html

# 2
req = urllib2.Request('http://baidu.com')
response = urllib2.urlopen(req)
html = response.read()
print html

