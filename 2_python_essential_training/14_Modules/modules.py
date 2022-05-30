#!/usr/bin/env python3
# https://docs.python.org/3.12/library/index.html
import datetime
import os
import random
import sys


def main():
    v = sys.version_info
    print("Python version {}.{}.{}".format(*v))
    p = sys.platform
    print(p)
    os_name = os.name
    print(os_name)
    # my_path_list = os.getenv("PATH")
    # print(my_path_list)
    # my_cwd = os.getcwd()
    # print(my_cwd)
    # my_random_number = os.urandom(25)  # no of bytes as arg
    # print(my_random_number.hex())
    # x = random.randint(1, 1000)
    # print(x)
    my_list = list(range(25))
    print(my_list)
    random.shuffle(my_list)
    print(my_list)
    now = datetime.datetime.now()
    print(now)
    print(
        now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond
    )


if __name__ == "__main__":
    main()
