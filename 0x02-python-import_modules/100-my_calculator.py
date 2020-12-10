#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv, exit
    arguments = len(argv)
    if arguments != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(argv[1])
        operator = argv[2]
        b = int(argv[3])
        result = 0
        if operator == "+":
            result = add(a, b)
        elif operator == "-":
            result = sub(a, b)
        elif operator == "*":
            result = mul(a, b)
        elif operator == "/":
            result = div(a, b)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        print("{0:d} {1:s} {2:d} = {3:d}".format(a, operator, b, result))
        exit(0)
