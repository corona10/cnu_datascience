# ggplot2 라이브러리와 MASS 임포트
library(ggplot2)
library(MASS)
# Cars93 데이터를 가져온다.
data("Cars93")
cars93 <- Cars93
# Cars93$Type을 플롯팅하게 지정한다.
g <- ggplot(cars93, aes(x = Type))
# Bar 그래프의 색깔을 지정한다.
b <- geom_bar(fill='white', color='steelblue')
# 그래프의 타이틀을 지정한다. 
t <- ggtitle("Bar Chart of Frequency by Car Type")
# 해당 설정을 모두 합쳐서 실행한다.
g + b + t

