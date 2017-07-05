
# coding: utf-8

# In[3]:


import pandas as pd
import matplotlib
get_ipython().magic('matplotlib inline')


# In[4]:


recent_grads=pd.read_csv("recent-grads.csv")
recent_grads.iloc[1]


# In[5]:


recent_grads.head()


# In[6]:


recent_grads.tail()


# In[7]:


recent_grads = recent_grads.dropna()


# In[8]:


recent_grads.describe()


# In[12]:


recent_grads.plot(x='Sample_size', y='Median', kind='scatter')


# In[ ]:




