library(sqldf)
library(ggplot2)
font_import("AppleMyungjo")
station = read.csv("station.csv", sep= ',')
tashu_log = read.csv("tashu_rental_log.csv", sep=',', encoding ='cp949')
popular_area <- sqldf("select 구별, count(*) as count
                                from tashu_log
                                left outer join station on tashu_log.RENT_STATION = station.번호
                                group by 구별
                                order by count desc")
g <- ggplot(popular_area, aes(x=구별, y=count)) 
b <-geom_bar(stat="identity", fill="black", colour="black")
t <- theme(text=element_text(family = "AppleMyungjo"))
print (popular_area)
g + b + t