import scrapy


class IncidentReportsSpider(scrapy.Spider):
    name = 'incident_reports'
    allowed_domains = ['www.joplinmo.org']
    start_urls = ['http://www.joplinmo.org/Archive.aspx?AMID=45']

    def parse(self, response):
        pdf_links_full = []
        pdf_links = response.xpath('//table[@summary=\'Archive Details\']/tr/td[2]/span/a/@href').getall()

        for link in pdf_links:
            pdf_links_full.append(response.urljoin(link))

        yield {
            'file_urls' : pdf_links_full
        }