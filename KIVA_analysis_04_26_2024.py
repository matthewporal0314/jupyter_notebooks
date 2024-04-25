#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 50000)


# In[2]:


data = pd.read_csv('kiva_loans.csv')


# In[4]:


data.head()


# In[5]:


data['posted_time'] = pd.to_datetime(data['posted_time'])
data['disbursed_time'] = pd.to_datetime(data['disbursed_time'])
data['funded_time'] = pd.to_datetime(data['funded_time'])


# In[10]:


data['loan_crowdsourcing_time'] = (data.funded_time-data.posted_time).dt.days
data['date'] = pd.to_datetime(data['date'])
data['month'] = data['date'].apply(lambda x: x.strftime('%Y-%m-01'))


# In[11]:


data.head()


# In[12]:


data.groupby(["month"])["loan_crowdsourcing_time"].mean().reset_index()


# In[13]:


import matplotlib.pyplot as plt
import numpy

fig, ax = plt.subplots(figsize=(20, 7.5))
(
    pd.cut(data['loan_crowdsourcing_time'], bins=numpy.arange(-1, 81, 1))
        .value_counts()
        .sort_index()
        .plot.bar(ax=ax)
)

