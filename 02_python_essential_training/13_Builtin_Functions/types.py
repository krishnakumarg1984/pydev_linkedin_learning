#!/usr/bin/env python3
# https://docs.python.org/3/library/functions.html
# x = "47"
# y = int(x)  # is a constructor for the 'int' type. is not a function
# y = float(x)
# x = -47
# x = -47.3
# y = abs(x)

x = 47
# y = divmod(x, 3)
# y = x + 73j
y = complex(x, 73)


print(f"x is {type(x)}")
print(f"x is {x}")
print(f"y is {type(y)}")
print(f"y is {y}")
