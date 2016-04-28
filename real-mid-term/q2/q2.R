library(ggmap)
setwd('/home/parallels/cnu_datascience/real-mid-term/q2')
loc <- read.csv("station.csv",header=T)
head(loc)
kor <- get_map("daejeon", zoom=13, maptype = "roadmap") # 지도를 가져온다.
kor.map<-ggmap(kor)+geom_point(data=loc,aes(x=lat,y=long),size=2,alpha=0.7)
kor.map + geom_text(data=loc, aes(x = lat, y = long+0.01, label=name),size=2.5)
