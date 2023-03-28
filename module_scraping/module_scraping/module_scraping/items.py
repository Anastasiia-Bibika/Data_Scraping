# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ModuleScrapingHeadphoneItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    url = scrapy.Field()
    image_urls = scrapy.Field()
    file_urls = scrapy.Field()

class ModuleScrapingShopsItem(scrapy.Item):
    name = scrapy.Field()
    image_urls = scrapy.Field()
