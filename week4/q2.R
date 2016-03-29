library(dplyr)
library(sqldf)
library(ggplot2)
station = read.csv("station.csv", sep= ',')
tashu_log = read.csv("tashu_rental_log.csv", sep=',', encoding ='cp949')
popular_course_top10  <- sqldf("select RENT_STATION||'~'||RETURN_STATION as course, count(*) as count
                          from tashu_log
                          group by RENT_STATION, RETURN_STATION
                          order by count desc
                          limit 0, 10")
print(popular_course_top10)
g <- ggplot(popular_course_top10, aes(x=course, y=count)) 
b <-geom_bar(stat="identity", fill="black", colour="black")
t <- theme(text=element_text(family = "AppleMyungjo"))
g + b + t
