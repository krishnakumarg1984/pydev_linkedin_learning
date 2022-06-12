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
import random


# +
def getWidth():
    """Generate width randomly (in feet) and return"""
    return random.randint(3, 11)


def getLength():
    """Get length (in feet) and return"""
    return random.randint(5, 16)


def rug_dim():
    """Select dimensions for rug (in feet) and display"""
    width = getWidth()
    length = getLength()
    print("width of rug:", width)
    print("length of rug:", length)


rug_dim()
# -
