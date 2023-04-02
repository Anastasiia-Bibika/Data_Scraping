import scrapy
from lab2.items import Lab2FacultyItem,Lab2DepartmentItem,StaffItem


class LnuCssSpider(scrapy.Spider):
    name = "lnu_css"
    allowed_domains = ["lnu.edu.ua"]
    start_urls = ["http://lnu.edu.ua/about/faculties/"]

    def parse(self, response):
        faculty = response.css('ul.structural-units').css('.clearfix')
        for facult in faculty:
            fac_name =facult.css('h2.title::text').get()
            fac_link = facult.css('p:nth-child(4)').css("a::attr(href)").get()
            yield Lab2FacultyItem(
                name = fac_name,
                url = fac_link ,
            )
            yield scrapy.Request(
                url = fac_link + "about/departments/",
                callback=self.parse_faculties,
                meta={
                    "faculty":  fac_name
                }
            )
    def parse_faculties(self,response):
        dep_list = response.css("article.divisions").css("section")
        self.logger.info(dep_list)
        for section in dep_list:
            dep_name = section.css("div.text").css('h2.title').css('a::text').get()
            dep_url = section.css('h2.title').css('a::attr(href)').get()
            yield Lab2DepartmentItem(
                name = dep_name,
                url = dep_url,
                faculty=response.meta.get("faculty")
                )
            yield scrapy.Request(
                     url = dep_url+"/staff",
                     callback=self.parse_department,
                     meta={
                         "department": dep_name
                     }
                 )
    def parse_department(self,response):
        professor_list = response.css("table")
        if professor_list:
            for section in professor_list("section"):
                name = section.css('table').css('td.name').css('a::text').get()
                yield StaffItem(
                    name = name,
                    department = response.meta.get("department")
                )