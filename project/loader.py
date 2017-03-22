# coding=utf-8
import requests
import urllib
import pandas as pd
from bs4 import BeautifulSoup
import pprint
from matplotlib import pyplot as plt
from html5print import HTMLBeautifier
import re

pp = pprint.PrettyPrinter()
f=open('chart.htm', 'r')
htmldata = f.read()
soup = BeautifulSoup(htmldata, "html5lib")
#tags_a=[]
links=[]
for tag_a in soup.findAll('a',attrs={"href" : re.compile("^20")}):
    links.append(tag_a['href'])
#print pp.pprint(tags_a)
l_df=pd.DataFrame(links)
l_df.columns=['link']
valueslist=l_df['link'].str.replace('.html','')
values=valueslist.str.split('-')
tvalues=zip(*values)
l_df['date']=pd.to_datetime(tvalues[0])
l_df['gender']=tvalues[1]
l_df['tournament']=tvalues[2]
l_df['stage']=tvalues[3]
l_df['player1']=tvalues[4]
l_df['player2']=tvalues[5]
#print pp.pprint(zip(*values))
#print l_df
url='http://tennisabstract.com/charting/'+l_df['link'][1]
response = requests.get(url)
l_data = response.content
soup2 = BeautifulSoup(l_data, "html5lib")
data=[]
for tag_span in soup2.findAll('table'):
    data.append(tag_span)
print pp.pprint(data)
#print soup.prettify().encode('UTF-8')
