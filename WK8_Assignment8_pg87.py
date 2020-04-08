#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


location = 'C:\\Users\\nchin\\DataViz\\Week8_files\\gradedata.csv'


# In[3]:


df = pd.read_csv(location)


# In[4]:


df.head()


# In[8]:


plt.figure(figsize=(16, 8))
plt.scatter(data = df, x = 'hours', y = 'grade')


# In[ ]:




