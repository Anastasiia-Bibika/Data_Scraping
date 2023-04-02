import scrapy
from lab2.items import Lab2FacultyItem,Lab2DepartmentItem


class LnuXpathSpider(scrapy.Spider):
    name = "lnu_xpath"
    allowed_domains = ["lnu.edu.ua"]
    start_urls = ["http://lnu.edu.ua/about/faculties/"]

    def parse(self, response):
        faculty = response.xpath('//ul[contains(@class, "structural-units")]'
            ).xpath('.//*[contains(@class,"clearfix")]')
        for facult in faculty:
            fac_name =facult.xpath('.//h2[contains(@class,"title")]/text()').get()
            fac_link = facult.xpath('.//span[contains(@class, "value")]'
            ).xpath('.//*[contains(@class,"a")]/@href').get()
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
        dep_list =response.xpath('//article[contains(@class, ".divisions")]'
        ).xpath('.//*[contains(@class,"section")]')
        for secton in dep_list:
            dep_name = secton.xpath('.//h2[contains(@class,"title")]/text()').get()
            dep_url = secton.xpath('//h2[contains(@class, "title")]'
                            ).xpath('.//*[contains(@class,"a")]/@href').get()
            yield Lab2DepartmentItem(
                name = dep_name,
                url = dep_url,
                faculty=response.meta.get("faculty")
                )
