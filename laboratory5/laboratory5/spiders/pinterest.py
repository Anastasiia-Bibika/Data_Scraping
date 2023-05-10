import scrapy
from laboratory5.SeleniumRequest import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions 
from laboratory5.items import Dynamiclab5Item


class PinterestSpider(scrapy.Spider):
    name = "pinterest"
    start_urls = ["http://www.pinterest.co.uk/"]

    def start_requests(self):   
        for url in self.start_urls:
             yield SeleniumRequest(
                url=url,
                callback=self.parse,
                wait_time=10,
                wait_until=expected_conditions.element_to_be_clickable(
                   (By.CSS_SELECTOR,
                    "div img")
                ),
                execute=self.login
            )
    def login(self, driver, wait):
        wait.until(expected_conditions.element_to_be_clickable((By.XPATH, '//input[@name="username"]')))
        email_input = driver.find_element(By.XPATH, '//input[@name="id"]')
        email_input.send_keys("EmailTest")
        username_password = driver.find_element(By.XPATH, '//input[@name="password"]')
        username_password.send_keys("NameTestPassword")   
        birthday_input = driver.find_element(By.XPATH, '//input[@type="date"]')
        birthday_input.send_keys("NameTestPassword")   
        login_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
        login_button.click()
    def parse(self, response):
        for img in response.css("div img"):
            url = img.css('::attr(src)').get()
            yield Dynamiclab5Item(
                url=url,
                image_urls=[url],
            )