#!/usr/bin/env python3


class bunny:
    def __init__(self, n):
        self._n = n

    def __repr__(self):
        # return f"repr: The number of bunnies is {self._n} 🖖"
        # return f"repr: The number of bunnies is {self._n} {chr(128406)}"
        return f"repr: The number of bunnies is {self._n} \U0001f596"

    def __str__(self):
        return f"str: The number of bunnies is {self._n}"


# s = "Hello, World."
s = bunny(47)
print(repr(s))
print(s)  # will take the __str__ version
print(ascii(s))  # will use __repr__ but return the ascii equivalent
print(chr(128406))
print(ord("\U0001f596"))
