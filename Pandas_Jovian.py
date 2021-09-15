#!/usr/bin/env python
# coding: utf-8

# In[218]:


import numpy as np
import pandas as pd

# days = pd.Series(['Monday', 'Tuesday', 'Wednesday']) # If you simply leave it like this, then i t will return 0,1,2 on the leftmost column
# days = pd.Series(['Monday', 'Tuesday', 'Wednesday'],
#                  index = (1,2,4)) # if u include the index bracket as shown here then the leftmost column will take the content of 'index' on the leftmost colun
# print(days)

# Creating series with a numpy array

days_list = np.array(['Monday', 'Tuesday', 'Wednesday'])
numpy_days = pd.Series(days_list)
# print(numpy_days)

# Using strings as index

days_lists = pd.Series(['Monday', 'Tuesday', 'Wednesday'],
                     index = ['a', 'b', 'c'])
# print(days_lists)

# Create series from a dictionary

days1 = pd.Series({'a': 'Monday', 'b': 'Tuesday', 'c': 'Wednesday'})
#print(days1)

# DataFrame can be described as a table (2 dimensions) made up of many series
# with the same index. It holds data in rows and columns just like a spreadsheet.
# Series, dictionaries, lists, and other dataframes and 
# numpy arrays can be used to create new ones

# print(pd.DataFrame())

# Create a dataframe from a dictionary

df_dict = {'Country': ['Ghana', 'Kenya', 'Nigeria', 'Togo'],
           'Capital': ['Accra', 'Nairobi', 'Abuja', 'Lome'],
           'Population' : [10000, 8500, 35000, 12000],
           'Age': [60, 70, 80, 75]}
dfd = pd.DataFrame(df_dict)
# print(dfd)
# print(dfd.loc[0])

df_list = [['Ghana', 'Accra', 10000, 60],
           ['Kenya', 'Nairobi', 8500, 70],
           ['Nigeria', 'Abuja', 35000, 80],
           ['Togo', 'Lome', 12000, 75]]
dfl = pd.DataFrame(df_list, columns = ['Country', 'Capital', 'Population', 'Age'],
                  index = [2,3,4,5]) # If this is not given then the default begins with zero 0
                  
# print(dfl)
# print(dfd.loc[1])
# print(dfd.iloc[1])

# Pandas is typically used  for working in tabular data(similar to the data stored in a spreadsheet).
# Pandas provides helper functions to read data from various file formats like CSV, Excel spreadsheet, 
# HTML tables, JSON, SQL and more. Lets download a file italy-covid-daywise.txt which contains daywise
# Covid-19 data for Italy in the following formats

from urllib.request import urlretrieve
# urlretrieve('https://hub.jovian.ml/wp-content/uploads/2020/09/italy-covid-daywise.csv', 
#             'italy-covid-daywise.csv')

covid_df = pd.read_csv('italy-covid-daywise.csv')

# Data from the file is read and stored in a DataFrame object - one of the core data structures in
# Pandas for storing and working with tabular data. We typically use _df suffix in the 
# variable names for dataframes

# print(type(covid_df))
# covid_df

# print(covid_df.info())

# For the numeric columns, you can view some statistical information like mean, standard deviation
# minimum/maximum values and number of non-empty values using  .describe method

# covid_df.describe()

# The columns property contains the list of columns within the data frame
# covid_df.columns

# You can also retrieve the number of rows and columns in
# the datafram using the .shape method
# covid_df.shape

# Pandas format is similar to 👇

covid_data_dict = {
    'date': ['2020-08-30', '2020-08-31', '2020-09-01', '2020-09-02', '2020-06-04'],
    'new_cases': [1444, 1365, 996, 975, 1326],
    'new_deaths': [1, 4, 6, 8, 6],
    'new_tests': [53541, 42583, 54395, None, None]
    
}

# print(covid_data_dict['new_cases'])
# print(covid_df['new_cases'])
# covid_df['new_cases'][246]
# covid_df['new_cases'][240]

# covid_df.at[246, 'new_cases']
# covid_df.at[240, 'new_cases']

# covid_df['new_cases'] is same as
covid_df.new_cases

# Further, you can also pass a list of columns within the indexing notation[]
# to access a subset of the data frame with just the given columns

cases_df = covid_df[['date', 'new_cases']]
# print(cases_df)

# changing any values inside cases_df or covid_df will also change
# the respective values in the other.
# Sometimes you might need a full copy of the data frame, in which case
# you can use the copy method

covid_df_copy = covid_df.copy

# To access a specific row of data, Pandas provides the
# .loc method.

# print(covid_df.loc[243])
# type((covid_df.loc[243]))

# To view the first or last few rows of data, we can use
# the .head and .tail methods

covid_df.head(5)
# covid_df.tail(5)

covid_df.at[0, 'new_tests']

# The distinction btw 0 and nan is subtle but important.
# 0 means there was 0 case, none; nan: not given or reported at all
# We can find the first index that doesnt contain a NaN value
# using first_valid_index method of a Series

# print(covid_df.new_tests.first_valid_index())
# print(covid_df.loc[111])
# print(covid_df.loc[108:113])

# The .sample method can be used to retrieve a random sample
# of rows from the data frame.

covid_df.sample(6)

# Analyzing Data from data frames

# Q1: What is the total number of reported cases and deaths related to 
# Covid in Italy

total_cases = covid_df.new_cases.sum() # alternatively, covid_df['new_cases'].sum
total_deaths = covid_df.new_deaths.sum()
# print(f'The total number of reported cases is {total_cases}\nThe total number of reported deaths is {total_deaths}')

# Q2: What is the overall death rate(ratio of reported deaths to reported cases)

death_rate = covid_df.new_deaths.sum() / covid_df.new_cases.sum()
# print('The overall reported death rate in Italy is {:.2f}%'.format(death_rate))

# Q3: What is the overall number of tests conducted? A total of 935310 tests were conducted
# before daily numbers were reported
initial_tests = 935310
total_tests = initial_tests + covid_df.new_tests.sum()

# print(f'Overall number of tests conducted is {total_tests}')

# Q4: What fraction of test returned a positive result

positive_rate = total_cases / total_tests
# print('{:.3f}% of tests in Italy led to a positive diagnosis.'.format(positive_rate))


# QUERYING AND SORTING ROWS

# Lets say we want to look at the days which had more than
# 1000 reported cases. We can use a boolean expression to
# check which rows satisfy this criterion.

high_new_cases = covid_df.new_cases > 1000
# print(high_new_cases)

# print(covid_df[high_new_cases])
# print(covid_df[high_new_cases]['date']) # If you want to get the dates whose new cases are greater than 1000

# We can write this on a single line by passing the boolean
# expression as an index to the data frame

# high_cases_df = covid_df[covid_df.new_cases > 1000 ]
# high_cases_df

# The data frame contains 72 rows, but only the first 5 and the last 5
# rows are displayed byt default with Jupyter, for brevity.
# To view all the rows, we can modify some display options

# from IPython.display import display
# with pd.option_context('display.max_rows', 100):
#     display(covid_df[covid_df.new_cases > 1000])
    
# We can also formulate more complex queries that involve multiple columns.
# As an example, lets try to determine the days when the ratio
# of cases reported to tests conducted is higher than the overall
# positive_rate

# above_1k = covid_df.new_cases > 1000
# print(above_1k)
# high_cov = covid_df[above_1k]['date'] # or simply .date (this is without the quotation marks)
# print(high_cov)

cases_tests_rate = covid_df.new_cases.sum() / covid_df.new_tests.sum()
# print('The ratio of cases reported to tests conducted is {:.4f}%'.format(cases_tests_rate))

high_ratio_df = covid_df.new_cases / covid_df.new_tests > positive_rate
# print(high_ratio_df)
# print(covid_df[high_ratio_df])

covid_df.new_cases / covid_df.new_tests # This creates a new series.. the daily positive rate or element wise division 

# Further, we can use this series to add a new column to the data frame.

covid_df['positive_rate'] = covid_df.new_cases / covid_df.new_tests
#print(covid_df)

# We can remove the positive_rate column using the drop method

covid_df.drop(columns = ['positive_rate'], inplace = True)
# print(covid_df)
# From the above, when inplace = True, the data is modified in place, which means
# it will return nothing and the dataframe is now updated. 
# When inplace = False, which is the default, then the operation
# is performed and it returns a copy of the object. You 
# then need to save it to something.

# SORTING ROWS USING COLUMN VALUES

# The rows can also be sorted by a specific column using .sort_values.
# Lets sort to identify the days with with the highest number of cases, 
# then chain it with the head method to get the 10 days with the most cases

covid_df.sort_values('new_cases', ascending = False).head(10)

# From the result,it looks like the last weeks of March had the highest number
# of daily cases.
# Lets compare this to the days where the highest number of deaths were recorded

covid_df.sort_values('new_deaths', ascending = False).head(10)

# Days with the least number of cases

covid_df.sort_values('new_cases').head(10)

covid_df.date = pd.to_datetime(covid_df.date)
covid_df.date

covid_df['year'] = pd.DatetimeIndex(covid_df.date).year
covid_df['month'] = pd.DatetimeIndex(covid_df.date).month
covid_df['day'] = pd.DatetimeIndex(covid_df.date).day
covid_df['weekday'] = pd.DatetimeIndex(covid_df.date).weekday

covid_df_may = covid_df[covid_df.month == 5]
# print(covid_df_may.new_cases.sum())
# print(covid_df_may.new_deaths.sum())
# print(covid_df_may.new_tests.sum())

covid_df_may_metrics = covid_df_may[['new_cases', 'new_deaths', 'new_tests']]
covid_df_may_metrics

covid_df_totals = covid_df_may_metrics.sum()
covid_df_totals = covid_df[covid_df.month == 5][['new_cases', 'new_deaths', 'new_tests']].sum()
covid_df_totals

# covid_df_sunday = covid_df[covid_df.weekday == 0]
# covid_df_sunday_high = covid_df_sunday.new_cases > 1000
# covid_df_sunday_high
# # highest = covid_df_sunday[covid_df_sunday_high]
# # highest

covid_df_sunday = covid_df[covid_df.weekday == 6].new_cases.mean()
#covid_df_sun_nc_sum = covid_df_sunday.new_cases.mean()
#print(covid_df_sunday)

# daily_avg = covid_df.new_cases.mean()
# daily_avg

# groupby

monthly_groups = covid_df.groupby('month')[['new_cases', 'new_deaths', 'new_tests']].sum()
monthly_groups

weekday_avg_groups = covid_df.groupby('weekday')[['new_cases', 'new_deaths', 'new_tests']].mean()
weekday_avg_groups

# cumsum or cummean or max is the aggregation to that particular point: the previous values added up to that point

covid_df['total_cases'] = covid_df.new_cases.cumsum()
covid_df['total_deaths'] = covid_df.new_deaths.cumsum()
covid_df['total_tests'] = covid_df.new_tests.cumsum() + initial_tests # initial_tests is the value given by the govt that didnt reflect on the dataset

covid_df

urlretrieve('https://hub.jovian.ml/wp-content/uploads/2020/09/locations.csv', 'locations.csv')

locations_df = pd.read_csv('locations.csv')
locations_df

locations_df[locations_df.location == 'Italy']

covid_df['location'] = 'Italy'

merged_df = covid_df.merge(locations_df, on = 'location')
merged_df

# monthly_groups.new_cases.plot(kind = 'bar')
# monthly_groups.new_deaths.plot(kind = 'bar')
# monthly_groups.new_tests.plot(kind = 'bar')

urlretrieve('https://raw.githubusercontent.com/WalePhenomenon/climate_change/master/fuel_ferc1.csv', 'fuel_record')

fuel_record_df = pd.read_csv('fuel_record')
fuel_record_df

#fuel_record_df.fuel_cost_per_unit_delivered.describe()
fuel_record_df.isnull()

