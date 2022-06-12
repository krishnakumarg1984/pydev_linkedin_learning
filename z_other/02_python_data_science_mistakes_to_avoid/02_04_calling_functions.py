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
import math

# +
# save location of hospital as a tuple in a variable
hospital_loc = (28, 3)

# save location of school as a tuple in a variable
school_loc = (5, 1)

# save location of fire department as a tuple in a variable
fire_dept_loc = (17, 9)

def euclidean_dist(location1, location2):
    """Compute euclidean distance between location1 and location2 and return result"""
    x1, y1 = location1
    x2, y2 = location2
    return math.sqrt((x2 - x1)**2 + (y2 - y2)**2)

# compute euclidean distance between hospital and school
print(euclidean_dist(hospital_loc, school_loc))

# compute euclidean distance between school and fire department
print(euclidean_dist(school_loc, fire_dept_loc))

# compute euclidean distance between fire department and hospital
print(euclidean_dist(fire_dept_loc, hospital_loc))
# -


