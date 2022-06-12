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

import requests
response = requests.get('https://api.github.com/repos/bsullins/data/contents/monthlySalesbyCategoryMultiple.json')

import json
resp_json = json.loads(response.text)

val = json.loads(resp_json['content'].decode('base64'))

from pprint import pprint as pp
pp(val)

# print the keys and values at the third level
for a in val['contents']:
    for b in a['monthlySales']:
        for key, value in b.items():
            print key + ": ", value

response = requests.get('https://api.github.com/repos/bsullins/data/contents/MonthlySales.csv')

response_json = json.loads(response.text)

csv_val = response_json['content'].decode('base64')

# using csv.DictReader needs a filestream so we're making an String IO and passing a unicode string in
# then reading the stream and adding each dictionary to the dictionary list
import csv
import io
csv_dict = csv.DictReader(io.StringIO(unicode(csv_val)))
dict_list = []
for a in csv_dict:
    dict_list.append(a)

for a in dict_list:
    print a

#print keys and values
for a in dict_list:
    for key, value in a.items():
        print key + ": ", value
    print '\n'


