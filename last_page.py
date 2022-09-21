import requests
from bs4 import BeautifulSoup


keyword = input("Enter a keyword for looking for jobs:\n")

URL = "https://www.kariyer.net/is-ilanlari?kw={}".format(keyword)
page = requests.get(URL)

soup = BeautifulSoup(page.text, "html.parser")

last_page = soup.find_all("li", class_ = "page-item tiny-padding")

pages = []
for element in last_page:
    pages.append(element.string)

print(pages[-1])

