import scrapy


class NewsAndPressSpider(scrapy.Spider):
    name = 'news_and_press'
    allowed_domains = ['www.joplinmo.org']
    start_urls = ['http://www.joplinmo.org/603/News-Press']

    def parse(self, response):

        # id of parent div as of 2021-04-16
        current_div_id = 'divEditora00e64e0-aa4f-4464-baf6-05a44c4f5acb' 

        news_links = response.xpath(f"//div[@id='{current_div_id}']/a/@href").getall()

        pdf_links_full = []
        
        for link in news_links:
            pdf_links_full.append(response.urljoin(link))

        yield {
            'file_urls' : pdf_links_full
        }
