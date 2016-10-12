# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


# 相当于数据库Model类
class Article(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 相当于数据库中的行元素
    title = scrapy.Field()
