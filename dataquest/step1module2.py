
# coding: utf-8

# In[2]:

import csv
import datetime


# In[5]:

f=open("guns.csv", "r") 
reader = csv.reader(f)
data = list(reader)


# In[6]:

print(data[:5])
headers = data[:1]
data = data[1:]
print(headers)
print(data[:5])


# In[7]:

years = [row[1] for row in data]
year_counts = {}


# In[8]:

for year in years:
    if year not in year_counts:
        year_counts[year]=1
    else:
        year_counts[year]+=1
print(year_counts)


# In[9]:

dates=[datetime.datetime(year=int(row[1]), month=int(row[2]), day=1) for row in data]


# In[10]:

dates[:5]


# In[11]:

date_counts = {}

for date in dates:
    if date not in date_counts:
        date_counts[date] = 1
    date_counts[date] += 1


# In[12]:

sex_counts = {}

for row in data:
    if row[5] not in sex_counts:
        sex_counts[row[5]] = 1
    sex_counts[row[5]] += 1
sex_counts


# In[13]:

race_counts = {}

for row in data:
    if row[7] not in race_counts:
        race_counts[row[7]] = 1
    race_counts[row[7]] += 1
race_counts


# ** Analyzed races,sex,dates,years

# In[3]:

f2=open("census.csv","r")
census=list(csv.reader(f2))
print(census[:5])


# In[30]:

mapping = {
    "Asian/Pacific Islander": 15159516 + 674625,
    "Black": 40250635,
    "Hispanic": 44618105,
    "Native American/Native Alaskan": 3739506,
    "White": 197318956
}

race_per_hundredk = {}
for k,v in race_counts.items():
    race_per_hundredk[k] = (v / mapping[k]) * 100000

race_per_hundredk


# In[43]:

intents=[row[3] for row in data]
races=[row[7] for row in data]
homicide_race_per_hundredk={}


# In[44]:

homicide_race_counts = {}
for i,race in enumerate(races):
    if race not in homicide_race_counts:
        homicide_race_counts[race] = 0
    if intents[i] == "Homicide":
        homicide_race_counts[race] += 1

race_per_hundredk = {}
for k,v in homicide_race_counts.items():
    race_per_hundredk[k] = (v / mapping[k]) * 100000

race_per_hundredk    


# In[ ]:



