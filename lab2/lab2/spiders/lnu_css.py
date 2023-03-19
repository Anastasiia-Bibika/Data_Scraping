import scrapy
from lab2.items import Lab2FacultyItem,Lab2DepartmentItem


class LnuCssSpider(scrapy.Spider):
    name = "lnu_css"
    allowed_domains = ["lnu.edu.ua"]
    start_urls = ["http://lnu.edu.ua/"]

    def parse(self, response):
        faculty = response.css('ul.structural-units').css('.clearfix')
        for facult in faculty:
            fac_name =facult.css('h2.title::text').get()
            fac_link = facult.css('span.value::attr(href)').get()
            yield Lab2FacultyItem(
                name = fac_name,
                url = fac_link
            )
            yield scrapy.Request(
                url = fac_link + "about/departments",
                callback=self.parse_faculties,
                meta={
                    "faculty":  fac_name
                }
            )
    def parse_faculties(self,response):
        dep_list = response.css("article.content divisions").css("section")
        for secton in dep_list:
            dep_name = secton.css('h2.title::text').get()
            dep_url = secton.css('h2.title').css('a::attr(href)').get()
            yield Lab2DepartmentItem(
                name = dep_name,
                url = dep_url,
                faculty=response.meta.get("faculty")
                )