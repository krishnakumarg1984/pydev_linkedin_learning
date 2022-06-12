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

# Start by importing our libraries
# %matplotlib inline
from ggplot import *
import pandas as pd
import numpy as np

# Let's start w/ a scatterplot
ggplot(aes(x='carat', y='price'), data=diamonds) + geom_point()

# Now let's add a color
ggplot(aes(x='carat', y='price', color='clarity'), data=diamonds) + geom_point()

# Use color brewer for better options
# Start with a sequential color range
ggplot(aes(x='carat', y='price', color='clarity'), data=diamonds) + \
    geom_point() + \
    scale_color_brewer(type='seq', palette='Reds')

# Let's try a diverging color palette
ggplot(aes(x='carat', y='price', color='clarity'), data=diamonds) + \
    geom_point() + \
    scale_color_brewer(type='div', palette=2)

# Lastly, try a qualitative palette
ggplot(aes(x='carat', y='price', color='clarity'), data=diamonds) +\
    geom_point() +\
    scale_color_brewer(type='qual')

# ### *view more at [http://colorbrewer2.org/](http://colorbrewer2.org/)*
