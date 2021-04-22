import scrapy


class YearEndReportSpider(scrapy.Spider):
    name = "year_end_report"
    allowed_domains = ["carthagemo.gov"]
    start_urls = ["https://carthagemo.gov/index.asp?SEC=CF093C24-1E49-489F-A3B7-ED735D233DBB"]

    def parse(self, response):
        reports_links = response.xpath("//div[@class='attachments']/div/a/@href").getall()

        pdf_links_full = []

        for link in reports_links:
            pdf_links_full.append(response.urljoin(link))

        yield {"file_urls": pdf_links_full}