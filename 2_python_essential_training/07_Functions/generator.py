#!/usr/bin/env python3


def main():
    # for i in range(25):
    # for i in inclusive_range(25):
    # for i in inclusive_range(5, 25):
    for i in inclusive_range(5, 25, 10):
        # for i in inclusive_range():
        # for i in inclusive_range(1, 2, 3, 4):
        # for i in range(25):
        print(i, end=" ")
    print()


def inclusive_range(*args):
    numargs = len(args)
    start = 0
    step = 1

    # initialize parameters
    if numargs < 1:
        raise TypeError(f"expected at least 1 argument, got {numargs}")
    elif numargs == 1:
        stop = args[0]
    elif numargs == 2:
        (start, stop) = args
    elif numargs == 3:
        (start, stop, step) = args
    else:
        raise TypeError(f"expected at most 3 arguments, got {numargs}")

    # generator
    i = start
    while i <= stop:
        yield i
        i += step


if __name__ == "__main__":
    main()
