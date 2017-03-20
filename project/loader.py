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
tags_a=soup.findAll('a',attrs={"href" : re.compile("^20")})
print pp.pprint(tags_a)
#print soup.prettify().encode('UTF-8')
