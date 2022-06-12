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

# yearly sales summary
df.groupby(df['Month of Order Date'].str[:4]).describe().reset_index().rename(columns={'Month of Order Date': 'Year of Order'})

# yearly product sales totals
df_export = df.groupby([df['Month of Order Date'].str[:4], 'Product Name']).sum().reset_index()
df_export.rename(columns={'Month of Order Date': 'Year of Order'})

# overall product sales totals
df.groupby('Product Name').sum().reset_index()


