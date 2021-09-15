#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd

df2 = pd.read_csv('Downloads/developer_survey_2020/survey_results_publicz.csv')


# In[1]:


df2['ConvertedComp'].median()
df2.median()
df2.shape


# In[3]:


df2.describe()


# In[4]:


df2['ConvertedComp'].count() # count() counts the number of non NaN rows, counts number of non missing rows

# The above returned 34756 which means out of the 64461 rows 34756 had values while the rest were NaN

df2['Hobbyist'].value_counts() # value_counts() counts up individual values in a specific row and reports how many of those values are in the column

df2['Hobbyist'].value_counts(normalize = True) # You use this to get the percentage

df2['CompFreq'].value_counts(normalize = True)


# In[5]:


pd.set_option('display.max_columns', 61)
df2.shape


# In[6]:


df2['OpSys'].value_counts(normalize = True)


# In[7]:


df2['Country'].value_counts(normalize = True)


# In[8]:


country_grp = df2.groupby(['Country'])
country_grp.get_group('Nigeria').shape


# In[9]:


filtr = df2['Country'] == 'Brazil'

df2.loc[filtr]['ConvertedComp'].median()

df2.loc[filtr, ['OpSys']].value_counts(normalize = True)


# In[10]:


country_grp.get_group('India')['ConvertedComp'].median()

country_grp.get_group('India')['OpSys'].value_counts()


# In[11]:


country_grp['OpSys'].value_counts().loc['United States'] #, 'Spain', 'Nigeria']]
country_grp.get_group('United States')['OpSys'].value_counts()


# In[12]:


country_grp['ConvertedComp'].min().loc['Nigeria']
country_grp.get_group('Germany')['ConvertedComp'].min()


# In[13]:


country_grp['ConvertedComp'].median().loc['Germany']


# In[14]:


# To run multiple aggregate function, say you want to see the mean and the median

country_grp['ConvertedComp'].agg(['median', 'mean'])
country_grp['ConvertedComp'].agg(['median', 'mean']).loc['South Africa']


# In[15]:


filt = df2['LanguageWorkedWith'].str.contains('Python', na = False)

df2.loc[filt, ['Country']].value_counts()


# In[16]:


filt = df2['Country'] == 'Germany'

df2.loc[filt, 'LanguageWorkedWith'].str.contains('Python')
df2.loc[filt]['LanguageWorkedWith'].str.contains('Python').sum()


# In[17]:


#country_grp['LanguageWorkedWith'].str.contains('Python').sum()
# The above returns an error bcos 'SeriesGroupBy' object has no attribute 'str'

country_grp['LanguageWorkedWith'].apply(lambda x: x.str.contains('Python').sum())


# In[18]:


country_grp['LanguageWorkedWith'].apply(lambda x: x.str.contains('Python').sum()).loc['India']


# In[19]:


country_grp['LanguageWorkedWith'].apply(lambda x: x.str.contains('Python').sum()) #.loc['Afghanistan': 'Zimbabwe']


# In[159]:


python_progmrs = country_grp['LanguageWorkedWith'].apply(lambda x: x.str.contains('Python').sum())# .loc['Nigeria']

country_responders = df2['Country'].value_counts()



# In[21]:


pyth_perc = pd.concat([python_progmrs, country_responders], axis = 'columns')
pyth_perc


# In[22]:


pyth_perc['perc_country(%)'] = (pyth_perc['LanguageWorkedWith'] / pyth_perc['Country']) * 100

pyth_perc


# In[23]:


pyth_perc.drop(columns = ['perc_country'], inplace = True)
pyth_perc


# In[ ]:


pyth_perc.rename(columns = {'LanguageWorkedWith': 'Python_Programmers', 'Country': 'Total_Country_Responders'}, inplace = True)
pyth_perc


# In[ ]:


pyth_perc.sort_values(by= ['perc_country(%)'], ascending = False, inplace = True)

pyth_perc.loc['Japan']


# In[ ]:


TotalResponders = df2['Country'].value_counts()


# In[ ]:


cntry_gp = df2.groupby(['Country'])
cntry_gp.get_group('India')
cntry_gp['OpSys'].value_counts().loc['Japan']
cntry_gp['ConvertedComp'].median().loc['Nigeria']
cntry_gp.get_group('Japan').shape
df2['CompFreq'].head(40)
df2.head()


# In[ ]:


con_grp = df2.groupby(['Country'])
con_grp.get_group('India')
con_grp['LanguageWorkedWith].mean().loc['Brazil']


# In[ ]:


country_grp['LanguageWorkedWith'].apply(lambda x: x.str.contains('Python')).value_counts()


# In[ ]:


country_grp['LanguageWorkedWith'].apply(lambda x: x.str.contains('Python').sum())


# In[ ]:


filt = (df2['LanguageWorkedWith'].str.contains('JavaScript', na = False)) & ((df2['LanguageWorkedWith']).str.contains('Python', na = False)) & (df2['ConvertedComp'] >= 950000)

df2.loc[filt]['ConvertedComp'].value_counts()


# In[35]:


ctry_grp = df2.groupby(['Country'])


# In[50]:


ctry_grp.get_group('Brazil')['ConvertedComp'].median()
ctry_grp['ConvertedComp'].median().loc['Brazil']


# In[49]:


ctry_grp.get_group('China')['OpSys'].value_counts(normalize = True)
ctry_grp['OpSys'].value_counts(normalize = True).loc['China']


# In[53]:


filtt = df2['Country'] == 'Brazil'
df2.loc[filtt]['ConvertedComp'].median()
df2.loc[filtt,['ConvertedComp']].median() # The 'ConvertedComp' can go without the square bracket, its fine


# In[57]:


ctry_grp.get_group('India')['ConvertedComp'].agg(['median', 'mean'])
ctry_grp['ConvertedComp'].agg(['median', 'mean']).loc[['India', 'Japan', 'France']]


# In[61]:


fille = df2['Country'] == 'Germany'
df2.loc[fille]['LanguageWorkedWith'].str.contains('JavaScript')#.value_counts()


# In[62]:


ctry_grp.get_group('Germany')['LanguageWorkedWith']


# In[75]:


ctry_grp['LanguageWorkedWith'].apply(lambda x: x.str.contains('JavaScript')).value_counts()
ctry_grp['ConvertedComp'].agg(['median', 'mean']).loc[['France', 'United States', 'Nigeria', 'India']]


# In[205]:


filr = df2['Country'] == 'Brazil'
df2.loc[filr]['LanguageWorkedWith'].str.contains('Python').sum()


# In[119]:


ctry_grp['LanguageWorkedWith'].str.contains('Python').sum()


# In[209]:


PythPrgrms = ctry_grp['LanguageWorkedWith'].apply(lambda x: x.str.contains('Python').sum())#.loc['United States']
PythPrgrms


# In[165]:


ctry_grp['Country'].value_counts().loc[['Afghanistan','Albania','Algeria','Andorra','Angola']]


# In[167]:


TotalResponders = df2['Country'].value_counts()
TotalResponders


# In[171]:


PythResults = pd.concat([PythPrgrms, TotalResponders], axis = 'columns') #, ignore_index = True
PythResults

PythResults['PctPythPrgmrs'] = PythPrgrms / TotalResponders
PythResults.drop(columns = {'PctPythPrgmrs'}, inplace = True)


# In[181]:


PythResults['%PythPrgmrs'] = PythPrgrms / TotalResponders * 100 
PythResults
PythResults.rename(columns = {'LanguageWorkedWith': 'PythBadGuys', 'Country': 'TotalRespondents'}, inplace = True)
PythResults


# In[203]:


PythResults.sort_values(by = ('%PythPrgmrs'), ascending = False, inplace = True)
PythResults


# In[94]:


df2.head()


# In[227]:


filtr = (df2['Country'] == 'Nigeria') & (df2['Age'].between(25, 30)) & (df2['ConvertedComp'] > 20000)
df2.loc[filtr, ['Age', 'ConvertedComp']] #.between(25, 30).sum()


# In[246]:


filtr = (df2['Country'] == 'United States') & (df2['Age'].between(25, 30))
(df2.loc[filtr]['ConvertedComp'] > 20000).sum()


# In[7]:


cntry_grp = df2.groupby(['Country'])


# In[35]:


cntry_grp.get_group('India').head(2)
df2.columns
df2['OpSys'].head()


# In[ ]:


PythPrgrms = ctry_grp['LanguageWorkedWith'].apply(lambda x: x.str.contains('Python').sum())#.loc['United States']
PythPrgrms


# In[168]:


AgeGrpTotal25_40 = cntry_grp['Age'].apply(lambda x: x.between(25, 40).sum())
LangDesrNYrPython = cntry_grp['LanguageDesireNextYear'].apply(lambda x: x.str.contains('Python').sum())


# In[179]:


ops = ('Windows', 'MacOS')
OpSystPrefrWind_MacOS = cntry_grp['OpSys'].apply(lambda x: x.isin(ops).sum())
#OpSystPrefrWind_MacOS


# In[188]:


payfreq = ('Yearly', 'Monthly')
CompFreqcyYearly_Monthly = cntry_grp['CompFreq'].apply(lambda x: x.isin(payfreq).sum())


# In[187]:


langs = ('SQL', 'Swift', 'JavaScript')
PrgLangPrefrSQL_Sw_JS = cntry_grp['LanguageWorkedWith'].apply(lambda x: x.isin(langs).sum())


# In[189]:


cntry_grp['ConvertedComp'].apply(lambda x: (x > 50000).sum())
SalOver50k = cntry_grp['ConvertedComp'].apply(lambda x: (x > 50000).sum())

#pyth_perc = pd.concat([python_progmrs, country_responders], axis = 'columns')


# In[190]:


df3 = pd.concat([AgeGrpTotal25_40, LangDesrNYrPython, OpSystPrefrWind_MacOS, CompFreqcyYearly_Monthly, PrgLangPrefrSQL_Sw_JS, SalOver50k  ], axis = 'columns') #, ignore_index = True)
df3


# In[192]:


df3.rename(columns = {'Age': 'AgeGrpTotal25_40', 'LanguageDesireNextYear': 'LangDesrNYrPython', 'OpSys': 'OpSystPrefrWind_MacOS', 'CompFreq': 'CompFreqcyYearly_Monthly', 'LanguageWorkedWith': 'PrgLangPrefrSQL_Sw_JS', 'ConvertedComp': 'SalOver50k'}, inplace = True)
df3


# In[199]:


df3.loc[['Afghanistan', 'Zambia', 'Nigeria', 'South Africa', 'Argentina'], ['AgeGrpTotal25_40', 'SalOver50k']]


# In[158]:


(cntry_grp.get_group('Japan')['ConvertedComp'] > 50000).sum()


# In[153]:


filr = (df2['Country'] == 'Canada') # & (df2['ConvertedComp'] > 400000) 
(df2.loc[filr]['ConvertedComp'] > 40000).sum()


# In[137]:


filr = (df2['Country'] == 'Japan') & (df2['Age'].between(25, 42)) 
(df2.loc[filr]['ConvertedComp'] > 50000).sum()


# In[50]:


filtt = df2['Country'] == 'Australia'
(df2.loc[filtt, 'OpSys'] == 'Windows').sum()


# In[81]:


firl =  df2['Country'] == 'India'
df2.loc[firl, ['LanguageWorkedWith']].apply(lambda x: x.isin(langs).sum())


# In[198]:


ful = df2['Country'] == 'Argentina'
df2.loc[ful, 'Age'].between(25,40).sum()


# In[17]:


df2['Age']#.between(25, 40).sum()

