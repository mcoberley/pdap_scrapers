import scrapy


class PreventionAndEducationSpider(scrapy.Spider):
    name = 'prevention_and_education'
    allowed_domains = ['www.joplinmo.org']
    start_urls = ['http://www.joplinmo.org/492/Prevention-Education']

    def parse(self, response):

        # get relative links from page
        # the list we want is in position 2 as of 2021-04-17
        relative_urls = response.xpath("//ol[@role='menu']/li/h4/a/@href").getall()

        pdf_links_full = []
        
        for url in relative_urls:
            pdf_links_full.append(response.urljoin(url))

        yield {
            'file_urls' : pdf_links_full
        }
