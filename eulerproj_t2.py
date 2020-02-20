#!/usr/bin/env python3
# This program counts the sum of even 
# Fibanacci's sequence numbers in range
import sys


def count(lim): 
    num1 = 1
    num2 = 2
    dig=num1+num2
    summa = 2

    while dig < lim:
        if dig%2 == 0:
            summa += dig
        num1 = num2
        num2 = dig
        dig = num1+num2
    
    print(str(summa))

if __name__ == "__main__":
    standart_limit = 4000000
    if len(sys.argv) == 2:
        try:
            limit = int(sys.argv[1])
            count(limit)
        except Exception:
            count(standart_limit)
    else:
        count(standart_limit)