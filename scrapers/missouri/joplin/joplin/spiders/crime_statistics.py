import scrapy


class CrimeStatisticsSpider(scrapy.Spider):
    name = 'crime_statistics'
    allowed_domains = ['www.joplinmo.org']
    start_urls = ['http://www.joplinmo.org/488/Crime-Statistics']

    def parse(self, response):

        # get crime statistics
        current_div_id = 'divEditoree68b3fd-8a1d-489b-9ea0-2e205c0799a0' # id of parent div as of 2021-04-16
        stats_links = response.xpath(f"//div[@id='{current_div_id}']/a/@href").getall()

        pdf_links_full = []
        
        for link in stats_links:
            pdf_links_full.append(response.urljoin(link))

        # get related items
        related_items_links = response.xpath("//h2[@class='subhead1'][text()='Related Resources']/following-sibling::ul/li/a/@href").getall()

        for link in related_items_links:
            pdf_links_full.append(response.urljoin(link))
        
        yield {
            'file_urls' : pdf_links_full
        }
