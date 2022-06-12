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

# import relevant modules and libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# create a variable named grades containing a pandas dataframe 
# that consists of students' grade on a particular exam
grades_part1 = np.random.normal(70, 10, size=50)
grades_part2 = np.random.normal(0.7, 0.1, size=50)
g = np.append(grades_part1, grades_part2)
grades = pd.DataFrame({'SID': np.arange(100), 'grade': g})

# display first few rows of grades
grades.head()

# visualize distribution of grade values
plt.hist(grades['grade']);

# show unique values in grade column of grades dataframe
grades['grade'].unique()


