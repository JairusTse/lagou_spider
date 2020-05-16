# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
from scrapy import Item
import json
import pymongo

from lagou.items import LagouItem


class LagouPipeline(object):

    @classmethod
    def from_crawler(cls, crawler):
        cls.DB_URL = crawler.settings.get('MONGO_DB_URI', 'mongodb://localhost:27017')
        cls.DB_NAME = crawler.settings.get('MONGO_DB_NAME', 'lagou')
        return cls()

    def open_spider(self, spider):
        print('启动爬虫')
        # self.file = open('lagou_jobs.txt', 'w', encoding='utf-8')
        self.client = pymongo.MongoClient(self.DB_URL)
        self.db = self.client[self.DB_NAME]

    def process_item(self, item, spider):
        if item['jobId']:
            print(item)
            collection = self.db['lagou_jobs_main_city']
            post = dict(item) if isinstance(item, Item) else item
            collection.insert_one(post)
            return item
        else:
            raise DropItem('没有标题，抛弃这个item')

    def close_spider(self, spider):
        print('关闭爬虫')
        self.client.close()
