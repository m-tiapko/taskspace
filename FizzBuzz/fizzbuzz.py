#!/usr/bin/env python3


def divider(a=3,b=5,until=100):
    output=""
    for i in range(1,until+1):
        output="FizzBuzz" if i%(a*b) == 0 else \
            ("Fizz" if i%a == 0 \
                else ("Buzz" if i%b== 0 \
                    else str(i)))
        print(output,end=" ")

if __name__ == "__main__":
    divider()