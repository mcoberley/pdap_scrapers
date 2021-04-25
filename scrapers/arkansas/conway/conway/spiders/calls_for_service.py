import scrapy
import json
import base64
from scrapy_splash import SplashRequest


class CallsForServiceSpider(scrapy.Spider):
    next_button_script = """
        function main(splash, args)
        assert(splash:go(args.url))
        assert(splash:wait(0.5))
        next_btn = assert(splash:select("#at_303_next"))
        next_btn:mouse_click()
        assert(splash:wait(4))
        return {
            html = splash:html(),
            png = splash:png(),
            har = splash:har(),
        }
        end 
    """

    def parse(self, response):
        pass
