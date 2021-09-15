#!/usr/bin/env python
# coding: utf-8

# In[274]:


import pandas as pd

# pd.set_option('display.max_columns', 85) # This is not a method or an attribute, its a setting
#pd.set_option('display.max_rows', 100) 

# if you want to see all the rows or columns, you must put the maximum number of the row or column
# meaning you want all (columns or rows) displayed. Any number outside the maximum will not work

df_schema = pd.read_csv('Downloads/survey_results_schema.csv')

# By default, pandas only displays 20 columns even if the columns are more than 20
# To view all the columns

# pd.set_option('display.max_columns', 85) # assuming the total number of columns are 85

# To display the total number of rows

# pd.set_option('display.max_rows', 85) # also assuming the total number of rows are 85

df_schema.head() # This is to display the first five rows
df_schema.head(7) # If you want to display a particular number of rows, enter the number in the parenthesis as shown
df_schema.tail() # To display the last five rows
df_schema.tail(7) # To display the last seven rows
df_schema.sample(5) # To display random five rows
df_schema

#df_schema.loc['ConvertedComp']
df_schema.head()


# In[199]:


people = {
    'first': ['Corey', 'Jane', 'John'],
    'last': ['Schafer', 'Doe', 'Doe'],
    'email': ['corey@mail.com', 'janedoe@mail.com', 'johndoe@mail.com']
}
# When you convert this to pandas, the keys are the columns while the values are the rows

# DataFrame is a two dimensional array which essentially means rows and columns
# Series is a one dimensional array which basically means rows of a single column
# people['last']
# people['email']

ppl_df = pd.DataFrame(people)
ppl_df['email'] # You can either use this or use the dot notation
# ppl_df.email
# ppl_df.first
ppl_df['email']

# If we want to set the email column as our index, or any column we choose for that matter
# ppl_df.set_index('email') # When you run this, the email becomes the index instead of the default 0,1,2,.. 

# ppl_df.set_index('email', inplace = True) # This mean you want to effect this change in the dataframe, modifies the dataframe permanently

# ppl_df.reset_index(inplace = True) # This is to reset the index to its original or default state
# ppl_df

filt = (ppl_df['last'] == 'Doe')
ppl_df[filt] # This is how you get the values, not the boolean
# ppl_df.loc[filt] # This is preferred bcos you can do things like ....
# ppl_df.loc[filt, 'email']

filt = (ppl_df['last'] == 'Doe') & (ppl_df['first'] == 'John') #last name is Doe and first is John
ppl_df.loc[filt, ['email']]

filt = (ppl_df['last'] == 'Schafer') | (ppl_df['first'] == 'John')
ppl_df.loc[filt, ['email']]

# To negate the result: to get opposit of the conditions, simply use a tilter sign ~

ppl_df.loc[~filt] # Returns the opposite of the above



# In[150]:


ppl_df.index
ppl_df.loc['corey@mail.com':, ['first', 'last']]


# In[89]:


# To access multiple columns at once

ppl_df[['last', 'email']] # Note that there are two pairs of brackets, an inner and outer one when, this is only when u want more than one columns

# To view all of the columns, you can simply do..

ppl_df.columns

# In order to get rows, we can use iloc and loc. iloc is short for integer location, while loc is for label location
# To get the first row,

ppl_df.iloc[0] # This returns all the details of the first person

ppl_df.iloc[[0,1]] # This returns the first two rows. Remember two pairs of brackets otherwise pandas will interpret it to mean a single item

ppl_df.iloc[[0,1], [0,1]] # This returns the first two rows, the first index which is the second column only
# [0,1]: represents the first two rows; 1: represents the first index which is the second column

ppl_df.iloc[0:2, 0:3] # We can also do slicing, but note that the slicing is without the inner bracket
#for iloc only integer indexing are used as shown in the examples below

# loc on the other hand uses labels, however it uses interger indexing if its default, eg below

ppl_df.loc[[0,1], ['email', 'last']] # 0,1 was used in the first bracket bcos thats the default label for the row.
# If we had assigned different labels for the rows, thats what we would have used in place of [0,1].
# For the second bracket, we simply put in the labels of the columns we are interested in




# In[352]:


df = pd.read_csv('Downloads//survey_results_public.csv')
df.shape
df.columns
df.head()
# df.ProgramHobby.value_counts() # This is to count the number of unique responses: How many ppl answered 'yes', 'no', etc
# df['ProgramHobby'].value_counts()
df.set_options('display', max_columns, 154)


# In[123]:


df.iloc[[0], 1:3]  # Note that iloc slicing is like ur regular python slicing: the second digit is not included
df.loc[0:3, 'Respondent': 'Country'] # With loc, the second label or digit(like in this case) is inclusive
df.loc[[1,2,3], 'ProgramHobby']
df.loc[0:3, 'ProgramHobby']
df.iloc[0:3, 1:3]


# In[133]:


df.loc[0:3, 'Respondent': 'Country']
df.columns[0]
df.columns[0:4]
df.columns[-1]

df.columns[-2]
df.iloc[0:7, [1,-2, -1]]
df.loc[0:5, ['Professional', 'Salary', 'ExpectedSalary']]

df.iloc[47700:47710, 3:5]
df.loc[47700:47710, 'Country': 'FormalEducation']


# In[182]:


df_schema = pd.read_csv('Downloads/survey_results_schema.csv', index_col = 'Column')
df_schema
#df_schema.set_index('Column', inplace = True)
df_schema.loc['Respondent': 'University', ['Question']]
df_schema.loc['InterestedAnswers', 'Question']
df_schema.sort_index() # This is to sort the index column alphabetically
df_schema.sort_index(ascending = False) # To sort in reverse order

# You can either set the index by using df.set_index('Respondent', inplace = True)
# Or you set it from the beginning at the point of reading the csv file by using index_col = 'Respondent'


# In[215]:


# FILTERING
# df.loc[0:20, ['Salary']]
high_pay = (df['Salary'] > 70000)  # To filter out ppl whose salary is over 70k
df.loc[high_pay, ['Salary', 'Country', 'University', 'FormalEducation']]

# To filter out ppl from some countries, say United States, United Kingdom, Israel, Inida, Germany
# We can do something cumber like👇

# country = (df['Countries'] = 'United States') | (df['Countries'] = 'Canada') | etc
# The above is too cumbersome, preferably we can do...👇

countries = ['United States', 'United Kingdom', 'India', 'Canada', 'Germany']
filt = df['Country'].isin(countries)
df.loc[filt, ['Country']]


# In[221]:


df2 = pd.read_csv('Downloads/developer_survey_2020/survey_results_publicz.csv')
df2.columns


# In[355]:


# df2.loc[0:20, ['ConvertedComp']]
# df2.set_index('Respondent', inplace = True)
df2.shape


# In[240]:


df2.loc[1:7, ['ConvertedComp', 'Country']]

countries = ['United States', 'Germany', 'India', 'Albania']
select_countries = df2['Country'].isin(countries)
df2.loc[1:7, ['Country', 'Age']]

df2.columns


# In[356]:


pythn = df2['LanguageWorkedWith'].str.contains('Python', na = False)
df2.loc[pythn, ['LanguageWorkedWith']].head(12)
df2['ConvertedComp'].head(10)
df2.shape


# In[350]:


df2.Hobbyist.value_counts()


# In[294]:


elite = (df2['Age'] < 30) & (df2['ConvertedComp'] > 70000) & (df2['Country'] == 'Germany') & (df2['Hobbyist'] == 'Yes')


df6 = df2.loc[elite, ['Age', 'ConvertedComp', 'Country', 'Hobbyist']]
df6
df6.set_index('Age', inplace = True)
df6.sort_index()



# In[304]:


df6.reset_index()
df2.reset_index(inplace = True)
df2.loc[0:20, ['Age1stCode']]


# In[349]:


df2.iloc[0:21, 2:9]
#df2.loc[0:21, 'MainBranch':'ConvertedComp']
#df2.set_index('Respondent', inplace = True)
df2.head()


# In[359]:


df2.loc[1:20, 'MainBranch':'ConvertedComp']
df2.head()


# In[336]:


countries = ('Germany', 'United Kingdom')
ops = ('MacOS', 'Windows')
filt = (df2['Hobbyist'] == 'Yes') & (df2['Age'] > 30) & (df2['Country'].isin(countries)) & (df2['Employment'] == 'Employed full-time') & (df2['OpSys'].isin(ops)) & (df2['LanguageWorkedWith'].str.contains('Python'))
df2_age = df2.loc[filt, ['Hobbyist', 'Age', 'Country', 'Employment', 'OpSys', 'LanguageWorkedWith']].head(20)
df2_age


# In[341]:


df2_age.set_index('Age', inplace = True)


# In[346]:


df2_age.sort_index()
df2_age.sort_index(ascending = False).head(10)
df2_age.sort_index().tail(10)

