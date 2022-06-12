#!/usr/bin/env python3
# base class
class Animal:
    def __init__(self, **kwargs):
        if "kind" in kwargs:
            self._kind = kwargs["kind"]
        if "name" in kwargs:
            self._name = kwargs["name"]
        if "sound" in kwargs:
            self._sound = kwargs["sound"]

    def kind(self, t=None):
        if t:
            self._kind = t
        try:
            return self._kind
        except AttributeError:
            return None

    def name(self, n=None):
        if n:
            self._name = n
        try:
            return self._name
        except AttributeError:
            return None

    def sound(self, s=None):
        if s:
            self._sound = s
        try:
            return self._sound
        except AttributeError:
            return None


# inherited class
class Duck(Animal):
    def __init__(self, **kwargs):
        self._kind = "duck"
        if "kind" in kwargs:
            del kwargs["kind"]
        super().__init__(**kwargs)


# inherited class
class Kitten(Animal):
    def __init__(self, **kwargs):
        self._kind = "kitten"
        if "kind" in kwargs:
            del kwargs["kind"]
        super().__init__(**kwargs)

    def kill(self, s):
        print(f"{self.name()} will now kill all {s}!")


def print_animal(o):
    if not isinstance(o, Animal):
        raise TypeError("print_animal(): requires an Animal")
    print(f'The {o.kind()} is named "{o.name()}" and says "{o.sound()}".')


def main():
    a0 = Kitten(name="fluffy", sound="rwar")
    a1 = Duck(name="donald", sound="quack")
    print_animal(a0)
    print_animal(a1)
    a0.kill("humans")
    # a1.kill("humans")


if __name__ == "__main__":
    main()
