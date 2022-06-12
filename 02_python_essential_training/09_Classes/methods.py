#!/usr/bin/env python3


class Animal:
    def __init__(self, **kwargs):
        # python does not have private variables
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

    # special method known as 'magic' method. String representation of the object
    # https://docs.python.org/3/reference/datamodel.html#special-method-names
    def __str__(self):
        return f"The {self.kind()} is named '{self.name()}' and says '{self.sound()}'."


def main():
    a0 = Animal(kind="kitten", name="fluffy", sound="rwar")
    a1 = Animal(kind="duck", name="donald", sound="quack")
    # a0.sound("bark")
    print(a0)
    print(a1)


if __name__ == "__main__":
    main()
