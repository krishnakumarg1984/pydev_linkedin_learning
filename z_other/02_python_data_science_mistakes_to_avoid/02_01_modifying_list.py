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
# initialize nums as a list containing 0,1,2,3,4,5
nums = [0, 1, 2, 3, 4, 5]
print(nums)


def is_even(n):
    """
    Takes in an integer n.
    Returns True if n is even; returns False otherwise.
    """
    return (n % 2) == 0


# call is_even to check whether 7 is even
is_even(7)

# call is_even to check whether 8 is even
is_even(8)

# use list comprehension to identify items from nums that are not even
# add them to a new list named not_even_nums
not_even_nums = [item for item in nums if not is_even(item)]

print(not_even_nums)

# use list comprehension to identify items from nums that are even
# add them to a new list named even_nums
even_nums = [item for item in nums if is_even(item)]

print(even_nums)
