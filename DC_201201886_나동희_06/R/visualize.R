library(ggplot2)
setwd('/Users/corona10/cnu_datascience/week6/R')
rf <- colorRampPalette(rev(brewer.pal(11,'Spectral')))
r <- rf(32)
# 파이썬에서 작업한 csv파일을 import한다.
data_set <- read.csv('data.csv', sep = ',')
p <- ggplot(data_set, aes(steps, heart_beat))
t <- theme(text=element_text(family = "AppleMyungjo"))
title <- ggtitle("발걸음과 심장박동수의 bin그래프")
h3 <- p + t + stat_bin2d() + title
h3
