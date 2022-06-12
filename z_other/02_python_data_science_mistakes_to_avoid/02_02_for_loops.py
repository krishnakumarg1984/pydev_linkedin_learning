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
# import relevant modules & libraries
import math

import numpy as np
import pandas as pd

# read grades dataset & save as pandas dataframe
grades = pd.read_csv("grades.csv")


# display first ten rows of grades

print(grades.iloc[:10])

# check for missing values in grade column
if grades["grade"].isnull().values.any():
    print("there are missing values")
else:
    print("there are no missing values")

# fill missing grades with zeros
grades["grade"] = grades["grade"].fillna(0)

# display first ten rows of grades
print(grades.iloc[:10])

# +
"""compute standard deviation for grades across all exams using for loop"""

# compute mean for grades across all exams
mean = grades["grade"].sum() / len(grades["grade"])
# initialize total, which will eventually be the sum of all squared distances to mean
total = 0
# iterate over grade values in grade column
for g in grades["grade"]:
    # each iteration, compute squared distance to mean, add to total
    total += (g - mean) ** 2
# compute variance, average squared distance to mean
variance = total / len(grades["grade"])
# compute standard deviation, square root of variance
standard_dev = math.sqrt(variance)

print(standard_dev)
# -

# compute standard deviation for grades across all exams using np.std
np.std(grades["grade"])

# +
"""compute mean grade for each exam using for loop"""

# initialize list where mean for each exam will be saved
exam_means = []
# iterate over distinct exams in exam column
for exam in grades["exam"].unique():
    # each iteration,
    # select subset containing grades for current exam,
    exam_grades = grades.loc[grades["exam"] == exam]["grade"]
    # compute mean grade for current exam,
    curr_mean = exam_grades.mean()
    # add current mean to exam_means
    exam_means.append(curr_mean)

print(exam_means)
# -

# compute mean grade for each exam using groupby function from pandas
print(grades.groupby("exam")["grade"].mean().values)
