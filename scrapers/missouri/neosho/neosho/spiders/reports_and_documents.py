import scrapy


class ReportsAndDocumentsSpider(scrapy.Spider):
    name = 'reports_and_documents'
    allowed_domains = ['www.neoshomo.org']
    start_urls = ['http://www.neoshomo.org/departments/police_department/accident_report.php']

    def parse(self, response):
        pass
