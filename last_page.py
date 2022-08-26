import requests
from bs4 import BeautifulSoup

keyword="data"

URL = "https://www.kariyer.net/is-ilanlari?kw={}".format(keyword)
page = requests.get(URL)

soup = BeautifulSoup(page.text, "html.parser")

last_page = soup.find_all("li", class_ = "page-item tiny-padding")

print(last_page)