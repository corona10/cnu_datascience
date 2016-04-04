library(ggmap)

setwd('/home/parallels/cnu_datascience/week5')

# 아래 둘 중 되는 것으로 한다. 유닉스/ 윈도우의 차이. 

loc <- read.csv("지역별장애인도서관정보.csv",header=T)

head(loc)

kor <- get_map("seoul", zoom=11, maptype = "roadmap") # 지도를 가져온다.

kor.map<-ggmap(kor)+geom_point(data=loc,aes(x=LON,y=LAT),size=5,alpha=0.7)

kor.map + geom_text(data=loc, aes(x = LON, y = LAT+0.01, label=자치구명),size=3) # 지도에 레이블을 출력하고 실제로 화면에 그린다.
