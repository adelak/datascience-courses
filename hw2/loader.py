# coding=utf-8
import requests
import pandas as pd
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt

def get_Data(p_url, p_pagestart, p_pageend):
    l_data=''
    # выгрузим страницы новостей в интервале [p_pagesstart,p_pagesend]
    for i_page in range(p_pagestart,p_pageend):
        response = requests.get(p_url+str(i_page))
        l_data += response.content
    return BeautifulSoup(l_data, "html5lib")

def parse_Data(p_data):
    l_divs=p_data.findAll('div',attrs={'class','lazy-loader'})
    l_newsamount=len(l_divs)
    l_data=[l_newsamount]
    for i_newsnote in range(0,l_newsamount):
        l_data.append([])
        l_data[i_newsnote]=[str(cell) for cell in l_divs[i_newsnote]['data-src'].split('/')]
    return l_data

def get_FilteredDataFrame(p_data):
    l_df=pd.DataFrame(p_data)
    # удалим лишние колонки
    l_df.drop(l_df.columns[[0,1,2,3]], axis=1, inplace=True)
    # проименуем столбцы
    l_df.columns=['type','year','month','day','hour','minute','name']
    # удалим лишние строки, нас интересуют только news
    l_df=l_df[l_df.type=='news']
    # удалим неправильные данные(есть строки, что не содержат года)
    l_df=l_df[l_df.year.str.isdigit()]
    # уменьшим названия, оставим только часть до точки
    l_df['name']=l_df.name.apply(lambda x: x.split('.')[0])
    # добавим новую колонку дата и преобразуем в нее год-месяц-день-часы-минуты
    l_df['date']=pd.to_datetime(l_df['year']+l_df['month']+l_df['day']+l_df['hour']+l_df['minute'])
    # удалим теперь ненужные колонки год-месяц-день-часы-минуты и тип
    l_df.drop(l_df.columns[[0,1,2,3,4,5]], axis=1, inplace=True)
    return l_df

def get_Frequency(p_df):
    # средний интервал появления новостей в часах
    l_avg_interval=float(pd.Timedelta(p_df.date.max()-p_df.date.min()).total_seconds())/p_df.name.count()/60/60
    #print pd.Timedelta(p_df.date.max()-p_df.date.min()).total_seconds()/60/60
    #print p_df.date.max()
    #print p_df.date.min()
    #print p_df.name.count()
    # частота
    l_fq=1/l_avg_interval
    return l_fq

# url выбранного источника новостей
SOURCE_URL='http://www.atpworldtour.com/en/news/news-filter-results/news-filter-results-ajax/all/on-court/all/all/all/?page=5&requestedPage='
# одной страницы новостей для анализа мало, выгрузим 30
# интервал выгружаемых страниц
PAGE_START=1 # первая страница интервала
PAGE_END=50 # последняя страница интервала
# получим данные(пример структуры данных в data_example.html)
soup=get_Data(SOURCE_URL,PAGE_START,PAGE_END)
# отфильтруем лишнее, нас интересует только содержимое атрибута data-src в div class="lazy-loader"
data=parse_Data(soup)
# загрузим данные в dataframe и преобразуем/отфильтруем лишнее
df=get_FilteredDataFrame(data)
# расчитаем частоту появления новостей(в час)
frequency=get_Frequency(df)
print frequency
# результат 0.129322489153
# мин дата 2016-10-09 01:34:00
# макс дата 2017-03-05 22:50:00
# всего новостей 459

#df.to_csv('source.tsv', sep='\t', encoding='utf-8', index=False)
