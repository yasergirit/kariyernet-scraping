import requests
from bs4 import BeautifulSoup
from pprint import pprint
import last_page


last_page.last_page()

"""
counter = 0
for i in range(lp):
    URL = "https://www.kariyer.net/is-ilanlari?kw={}&cp={}".format(keyword, i)
    page = requests.get(URL)
    
    soup = BeautifulSoup(page.text, "html.parser")

    notices = soup.find_all(class_ = "k-space medium left")

    for text in notices:
        company_element = text.find("div", class_="k-text small").get_text()
        job_element = text.find("h3").get_text()
        print(company_element.replace(" "*21, ""), job_element.replace(" "*23, ""))
        
    counter += 1
    print("Page:", counter)"""