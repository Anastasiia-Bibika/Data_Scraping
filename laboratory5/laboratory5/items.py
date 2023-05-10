# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Dynamiclab5Item(scrapy.Item):
    url = scrapy.Field()
    file_urls = scrapy.Field()
    image_urls = scrapy.Field()

