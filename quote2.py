# -*- encoding:utf8-*-
# Python version in the development environment 2.7.11
# created by Kelly 2017-1-31
# 유승민 후보자 Quote

import os,sys,time
os.chdir(os.path.dirname(__file__))
import requests, copy, urllib
from html.parser import HTMLParser
from bs4 import BeautifulSoup

def findvalue(STRING,aSub,aStart,bSub):
    '''STRING,aSub,aStart,bSub'''

    # aStart(위치) 부터 aSub 문자 Searching.
    indexA = STRING.index(aSub,aStart)+len(aSub)

    # 위에서 aStart부터 찾았으니까 그 이후인 indexA부터 bSub 문자 Searching.
    indexB = STRING.index(bSub,indexA)

    # STRING 에서 aSub에 입력한 문자열과 bSub에 입력한 문자열의 중간 문자열 리턴
    returnvalue = (indexA,indexB+len(bSub),STRING[indexA:indexB].strip())

    # indexA = s, indexB = indexB+len(bSub) = e, v = quote

    return returnvalue

url = 'http://news.joins.com/article/21359704'
r = requests.get(url)
content = r.content
r.close()


soup = BeautifulSoup(content,'html.parser')
soup2 = soup.find('div',attrs={'class':'article_body'})


# 텍스트만 추출
article_text = soup2.text

# 공백 최소화 처리
article_text2 = ' '.join(article_text.split())

# entiti 문자 처리
article_text3 = HTMLParser().unescape(article_text2)

print(111)

print(article_text3)

quotations = list()

# index = 0 부터 searching.
e = 0

# infinite repeating without break

# 결과값 DB에 넣을 수 있는 형태로 만든 담에 Give to M.S

while True:
    try:
        print(1)
        s,e,v = findvalue(article_text3,'"',e,'"')
        print(2)
        quotations.append(v)
        print(3)
        index_tuple = s, e
        print(index_tuple)

        print(4)


    except ValueError:
        break
        print(5)

# 위에서 quotation list()를 line by line printing out.
for quotation in quotations:
    print("QUOTE:")
    print(quotation)

# tuple 값으로 저장

