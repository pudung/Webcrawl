
import requests
from bs4 import BeautifulSoup

def spider():

    url = 'http://www.yonhapnews.co.kr/bulletin/2017/01/25/0200000000AKR20170125098552001.HTML?from=search'

    source_code = requests.get(url)

    # --------------------encoding commit 2017-01-25 ------------------#

    # plain_text = source_code.text
    plain_text = source_code.content
    soup = BeautifulSoup(plain_text, 'html.parser',from_encoding='utf-8')

    # -----------------------parsing---------------------------------#

    # title
    title = soup.find_all('h1', {'class':'tit-article'})
    print(title)

    article_chunk = soup.find_all('div', {'class':'article'})

    if len(article_chunk) > 0:
        article = article_chunk[0].find_all('p')

        for one_article in article:
            one_article = one_article.get_text()
            one_article = one_article.replace('</p>','')
            # 한줄씩 뽑기.
            print(one_article)





spider()


