import requests
from bs4 import BeautifulSoup

def spider(code):
    # code = 116233

    url = 'http://movie.naver.com/movie/bi/mi/basic.nhn?code=' + str(code)
    source_code = requests.get(url)

    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,"html.parser")
    for reviews in soup.find_all(['p','class']):

        review= reviews.text
        print(review)

spider(116233) # passengers