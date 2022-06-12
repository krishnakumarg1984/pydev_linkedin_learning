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
import pandas as pd

# read grades.csv into a pandas dataframe 
# and save the dataframe in a variable named grades
grades = pd.read_csv('grades.csv')

# display grades
grades

grades.drop(columns={'student_id'})

# display grades
grades

# drop student_id column and update grades dataframe
grades = grades.drop(columns={'student_id'})

# display grades
grades


