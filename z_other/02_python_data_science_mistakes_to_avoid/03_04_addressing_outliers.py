# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.8
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# import relevant libraries and modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

airbnb = pd.read_csv('Airbnb_NYC_2019.csv')

# display first few rows of airbnb
airbnb.head()

# display distribution of listing prices
sns.distplot(airbnb['price']);

# +
# create subset of airbnb without outliers in price column
withoutPricesOver1000 = airbnb[airbnb['price'] <= 1000]

# display distribution of prices without outliers
sns.distplot(withoutPricesOver1000['price']);
# -


