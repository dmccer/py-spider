#!/usr/bin/env python
# encoding: utf-8

import urllib
import urllib2


# 伪装成浏览器访问


def imitate_browser():
    postdata = urllib.urlencode({
        'nickname': 'kane',
        'username': 'b@t.com',
        'passwd': 't1234567890',
        'confirmPasswd': 't1234567890'
    })

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36'
    }

    req = urllib2.Request(
        url='http://www.talang100.com/signin',
        data=postdata,
        headers=headers
    )

    res = urllib2.urlopen(req)

    print res.read()

# 反盗链，查看头部 referer 是否为访问的网站


def reverse_link():
    postdata = urllib.urlencode({
        'username': 'a@t.com',
        'passwd': 't1234567890'
    })

    headers = {
        'Referer': 'http:/www.cnbeta.com/articles'
    }

    req = urllib2.Request(url="http://www.talang100.com/login", data=postdata, headers=headers)

    res = urllib2.urlopen(req)

    print res.read()

reverse_link()
