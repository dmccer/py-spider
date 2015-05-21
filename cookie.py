#!/usr/bin/env python
# encoding: utf-8

import urllib2
import cookielib

cookie = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
res = opener.open('http://www.baidu.com')

for item in cookie:
    print item.name + ' : ' + item.value
