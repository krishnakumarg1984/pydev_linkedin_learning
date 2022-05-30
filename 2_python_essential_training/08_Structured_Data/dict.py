#!/usr/bin/env python3


def main():
    animals = dict(
        kitten="meow",
        puppy="ruff!",
        lion="grrr",
        giraffe="I am a giraffe!",
        dragon="rawr",
    )
    # animals = {
    #     "kitten": "meow",
    #     "puppy": "ruff!",
    #     "lion": "grrr",
    #     "giraffe": "I am a giraffe!",
    #     "dragon": "rawr",
    # }
    # print_dict(animals)
    # print("")
    # for k in animals.keys():
    #     print(k)
    # for v in animals.values():
    #     print(v)
    animals["lion"] = "I am a Lion"
    animals["monkey"] = "haha"
    # print(animals["lion"])
    print("lion" in animals)
    print("squirrel" not in animals)
    print("found lion!" if "lion" in animals else "No lion!")
    print("found lion!" if "godzilla" in animals else "No lion!")
    # print(animals["godzilla"])
    print(animals.get("godzilla"))
    # print_dict(animals)


def print_dict(o):
    for k, v in o.items():
        print(f"{k} {v}")
    # for x in o:
    #     print(f"{x}: {o[x]}")


if __name__ == "__main__":
    main()
