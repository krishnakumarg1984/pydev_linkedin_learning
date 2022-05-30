#!/usr/bin/env python3
from math import pi


def main():
    seq = range(11)

    seq2 = [x * 2 for x in seq]  # list
    seq3 = [x for x in seq if x % 3 != 0]  # list
    seq4 = [(x, x**2) for x in seq if x % 2 != 0]  # list of tuples
    seq5 = [round(pi, i) for i in seq]  # list

    seq6 = {x: x**3 for x in seq}  # dictionary
    seq7 = {x for x in "superduper" if x not in "pd"}  # set

    print_list(seq)
    print_list(seq2)
    print_list(seq3)
    print_list(seq4)
    print_list(seq5)
    print(seq6)
    print_list(seq7)


def print_list(o):
    for x in o:
        # print(x, end=", ")
        print(x, end=" ")
    print()


if __name__ == "__main__":
    main()
