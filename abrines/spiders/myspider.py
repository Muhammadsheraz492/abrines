import scrapy


class MyspiderSpider(scrapy.Spider):
    name = "myspider"
    allowed_domains = ["X"]
    start_urls = ["https://X"]

    def parse(self, response):
        pass
