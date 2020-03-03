#!/usr/bin/env python3
from fraction import Fraction


def helper():
    print("Instance: ", end=" ")
    print("4/5 * 43/90")


def calculate(obj1, obj2, sign):
    if sign == '+':
        result = obj1 + obj2
    elif sign == '-':
        result = obj1 - obj2
    elif sign == '*':
        result = obj1 * obj2
    elif sign == '/':
        result = obj1 / obj2
    else:
        result = "Unknown operation"
    return result


if __name__ == "__main__":
    dic_fractions = {}
    while True:
        command = input("Input the equation: ")

        if command == "exit":
            break
        elif command == "help":
            helper()
        else:
            lst = command.split()
            if len(lst) != 3:
                continue
            operation = lst[1]
            left = lst[0]
            right = lst[2]

            first = Fraction(left)
            second = Fraction(right)
            if (first is None) or (second is None):
                print("Invalid syntax in first digit")

            print("= {}".format(first, second, operation))
    exit(0)
else:
    exit(0)
