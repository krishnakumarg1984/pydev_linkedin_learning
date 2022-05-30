#!/usr/bin/env python3


def main():
    # kitten(Buffy="meow", Zilla="grr", Angel="rawr")
    # x = dict(Buffy="meow", Zilla="grr", Angel="rawr")
    x = {"Buffy": "meow", "Zilla": "grr", "Angel": "rawr"}
    kitten(**x)


def kitten(**kwargs):
    if len(kwargs):
        for k, v in kwargs.items():
            print(f"Kitten {k} says {v}")
    else:
        print("Meow.")


if __name__ == "__main__":
    main()
