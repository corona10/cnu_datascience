library(sqldf)
library(ggplot2)
font_import("AppleMyungjo")
station = read.csv("station.csv", sep= ',')
tashu_log = read.csv("tashu_rental_log.csv", sep=',', encoding ='cp949')
popular_station_top10  <- sqldf("select 명칭, count(*) as count
                               from tashu_log
                               left outer join station on tashu_log.RENT_STATION = station.번호
                               group by RENT_STATION
                               order by count desc
                               limit 0, 10")
g <- ggplot(popular_station_top10, aes(x=명칭, y=count)) 
b <-geom_bar(stat="identity", fill="black", colour="black")
t <- theme(text=element_text(family = "AppleMyungjo"))
print (popular_station_top10)
g + b + t