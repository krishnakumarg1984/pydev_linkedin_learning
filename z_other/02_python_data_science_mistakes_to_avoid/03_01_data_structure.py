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

# create a set containing the types of pets in household #1,
# save in a variable
pets_house1 = {'hamster', 'bird', 'dog', 'cat', 'snake', 'bunny', 'guinuea pig',
               'horse', 'fish'}

if 'bunny' in pets_house1:
    print('bunny in house #1')
else:
    print('no bunny in house #1')

if 'chameleon' in pets_house1:
    print('chameleon in house #1')
else:
    print('no chameleon in house #1')

# create a list containing the things that have to be done in the order they should be done,
# save in a variable
to_do = ['check mail', 'deposit checks', 'pay rent', 'buy groceries', 'do meal prep',
         'do laundry']

# task to complete first
to_do[0]

# third task to complete
to_do[2]

# last task to complete
to_do[-1]


