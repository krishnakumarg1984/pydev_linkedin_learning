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

import json

# load json file from /data folder
with open('data/monthlySalesbyCategoryMultiple.json') as json_data:
    d = json.load(json_data)

# see what the dictionary looks like
from pprint import pprint as pp
pp(d)

# print keys at the top level
print d.keys()

# print keys at the second level
for a in d['contents']:
    print a.keys()

# print keys at the third level
for a in d['contents']:
    for b in a['monthlySales']:
        print b.keys()

# print the keys and values at the first level
for key, value in d.items():
    print key + ': ', pp(value)

# print the keys and values at the second level
for a in d['contents']:
    for key, value in a.items():
        print key + ': ', value    

# print the keys and values at the third level
for a in d['contents']:
    for b in a['monthlySales']:
        for key, value in b.items():
            print key + ": ", value


