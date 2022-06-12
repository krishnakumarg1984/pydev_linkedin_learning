# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.8
#   kernelspec:
#     display_name: Python 2
#     language: python
#     name: python2
# ---

import pandas as pd

df = pd.read_csv('data/MonthlySales.csv')

df

# +
import json
from pandas.io.json import json_normalize

with open('data/monthlySalesbyCategoryMultiple.json') as json_data:
    d = json.load(json_data)
# -

df = json_normalize(d['contents'], 'monthlySales', ['category', 'region'])

df

#reading parquet into panda dataframe
import pyarrow.parquet as pq

table = pq.read_table('data/MonthlyProductSales.parquet')

table.to_pandas()

# you need to install html5lib
# pip install html5lib
# reading data from a html site
df = pd.read_html('https://en.wikipedia.org/wiki/List_of_U.S._state_abbreviations')

# get part that has the states and abbreviations
df_usa = df[0]

# remove unnecessary rows and columns
final_df = df_usa.drop(df_usa.index[range(0,11)]).drop(df_usa.columns[range(10,15)], axis=1)

# rename columns
final_df.rename(columns={0: 'Region Name', 1: 'Region Status', 2: 'ISO', 3: 'ANSI_Letter', 4: 'ANSI_Code'
                         , 5: 'USPS', 6: 'USCG', 7: 'GPO', 8: 'AP', 9: 'Other Abbreviations'}, inplace=True)

# reset index of rows
final_df.reset_index(drop=True)


