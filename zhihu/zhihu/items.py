# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class ZhihuItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 问题的 url
    url = Field()
    # 问题的标题
    title = Field()
    # 问题的描述
    description = Field()
    # 问题的答案
    answer = Field()
    # 个人用户的名称
    name = Field()
