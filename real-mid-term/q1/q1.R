library(sqldf)
library(ggplot2)
font_import("AppleMyungjo")
station = read.csv("station.csv", sep= ',')
tashu_log = read.csv("tashu_rental_log.csv", sep=',')
popular_station_top10  <- sqldf("select no, name , count(*) as count
                               from tashu_log
                               left outer join station on tashu_log.RENT_STATION = station.no
                               group by RENT_STATION
                               order by count desc
                               limit 0, 10")
v = c(1,2,3,4,5,6,7,8,9,10)
symbols(v, popular_station_top10$count, circles=popular_station_top10$count, xlab="ranking", ylab ='usage count')
text(v, popular_station_top10$count, popular_station_top10$name, cex=0.5)