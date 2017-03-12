# 본문 태그 탐색 후 article_text 에 저장
# example - 중앙일보

import requests, copy, urllib
from html.parser import HTMLParser
from bs4 import BeautifulSoup


# match pub - tag using dic
# 여기서 얻어진 태그를 밑에 soup.find에 넣기


dic = {'중앙일보':'article_body','연합뉴스':'article'}

tag = dic.get('중앙일보')

# 중앙일보
url = 'http://news.joins.com/article/21359704'

r = requests.get(url)
content = r.content
r.close()

soup = BeautifulSoup(content,'html.parser')

# 본문들어가있는 태그
soup2 = soup.find('div',attrs={'class':tag})


article_text = soup2.text

# 공백 최소화 처리
article_text = ' '.join(article_text.split())

# entiti 문자 처리
article_text = HTMLParser().unescape(article_text)
print(article_text)
# 본문
