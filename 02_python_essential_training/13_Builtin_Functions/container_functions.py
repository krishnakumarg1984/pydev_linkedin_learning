#!/usr/bin/env python3
# https://docs.python.org/3/library/functions.html


x = (1, 2, 3, 4, 5)
# y = x
# y = len(x)
# y = list(reversed(x))

# for i in reversed(x):
#     print(i)

# y = sum(x)
# y = sum(x, 10)
# y = max(x)
# y = min(x)

# x = (0, 0, 0, 0, 0)
# x = (0, 0, 0, 7, 0)
x = (9, 3, 5, 7, 4)
# y = any(x)
# y = all(x)

y = (6, 7, 8, 9, 1)

print(x)
print(y)

z = zip(x, y)  # returns an iterator

for a, b in z:
    print(f"{a} : {b}")

my_tuple = ("cat", "dog", "rabbit", "velociraptor")
for idx, val in enumerate(my_tuple):
    print(f"{idx}: {val}")
