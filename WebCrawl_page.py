import requests
from bs4 import BeautifulSoup

def spider(max_pages):
    page = 1
    while page < max_pages:
        url = 'http://creativeworks.tistory.com/' + str(page)
        source_code = requests.get(url)

        plain_text = source_code.text
        soup = BeautifulSoup(plain_text,"html.parser")
        for title_list in soup.find_all(['h3','class']):

            title = title_list.text
            print(title)

        page += 1

spider(100)
