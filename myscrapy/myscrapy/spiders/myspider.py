# -*- coding: utf-8 -*-
import scrapy
from myscrapy.items import MyscrapyItem


class MyspiderSpider(scrapy.Spider):
    name = 'myspider'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml#ajavaee']

    def parse(self, response):
        list = response.xpath('//div[@class="li_txt"]')
        for element in list:
            item = MyscrapyItem()
            name = element.xpath('./h3/text()').extract()
            title = element.xpath('./h4/text()').extract()
            info = element.xpath('./p/text()').extract()

            item['name'] = name[0].strip()
            item['title'] = title[0].strip()
            item['info'] = info[0].strip()
            yield item


