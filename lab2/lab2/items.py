# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Lab2FacultyItem(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()

class Lab2DepartmentItem(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
    faculty = scrapy.Field()

class StaffItem(scrapy.Item):
    name = scrapy.Field()
    department = scrapy.Field()
