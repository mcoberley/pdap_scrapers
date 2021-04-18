import scrapy

class AccidentReportsSpider(scrapy.Spider):
    name = 'accident_reports'
    allowed_domains = ['www.joplinmo.org']
    start_urls = ['http://www.joplinmo.org/Archive.aspx?AMID=55']

    def parse(self, response):
        pdf_links_full = []
        pdf_links = response.xpath('//table[@summary=\'Archive Details\']/tr/td[2]/span/a/@href').getall()

        for link in pdf_links:
            pdf_links_full.append(response.urljoin(link))

        yield {
            'file_urls' : pdf_links_full
        }