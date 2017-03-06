# coding=utf-8
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
df = pd.read_csv('D:\RepositoryStudy\datascienceua_tasks\hw3\source.tsv', sep='\t',parse_dates=['date'])
# посмотри распределение по часам дня, увидим когда чаще всего выкладываются новоости
df.date.dt.hour.value_counts().sort_index(ascending=True).plot.bar()
plt.show()
# посмотри распределение по неделям года, увидим в какие недели было больше/меньше новостей
df.date.dt.week.value_counts().sort_index(ascending=True).plot.bar()
plt.show()
# посмотри распределение по месяцам года, увидим в какие месяцы было больше/меньше новостей
df.date.dt.month.value_counts().sort_index(ascending=True).plot.bar()
plt.show()
df['index']=df.date.sort(ascending=True, inplace=False).index
df['date_timestamp']= pd.to_numeric(df['date']).apply(lambda x:x/float(10**9))
df['date_timestamp']=df['date_timestamp']-df['date_timestamp'].min()
sns.regplot(x='date_timestamp', y='index', data=df)
plt.show()
# графики можно посмотреть в папке results
# Выводы
# 1) наочно видно, что в период зимнего перерыва(декабрь) идет сильный спад публикации новостей
# объяснить это легко, тогда нет официальных турниров
# 2) публикации делаются в любое время дня, наиболее активный период 12:00-21:00
# 3) максимум публикаций в январе можно связать с 2 факторами: начало сезона, турнир большого шлема(чего не было в другие анализируемые месяцы)
