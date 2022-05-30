#!/usr/bin/env python3


def main():
    infile = open("lines.txt", "rt")  # 'rt' is the default
    outfile = open("lines-copy.txt", "wt")
    for line in infile:
        # the print function, I'm able to strip these line endings, and rewrite the line endings with the default line endings for this operating system, which print does by default, and that way, if my input file is from another operating system with different line endings, I'm actually serving to translate those line endings into the correct one for this operating system, so it's important to know that distinction.
        # print(line.rstrip(), file=outfile)
        outfile.writelines(line)
        print(".", end="", flush=True)
    outfile.close()
    infile.close()
    print("\ndone.")


if __name__ == "__main__":
    main()
