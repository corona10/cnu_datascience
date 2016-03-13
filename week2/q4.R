library(ggplot2)
library(MASS)
data("Cars93")
cars93 <- Cars93
g <- ggplot(cars93, aes(x = Type))
b <- geom_bar(fill='white', color='steelblue') 
t <- ggtitle("Bar Chart of Frequency by Car Type")
g + b + t

