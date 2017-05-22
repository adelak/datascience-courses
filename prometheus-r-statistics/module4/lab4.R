library(ggplot2)

ggplot(data.frame(x = c(-263,263)), aes(x)) +
  geom_vline(xintercept = -2, linetype=2, colour="blue") +
  stat_function(fun = dnorm, colour="blue") +
  geom_area(stat = "function", fun = dnorm, fill = "red", xlim = c(-2,263)) 
pnorm(-2, lower.tail = FALSE)

anscombe
# компактно отобразим структуру объекта
str(anscombe)
# подсчитывает базовые статистические критерии(макс/мин, среднее, медиана...) структуры объекта
summary(anscombe)
dput(anscombe)
# вычислим коеф корреляции
cor.test(anscombe$x1, anscombe$y1)
cor.test(anscombe$x2, anscombe$y2)
cor.test(anscombe$x3, anscombe$y3)
cor.test(anscombe$x4, anscombe$y4)

# линейная модель 
lm(anscombe$x1, anscombe$y1)
summary(anscombe)

data("diamonds")
View(diamonds)

cor.test(diamonds$price, diamonds$carat)