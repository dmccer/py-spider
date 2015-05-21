#!/usr/bin/env python
# encoding: utf-8

from urllib2 import Request, urlopen, URLError

req = Request('http://www.zhihu.com/f')

try:
    response = urlopen(req)
    print 'Everything is ok.'
except URLError, e:
    if hasattr(e, 'code'):
        print 'The server couldn\'t fulfill the request.'
        print 'Error code: ', e.code
    elif hasattr(e, 'reason'):
        print 'We failed to reach a server.'
        print 'Reason: ', e.reason
    else:
        print 'No exception was raised'
