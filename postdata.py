#!/usr/bin/env python
# encoding: utf-8

import urllib2
import urllib

url = 'http://www.talang100.com/signin'

values = {
    'nickname': 'kane',
    'username': 'a@t.com',
    'passwd': 't1234567890',
    'confirmPasswd': 't1234567890'
}

# user_agent = 'Mozilla/4.0'
# header = { 'User-Agent': user_agent  }

# data 数据需要编码成标准形式
data = urllib.urlencode(values)
print data

# 方式1
# 发送请求同时传送 data 表单
req = urllib2.Request(url, data)
# url 表单数据 伪装头部
# req = urllib2.Request(url, data, header)
# 接收反馈数据
response = urllib2.urlopen(req)
html = response.read()

print html
