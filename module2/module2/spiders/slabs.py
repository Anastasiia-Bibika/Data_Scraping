import scrapy


class SlabsSpider(scrapy.Spider):
    name = "slabs"
    allowed_domains = ["ek.ua"]
    start_urls = [f"https://ek.ua/ua/list/84/?p={page}" for page in range(1, 5)]

    def parse(self, response):
        pass
