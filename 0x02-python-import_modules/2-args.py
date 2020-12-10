#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    for arguments in argv:
        if len(argv) < 2:
            print("0 arguments.")
        elif len(argv) == 2:
            print("1 argument:")
            print("1:", argv[1])
            break
        elif len(argv) > 2:
            print("{0:d} arguments:".format(len(argv) - 1))
            n = 1
            for i in argv[1:]:
                print("{0:d}: {1:s}".format(n, i))
                n = n + 1
                break
