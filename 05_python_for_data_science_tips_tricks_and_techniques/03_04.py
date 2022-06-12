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

# Let's start w/ a scatterplot
ggplot(mpg, aes(x='cty', y='hwy')) + geom_point()

# Let's add a title
ggplot(mpg, aes(x='cty', y='hwy')) + geom_point() + \
    ggtitle("City vs. Highway Miles per Gallon")

# Now let's add some custom labels
ggplot(mpg, aes(x='cty', y='hwy')) + geom_point() + ggtitle("City vs. Highway Miles per Gallon") + \
    xlab("City MPG (Miles per Gallon)") + \
    ylab("Highway MPG (Miles per Gallon)")

# Color might help here
ggplot(mpg, aes(x='cty', y='hwy', color='class')) + geom_point() + ggtitle("City vs. Highway Miles per Gallon") + \
    xlab("City MPG (Miles per Gallon)") + \
    ylab("Highway MPG (Miles per Gallon)") + \
    scale_color_brewer(type='qual')

# How about splitting these out?
ggplot(mpg, aes(x='cty', y='hwy', color='class')) + geom_point() + ggtitle("City vs. Highway Miles per Gallon") + \
    xlab("City MPG (Miles per Gallon)") + \
    ylab("Highway MPG (Miles per Gallon)") + \
    scale_color_brewer(type='qual') + \
    facet_wrap(x='year',y='cyl')


