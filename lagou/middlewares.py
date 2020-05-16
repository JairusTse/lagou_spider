# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals


class LagouSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class LagouDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class CookieMiddleware(object):

    # ua_list = [
    #     'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0',
    #     'Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0',
    #     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
    #     'Opera/9.80 (Macintosh; Intel Mac OS X; U; en) Presto/2.2.15 Version/10.00'
    # ]
    #
    # custom_settings = {
    #     "COOKIES_ENABLED": False,
    #     "DOWNLOAD_DELAY": 1,
    #     'DEFAULT_REQUEST_HEADERS': {
    #         'Accept': 'application/json, text/javascript, */*; q=0.01',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'zh-CN,zh;q=0.8',
    #         'Connection': 'keep-alive',
    #         'Cookie': 'user_trace_token=20171015132411-12af3b52-3a51-466f-bfae-a98fc96b4f90; LGUID=20171015132412-13eaf40f-b169-11e7-960b-525400f775ce; SEARCH_ID=070e82cdbbc04cc8b97710c2c0159ce1; ab_test_random_num=0; X_HTTP_TOKEN=d1cf855aacf760c3965ee017e0d3eb96; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=0; PRE_UTM=; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DsXIrWUxpNGLE2g_bKzlUCXPTRJMHxfCs6L20RqgCpUq%26wd%3D%26eqid%3Dee53adaf00026e940000000559e354cc; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; index_location_city=%E5%85%A8%E5%9B%BD; TG-TRACK-CODE=index_hotjob; login=false; unick=""; _putrc=""; JSESSIONID=ABAAABAAAFCAAEG50060B788C4EED616EB9D1BF30380575; _gat=1; _ga=GA1.2.471681568.1508045060; LGSID=20171015203008-94e1afa5-b1a4-11e7-9788-525400f775ce; LGRID=20171015204552-c792b887-b1a6-11e7-9788-525400f775ce',
    #         'Host': 'www.lagou.com',
    #         'Origin': 'https://www.lagou.com',
    #         'Referer': 'https://www.lagou.com/',
    #         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    #     }
    # }

    def process_request(self, request, spider):
        request.headers['accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        request.headers['accept-encoding'] = 'gzip, deflate, br',
        request.headers['accept-language'] = 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
        request.headers['cache-control'] = 'max-age=0',
        request.headers['cookie'] = 'JSESSIONID=ABAAAECABIEACCADB90A86A71E6DAD2ECF2B38727C77577; WEBTJ-ID=20200502161006-171d46f74bba8-021a03d728c4-153f6554-1440000-171d46f74bc406; user_trace_token=20200502161006-5f64092b-68ad-49bb-85a1-952defce0136; LGUID=20200502161006-24b8a27b-853e-42e1-9809-59c326101987; _ga=GA1.2.1074256822.1588407007; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1587110728; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22171d47186695ae-07036821372d5c-153f6554-1440000-171d471866ab1b%22%2C%22%24device_id%22%3A%22171d47186695ae-07036821372d5c-153f6554-1440000-171d471866ab1b%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; X_MIDDLE_TOKEN=02fc7f6174fa05f29534d0042e6e367e; _gid=GA1.2.1621370232.1589458129; RECOMMEND_TIP=true; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; privacyPolicyPopup=false; TG-TRACK-CODE=index_navigation; SEARCH_ID=3ba76d5b9b864e779f1d0273fb7905d9; index_location_city=%E5%85%A8%E5%9B%BD; LGSID=20200517011232-2aa8e8d6-da46-46b4-85fb-5cedd9d0786b; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fpassport.lagou.com%2Flogin%2Flogin.html%3Fmsg%3Dvalidation%26uStatus%3D2%26clientIp%3D101.104.53.73; gate_login_token=f1b9dbaba1d5b52e5a9da435b228976eea3cb5c1fae38c6329dae2ac4305d11b; _putrc=43F69FDFC6C99C97123F89F2B170EADC; login=true; unick=%E7%94%A8%E6%88%B78772; _gat=1; hasDeliver=0; X_HTTP_TOKEN=1a6f741dbfa808232059469851197b66cad4d9d31a; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1589649504; LGRID=20200517011822-317e4c36-5f46-4051-a7a9-3880a2af4d31',
        request.headers['user-agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0',

    def process_response(self, request, response, spider):
        return response

    def process_exception(self, request, exception, spider):
        return None