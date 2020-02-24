#!/usr/bin/env python3

import argparse
import sys

parser = argparse.ArgumentParser(description="This program calculate factorial of the number")

parser.add_argument("x",type=int, help="first argument")
parser.add_argument("y",type=int, help="second argument")
parser.add_argument("-a","--add", default=0, help="add two arguments",action="count")
parser.add_argument("-s","--sub", default=0, help="substitute one argument by another",action="count")
parser.add_argument("-m","--mult", default=0, help="add two arguments",action="count")
parser.add_argument("-d","--div", default=0, help="divide argument",action="count")
if len(sys.argv) > 1:
    args = parser.parse_args()

    if args.x and args.y:
        success = 0
        if args.add >= 1:
            answer = args.x + args.y
            print("{} + {} = {}".format(args.x,args.y,answer))
            success = 1
        if args.sub >= 1:
            answer = args.x - args.y
            print("{} - {} = {}".format(args.x,args.y,answer))
            success = 1
        if args.mult >=1:
            answer = args.x * args.y
            print("{} * {} = {}".format(args.x,args.y,answer))
            success = 1
        if args.div >=1:
            answer = args.x / args.y
            print("{} / {} = {}".format(args.x,args.y,answer))
            success = 1
        if success == 0:
            print("You must choose the option")
        