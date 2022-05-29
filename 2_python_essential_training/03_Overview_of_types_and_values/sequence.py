#!/usr/bin/env python3
# x = [1, 2, 3, 4, 5]
# x = (1, 2, 3, 4, 5)
# x[2] = 42
# x[4] = 42
# x = range(10)
# x = range(5, 50, 5)
x = list(range(5, 50, 5))
x[2] = 42
for i in x:
    # print("i is {}".format(i))
    print(f"i is {i}")

x = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}
x["three"] = 42
for k, v in x.items():
    print(f"key: {k}, value: {v}")
