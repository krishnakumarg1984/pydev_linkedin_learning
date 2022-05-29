#!/usr/bin/env python3


class Duck:
    sound = "Quaaack!"
    walking = "Walking like a duck."

    def quack(self):
        # print("Quaaack!")
        print(self.sound)

    def walk(self):
        # print("Walks like a duck.")
        print(self.walking)


def main():
    donald = Duck()
    donald.quack()
    donald.walk()


if __name__ == "__main__":
    main()
