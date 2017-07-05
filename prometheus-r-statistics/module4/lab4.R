# вычисли уравнения лин регрессии для датасетов anscombe,diamonds
# построим ленейную модель для поиска цен 
# приемлемо обработанного диаманта/идеально обработанного диаманта
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
fit <- lm(y4 ~ x4, data=anscombe)
summary(fit) 
# уравнение лин регрессии получится
# y=0.5x+3

diamonds
fit2 <- lm(price~carat, data=diamonds)
summary(fit2) # show results

ggplot(data=diamonds, aes(x=carat, y=price)) +
  geom_point(col="lightblue") +
  geom_smooth(method="lm", se=FALSE) +
  facet_wrap(~cut)

# построим модель lin.diamond.ideal для поиска цены
# для идеально обработанного диаманта весом 1 карат
price.ideal <- diamonds$price[diamonds$cut == "Ideal"]
carat.ideal <- diamonds$carat[diamonds$cut == "Ideal"]

lin.diamond.ideal <- lm(price.ideal ~ carat.ideal, data=diamonds)
summary(lin.diamond.ideal)
# y = a * x + b, 
# где a = -2300.37, x=1(карат), b=8192.39
# имеем y=5832,02

# построим модель lin.diamond.fair для поиска цены
# для приемлемо обработанного диаманта весом 1 карат
price.ideal <- diamonds$price[diamonds$cut == "Fair"]
carat.ideal <- diamonds$carat[diamonds$cut == "Fair"]

lin.diamond.fair <- lm(price.ideal ~ carat.ideal, data=diamonds)
summary(lin.diamond.fair)
# y = a * x + b, 
# где a = -1839.07, x=1(карат), b=5924.50
# имеем y=4085.43
