# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class TcpositionPipeline(object):
    def __init__(self):
        # win下要指定文件打开编码格式，默认打开容易出现中文转码错误
        self.filename = open('position.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        self.filename.write(json.dumps(dict(item), ensure_ascii=False) + '\n')
        return item

    def close_spider(self, spider):
        self.filename.close()


