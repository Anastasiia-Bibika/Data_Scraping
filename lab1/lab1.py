from requests import get
from bs4 import BeautifulSoup


BASE_URL = "https://lnu.edu.ua"
URL = f"{BASE_URL}/about/faculties/"
HEADERS = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}
FILE_NAME = "laboratory.txt"
with open(FILE_NAME, "w", encoding="utf-8") as file:
    page = get(URL, headers=HEADERS)
    soup = BeautifulSoup(page.content,  "html.parser")
    faculty = soup.find(class_= "structural-units")
    for li in faculty.find_all("li"):
        div = li.find("div")
        a = div.find("a")
        h2 = li.find("h2")
        fac_name =h2.find(text=True,recursive=False)
        fac_link = BASE_URL+ a.get("href")
        print(f"Факультет: {fac_name}")
        print(f"URL: {fac_link}")
        file.write(f"Факультет: {fac_name}")
        file.write(f"URL: {fac_link}")
    dep_url = "https://lnu.edu.ua/structure/departments/"
    dep_page = get(dep_url, headers=HEADERS)
    soup = BeautifulSoup(dep_page.content,  "html.parser")
    dep_list = soup.find(class_="units-list")
    if dep_list:
            for li in dep_list.find_all("li"):
                dep_name = li.h2.find(string=True, recursive=False)
                dep_url =li.a.get("href")

                print(f"    Назва кафедри: {dep_name}")
                print(f"    URL: {dep_url}")
                file.write(f"Назва кафедри: {dep_name}")
                file.write(f"    URL: {dep_url}")
