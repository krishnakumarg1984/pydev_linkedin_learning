#!/usr/bin/env python3
import platform


def main():
    message()


def message():
    # print("This is python version {}".format(platform.python_version()))
    print(f"This is python version {platform.python_version()}")
    print("Line 2")
    # if True:  # this is a comment
    #     print("In the block")  # this is another comment
    # else:
    #     print("Not in the block")


if __name__ == "__main__":
    main()
