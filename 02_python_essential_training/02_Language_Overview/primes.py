#!/usr/bin/env python3


def isprime(n):
    if n <= 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    return True


def list_primes():
    for number in range(100):
        if isprime(number):
            print(number, end=" ", flush=True)


list_primes()

num = 6
if isprime(num):
    print(f"{num} is prime")
else:
    print(f"{num} not prime")
