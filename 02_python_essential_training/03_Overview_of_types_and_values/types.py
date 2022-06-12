#!/usr/bin/env python3
from decimal import Decimal

# x = 7
# x = 7.0
# x = "7.0"
# x = True
# x = None
# print("x is {}".format(x))
# x = "seven"
# x = """
# seven
# """
# x = "seven".capitalize()
# x = "seven".upper()
# x = "seven {1} {0}".format(8, 9)
# x = "seven '{1:<9}' '{0:>9}'".format(8, 9)
# x = "seven '{1:<09}' '{0:>09}'".format(8, 123459)
# print("x is {}".format(x))

a = 8
b = 123459
x = f"seven {b:<09} {a:09}"
print(f"x is {x}")

# x = 7 * 3.14159
# x = 7 / 3
# x = 7 // 3
a = Decimal(".10")
b = Decimal(".30")
# x = 0.1 + 0.1 + 0.1 - 0.3
x = a + a + a - b
print(f"x is {x}")
print(type(x))

# All these are false
# x = 0
# x = None
# x = ""

x = "haha"
if x:
    print("True")
else:
    print("False")

# x = (1, 2, 3, 4, 5)
x = (1, "two", 3.0, [4, "four"], 5)
y = (1, "two", 3.0, [4, "four"], 5)
print(f"x is {x}")
print(type(x[1]))
print(type(x))
print(type(y))
print(id(x))
print(id(y))
print(id(x[0]))
print(id(y[0]))

if x[0] is y[0]:
    print("Yup.They are exactly the same objects in memory")
else:
    print("Nope.They are not the same objects in memory")

if x is y:
    print("Yup.They are exactly the same objects in memory")
else:
    print("Nope.They are not the same objects in memory")

# if type(x) == "tuple":
if isinstance(x, tuple):
    print("x is a tuple")
elif isinstance(x, list):
    print("x is a list")
else:
    print("Nope. x is neither a tuple nor a list")


y = [1, 2]
if isinstance(y, tuple):
    print("y is a tuple")
elif isinstance(y, list):
    print("y is a list")
else:
    print("Nope. y is neither a tuple nor a list")
