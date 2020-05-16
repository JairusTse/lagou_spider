# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector
from scrapy.http import Response
from scrapy.http import Request
from ..items import LagouItem

class LagouSpiderSpider(scrapy.Spider):
    name = 'lagou_spider'
    allowed_domains = ['lagou.com']
    # start_urls = ['https://www.lagou.com/']
    start_urls = [
        'https://www.lagou.com/guangzhou/',
        'https://www.lagou.com/beijing/',
        'https://www.lagou.com/shanghai/',
        'https://www.lagou.com/hangzhou/',
        'https://www.lagou.com/shenzhen/',
        'https://www.lagou.com/chengdu/',
        'https://www.lagou.com/wuhan/',
        'https://www.lagou.com/jiangsu/',
        'https://www.lagou.com/',
    ]

    def parse(self, response):
        # 爬取首页的关键字
        sel = Selector(text=response.text)
        labels = sel.xpath('//*[@id="sidebar"]/div/div')

        for label in labels:
            li = label.xpath('div[2]/dl')

            for item in li:
                jobs = item.xpath('dd/a')
                for job in jobs:
                    url = job.xpath('./@href').extract_first()
                    # name = job.xpath('h3/text()').extract_first()
                    print(url)

                    request = Request(url=url, callback=self.parse_list)
                    yield request

    # 解析列表的函数
    def parse_list(self, response):
        sel = Selector(text=response.text)
        li = sel.xpath('//*[@id="s_position_list"]/ul/li')

        for item in li:
            listItem = LagouItem()
            listItem['jobName'] = item.xpath('div[1]/div[1]/div[1]/a/h3/text()').extract_first()
            listItem['jobId'] = item.xpath('div[1]/div[1]/div[1]/a/@data-lg-tj-cid').extract_first()
            listItem['district'] = item.xpath('div[1]/div[1]/div[1]/a/span/em/text()').extract_first()
            listItem['company'] = item.xpath('./@data-company').extract_first()
            listItem['companyId'] = item.xpath('./@data-companyid').extract_first()
            listItem['salary'] = item.xpath('div[1]/div[1]/div[2]/div/span/text()').extract_first()
            listItem['tempt'] = item.xpath('div[2]/div[2]/text()').extract_first()

            '//*[@id="s_position_list"]/ul/li[1]/div[2]/div[1]/span[1]'
            # 拼接标签
            labels = item.xpath('div[2]/div[1]/span')
            if labels:
                label_str = ''
                for label in labels:
                    label_str += label.xpath('./text()').extract_first() + ','

                if label_str.endswith(','):
                    label_str = label_str[0:-1]

                # print(label_str)
                listItem['label'] = label_str

            # yield listItem
            # print(listItem)

            detail_url = item.xpath('div[1]/div[1]/div[1]/a/@href').extract_first()
            # print(detail_url)

            # 爬取详情
            # detail_rq = Request(url=detail_url, callback=self.parse_detail, meta={'data': listItem}, encoding='utf-8')
            # yield detail_rq
            yield listItem

        # 获取总页数
        page = sel.xpath('//*[@id="s_position_list"]/div[2]/div/a[5]/text()').extract_first()
        print(response.url, '的总页数：', page)
        # 爬取下一页
        if int(page) > 1:

            for i in range(2, int(page)):
                next_page = response.url + str(i) + '/'
                # print(next_page)
                request = Request(url=next_page, callback=self.parse_list_more)
                yield request

    # 解析列表的函数
    def parse_list_more(self, response):
        sel = Selector(text=response.text)
        li = sel.xpath('//*[@id="s_position_list"]/ul/li')

        for item in li:
            listItem = LagouItem()
            listItem['jobName'] = item.xpath('div[1]/div[1]/div[1]/a/h3/text()').extract_first()
            listItem['jobId'] = item.xpath('div[1]/div[1]/div[1]/a/@data-lg-tj-cid').extract_first()
            listItem['district'] = item.xpath('div[1]/div[1]/div[1]/a/span/em/text()').extract_first()
            listItem['company'] = item.xpath('./@data-company').extract_first()
            listItem['companyId'] = item.xpath('./@data-companyid').extract_first()
            listItem['salary'] = item.xpath('div[1]/div[1]/div[2]/div/span/text()').extract_first()
            listItem['tempt'] = item.xpath('div[2]/div[2]/text()').extract_first()

            '//*[@id="s_position_list"]/ul/li[1]/div[2]/div[1]/span[1]'
            # 拼接标签
            labels = item.xpath('div[2]/div[1]/span')
            if labels:
                label_str = ''
                for label in labels:
                    label_str += label.xpath('./text()').extract_first() + ','

                if label_str.endswith(','):
                    label_str = label_str[0:-1]

                # print(label_str)
                listItem['label'] = label_str

            # yield listItem
            # print(listItem)
            detail_url = item.xpath('div[1]/div[1]/div[1]/a/@href').extract_first()
            # print(detail_url)

            # 爬取详情
            # detail_rq = Request(url=detail_url, callback=self.parse_detail, meta={'data': listItem}, encoding='utf-8')
            # yield detail_rq
            yield listItem

    # 解析详情
    def parse_detail(self, response):
        sel = Selector(text=response.text)

        detailItem = response.meta['data']
        # detailItem['jobId'] = sel.xpath('//*[@id="no_interest"]/div/span[2]/@data-lg-tj-cid').extract_first()
        detailItem['level'] = sel.xpath('//*[@id="job_company"]/dd/ul/li[2]/h4/text()').extract_first()
        detailItem['scale'] = sel.xpath('//*[@id="job_company"]/dd/ul/li[3]/h4/text()').extract_first()
        detailItem['url'] = sel.xpath('//*[@id="job_company"]/dd/ul/li[4]/a/@href').extract_first()

        # 拼接要求
        reqs = sel.xpath('/html/body/div[6]/div/div[1]/dd/h3/span')
        if reqs:
            req_str = ''
            for re in reqs:
                req_str += re.xpath('./text()').extract_first()
            detailItem['request'] = req_str

        # 拼接地址
        address = sel.xpath('//*[@id="job_detail"]/dd[3]/div[1]/a')
        if address:
            ad_str = ''
            for ad in address:
                ad_str += ad.xpath('./text()').extract_first()

            if ad_str.endswith('查看地图'):
                ad_str = ad_str[0: -4]

            detailItem['address'] = ad_str

        print(detailItem)

        # yield detailItem
