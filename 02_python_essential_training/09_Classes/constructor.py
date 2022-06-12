#!/usr/bin/env python3


class Animal:
    # def __init__(self, kind, name, sound):
    def __init__(self, **kwargs):
        self._kind = kwargs["kind"] if "kind" in kwargs else "default_kind"
        self._name = kwargs["name"] if "name" in kwargs else "default_name"
        self._sound = kwargs["sound"] if "sound" in kwargs else "default_sound"

    def kind(self):
        return self._kind

    def name(self):
        return self._name

    def sound(self):
        return self._sound


def print_animal(o):
    if not isinstance(o, Animal):
        raise kindError("print_animal(): requires an Animal")
    print(f"The {o.kind()} is named {o.name()} and says {o.sound()}.")


def main():
    # a0 = Animal("kitten", "fluffy", "rwar")
    a0 = Animal(kind="kitten", name="fluffy", sound="rwar")
    a1 = Animal(kind="duck", name="donald", sound="quack")
    print_animal(a0)
    print_animal(a1)
    print_animal(Animal(kind="velociraptor", name="veronica", sound="hello"))
    print_animal(Animal())


if __name__ == "__main__":
    main()
