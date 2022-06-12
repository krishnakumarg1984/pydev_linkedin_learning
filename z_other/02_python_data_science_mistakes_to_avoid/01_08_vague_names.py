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

# create a variable containing a numpy array that represents the temperatures
# (in fahrenheit) for 7 consecutive days in santa barbara, ca
temps_sb = np.array([72, 73, 77, 81, 79, 72, 68])

# create a variable containing a numpy array that represents the temperatures
# (in fahrenheit) for 7 consecutive days in memphis, tn
temps_mem = np.array([93, 91, 91, 91, 91, 88, 90])

# compute absolute differences between t1 data and t2 data
np.abs(temps_sb - temps_mem)
