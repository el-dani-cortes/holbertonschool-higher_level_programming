#!/usr/bin/python3
def uppercase(str):
    for i in str:
        i = ord(i)
        if i >= 97 and i < 123:
            i = i - 32
        chr(i)
        print("{:c}".format(i), end='')
    print()
