
# coding: utf-8

# In[6]:

get_ipython().magic(u'matplotlib inline')
from pandas import Series, DataFrame
import pandas as pd
import operator
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import copy
import math
from datetime import datetime
matplotlib.rc('font',family='AppleGothic')
# 한글 폰트가 깨지는 것을 방지하기 위한 설정 및 라이브러리 선언


# In[7]:

# 선처리 된 엑셀 파일 읽어오기
tashu_2013_1 = pd.read_csv('tashu_rental_2013_1.csv')
tashu_2013_2 = pd.read_csv('tashu_rental_2013_2.csv')
tashu_2014_1 = pd.read_csv('tashu_rental_2014_1.csv')
tashu_2014_2 = pd.read_csv('tashu_rental_2014_2.csv')


# In[8]:

# 회원 비회원 구분
# NO는 비회원
# YES는 회원
# SELECT COUNT(*)
# FROM TASHU_LOG
# GROUP BY IS_MEMBER
member_count =  tashu_2013_1.groupby('IS_MEMBER').size()     + tashu_2013_2.groupby('IS_MEMBER').size()     + tashu_2014_1.groupby('IS_MEMBER').size()     + tashu_2014_2.groupby('IS_MEMBER').size()
    
plot = member_count.plot(kind = 'bar', alpha = 0.75, title = u'회원/비회원 이용 횟수', rot = 0)
plot.set_xlabel(u'회원 구분')
plot.set_ylabel(u'이용 횟수')


# In[9]:

# 지역구별 정류장 수
# SELECT COUNT(*)
# FROM STATION_INFO
# GROUP BY STATION_INFO.구별
station_info = pd.read_csv('201503_station_info.csv', encoding = 'cp949')
station_count = station_info.groupby(u'구별').size()
plot = station_count.plot(kind ='bar',alpha=0.75, title = u'구별 정류장 수',rot=0)
plot.set_ylabel(u'정류장 수')
plot.set_xlabel(u'지역구')


# In[25]:

# 인기있는 코스
# SELECT COUNT(*) 
#        FROM TASHU_LOG
#        GROUP BY 
#        TASHU_LOG.RENT_STATION AND RETURN_STATION
#        ORDER BY DESC
popular_course =  tashu_2013_1.groupby(['RENT_STATION', 'RETURN_STATION']).size()                     + tashu_2013_2.groupby(['RENT_STATION', 'RETURN_STATION']).size()                     + tashu_2014_2.groupby(['RENT_STATION', 'RETURN_STATION']).size()                     + tashu_2014_1.groupby(['RENT_STATION', 'RETURN_STATION']).size()
popular_course =  popular_course.sort_values(ascending= False)
for i in popular_course.index[:10]:
    print station_info[station_info[u'번호'] == i[0]][u'명칭'].iloc[0],'to',station_info[station_info[u'번호'] == i[1]][u'명칭'].iloc[0], popular_course[i]


# In[26]:

# 인기있는 정류장
# SELECT COUNT(*) 
#        FROM TASHU_LOG
#        GROUP BY 
#        TASHU_LOG.RENT_STATION
#        ORDER BY DESC
top10_station =  tashu_2013_1.groupby('RENT_STATION').size()                     + tashu_2013_2.groupby('RENT_STATION').size()                     + tashu_2014_2.groupby('RENT_STATION').size()                     + tashu_2014_1.groupby('RENT_STATION').size()
top10_station =  top10_station.sort_values(ascending= False)
for i in top10_station.index[:10]:
    print station_info[station_info[u'번호'] == i][u'명칭'].iloc[0], top10_station[i]

