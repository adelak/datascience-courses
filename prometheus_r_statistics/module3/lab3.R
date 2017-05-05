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

# посчитаем вероятность получить фильм с оценкой <=4
sum(movie_body_counts$IMDB_Rating<=4)/length(movie_body_counts$IMDB_Rating)

