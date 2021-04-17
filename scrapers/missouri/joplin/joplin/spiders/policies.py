import scrapy
import json


class PoliciesSpider(scrapy.Spider):
    name = 'policies'
    allowed_domains = ['www.joplinmo.org']
    start_urls = ['http://www.joplinmo.org/1095/Policies']

    def parse(self, response):
        # find <section> with class = widgetRelatedDocuments and get the data-sections attribute
        data_sections = json.loads(response.xpath("//section[contains(@class,'widgetRelatedDocuments')]/@data-sections").get())

        # Example of data_sections format
        # 
        # [
        #    {
        #        "Title": "Annual Reports",
        #        "DocumentIDs": "8860,8859,8858,8857,8856,9239,",
        #        "FolderIds": ",",
        #        "SortedDocumentIds": "9239,8860,8859,8858,8857,8856,"
        #     },
        #     {
        #         "Title": "Quarterly Reports",
        #         "DocumentIDs": "8861,8862,8970,",
        #         "FolderIds": ",",
        #         "SortedDocumentIds": "8861,8862,8970,"
        #     }
        # ]

        pdf_links_full = []
        for section in data_sections:

            # either remove the last element because they all seem to have a trailing ','
            documentIDs = section['DocumentIDs'].split(",")
            # or make sure that the doc ID isn't blank while you're looping through the array
            # we'll go with the latter in case they remove that trailing comma in the future.
            
            for id in documentIDs:
                if(id != ''):
                    relative_url = response.xpath(f"//li[@data-documentid={id}]/a/@href").get()
                    absolute_url = response.urljoin(relative_url)
                    pdf_links_full.append(absolute_url)
                    print(absolute_url)

        yield {
            'file_urls' : pdf_links_full
        }

