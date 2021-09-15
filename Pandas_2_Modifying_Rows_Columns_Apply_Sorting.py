#!/usr/bin/env python
# coding: utf-8

# In[68]:


# UPDATING ROWS AND COLUMNS -- MODIFYING DATA WITHIN DATAFRAMES
import pandas as pd
people = {
    'first': ['Corey', 'Jane', 'John'],
    'last': ['Schafer', 'Doe', 'Doe'],
    'email': ['corey@mail.com', 'janedoe@mail.com', 'johndoe@mail.com']
}

ppl_df = pd.DataFrame(people)
ppl_df


# In[69]:


# To modify the names of the columns, you simply assign the modified names to .columns

ppl_df.columns = ['first name', 'last name', 'email']
ppl_df
ppl_df.columns = [x.lower() for x in ppl_df.columns] # Use list comprehension to change to upper case
ppl_df
ppl_df.columns = ppl_df.columns.str.replace(' ', '_') # Using the str method to replace underscore with space or vice versa
ppl_df
# ppl_df['EMAIL'] = ppl_df['EMAIL'].str.replace('@', '/') # As seen here, this method can also be used to replace any character in any column
ppl_df['email'] = ppl_df['email'].str.replace('/', '@')

ppl_df.rename(columns = {'first_name': 'first', 'last_name': 'last'}, inplace = True) # This is to rename specific columns

ppl_df

# To change values inside the dataframe:

ppl_df.loc[2]
ppl_df.loc[2] = ['John', 'Smith', 'johnsmith@email.com'] # If you dont specify the columns, then u have to provide values for all the columns
ppl_df
ppl_df.loc[2, ['last', 'email']] = ['Doe', 'johndoe@email.com'] # here we have specified the columns: last and email to be changed
ppl_df
ppl_df.loc[2, 'first'] = 'Charming'

# filt = ppl_df['last'] == 'Schafer'
# ppl_df[filt]
ppl_df.loc[1, 'last'] = 'Trump'
ppl_df

filt = ppl_df['last'] == 'Schafer'
ppl_df.loc[filt, 'email'] = 'barcelona@email.com'
ppl_df


# In[70]:


# To change multiple rows at once. Say, change all the emails in the email column to lower case

ppl_df['email'].str.title() # .str.lower(), upper(), title(), whatever
ppl_df['email'] = ppl_df['email'].str.title()
ppl_df



# In[71]:


# Advance method of doin same thing
# -: apply
# -: map
# -: applymap
# -: replace

# ppl_df['last'].max()
# ppl_df['last'].min()

# APPLY
# Apply is used for callin a function on our values. Works on dataframe and on a series object

ppl_df['email'].apply(len) # To get the lenght of all the emails in the email column


# In[72]:


def update_email(email):
    return email.upper()



# In[73]:


ppl_df['email'].apply(update_email)
ppl_df['email'] = ppl_df['email'].apply(update_email)
ppl_df['email'] = ppl_df['email'].apply(lambda x: x.lower())



# In[74]:


ppl_df.apply(len)


# In[75]:


len(ppl_df['last'])  # This returns number of rows in 'last'


# In[76]:


ppl_df.apply(pd.Series.min)

ppl_df.min()


# In[77]:


# APPLY MAP 
# Apply map only works on dataframe. Series objects dont have the apply maps method

ppl_df.applymap(len) # Gets the lenght of everything in the dataframe
ppl_df.applymap(str.lower)


# In[124]:


# MAP method only works on a Series
# MAP is used for subsitituting each values in Series with
# another value

ppl_df['first'].map({'Corey': 'Chris', 'Jane': 'Mary'})
ppl_df['first'] = ppl_df['first'].map({'Corey': 'Chris', 'Jane': 'Mary'})
ppl_df



# In[79]:


ppl_df.loc[2, 'first'] = 'Spencer'
ppl_df
ppl_df['first'].replace({'Chris': 'Don', 'Mary': 'Crystal'})
ppl_df['first'] = ppl_df['first'].replace({'Chris': 'Don', 'Mary': 'Crystal'})
ppl_df



# In[80]:


df2 = pd.read_csv('Downloads/developer_survey_2020/survey_results_publicz.csv')
df2.rename(columns = {'ConvertedComp': 'Salary_USD'}, inplace = True)
df2.head()


# In[81]:


df2['Hobbyist'].map({'Yes': True, 'No': False})
df2['Hobbyist'] = df2['Hobbyist'].map({'Yes': True, 'No': False})
df2.head()


# In[128]:


# ADDING A COLUMN TO OUR DATAFRAME
# Lets say we want to add a full name column which is a combination of the first and last name

ppl_df['first'] + ' ' + ppl_df['last']

ppl_df['full_name'] = ppl_df['first'] + ' ' + ppl_df['last']

ppl_df

# REMOVING A COLUMN FROM OUR DATAFRAME

ppl_df.drop(columns = ['first', 'last'], inplace = True)
ppl_df






# In[83]:


# To reverse it and split it back to it's original four columns
ppl_df['full_name'].str.split(' ')


# In[84]:


ppl_df['full_name'].str.split(' ', expand = True)


# In[85]:


ppl_df[['first', 'last']] = ppl_df['full_name'].str.split(' ', expand = True)
ppl_df


# In[86]:


# ADDING AND REMOVING ROWS OF DATA

ppl_df.append({'first': 'Tony'}, ignore_index = True) # This is to add a single row of data to the dataframe


# In[87]:


people = {
    'first': ['Tony', 'Steve'],
    'last': ['Stark', 'Rogers'],
    'email': ['ironman@avenge.com', 'cap@avenge.com']
}

ppl2 = pd.DataFrame(people)

ppl_df.append(ppl2, ignore_index = True)

ppl_df


# In[88]:


ppl_df = ppl_df.append(ppl2, ignore_index = True)
ppl_df


# In[89]:


# REMOVING ROWS FROM A DATAFRAME

ppl_df.drop(index = 4)
ppl_df.loc[3, 'last'] = 'Doe'
ppl_df

# ppl_df.drop(index = [3,4])
# ppl_df






# In[90]:


filt = ppl_df['last'] == 'Doe'
ppl_df.drop(index = ppl_df[filt].index )

ppl_df[filt].index # This is how you get the index of a a particular condition

ppl_df


# In[91]:


filt = (ppl_df['first'] == 'Corey') | (ppl_df['first'] == 'Jane')

ppl_df[filt].index


# In[104]:


ppl2.append({'first': 'James', 'last': 'Andy'}, ignore_index = True)

ppl2 = ppl2.append({'first': 'James', 'last': 'Andy'}, ignore_index = True)

ppl2

ppl2.append({'first': 'Manuel', 'last': 'Adriano'}, ignore_index = True)

ppl2 = ppl2.append({'first': 'Manuel', 'last': 'Adriano'}, ignore_index = True)

ppl2.drop(index = [6,5])

ppl2



# In[ ]:


ppl2.drop(index = [3,4,7,8])


# In[ ]:


ppl2

filt = ppl2['first'] == 'James'
ppl2.drop(index = (ppl2[filt].index))
ppl2 = ppl2.drop(index = (ppl2[filt].index))
ppl2.loc[['Rogers', 'Stark'], ['email']]# = ['stunt@mail.com', 'zion@mail.com']


# In[94]:


# SORTING

people = {
    'first': ['Corey', 'Jane', 'John', 'Adam'],
    'last': ['Schafer', 'Doe', 'Doe', 'Doe'],
    'email': ['corey@mail.com', 'janedoe@mail.com', 'johndoe@mail.com', 'art@mail.com']
}

ppl3 = pd.DataFrame(people)


# In[ ]:


ppl3['last'].value_counts()


# In[ ]:


ppl3.sort_values(by = 'last') # Sorting by last name, goes in an ascending order
ppl3.sort_values(by = 'last', ascending = False) # still sorting by last name but goes in a descending order




# In[101]:


# sort on multiple columns: when the first values u are sorting by have identical values
# therefore you want to sort on a different value or column

# ppl3.sort_values(by = ['last', 'first'], ascending = False) # sorting both 'last' and 'first' in descending order in the event of identical 'last' values
ppl3.sort_values(by = ['last', 'first'], ascending = [False, True], inplace = True)
ppl3

ppl3.sort_index()  # To reverse to its original state

ppl3['last'].sort_values() # To sort individual columns. Can also do sort_index






# In[123]:


df2.sort_values(by = 'Country', inplace = True)
df2[['Country', 'Salary_USD']].head(50)

df2.sort_values(by = ['Country', 'Salary_USD'], ascending = [True, False], inplace = True)

df2[['Country', 'Salary_USD']].head(5)


# In[118]:


df2[['Country', 'Salary_USD']].tail()


# In[122]:


# To get the ten largest salary reported

df2['Salary_USD'].nlargest(10)  # 10 largest salaries

df2['Salary_USD'].nsmallest(10) # 10 smallest salaries

df2.nlargest(5, 'Salary_USD')


