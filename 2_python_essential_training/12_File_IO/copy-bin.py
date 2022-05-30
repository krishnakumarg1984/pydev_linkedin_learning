#!/usr/bin/env python3


def main():
    infile = open("berlin.jpg", "rb")
    outfile = open("berlin-copy.jpg", "wb")
    while True:
        buf = infile.read(10240)  # 10kb (we don't know how big the file is)
        if buf:
            outfile.write(buf)
            print(".", end="", flush=True)
        else:
            break
    outfile.close()
    infile.close()
    print("\ndone.")


if __name__ == "__main__":
    main()
