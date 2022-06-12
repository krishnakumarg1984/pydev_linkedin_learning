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

df = pd.read_csv('data/MonthlyProductSales.csv',  encoding='cp1252')

# yearly product sales totals
df_export = df.groupby([df['Month of Order Date'].str[:4], 'Product Name']).sum().reset_index()
df_export = df_export.rename(columns={'Month of Order Date': 'Year of Order'})

# export to csv, check csv when finished
df_export.to_csv('data/output/YearlyProductSalesTotals.csv', header=True, index=False, encoding='utf-8')

# export to json, check json when finished
df_export.to_json('data/output/YearlyProductSalesTotals.json', orient='records')

# export to excel, check excel file when finished
df_export.to_excel('data/output/YearlyProductSalesTotals.xlsx', header=True, index=False)


