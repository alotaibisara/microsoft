#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np


# In[ ]:





# In[7]:


df = pd.read_csv('microsoft.csv')
df


# In[9]:


df['Date'].isnull().values.any()


# In[11]:


df['High'].isnull().sum()


# In[12]:


df.isnull().values.any()


# In[13]:


df.isnull().sum().sum()


# In[15]:


numbers = {'set_of_numbers': [1,2,3,4,5,np.nan,6,7,np.nan,8,9,10,np.nan]}
df = pd.DataFrame(numbers,columns=['set_of_numbers'])
print (df)


# In[16]:



check_for_nan = df['set_of_numbers'].isnull()
print (check_for_nan)


# In[19]:


numbers = {'set_of_numbers': [1,2,3,4,5,np.nan,6,7,np.nan,8,9,10,np.nan]}
df = pd.DataFrame(numbers,columns=['set_of_numbers'])

df.loc[df['set_of_numbers'].isnull(),'value_is_NaN'] = 'Yes'
df.loc[df['set_of_numbers'].notnull(), 'value_is_NaN'] = 'No'
print (df)


# In[23]:


numbers = {'set_of_numbers': [1,2,3,4,5,np.nan,6,7,np.nan,8,9,10,np.nan]}
df = pd.DataFrame(numbers,columns=['set_of_numbers'])

count_nan = df['set_of_numbers'].isnull().sum()
print ('Count of NaN: ' + str(count_nan))


# In[24]:


numbers = {'set_of_numbers': [1,2,3,4,5,np.nan,6,7,np.nan,8,9,10,np.nan]}
df = pd.DataFrame(numbers,columns=['set_of_numbers'])

df.loc[df['set_of_numbers'].isnull(),'value_is_NaN'] = 'Yes'
df.loc[df['set_of_numbers'].notnull(), 'value_is_NaN'] = 'No'

count_nan = df.loc[df['value_is_NaN']=='Yes'].count()
print (count_nan)


# In[25]:


numbers = {'first_set_of_numbers': [1,2,3,4,5,np.nan,6,7,np.nan,8,9,10,np.nan],
           'second_set_of_numbers': [11,12,np.nan,13,14,np.nan,15,16,np.nan,np.nan,17,np.nan,19]}
df = pd.DataFrame(numbers,columns=['first_set_of_numbers','second_set_of_numbers'])

print (df)


# In[26]:


df.isnull().values.any()


# In[27]:


numbers = {'first_set_of_numbers': [1,2,3,4,5,np.nan,6,7,np.nan,8,9,10,np.nan],
           'second_set_of_numbers': [11,12,np.nan,13,14,np.nan,15,16,np.nan,np.nan,17,np.nan,19]}
df = pd.DataFrame(numbers,columns=['first_set_of_numbers','second_set_of_numbers'])

check_nan_in_df = df.isnull().values.any()
print (check_nan_in_df)


# In[28]:


check_nan_in_df = df.isnull()
print (check_nan_in_df)


# In[29]:


df.isnull().sum().sum()


# In[30]:


count_nan_in_df = df.isnull().sum().sum()
print ('Count of NaN: ' + str(count_nan_in_df))


# In[31]:


count_nan_in_df = df.isnull().sum()
print (count_nan_in_df)


# In[ ]:




