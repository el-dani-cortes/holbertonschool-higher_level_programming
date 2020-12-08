#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= 97 and ord(i) < 123:
            c = ord(i) - 32
            print("{:c}".format(c), end='')
        else:
            print("{:s}".format(i), end='')
    print()
