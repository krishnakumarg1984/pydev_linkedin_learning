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

# read grades.csv into a pandas dataframe 
# and save the dataframe in a variable named grades
grades = pd.read_csv('grades.csv')

# display grades
grades

# fill missing values (NaNs) in grade column of grades dataframe with zeros
grades['grade'] = grades['grade'].fillna(0)

# display grades
grades

# use a histogram to visualize distribution of students' exam grades
plt.hist(grades['grade']);


