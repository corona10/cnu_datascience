library(ggmap)
setwd('/home/parallels/cnu_datascience/week5')
# 아래 둘 중 되는 것으로 한다. 유닉스/ 윈도우의 차이. 
loc <- read.csv("bike.csv",header=T)
head(loc)
kor <- get_map("seoul", zoom=11, maptype = "roadmap") # 지도를 가져온다.
kor.map<-ggmap(kor)+geom_point(data=loc,aes(x=LNG,y=LAT),size=0.5,alpha=0.7)
kor.map
