import scrapy

class MediaReportsSpider(scrapy.Spider):
    name = 'media_reports'
    allowed_domains = ['www.joplinmo.org']

    # AMIDs as of 2021-04-18
    # 45 = Incident reports
    # 46 = Arrest reports
    # 47 = Dispatch reports
    # 48 = In-custody reports
    # 49 = Warrants issued
    # 55 = Accident reports
    start_urls = ['http://www.joplinmo.org/Archive.aspx?AMID=45', 'http://www.joplinmo.org/Archive.aspx?AMID=46', 'http://www.joplinmo.org/Archive.aspx?AMID=47', 'http://www.joplinmo.org/Archive.aspx?AMID=48', 'http://www.joplinmo.org/Archive.aspx?AMID=49' 'http://www.joplinmo.org/Archive.aspx?AMID=55']

    def parse(self, response):
        pdf_links_full = []
        pdf_links = response.xpath('//table[@summary=\'Archive Details\']/tr/td[2]/span/a/@href').getall()

        for link in pdf_links:
            pdf_links_full.append(response.urljoin(link))

        yield {
            'file_urls' : pdf_links_full
        }