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

import csv

MonthlySales = []

with open('data/MonthlySales.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        MonthlySales.append(row)

for a in MonthlySales:
    print a

#print keys
for a in MonthlySales:
    print a.keys()

#print keys and values
for a in MonthlySales:
    for key, value in a.items():
        print key + ": ", value
    print '\n'


