#!/usr/bin/env python3
import sys


def main():
    try:
        # x = int("foo")
        x = 5 / 0
    except ValueError:
        print("I caught a ValueError")
    # except ZeroDivisionError:
    #     print("Don't divide by zero")
    except:
        print(f"Unknown error: {sys.exc_info()[1]}")
    else:
        print("Good job!")
        print(x)

    print("Execution continues here ...")


if __name__ == "__main__":
    main()
