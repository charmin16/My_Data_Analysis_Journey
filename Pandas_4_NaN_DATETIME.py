#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# In[3]:


people = {
    'first': ['Corey', 'Jane', 'John', 'Chris', np.nan, None, 'NA'],
    'last': ['Schafer', 'Doe', 'Doe', 'Schafer', np.nan, np.nan, 'Missing'],
    'email': ['CoreySchafer@gmail.com', 'JaneDoe@email.com', 'JohnDoe@email.com', None, np.nan, 'Anonymous@email.com', 'NA'],
    'age': ['33', '55', '63', '36', None, None, 'Missing']
}


# In[52]:


dp = pd.DataFrame(people)
dp


# In[5]:


dp.dropna()


# In[6]:


dp.dropna(axis = 'index', how = 'any') # This is the dafualt argument that pandas uses in the background

# from the above, use the index, if there's a missing value(NaN) in any of the rows


# In[7]:


dp.dropna(axis = 'index', how = 'all')

# drop values only if all the values in the columns of that index are missing(NaN)
# index 4 has been dropped bcos all the values in the columns are missing


# In[8]:


dp.dropna(axis = 'columns', how = 'all')

# Again, as in index, all: drop column if everythin in the 
# column is missing
# In this case, no column is dropped bcos we dont have any columns with all missing values


# In[9]:


dp.dropna(axis = 'columns', how = 'any')

# In this case, all the columns are dropped bcos there's at least one
# missing value in each of the column. Empty dataframe


# In[11]:


dp


# In[12]:


dp.dropna(axis = 'index', how = 'any')


# In[13]:


dp.dropna(axis = 'index', how = 'all')


# In[15]:


dp.dropna(axis = 'columns', how = 'all')


# In[17]:


dp.dropna(axis = 'index', how = 'all', subset = ['email', 'last'])


# In[18]:


dp.dropna(axis = 'index', how = 'any', subset = ['last', 'email'])


# In[19]:


dp.dropna(axis = 'index', how = 'any', subset = ['age'])


# In[22]:


dp


# In[23]:


dp.dropna(axis = 'index', how = 'all', subset = ['first', 'email'])


# In[24]:


dp.dropna(axis = 'index', how = 'any', subset = ['first', 'email'])


# In[25]:


dp


# In[58]:


# To replace custom missing values such as NA,Missing, etc
# like we have on index 6, we can replace them with proper Nan
# using the replace method

dp.replace('NA', np.nan, inplace = True)
dp.replace('Missing', np.nan, inplace = True)
dp


# In[27]:


# If we just want to see if certain values would or would not
# be treated as na values, then we can just run the isna method

dp.isna()


# In[32]:


# Sometimes you may want to fill your nan values with a particular value
# Say, u re grading scores for a test, for a student who didnt turn in their
# assignt, the record will show nan but u may want to fill it in with zero (0)
# or any other number, if u like, to enable u do ur grading.
# Or u can choose to replace NaN with any other string(word of your choice)

dp.fillna('MISSING')


# In[31]:


dp.fillna(0) # This would make more sense with numerical data


# In[47]:


# CASTING DATA TYPES
# Arithmetic operations such as mean, median etc cannot be done on 
# the age column even though they are 'numbers', but they are actually
# strings. 

# 'age'  object (object means a string or a mix of different things)

# because 'age' column is an object, we cant do arithmetic operations on it
# we will have to convert it to an int or float first

# When we have NaN values in a column that we are trying to convert to numbers
# then we need to use the float data type, this is bcos the nan value is actually a float
 
dp.dtypes


# In[48]:


# When we have NaN values in a column that we are trying to convert to numbers
# then we need to use the float data type, this is bcos the nan value is actually a float

# If we try to convert a column that has nan values to integers, then its going to throw
# an error when it runs into those nan values. But if we have replaced the nan values with
# zeros for example then we wont encounter any errors

so doing
dp['age'] = dp['age'].astype(int) will return an error. We should use float instead as explained earlier
type(np.nan)


# In[60]:


dp['age'] = dp['age'].astype(float)


# In[61]:


dp.dtypes


# In[64]:


dp['age'].sum() # Now we can carry out any arithmetic operation on the 'age' column


# In[65]:


# To convert the entire dataframe from one type to another, we can simply do:

dp.astype(int) # int, float, whatever you want to cast it to


# In[67]:


df = pd.read_csv('Downloads/developer_survey_2020/survey_results_publicz.csv')


# In[72]:


df['YearsCode'] = df['YearsCode'].astype(float) 

# The reason why this failed is because 
# there's a string in the response: ('less than 1 year') and pnadas doesnt know how to c
# string to float.
# So we will replace the string with an integer, reasonably. We ll replace 'less than 1 year' with a zero
# and replace 'more than 50 years' with 51
# Then we will now convert or cast to float.


# In[73]:


df['YearsCode'].unique() # you use this method to get the unique responses in a column


# In[75]:


df['YearsCode'].replace('Less than 1 year', 0, inplace = True)


# In[76]:


df['YearsCode'].replace('More than 50 years', 51, inplace = True)


# In[81]:


df['YearsCode'] = df['YearsCode'].astype(float) # Now we can cast to float since we have replaced the strings with integer. We are converting to float not integers because nan is still among the values


# In[85]:


df['YearsCode'].sum()


# In[ ]:


# DATETIME


# In[86]:


df = pd.read_csv('Downloads/ETH_1H.csv')


# In[91]:


df.set_index('Date', inplace = True)
df


# In[94]:


df.head(2)


# In[95]:


df['2020-01':'2020-02']


# In[96]:


df.loc['2019-01':'2020-02']


# In[100]:


df.reset_index(inplace = True)
df['Date'] = pd.to_datetime(df['Date'])


# In[102]:


df.set_index('Date', inplace = True)
df.head()


# In[106]:


df.loc['2020-04-15 20:00:00':'2020-04-16 00:00:00']


# In[ ]:




