# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ShopItem(scrapy.Item):
    name_product = scrapy.Field()
    img_url = scrapy.Field()
    shop = scrapy.Field()
    price = scrapy.Field()
