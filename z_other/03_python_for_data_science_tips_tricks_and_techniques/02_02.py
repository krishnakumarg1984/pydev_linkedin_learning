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

df = pd.read_csv('data/MonthlyProductSales.csv')

df

# show first 10 rows
df.head(n=10)

# show last 10 rows
df.tail(n=10)

# show summary stats of the sales column
df.describe()

df.info()

# +
# return as a series
s = df['Product Name']

# get count of values
s.value_counts(dropna=False)
# -


