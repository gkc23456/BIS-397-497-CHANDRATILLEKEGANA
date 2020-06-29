# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 16:52:37 2020

@author: chagan
"""

import pandas as pd
import numpy as np
import pickle

import matplotlib as mpl
import matplotlib.pyplot as plt

# Use pd.set_option to apply the format globally:
pd.set_option('display.float_format', lambda x: '%.5f' % x)

# To disable "SettingWithCopyWarning..."
pd.options.mode.chained_assignment = None  # default='warn'

# Read in csv file
cv = pd.read_csv("us-states.csv")

cv.dtypes
cv['state'].describe()

# Curate Data to only include Pennsylvania

cv['valid'] = cv['state'].str.match('Pennsylvania')

cv[['state','valid']].head()

cv = cv[cv.valid == True]

cv['state'].describe()

del cv['valid']
del cv['fips']

cv.head()

# Convert date column from object to datetime integer

cv['date1'] = pd.to_datetime(cv['date'],infer_datetime_format=True)

cv.dtypes

del cv['date']

cv.head()
cv.columns
cv.dtypes

# Adjusting death count for 4/21 (by -282) & 4/22 (by-297)

cv.loc[cv.date1 == '2020-04-21', "deaths"] = cv.deaths - 282
cv.loc[cv.date1 == '2020-04-22', "deaths"] = cv.deaths - 297

cv.loc[cv['date1'] == '2020-04-21']
cv.loc[cv['date1'] == '2020-04-22']

cv.head()
cv.columns
cv.dtypes

#tried to shorten date_time to help define the function but didn't work
#cv['Month_Date'] = cv.date1.map(lambda x: x.strftime('%m%d'))

#cv['adj_deaths'] = cv['deaths']-0

#following function kept giving me 'the truth value of a series is ambigous'. Therefore ended up
#using a different way to calculate adjusted deaths                     
#def ad (val):
       #if cv['date1'] == '2020-04-21':
            #return cv['adj.deaths'] == cv['deaths']-282
       #elif cv['date1'] == '2020-04-22':
            #return cv['adj.deaths'] == cv['deaths']-297
        #else:
            #return cv['adj.deaths'] == cv['deaths']


#cv['adj_deaths1'] = cv.apply(ad, axis=1)

# dump information to that file

#pickle.dump(cv, file)

# close the file
#file.close()


# Saving our altered data set

cv.to_csv('us-states_graph.csv', index = False)

# Reading the data
file = open('us-states_graph.csv', 'rb')

#cv = pickle.load(file)
# close the file
#file.close()

# Verifying that pickle kept the data types unchanged
cv

cv.dtypes

# Plotting death count

import matplotlib.ticker as ticker

#Trying to format date label. Couldn't get it to work

#df = pd.DataFrame(cv)

#x = df['date1']
#data = df['deaths']
#plt.bar(x,data)



#read data from csv
#data = pd.read_csv("us-states_graph.csv", usecols=['date1','deaths'], parse_dates=['date1'])
#set date as index
#data.set_index('date1',inplace=True)

#plot data
#fig, ax = plt.subplots(figsize=(20,10))
#ax.bar(data.index, data['deaths'])

#plt.title('Covid-19 Deaths in PA', color='black')
#plt.xlabel('Date')
#plt.ylabel('Deaths')

#set ticks every week
#ax.xaxis.set_major_locator(mdates.WeekdayLocator())
#set major ticks format
#ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))


data = pd.read_csv('us-states_graph.csv')


#data['date2'] = cv.date1.map(lambda x: x.strftime('%m%d'))
#data['date2'] = pd.to_datetime(data['date2'],infer_datetime_format=True)

plt.style.use('fivethirtyeight')
plt.figure(figsize=(20,10))

Date = data['date1']
Deaths = data['deaths']

plt.bar(Date, Deaths)
plt.title('Covid-19 Deaths in PA', color='black')
plt.xlabel('Date')
plt.ylabel('Deaths')
plt.grid(axis='y', alpha=1.0)
plt.xticks(Date[::15], rotation='vertical')

plt.tight_layout()
plt._show()
 



