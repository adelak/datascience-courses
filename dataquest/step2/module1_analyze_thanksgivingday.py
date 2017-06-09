
# coding: utf-8

# In[25]:


import pandas as pd

data=pd.read_csv("thanksgiving.csv",encoding="Latin-1")


# In[12]:


data.head()


# In[10]:


data.columns


# In[13]:


data["Do you celebrate Thanksgiving?"].value_counts()


# In[26]:


data=data[data["Do you celebrate Thanksgiving?"]=="Yes"]


# In[17]:


data["Do you celebrate Thanksgiving?"].value_counts()


# In[18]:


data["What is typically the main dish at your Thanksgiving dinner?"].value_counts()


# In[4]:


isTofurkey=data["What is typically the main dish at your Thanksgiving dinner?"]=="Tofurkey"


# In[5]:


data["Do you typically have gravy?"][isTofurkey]


# In[6]:


apple_isnull=pd.isnull(data["Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Apple"])
apple_isnull.head(2)


# In[7]:


pumpkin_isnull=pd.isnull(data["Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pumpkin"])


# In[8]:


pecan_isnull=pd.isnull(data["Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pecan"])


# In[16]:


ate_pies=apple_isnull & pumpkin_isnull & pecan_isnull


# In[19]:


ate_pies.value_counts()


# In[29]:


def converttoint(row):
    if pd.isnull(row):
        return None
    else:
        row =row.split(" ")[0]
        row =row.replace("+", "")
        return int(row)


# In[30]:


data["int_age"] = data["Age"].apply(converttoint)
data["int_age"].describe()


# In[31]:



data["How much total combined money did all members of your HOUSEHOLD earn last year?"].value_counts()


# In[32]:



def extract_income(income_str):
    if pd.isnull(income_str):
        return None
    income_str = income_str.split(" ")[0]
    if income_str == "Prefer":
        return None
    income_str = income_str.replace(",", "")
    income_str = income_str.replace("$", "")
    return int(income_str)

data["int_income"] = data["How much total combined money did all members of your HOUSEHOLD earn last year?"].apply(extract_income)
data["int_income"].describe()


# In[33]:


data[data["int_income"] < 50000]["How far will you travel for Thanksgiving?"].value_counts()


# In[34]:



data[data["int_income"] > 150000]["How far will you travel for Thanksgiving?"].value_counts()


# In[35]:



data.pivot_table(
    index="Have you ever tried to meet up with hometown friends on Thanksgiving night?", 
    columns='Have you ever attended a "Friendsgiving?"',
    values="int_age"
)


# In[36]:



data.pivot_table(
    index="Have you ever tried to meet up with hometown friends on Thanksgiving night?", 
    columns='Have you ever attended a "Friendsgiving?"',
    values="int_income"
)


# In[ ]:




