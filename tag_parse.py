# 본문 태그 탐색 후 article_text 에 저장
# example - 중앙일보

import requests, copy, urllib
from html.parser import HTMLParser
from bs4 import BeautifulSoup


def findvalue(STRING,aSub,aStart,bSub):

    '''STRING,aSub,aStart,bSub'''
    print("1")
    # aStart(위치) 부터 aSub 문자 Searching.

    # index A 접근이 안됨 .

    indexA = STRING.index(aSub,aStart)+len(aSub)
    print("1")
    # 위에서 aStart부터 찾았으니까 그 이후인 indexA부터 bSub 문자 Searching.
    indexB = STRING.index(bSub,indexA)
    print("1")
    # STRING 에서 aSub에 입력한 문자열과 bSub에 입력한 문자열의 중간 문자열 리턴
    returnvalue = (indexA,indexB+len(bSub),STRING[indexA:indexB].strip())
    print("1")
    # indexA = s, indexB = indexB+len(bSub) = e, v = quote

    return returnvalue


# match pub - tag using dic
# 여기서 얻어진 태그를 밑에 soup.find에 넣기


dic = {'중앙일보':'article_body','연합뉴스':'article'}

tag = dic.get('중앙일보') # value 값 가져오기

# 중앙일보
url = 'http://news.joins.com/article/21384797?cloc=joongang|section|clickraking'

r = requests.get(url)
content = r.content
r.close()

soup = BeautifulSoup(content,'html.parser')

# 본문들어가있는 태그
soup2 = soup.find('div',attrs={'class':tag})
#print("soup2:",soup2)

article_text = soup2.text
print("article_text:",article_text)
# 공백 최소화 처리
article_text = ' '.join(article_text.split())

# entiti 문자 처리
article_text = HTMLParser().unescape(article_text)
print(article_text)

# 본문

quotations = list()

# index = 0 부터 searching.
e = 0

# infinite repeating without break

# 결과값 DB에 넣을 수 있는 형태로 만든 담에 Give to M.S

while True:
    try:

        s,e,v = findvalue(article_text,'"',e,'"')

        # v = STRING[indexA:indexB].strip() "인용구"

#         print("indexA, indexB+len(bSub), quote: ")

        # print(s,e,v)

        # 인용문 리스트에 추가
        quotations.append(v)


        # Step1. tuple 형태로 인용문 줄 마다 저장.
        # Step2. 저장된 tuple을 SavedToDB에서 callable?

        index_tuple = s, e
        print(index_tuple)


    except ValueError:
        break

# 위에서 quotation list()를 line by line printing out.
for quotation in quotations:
    print("QUOTE:")
    print(quotation)

# tuple 값으로 저장
