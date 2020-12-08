#!/usr/bin/python3
for i in range(1, 100):
    if i < 10:
        print("0{0:d},".format(i), end=' ')
    elif i < 89 and i // 10 != i % 10 and i // 10 < i % 10:
        print("{0:d},".format(i), end=' ')
    elif i == 89:
        print("{0:d}".format(i))
