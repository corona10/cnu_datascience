#-*- coding: utf-8 -*-
# 필요한 라이브러리를 임포트
import urllib2
import json

serviceurl = 'http://python-data.dr-chuck.net/comments_42.json'
# urllib2로 http response 결과를 가져온다.
response = urllib2.urlopen(serviceurl)
# 가져온 response 결과를 json라이브러리가 읽을수 있게 해준다.
data = json.load(response)
sum = 0
# json 구조 comments 하부에 names와 count가 배열로 묶여있음
# 따라서 data['comments'] 아래의 count 요소를 전부다 더하면 된다.
for i in data['comments']:
    sum += i['count']

# 결과를 출력
print sum
