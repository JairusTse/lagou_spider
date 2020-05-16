# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class LagouItem(scrapy.Item):
    # 列表页数据
    jobName = scrapy.Field()
    jobId = scrapy.Field()
    district = scrapy.Field()
    company = scrapy.Field()
    companyId = scrapy.Field()
    salary = scrapy.Field()
    label = scrapy.Field()
    tempt = scrapy.Field()

    # 详情页数据
    request = scrapy.Field()
    level = scrapy.Field()
    scale = scrapy.Field()
    url = scrapy.Field()
    address = scrapy.Field()


