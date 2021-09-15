#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv('Downloads/ETH_1H.csv')


# In[3]:


df.head()


# In[4]:


df.loc[2, 'Date'].day_name() # This wont work bcos 'Date' is read as a string


# In[7]:


df['Date'] = pd.to_datetime(df['Date'])#, format = '%Y-%m-%d %I-%p')


# In[ ]:


df['Date']


# In[ ]:


df.dtypes


# In[ ]:


df.loc[2, 'Date'].day_name()


# In[ ]:


df['Date'].dt.day_name() # dt here is like the str class. dt.day_name, etc


# In[ ]:


df['Week_day'] = df['Date'].dt.day_name()


# In[ ]:


df.head()


# In[ ]:


df['Date'].min() # To view the earliest date in the dataset


# In[ ]:


df['Date'].max() # To view the most recent date in the dataset


# In[ ]:


df['Date'].max() - df['Date'].min() # To get the number of days between the earliest date and the most recent date. Its called timedelta


# In[11]:


df.set_index('Date', inplace = True)
df.head()


# In[ ]:


# Filtering dates

filt = (df['Date'] >= '2020')
df.loc[filt].head(2) # This will return all the data in 2020 and above


# In[ ]:


filt = (df['Date'] >= '2019') & (df['Date'] < '2020')
df.loc[filt]

# The above is how you get the data for 2019
# filt = (df['Date'] == '2019') will not work


# In[ ]:


df.head()


# In[ ]:


df['2019']


# In[ ]:


df.loc['2019']


# In[8]:


df.dtypes


# In[14]:


df['2019']


# In[20]:


df['2019-01-01':'2019-02-01']


# In[29]:


df.loc['2018'].head(2)


# In[31]:


df.reset_index(inplace = True)
df.head(2)


# In[37]:


filt = (df['Date'] >= '2019-02-01') & (df['Date'] <= '2019-06-20')
df.loc[filt, ['Close']]


# In[39]:


df.loc[filt, ['Close']].mean() # or
df.loc[filt, 'Close'].mean()


# In[42]:


df.set_index('Date',inplace = True)
df.head(2)


# In[48]:


df.loc['2020-04-12']['High'].max()


# In[47]:


df['High'].resample('D').max() # data in column 'High' to be broken down by days and then grab the maximum


# In[49]:


df['High'].resample('W').max()


# In[52]:


h = df['High'].resample('M').max().head()


# In[53]:


h.plot()


# In[54]:


# To resample multiple columns at once. We can do that by running
# the resample method on the entire dataframe instead of on a single
# series

df.resample('W').mean() 


# In[55]:


# We may not want one method applied to all columns like it is on
# the previous cell. Say, we want max value for 'High' column,
# min value for 'Low' column, etc

df.resample('W').agg({'Close':'mean', 'High': 'max', 'Low':'min', 'Volume':'sum'})


# In[ ]:




