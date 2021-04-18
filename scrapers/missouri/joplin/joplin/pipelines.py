# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import scrapy
from scrapy.exceptions import DropItem
import pymongo
from logging import log
# from scrapy.conf import settings

from scrapy import Request


class JoplinPipeline:
    def file_path(self, request, response=None, info=None):
        return ''
    
    def get_media_requests(self, item, info):
        file_url = item['file_url']
        meta = {'filename': item['name']}
        yield Request(url=file_url, meta=meta)

    def process_item(self, item, spider):
        return item

class MongoDBPipeline(object):

    def __init__(self):
        connection = pymongo.MongoClient(
            scrapy.conf.settings['MONGODB_SERVER'],
            scrapy.conf.settings['MONGODB_PORT']
        )
        db = connection[scrapy.conf.settings['MONGODB_DB']]
        self.collection = db[scrapy.conf.settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            self.collection.insert(dict(item))
            log.msg("Sex offender added to MongoDB database!", level=log.DEBUG, spider=spider)
        return item