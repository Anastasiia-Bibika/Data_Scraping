import scrapy
from bs4 import BeautifulSoup
from laboratory3.items import TvItem

class FoxtrotSpider(scrapy.Spider):
    name = "foxtrot"
    allowed_domains = ["www.foxtrot.com.ua"]
    start_urls = ["https://www.foxtrot.com.ua/uk/shop/led_televizory.html"]

    def parse(self, response):
        soup = BeautifulSoup(response.body,  "html.parser")

        items = soup.find(
            name="div", class_="listing__body-wrap").find_all(class_="card")
        for item in items:
            name = item.find(name="a", class_="card__title").find(
                string=True, recursive=False).strip()
            url = item.find(name="a", class_="card__title").get("href")
            price = item.find(class_="card-price").find(
                string=True, recursive=False)
            image_url = item.find(name="img").get("src")
            yield TvItem(
                name=name,
                price=price,
                url=url,
                image_urls=[image_url]
            )