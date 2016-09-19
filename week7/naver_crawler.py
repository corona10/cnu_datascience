#-*- coding: utf-8 -*-
import urllib2
from urllib import urlencode
from bs4 import BeautifulSoup
import codecs

## 네이버 API를 호출하기 위한 기본 세팅
clientID = 'id'
clientSecret = 'secret'

keyword = u'미세먼지'
display = 100
start = 1

params = {'query': keyword.encode('utf8'), 'display': display, 'start': start}
params = urlencode(params)

# 네이버 API를 호출하기 위해 헤더값에
# 'X-Naver-Client-Id'과 'X-Naver-Client-Secret'를 부여한다
uri = "https://openapi.naver.com/v1/search/news.xml?" + params
req = urllib2.Request(uri)
req.add_header('X-Naver-Client-Id', clientID)
req.add_header('X-Naver-Client-Secret', clientSecret)

# 결과값이 오면 Response값을 파싱한다
# 이 때 불필요한 HTML 문법은 제거한다
response = urllib2.urlopen(req)
data = BeautifulSoup(response, "html.parser")
data_file = codecs.open('data.txt', 'w', 'utf-8')
for item in data.findAll('item'):
    desc = item.description.contents[0]
    desc = desc.replace('<b>', '')
    desc = desc.replace('</b>', '')
    desc = desc.replace('!', '')
    desc = desc.replace('.', '')
    desc = desc.replace('&quot', '')
    data_file.write(desc+'\n')


uri = "https://openapi.naver.com/v1/search/blog.xml?" + params
req = urllib2.Request(uri)
req.add_header('X-Naver-Client-Id', clientID)
req.add_header('X-Naver-Client-Secret', clientSecret)

# 결과값이 오면 Response값을 파싱한다
# 이 때 불필요한 HTML 문법은 제거한다
response = urllib2.urlopen(req)
data = BeautifulSoup(response, "html.parser")
for item in data.findAll('item'):
    desc = item.description.contents[0]
    desc = desc.replace('<b>', '')
    desc = desc.replace('</b>', '')
    desc = desc.replace('!', '')
    desc = desc.replace('.', '')
    desc = desc.replace('&quot', '')
    data_file.write(desc+'\n')

data_file.close()
