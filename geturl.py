#!/usr/bin/env python
# encoding: utf-8

# 查看重定向 url 的真实地址
from urllib2 import Request, urlopen

old_url = 'http://www.baidu.com'
req = Request(old_url)
response = urlopen(req)
print 'Old url: ' + old_url
print 'Real url: ' + response.geturl()

print '\nInfo():'
print response.info()
