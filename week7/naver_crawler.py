#-*- coding: utf-8 -*-
import urllib2
from urllib import urlencode
from bs4 import BeautifulSoup
import codecs

clientID = 'cu3NbgMxKj9IEYPdjncH'
clientSecret = 'V85AQbB043'

keyword = u'20대국회의원선거'
display = 100
start = 1

params = {'query': keyword.encode('utf8'), 'display': display, 'start': start}
params = urlencode(params)
print params
uri = "https://openapi.naver.com/v1/search/news.xml?" + params
req = urllib2.Request(uri)
req.add_header('X-Naver-Client-Id', clientID)
req.add_header('X-Naver-Client-Secret', clientSecret)

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

data_file.close()