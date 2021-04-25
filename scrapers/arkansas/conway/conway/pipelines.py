# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import scrapy
from scrapy.exceptions import DropItem

from scrapy import Request


class ConwayPipeline:
    def file_path(self, request, response=None, info=None):
        return ''
    
    def get_media_requests(self, item, info):
        file_url = item['file_url']
        meta = {'filename': item['name']}
        yield Request(url=file_url, meta=meta)

    def process_item(self, item, spider):
        return item
