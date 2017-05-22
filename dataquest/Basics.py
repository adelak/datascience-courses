
# coding: utf-8

# In[1]:

text=open("US_births_1994-2003_CDC_NCHS.csv","r").read()


# In[2]:

text_list=text.split("\n")


# In[3]:

print(text_list[:10])


# In[8]:

def read_csv(file_name):
    text_list=open(file_name,"r").read().split("\n")
    string_list=text_list[1:]
    final_list=[]
    for item in string_list:
        int_fields=[]
        string_fields=item.split(",")
        for field in string_fields:
            int_fields.append(int(field))
        final_list.append(int_fields)
    return final_list 
        


# In[9]:

cdc_list=read_csv("US_births_1994-2003_CDC_NCHS.csv")
print(cdc_list[:10])


# In[12]:

def month_births(birth_list):
    births_per_month={}
    for birth in birth_list:
        if birth[1] in births_per_month:
            births_per_month[birth[1]]+=birth[4]
        else:
            births_per_month[birth[1]]=birth[4]
    return births_per_month


# In[14]:

cdc_month_births=month_births(cdc_list)
print(cdc_month_births)


# In[15]:

def dow_births(birthdata):
    births_per_day={}
    for birth in birthdata:
        if birth[3] in births_per_day:
            births_per_day[birth[3]]+=birth[4]
        else:
            births_per_day[birth[3]]=birth[4]
    return births_per_day


# In[17]:

cdc_day_births=dow_births(cdc_list)
print(cdc_day_births)


# In[18]:

def calc_counts(birthdata,icolumn):
    births_per={}
    for birth in birthdata:
        if birth[icolumn] in births_per_day:
            births_per[birth[icolumn]]+=birth[4]
        else:
            births_per[birth[icolumn]]=birth[4]
    return births_per


# In[ ]:



