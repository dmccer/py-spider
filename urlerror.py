#!/usr/bin/env python
# encoding: utf-8

import urllib2

req = urllib2.Request('http://www.csdn.com/ax')

try:
    urllib2.urlopen(req)
except urllib2.URLError, e:
    print e.code
    print e.reason
