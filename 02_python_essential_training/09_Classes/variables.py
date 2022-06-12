#!/usr/bin/env python3


class Animal:
    # BAD PRACTICE: Never put mutable variable as a class variable
    x = [1, 2, 3]  # class variable and is mutable
    y = "hello"  # immutable class variable

    def __init__(self, **kwargs):
        self._kind = kwargs["kind"] if "kind" in kwargs else "kitten"
        self._name = kwargs["name"] if "name" in kwargs else "fluffy"
        self._sound = kwargs["sound"] if "sound" in kwargs else "meow"

    def kind(self, t=None):
        if t:
            self._kind = t
        return self._kind

    def name(self, n=None):
        if n:
            self._name = n
        return self._name

    def sound(self, s=None):
        if s:
            self._sound = s
        return self._sound

    def __str__(self):
        return f'The {self.kind()} is named "{self.name()}" and says "{self.sound()}".'


def main():
    a0 = Animal(kind="kitten", name="fluffy", sound="rwar")
    a1 = Animal(kind="duck", name="donald", sound="quack")
    print(a0)
    print(a1)
    # a0._name = "Joe"
    # print(a0._name)
    # print(a1._name)
    print(a0.x)
    a1.x[0] = 7
    print(a1.x)
    print(a0.x)
    a1.y = "bye"
    print(a0.y)
    print(a1.y)


if __name__ == "__main__":
    main()
