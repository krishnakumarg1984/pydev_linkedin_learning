def hello(name):
    print(f"Hello {name}!")


hello("Nick")
hello("Sara")
hello("John")


def add_numbers(num1, num2):
    print(num1 + num2)


add_numbers(4, 8)
add_numbers(3, 7)


def dog_info(name, age):
    print(f"Hi! My name is {name} and I am {age} years old.")


dog_info("fido", 8)


def double(number):
    return number * 2


print(double(5))

new_number = double(5)
print(new_number)


def return_caps(my_str):
    return my_str.upper()


print(return_caps("namaskaram"))

names = ["nick", "jane", "sara"]

for name in names:
    print(return_caps(name))
