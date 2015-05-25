#!/usr/bin/env python
# encoding: utf-8

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from scrapy.http import Request, FormRequest
from zhihu.items import ZhihuItem


class ZhihuSpider(CrawlSpider):
    name = 'zhihu'
    allowed_domains = ['www.zhihu.com']
    start_urls = [
        'http://www.zhihu.com/topic/19552521'
    ]

    rules = (
        Rule(SgmlLinkExtractor(allow=('/question/\d+#.*?', )), callback='parse_page', follow=True),
        Rule(SgmlLinkExtractor(allow=('/question/\d+', )), callback='parse_page', follow=True)
    )

    headers = {
        'Accepts': '*/*',
        'Accept-Encoding': 'gzip,deflate',
        'Accept-Language': 'en-US,en;q=0.8,zh-TW;q=0.6,zh;q=0.4',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36',
        'Referer': 'http://www.zhihu.com'
    }

    def start_requests(self):
        return [Request('https://www.zhihu.com/login', meta={'cookiejar': 1}, callback=self.post_login)]

    def post_login(self, response):
        print 'Preparing login'
        xsrf = Selector(response).xpath('//input[@name="_xsrf"]/@value').extract()[0]
        print xsrf
        return [FormRequest.from_response(
            response,
            meta={'cookiejar': response.meta['cookiejar']},
            headers=self.headers,
            formdata={
                '_xsrf': xsrf,
                'email': '123456',
                'password': '123456'
            },
            callback=self.after_login,
            dont_filter=True
        )]

    def after_login(self, response):
        for url in self.start_urls:
            print url
            yield self.make_requests_from_url(url)

    def parse_page(self, response):
        problem = Selector(response)
        item = ZhihuItem()
        item['url'] = response.url
        item['name'] = problem.xpath('//span[@class="name"]/text()').extract()
        item['title'] = problem.xpath('//h2[@class="zm-item-title zm-editable-content"]/text()').extract()
        item['description'] = problem.xpath('//div[@class="zm-editable-content"]/text()').extract()
        item['answer'] = problem.xpath('//div[@class="fixed-summary zm-editable-content clearfix"]/text()').extract()
        return item
