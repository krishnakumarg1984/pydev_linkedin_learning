#!/usr/bin/env python3
#############################################################################
# print("Hello, World.")
# def f1():
#     print("this is f1")
# f1()
# x = f1
# def f1():
#     def f2():
#         print("this is f2")
#
#     return f2
# x = f1()  # return value from 'f1' is the object that is 'f2'
# x()
# # f2()


def f1(f):
    def f2():
        print("This is before the function call")
        f()
        print("This is after the function call")

    return f2


@f1
def f3():
    print("this is f3")


# x = f1(f3)
# x()

# f3 = f1(f3)

f3()
