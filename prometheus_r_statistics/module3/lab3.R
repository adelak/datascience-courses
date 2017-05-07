install.packages("dplyr");
install.packages("ggplot2");
install.packages("proto")
install.packages('ggplot2', dep = TRUE)
library(ggplot2)
movie_body_counts <- read.csv('filmdeathcounts.csv')

head(movie_body_counts)
movie_body_counts.columns

install.packages("colorspace")

ggplot(movie_body_counts, aes(x=IMDB_Rating)) +
  geom_histogram(bins=10, color="grey", fill="lightblue") 


movie_body_counts[c('Film','IMDB_Rating')]
class(movie_body_counts$IMDB_Rating)
shapiro.test(movie_body_counts$IMDB_Rating) # х должен быть вектором

# среднее значение
imdb_mean <- mean(movie_body_counts$IMDB_Rating)
# sum(movie_body_counts$IMDB_Rating)/length(movie_body_counts$IMDB_Rating)

# среднеквадратическое отклонение
imdb_sd <- sqrt(var(movie_body_counts$IMDB_Rating))

#  сгенерируем норм распределение с параметрами imdb_mean/imdb_sd

# чтоб генерируемая последовательность была константная
set.seed(900)
imdb_simulation <- rnorm(n=nrow(movie_body_counts), mean = imdb_mean, sd = imdb_sd)

#добавим в наш набор значений сгенерированные данные
movie_body_counts$imdb_simulation <- imdb_simulation

# посчитаем вероятность получить фильм с оценкой <=4 для сгенерированной последовательности
length(which(movie_body_counts$imdb_simulation<=4.0))/length(movie_body_counts$imdb_simulation)


# посчитаем вероятность получить фильм с оценкой >4 <8 для сгенерированной последовательности
length(which(movie_body_counts$imdb_simulation>4 & movie_body_counts$imdb_simulation<8))/length(movie_body_counts$imdb_simulation)

ggplot(movie_body_counts, aes(x=IMDB_Rating)) +
  geom_histogram(bins=10, color="green", fill="lightgreen") 
ggplot(movie_body_counts, aes(x=imdb_simulation)) +
  geom_histogram(bins=10, color="grey", fill="lightblue") 

# коэффициентр корреляции(Пирсона) выявляет наличие лин зависимости между 2мя переменными
# чтоб использовать необходимо выполнение:
# - исследуемые переменные X и Y должны быть распределены нормально.
# - исследуемые переменные X и Y должны быть измерены в интервальной шкале или шкале отношений.
# - количество значений в исследуемых переменных X и Y должно быть одинаковым.
cor.test(movie_body_counts$Body_Count, movie_body_counts$IMDB_Rating)
