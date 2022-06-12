#!/usr/bin/env python3


class MyString(str):
    def __str__(self):
        return self[::-1]


s = MyString("Hello, World")
print(s)

print("Hello, World.".upper())
print("Hello, World.".swapcase())

print(
    """
Hello,
World.
""".swapcase()
)
