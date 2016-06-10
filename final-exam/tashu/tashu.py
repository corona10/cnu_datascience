from operator import add
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("tashu-stations")
sc = SparkContext(conf = conf)

def loadStationInfo():
    stationLocations = {}
    with open("file:/Users/corona10/spark-study/station.txt"):
        for line in f:
            fields = line.split(',')
            stationLocations[int(fields[0])] = fields[2]
    return stationLocations

def parseLine(line):
    fields = line.split(",")
    station_no = int(fields[1])
    print station_no
    return station_no


lines = sc.textFile("file:/Users/corona10/spark-study/tashu_rental_log.txt")
rdd = lines.map(parseLine)
stationCount = rdd.mapValues(lambda  x: (x, 1)).reduceByKey(lambda x, y: (x[1] + y[1]))
result = stationCount.collect()
#print result
