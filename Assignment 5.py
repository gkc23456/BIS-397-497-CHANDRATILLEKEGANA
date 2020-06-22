# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 20:19:49 2020

author: Troy Adair
"""

import pandas as pd

# Read in csv file from first script
YT = pd.read_csv("Yellow_Saved.csv")

# Look at DataFrame
YT

# DataFrames are constructed of columns called Series. To see columns:
YT.columns

# Looking at dtypes
YT.dtypes

# pickup, dropoff, and duration were stored as strings!!!!
# Let's convert them back to datetimes
YT['pickup'] = pd.to_datetime(YT['pickup'],
                              infer_datetime_format=True)


YT['dropoff'] = pd.to_datetime(YT['dropoff'],
                              infer_datetime_format=True)

YT['duration'] = pd.to_datetime(YT['duration'],
                              infer_datetime_format=True)


YT[['pickup','dropoff','duration']].head()

# Let's look for other problematic values

YT.describe()

YT.columns

pd.set_option('display.float_format', lambda x: '%.2f' % x)

YT['passenger_count'].describe()

YT['trip_distance'].describe()

YT['fare_amount'].describe()

YT['extra'].describe()

YT['mta_tax'].describe()

YT['tolls_amount'].describe()

YT['improvement_surcharge'].describe()

YT['total_amount'].describe()

# Rules we agree to
# trip_distance <= 100 (already implemented)
# delete any rows where passengers = 0 

YT['passenger_count'].describe()

YT['valid2'] = YT['passenger_count'] > 0

YT[['passenger_count','valid2']].head()

YT['passenger_count'].describe()

YT = YT[YT.valid2 == True]

YT['passenger_count'].describe()

# delete trip distance = 0

YT['trip_distance'].describe()

YT['valid1'] = YT['trip_distance'] > 0

YT[['trip_distance','valid1']].head()

YT['trip_distance'].describe()

YT = YT[YT.valid1 == True]

YT['trip_distance'].describe()

# fare amount make greater than zero, lt 1,000

YT['fare_amount'].describe()

YT['valid3'] = YT['fare_amount'] > 0

YT[['fare_amount','valid3']].head()

YT['fare_amount'].describe()

YT = YT[YT.valid3 == True]

YT['fare_amount'].describe()


YT['valid4'] = YT['fare_amount'] < 1000

YT[['fare_amount','valid4']].head()

YT['fare_amount'].describe()

YT = YT[YT.valid4 == True]

YT['fare_amount'].describe()

# make "extra" >= 0

YT['extra'].describe()

YT['valid5'] = YT['extra'] > 0

YT[['extra','valid5']].head()

YT['extra'].describe()

YT = YT[YT.valid5 == True]

YT['extra'].describe()

YT.to_csv('YT_curated.csv', index = False)

