#-*- coding: utf-8 -*-
from operator import add
from pyspark import SparkConf, SparkContext

conf = SparkConf().setAppName("tashu-stations")
sc = SparkContext(conf = conf)

def loadStationInfo():
    stationLocations = {}
    with open("station.txt") as f:
        for line in f:
            fields = line.split(',')
            stationLocations[int(fields[0])] = fields[2]
    return stationLocations

def parseLine(line):
    fields = line.split(",")
    station_no = fields[1]
    return station_no

def castToInteger(x):
    try:
        return (int(x.split(',')[1]), 1)
    except ValueError:
        return (-1, 1)

station_names = sc.broadcast(loadStationInfo())
def changeToArea((id, count)):
    try:
        return (station_names.value[id], count)
    except KeyError:
        return ('기타', count)
#station_names = sc.broadcast(loadStationInfo())
lines = sc.textFile("tashu_rental_log.txt")
stations = lines.map(castToInteger)
stationCount = stations.reduceByKey(lambda x,y: x+y)
stationCount = stationCount.map(changeToArea)
stationCount = stationCount.reduceByKey(lambda x,y: x+y)
#stationCount = stationCount.sortByKey()
result = stationCount.collect()
for r in result:
    print r[0],':',r[1]
#for r in result:
#    print r
#for station_no, count in stationCount.items():
#    print station_no, count
