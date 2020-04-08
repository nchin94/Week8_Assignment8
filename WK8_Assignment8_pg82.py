#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt 
import pandas as pd 
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


location = 'C:\\Users\\nchin\\DataViz\\Week8_files\\gradedata.csv'


# In[3]:


df = pd.read_csv(location)


# In[4]:


df.head()


# In[7]:


plt.rcParams["patch.force_edgecolor"] = True


# In[8]:


df.hist(column="age", by="gender")

