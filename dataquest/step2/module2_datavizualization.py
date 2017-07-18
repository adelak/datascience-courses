
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')


# In[36]:


recent_grads=pd.read_csv("recent-grads.csv")
recent_grads.iloc[1]


# In[39]:


recent_grads.head()


# In[4]:


recent_grads.tail()


# In[5]:


raw_data_count=len(recent_grads)
recent_grads = recent_grads.dropna()
cleaned_data_count=len(recent_grads)
print(raw_data_count)
print(cleaned_data_count)


# In[6]:


recent_grads.describe()


# In[7]:


recent_grads.plot(x='Sample_size', y='Median', kind='scatter')
# 


# In[8]:


recent_grads.plot(x='Sample_size', y='Unemployment_rate', kind='scatter')
# 


# In[9]:


recent_grads.plot(x='Full_time', y='Median', kind='scatter')


# In[10]:


recent_grads.plot(x='ShareWomen', y='Unemployment_rate', kind='scatter')


# In[8]:


recent_grads.plot(x='Men', y='Median', kind='scatter')


# In[18]:


recent_grads.plot(x='Women', y='Median', kind='scatter')


# In[11]:


cols = ["Sample_size", "Median", "Employed", "Full_time", "ShareWomen", "Unemployment_rate", "Men", "Women"]


# In[12]:


fig = plt.figure(figsize=(5,20))
for key,col in enumerate(cols):
    ax = fig.add_subplot(8,1,key+1)
    ax = recent_grads[col].plot(kind='hist', rot=40,title=col)
    plt.subplots_adjust(wspace=0.9, hspace=0.9)


# In[59]:


# The most common median salary range 30000 - 40000


# In[13]:


total=sum(row for row in recent_grads["Total"])
total_men=sum(row for row in recent_grads["Men"])
total_women=sum(row for row in recent_grads["Women"])
print(total)
print(total_men)
print(total_women)
# Percent of majors that are predominantly male
total_men/total


# In[26]:


# Percent of majors that are predominantly female 
total_women/total


# In[27]:


from pandas.tools.plotting import scatter_matrix
scatter_matrix(recent_grads[['Sample_size', 'Median']], 
               figsize=(6,6))


# In[28]:


scatter_matrix(recent_grads[['Sample_size', 'Median','Unemployment_rate']], 
               figsize=(10,6))


# In[41]:





# In[42]:


recent_grads[:10].plot.bar(x='Major', y='ShareWomen', legend=False)
recent_grads[163:].plot.bar(x='Major', y='ShareWomen', legend=False)


# In[ ]:




