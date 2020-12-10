#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) < 2:
        print("0")
    elif len(argv) > 2:
        sum = 0
        for i in argv[1:]:
            sum = sum + int(i)
            print(sum)
