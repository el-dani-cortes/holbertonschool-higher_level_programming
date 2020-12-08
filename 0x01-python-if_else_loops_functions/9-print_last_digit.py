#!/usr/bin/python3
def print_last_digit(number):
    number = abs(number)
    number = number % 10
    print("{0:d}".format(number), end='')
    return (number)
