#!/usr/bin/env python3


def main():
    # kitten()
    # kitten(5, 6, 7, 8)
    # kitten(15, 63, 92)
    # a = 18
    # a = [18]
    # print(f"In main: initially, a is {a}")
    # id_a = id(a)
    # print(f"In main: id of a is {id_a}")
    # b = a
    # b[0] = 3
    # id_b = id(b)
    # print(f"In main: id of b is {id_b}")
    # print(f"AFTER list assignment, a is {a}")
    # print(f"AFTER list assignment, b is {b}")
    # kitten_singlearg(a)
    x = kitten_noargs()
    print(type(x), x)


def kitten_singlearg(a):
    id_a = id(a)
    print(f"In kitten_singlearg (BEFORE local change): a is {a}")
    print(f"In kitten_singlearg (BEFORE local change): id of a is {id_a}")
    # a = 3
    a[0] = 3
    id_a = id(a)
    print(f"In kitten_singlearg (AFTER local change): id of a is {id_a}")
    print(f"In kitten_singlearg (AFTER local change): a is {a}")


def kitten_noargs():
    print("Meow.")
    # return "Meow."
    # return 42
    # return [42, 43, 44]
    return dict(x=42, y=43, z=44)


def kitten(a, b, c=0, d=-21):
    # print(f"Meow. {a}")
    print("Meow.")
    print(a, b, c, d)


if __name__ == "__main__":
    main()
