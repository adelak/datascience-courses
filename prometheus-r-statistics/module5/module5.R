library(lubridate)
library(dplyr)
library(ggplot2)

crime <- read.csv("crimes.csv", header = TRUE)
str(crime)
# названия колонок
colnames(crime)
# первые 10 строк
head(crime,10)

crime$POSIX <- ymd_hms(as.character(crime$Dates))
crime$Dates <- as.Date(ymd_hms(as.character(crime$Dates)))

#crime_friday=crime[crime$"DayOfWeek"=="Friday",]
#df.residual(crime_friday$"X")
moon <- read.csv("moon.csv", header = TRUE)
head(moon,2)
moon$date <- as.Date(moon$date, "%m/%d/%Y")
full_data <- merge(crime, moon, by.x = "Dates", by.y="date")
full_data <- inner_join(crime, moon, by=c("Dates"="date"))
head(full_data,2)

crimes_by_day <- full_data %>%
  group_by(Dates, DayOfWeek) %>%
  count()

sample_vector <- crimes_by_day$n[crimes_by_day$DayOfWeek ==
                                   "Friday"]

head(sample_vector,5)
# кол-во степеней свободы
length(sample_vector)-1

t.test(x=sample_vector)
# изменим числовой способ отображения
options(scipen=999)
# расчитаем p-value
p_value2 <- 2*pt(33.883, df=39, lower.tail = FALSE)
p_value2
