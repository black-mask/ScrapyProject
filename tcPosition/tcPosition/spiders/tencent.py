# -*- coding: utf-8 -*-
import scrapy
from tcPosition.items import TcpositionItem

class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['hr.tencent.com']
    url = 'https://hr.tencent.com/position.php?&start='
    # 设置参数来遍历所有的页面
    offset = 0
    start_urls = [url + str(offset)]

    def parse(self, response):
        # 找到所需要信息的父节点
        list = response.xpath('//tr[@class="odd"] | //tr[@class="even"]')
        item = TcpositionItem()
        for position in list:
            item['position_name'] = position.xpath('./td[1]/a/text()').extract()[0]
            item['position_link'] = position.xpath('./td[1]/a/@href').extract()[0]
            # 部分条目职位类型会有缺失，用条件判断来处理
            item['position_type'] = position.xpath('./td[2]/text()').extract()[0] if position.xpath('./td[2]/text()').extract() else None
            item['position_num'] = position.xpath('./td[3]/text()').extract()[0]
            item['addr'] = position.xpath('./td[4]/text()').extract()[0]
            item['publishtime'] = position.xpath('./td[5]/text()').extract()[0]
            yield item

        # 控制页面遍历条件
        if self.offset < 3940:
            self.offset += 10
        # 循环调用爬虫来处理多个页面
        yield scrapy.Request(self.url + str(self.offset), callback=self.parse)

