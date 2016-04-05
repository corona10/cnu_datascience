library(ggmap)
setwd('/home/parallels/cnu_datascience/week5')
# 아래 둘 중 되는 것으로 한다. 유닉스/ 윈도우의 차이. 
loc <- read.csv("toy_lib.csv",header=T)
head(loc)
kor <- get_map("seoul", zoom=11, maptype = "roadmap") # 지도를 가져온다.
# 데이터파일에서 위도 경도 정보인 LONGITUDE  와 LATTITUDE를 가져와 지도에 표현
kor.map<-ggmap(kor)+geom_point(data=loc,aes(x=LONGITUDE,y=LATITUDE),size=3,alpha=0.7)
kor.map + geom_text(data=loc, aes(x = LONGITUDE, y = LATITUDE+0.01, label=LIB_NM),size=2.5)
