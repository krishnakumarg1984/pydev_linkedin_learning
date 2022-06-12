#!/usr/bin/env python3
# interesting:
# 1. and
# 2. or
# 3. not
# 4. in
# 5. not in
# 6. is
# 7. is not
# NO xor

a = True
b = False
x = ("bear", "bunny", "tree", "sky", "rain")
y = "bear"

# if a and b:
# if a or b:
# if not b:
# if y in x:
# if "leaf" in x:
# if "tree" in x:
if y is not x[1]:
    print("expression is true")
else:
    print("expression is false")

print(id(y), id(x[0]))
