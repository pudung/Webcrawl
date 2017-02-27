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

url = 'http://www.yonhapnews.co.kr/bulletin/2017/02/27/0200000000AKR20170227050951001.HTML?from=search'
r = requests.get(url)
content = r.content
r.close()

soup = BeautifulSoup(content,'html.parser')
soup2 = soup.find('div',attrs={'class':'article'})

# 기사의 이미지부분과 이미지주석 부분, 제거
for article_img in soup2.findAll('div',attrs={'class':'article-img'}):
    article_img.\
        extract()

# 기사의 헤더(요약)부분, 제거
for article_stit in soup2.findAll('div',attrs={'class':'stit'}):
    article_stit.extract()

# 기사 내의 스크립트 태그, 제거
for article_script in soup2.findAll('script'):
    article_script.extract()

# 링크 텍스트 제거
for article_p in soup2.findAll('p',attrs={'class':'blind'}):
    article_p.extract()

# 광고부분 제거
for article_adbox in soup2.findAll('div',attrs={'class':'article-ad-box'}):
    article_adbox.extract()

# 텍스트만 추출
article_text = soup2.text

# 공백 최소화 처리
article_text2 = ' '.join(article_text.split())

# entiti 문자 처리
article_text3 = HTMLParser().unescape(article_text2)

# print("article_text3: ")

print(article_text3)

quotations = list()

# index = 0 부터 searching.
e = 0

# infinite repeating without break

# 결과값 DB에 넣을 수 있는 형태로 만든 담에 Give to M.S

while True:
    try:
        s,e,v = findvalue(article_text3,'"',e,'"')

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

