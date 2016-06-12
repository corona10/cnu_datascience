#-*- coding: utf-8 -*-
from operator import add
from pyspark import SparkConf, SparkContext

conf = SparkConf().setAppName("tashu-top10Course")
sc = SparkContext(conf = conf)

def loadStationInfo():
    stationLocations = {}
    with open("station.txt") as f:
        for line in f:
            fields = line.split(',')
            stationLocations[int(fields[0])] = fields[3]
    return stationLocations

def parseLine(line):
    fields = line.split(",")
    start_no = fields[1]
    dest_no = fields[3]
    return (start_no, dest_no)

def castToInteger(x):
    try:
        return ((int(x.split(',')[1]), int(x.split(',')[3])), 1)
    except ValueError:
        return ((-1, -1), 1)

station_names = sc.broadcast(loadStationInfo())
def changeToArea(((start, dst), count)):
    try:
        return ((station_names.value[start], station_names.value[dst]), count)
    except KeyError:
        return ('기타', count)

lines = sc.textFile("tashu_rental_log.txt")
stations = lines.map(castToInteger)
stations = stations.partitionBy(4)
stationCount = stations.reduceByKey(lambda x,y: x+y)
stationCount = stationCount.map(changeToArea)

result = stationCount.collect()
result = stationCount.takeOrdered(10, key = lambda x: -x[1])
for r in result:
    station = r[0]
    print station[0],'~',station[1],':',r[1]
