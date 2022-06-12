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

# import libraries
# install ggplot in terminal: conda install -c conda-forge ggplot
# %matplotlib inline
from ggplot import *
import pandas as pd
import numpy as np

# Take a look at the diamonds data set
diamonds.head()

diamonds.tail()

# How big is the data set?
len(diamonds)

# Now let's build a quick plot (qplot)
qplot(x='price',data=diamonds)

qplot(x='cut',y='price', data=diamonds, geom='bar')

qplot(x='price',y='carat', data=diamonds, geom='line')

qplot(x='price',y='carat', data=diamonds, geom='jitter', color='cut')

# Create a separate line for each clarity
ggplot(diamonds, aes(x='price', color='clarity')) + \
    geom_density()


