from scrapers.missouri.joplin.joplin.cityprotect.cityprotect import CityProtect

import scrapy


class CityconnectSpider(scrapy.Spider):
    name = 'cityprotect'
    allowed_domains = ['']
    start_urls = ['']

    def parse(self, response):
        sex_offenders_list = CityProtect.get_sex_offenders()
        print(sex_offenders_list)
        yield sex_offenders_list
