#-*- coding: utf-8 -*-
from operator import add
from pyspark import SparkConf, SparkContext
import sys
conf = SparkConf().setAppName("fitbit-heart")
sc = SparkContext(conf = conf)

def str2float(x):
    try:
        return float(x)
    except ValueError:
        return 0.0
def normalizeValue(value, max_val, min_val):
    normalize = (float(value - min_val))/(max_val -min_val)* 10
    return normalize

def mapData(x):
    data = x.split(',')
    steps = str2float(data[2])
    heart_beat = str2float(data[3])
    return (data[5], (steps, heart_beat, 1))

def mapToAvgStep((x, (h, s, c))):
    return (x, float(s)/c)

def mapToAvgHeart((x, (h,s,c))):
    return (x, float(h)/c)

def getHeartbeat(x):
    data = x[1]
    return data[0]

def getStep(x):
    data = x[1]
    return data[1]

lines = sc.textFile("fitbit/fitbit.csv")
header = lines.first()
data = lines.filter(lambda x:x != header)
data = data.map(mapData)
data = data.partitionBy(99)
totalCount = data.reduceByKey(lambda x,y: (x[0]+y[0], x[1] + y[1], x[2] + y[2]))
totalCount = totalCount.map(mapToAvgHeart)
result = totalCount.collect()

max_val = 0
min_val = sys.maxint
for r in result:
    max_val = max(max_val, r[1])
    min_val = min(min_val, r[1])

min_max = {}
min_max['max'] = max_val
min_max['min'] = min_val
minmax = sc.broadcast(min_max)
totalCount = totalCount.map(lambda x: (x[0], (float(x[1] - minmax.value['min'])/(minmax.value['max'] - minmax.value['min'])*10)))
result = totalCount.collect()
for r in result:
    print r[0],";",r[1]
