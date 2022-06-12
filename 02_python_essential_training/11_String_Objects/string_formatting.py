#!/usr/bin/env python3
# https://docs.python.org/3/library/string.html#format-string-syntax

x = 42
y = 73
# print("The number(s): {}, {}".format(x, y))
# print("The number(s): {xx}, {bb}".format(xx=x, bb=y))
print("The number(s): {bb}, {xx}".format(xx=x, bb=y))
print("The number(s): {0}, {1}".format(x, y))
print("The number(s): {1}, {0}, {1}".format(x, y))
print("The number(s): {0:<5}, {1:>05}".format(x, y))
print("The number(s): {0:<5}, {1:>+5}".format(x, y))
print("The number(s): {0:<5}, {1:+05}".format(x, y))

# a = 42 * 747
a = 42 * 747 * 1000
# print("The number(s): {:,}".format(a))
print("The number(s): {:,}".format(a).replace(",", "."))
print("The number(s): {:f}".format(a))
print("The number(s): {:,f}".format(a))

b = 42.07 * 747.41 * 997.67
print("The number(s): {:,.3f}".format(b))
c = 42
print("The number(s): {:x}".format(c))
print("The number(s): {:X}".format(c))
print("The number(s): {:b}".format(c))
print("The number(s): {:o}".format(c))
