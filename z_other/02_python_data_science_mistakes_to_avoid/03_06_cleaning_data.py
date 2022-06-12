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

# import relevant libraries
import numpy as np
import pandas as pd

# create a variable named grades containing a numpy array that represents students' grades
# on a particular exam as percentages
grades = np.random.randint(50, 121, size=50)

# display grades
grades

# remove grade values higher than 100%:
# select grade values between 0% and 100% inclusive,
# reassign grades to that selection
grades = grades[(grades >= 0) & (grades <= 100)]

# display grades
grades


