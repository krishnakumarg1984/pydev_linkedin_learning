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

# Now let's build a quick plot (qplot)
qplot(x='price',data=diamonds)

# Create a Facets (trellis) for our chart
qplot(x='price',data=diamonds) + facet_wrap(x='clarity', y='cut')

# Let's organize these better into a grid
qplot(x='price',data=diamonds) + facet_grid(x='clarity', y='cut')

# Let's look at Anscombe's Quartet
aq=pd.read_csv('data/anscombes-quartet-hier.csv',header=[0,1],index_col=[0])
aq

aq.mean()
aq.var()

df=pd.read_csv('data/anscombes-quartet.csv',header=0,index_col=0)

ggplot(aes(x='x', y='y'), data=df)+geom_point()+facet_wrap('group')
