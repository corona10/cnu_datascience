import urllib2
import json

serviceurl = 'http://python-data.dr-chuck.net/comments_42.json'
response = urllib2.urlopen(serviceurl)
data = json.load(response)
sum = 0
for i in data['comments']:
    sum += i['count']

print sum
