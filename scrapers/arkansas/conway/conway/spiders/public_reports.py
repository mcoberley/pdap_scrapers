import scrapy


class PublicReportsSpider(scrapy.Spider):
    name = 'public_reports'
    allowed_domains = ['www.conwaypd.org']
    start_urls = ['http://www.conwaypd.org/index.php/forms-reports/public-reports']

    def parse(self, response):
        pdf_links_full = []

        pdf_links = response.xpath("//div[@class=' span4']/h5/a/@href").getall()

        for link in pdf_links:
            pdf_links_full.append(response.urljoin(link))

        yield {"file_urls": pdf_links_full}
