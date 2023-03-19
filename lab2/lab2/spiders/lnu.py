import scrapy
from bs4 import BeautifulSoup
from lab2.items import Lab2FacultyItem,Lab2DepartmentItem,StaffItem


class LnuSpider(scrapy.Spider):
    name = "lnu"
    allowed_domains = ["lnu.edu.ua"]
    start_urls = ["http://lnu.edu.ua/about/faculties/"]

    def parse(self, response):
        soup = BeautifulSoup(response.body,  "html.parser")
        faculty = soup.find(class_= "structural-units")
        for li in faculty.find_all("li"):
            div = li.find("div")
            a = div.find("a")
            h2 = li.find("h2")
            fac_name =h2.find(text=True,recursive=False)
            fac_link = a.get('href')
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
        soup = BeautifulSoup(response.body,  "html.parser")
        dep_list = soup.find(class_="content divisions")
        if dep_list:
            for secton in dep_list.find_all("section"):
                h2 = secton.find('h2')
                dep_name = h2.a.find(string=True, recursive=False)
                dep_url =h2.a.get('href')
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
        soup =  BeautifulSoup(response.body,  "html.parser")
        professor_list = soup.find("table")
        if professor_list:
            for td in professor_list.find_all("td"):
                name = td.a.find(string=True, recursive=False)
                yield StaffItem(
                    name = name,
                    department = response.meta.get("department")
                )
            

