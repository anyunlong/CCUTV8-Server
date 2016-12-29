#!/usr/bin/python
# #-*-coding:utf-8 -*-

import scrapy
from crawler.items import CartoonItem, EpisodeItem
from v8.models import Cartoon, Episode
from scrapy.http import Request

class CartoonSpider(scrapy.Spider):
    name = "cartoon"
    start_urls = ["http://v8.ccut.edu.cn/sort.php?/7/"]

    def parse(self, response):
        Cartoon.objects.all().delete()
        Episode.objects.all().delete()
        for sel in response.xpath('//td/span/b/a'):
            cartoonItem = CartoonItem()
            for name in sel.xpath('text()').extract():
                cartoonItem["name"] = name.encode('utf-8')
            for url in sel.xpath('@href').extract():
                cartoonItem["url"] = url.encode('utf-8')
            cartoonItem.save()
            yield Request(cartoonItem["url"], callback=self.parse_episode)

    def parse_episode(self, response):
        selectors = response.xpath('//tr/td[1]/span/a')
        for index in range(len(selectors)):
            if (index > 4):
                for url in selectors[index].xpath('@href').extract():
                    yield Request(url, callback=self.parse_detail_episode)

        selectors = response.xpath('//td[@align="right"]/span[@class="normalfont"]/a')
        for sel in selectors:
            for text in sel.xpath('text()').extract():
                if text == u"下一页":
                    for url in sel.xpath('@href').extract():
                        yield Request(url, callback=self.parse_episode)

    def parse_detail_episode(self, response):
        episodeItem = EpisodeItem()
        for title in response.xpath('//font/b/text()').extract():
            episodeItem["title"] = title.encode('utf-8')
        for cartoon_name in response.xpath('//span[@class="normalfont"]/a[3]').xpath('text()').extract():
            episodeItem["cartoon"] = cartoon_name.encode('utf-8')
        for url in response.xpath('//td/p/a[@target="_blank"]/@href').extract():
            episodeItem["url"] = url.encode('utf-8')
        episodeItem.save()