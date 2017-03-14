# coding=utf-8
import requests
import pandas as pd
from bs4 import BeautifulSoup
import pprint
from matplotlib import pyplot as plt

pp = pprint.PrettyPrinter()
f=open('source.html', 'r')
soup = BeautifulSoup(f.read(),"html5lib")
print soup.prettify()
