#!/usr/bin/env python3


def main():
    # kitten("meow", "grrr", "purr")
    x = ("meow", "grrr", "purr", "hello", "world")
    kitten(*x)  # will pass a reference to x


# variable length argument list
def kitten(*args):
    if len(args):
        for s in args:
            print(s)
    else:
        print("Meow.")


if __name__ == "__main__":
    main()
