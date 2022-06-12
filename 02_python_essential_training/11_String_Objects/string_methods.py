#!/usr/bin/env python3
# https://docs.python.org/3/library/stdtypes.html#string-methods
# print("Hello, World straße".upper())
print("Hello, World straße".capitalize())
# print("Hello, World straße".title())
# print("Hello, World straße".swapcase())
# print("Hello, World straße".lower())
# print("Hello, World straße".casefold())

s1 = "Hello, World"
s2 = s1.upper()
s3 = "This is another string"
print(id(s1))
print(id(s2))
print(s1 + " " + s3)
s4 = "This string" " that string"
print(s4)
