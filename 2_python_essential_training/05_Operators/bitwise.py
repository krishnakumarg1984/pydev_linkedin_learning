#!/usr/bin/env python3

x = 0x0A

# y = 0x02
# y = 0x05
# y = 0x0F
# z = x & y
# z = x | y
# z = x ^ y

y = 0x01
# z = x << 1
# z = x >> 1

z = x ^ x

print(f"(hex) x is {x:02x}, y is {y:02x}, z is {z:02x}")
# print(f"(bin) x is {x:08b}, y is {y:08b}, z is {z:08b}")

print(f"(bin) x is {x:08b}")
print(f"(bin) y is {y:08b}")
print(f"(bin) z is {z:08b}")
