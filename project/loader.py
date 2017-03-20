# coding=utf-8
import requests
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
l_df['date']=l_df['link'].str.rsplit('-',6)
#l_df['gender']=l_df['link'].str.rsplit('-',5)
#l_df['tour']=l_df['link'].str.rsplit('-',4)
#l_df['stage']=l_df['link'].str.rsplit('-',3)
#l_df['player1']=l_df['link'].str.rsplit('-')[2]
#l_df['player2']=l_df['link'].str.rsplit('-')[1]
print l_df
#print soup.prettify().encode('UTF-8')
