import scrapy
from laboratory4.items import MouseItem

class MousesSpider(scrapy.Spider):
    name = "mouses"
    allowed_domains = ["hotline.ua"]
    start_urls = ["https://hotline.ua/ua/computer/myshi-klaviatury/1362/?q=Миші"]

    def parse(self, response):
        items = response.css('div.list-body__content').css('.list-item')

        for item in items:
            name = item.css('a.list-item__title::text').get()
            url = item.css('a.list-item__title::attr(href)').get()
            price = item.css('.price__value::text').get()
            image_url = item.css('img::attr(src)').get()
            yield MouseItem(
                name=name,
                price=price,
                url=url,
                image_urls=[f"https://hotline.ua{image_url}"]
            )
