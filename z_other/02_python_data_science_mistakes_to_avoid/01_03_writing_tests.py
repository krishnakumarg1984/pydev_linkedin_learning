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
import pandas as pd

# import numpy as np
# import relevant libraries
# import matplotlib.pyplot as plt

# read grades dataset, save as a pandas dataframe
grades = pd.read_csv("grades.csv")

# display first few rows of grades
grades.head()

# test for missing values in grades dataset
assert grades.isnull().sum().sum() == 0, "there are missing values"


def lowest_grade(student_id):
    """
    Find lowest grade across all exams for student with given student_id.
    Treat missing exam grades as zeros.
    """

    return grades.loc[grades["student_id"] == student_id]["grade"].fillna(0).min()


# lowest grade for student with student_id 1
lowest_grade(1)

# grades for student with student_id 1
grades.loc[grades["student_id"] == 1]
