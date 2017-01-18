# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

import urllib
from urllib import request

# title, link, description 을 뱉는 모듈 만들기
# <pubDate>Sat, 14 Jan 2017 08:35:00 +0900</pubDate>
def get_date():
    pass

    # rescode = getcode 까지 중복되는 부분 모든 함수에서 쓰지 않고 1번만 타이핑할 수 있게 모듈화방법?
    # 함수 생성전에 위에
    # pubDate string 으로 안받아짐

def get_title():
    client_id = "YOUR_CLIENT_ID"
    client_secret = "YOUR_CLIENT_SECRET"

    # request parameter
    display = '10'
    start = '1000'

    encText = urllib.parse.quote("안철수")

    # url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과
    url = "https://openapi.naver.com/v1/search/news.xml?query=" + encText + "&display=" + display + "&start=" + start  # xml 결과

    print("url= " + url)
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", "oKYDp0sAGUP2ZaDMDX8z")
    request.add_header("X-Naver-Client-Secret", "KHe_G13uer")

    response = urllib.request.urlopen(request)
    rescode = response.getcode()

    if (rescode == 200):
        response_body = response.read()
        print(response_body.decode('utf-8'))
        soup = BeautifulSoup(response_body.decode('utf-8'), "html.parser")

        titles = soup.findAll('title')

        title_list = []

        for title in titles:
            title = title.get_text()
            title = title.replace('&', '')
            title = title.replace('apos', '')
            title = title.replace('quot;', '')
            title = title.replace('<b>','')
            title = title.replace('</b>','')

            print(title)
            title_list.append(title)

            print(title_list)

def get_link():
    client_id = "YOUR_CLIENT_ID"
    client_secret = "YOUR_CLIENT_SECRET"

    # request parameter
    display = '10'
    start = '1000'

    encText = urllib.parse.quote("안철수 대선")

    # url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과
    url = "https://openapi.naver.com/v1/search/news.xml?query=" + encText + "&display=" + display + "&start=" + start  # xml 결과

    print("url= " + url)
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", "oKYDp0sAGUP2ZaDMDX8z")
    request.add_header("X-Naver-Client-Secret", "KHe_G13uer")

    response = urllib.request.urlopen(request)
    rescode = response.getcode()

    if (rescode == 200):
        response_body = response.read()
        print(response_body.decode('utf-8'))
        soup = BeautifulSoup(response_body.decode('utf-8'), "html.parser")

        links = soup.findAll('link')

        link_list = []

        for link in links:
            link = link.get_text()
            print("link_list")
            link_list.append(link)
            print(link_list)

def get_description():
    client_id = "YOUR_CLIENT_ID"
    client_secret = "YOUR_CLIENT_SECRET"

    # request parameter
    display = '10'
    start = '1000'

    encText = urllib.parse.quote("안철수 대선")

    # url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과
    url = "https://openapi.naver.com/v1/search/news.xml?query=" + encText + "&display=" + display + "&start=" + start  # xml 결과

    print("url= " + url)
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", "oKYDp0sAGUP2ZaDMDX8z")
    request.add_header("X-Naver-Client-Secret", "KHe_G13uer")

    response = urllib.request.urlopen(request)
    rescode = response.getcode()

    if (rescode == 200):
        response_body = response.read()
        print(response_body.decode('utf-8'))
        soup = BeautifulSoup(response_body.decode('utf-8'), "html.parser")

    descriptions = soup.findAll('description')

    description_list = []

    for description in descriptions:
        description = description.get_text()
        description = description.replace('&', '')
        description = description.replace('apos', '')
        description = description.replace('quot;', '')
        description = description.replace('<b>', '')
        description = description.replace('</b>', '')

    # print("description list ")
        description_list.append(description)   # add to List
        print(description_list)
#
def main():
    get_title()
    get_link()
    get_description()

if __name__ == '__main__':
    main()

