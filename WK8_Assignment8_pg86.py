#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import matplotlib.pyplot as plt 
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


names = ['Bob','Jessica','Mary','John','Mel'] 
absences = [3,0,1,0,8] 
detentions = [2,1,0,0,1] 
warnings = [2,1,5,1,2]


# In[3]:


GradeList = zip(names,absences,detentions,warnings) 
columns=['Names', 'Absences', 'Detentions','Warnings'] 
df = pd.DataFrame(data = GradeList, columns=columns) 


# In[5]:


df['TotalDemerits'] = df['Absences'] +  df['Detentions'] + df['Warnings'] 


# In[6]:


df


# In[7]:


plt.pie(df['TotalDemerits'])


# In[12]:


plt.pie(df['TotalDemerits'],       
        labels=df['Names'],       
        explode=(0,0,0,0.4,0),       
        startangle=90,      
        autopct='%1.1f%%',) 
plt.axis('equal') 
plt.show()


# In[ ]:




