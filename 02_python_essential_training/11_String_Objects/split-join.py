#!/usr/bin/env python3

s = """This is a      long string
with a                    bunch of words                          in
it.
"""
# print(s)
# print(s.split())
# print(s.split("i"))
mylist = s.split()
s2 = ":".join(mylist)
print(s2)
s3 = " ~~ ".join(mylist)
print(s3)
