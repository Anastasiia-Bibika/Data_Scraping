import scrapy
from module_scraping.items import ModuleScrapingHeadphoneItem,ModuleScrapingShopsItem

class HeadphonesCssSpider(scrapy.Spider):
    name = "headphones_css"
    allowed_domains = ["hotline.ua"]
    start_urls = [
          f"https://hotline.ua/ua/av/naushniki-garnitury/?p={page}" for page in range(1, 12)]

    def parse(self, response):
        items = response.css('div.list-body__content').css('.list-item')
        for item in items:
            name = item.css('a.list-item__title::text').get()
            url = item.css('a.list-item__title::attr(href)').get()
            price = item.css('.price__value::text').get()
            image_url = item.css('img::attr(src)').get()
            yield ModuleScrapingHeadphoneItem(
                name=name,
                price=price,
                url=url,
                image_urls=[f"https://hotline.ua{image_url}"]
            )
            yield scrapy.Request(
                url = "https://hotline.ua" + url,
                callback=self.parse_shops,
            )
    def parse_shops(self,response):
        shops = response.css('div.list').css('.list__item')
        for shop in shops:
            name = shop.css('div.shop__header').css('a.shop__title::text').get()
            url = shop.css('div.shop__header').css('a.shop__title::attr(href)').get()
            yield ModuleScrapingShopsItem(
                name=name,
                url=url,
            )
            


