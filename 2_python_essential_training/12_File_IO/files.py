#!/usr/bin/env python3


def main():
    # f = open("lines.txt")
    # f = open("lines.txt", "r")
    # f = open("lines.txt", "w") # 'w' is dangerous
    # f = open("lines.txt", "a")
    # f = open("lines.txt", "r+")
    # f = open("lines.txt", "a+")
    # f = open("lines.txt", "r+b")
    f = open("lines.txt", "r+t")  # defaults to text mode anyway
    for line in f:
        print(line.rstrip())


if __name__ == "__main__":
    main()
