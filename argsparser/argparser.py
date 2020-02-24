#!/usr/bin/env python3

import argparse
import sys
import string 
from jproperties import Properties

parser = argparse.ArgumentParser(description="Replace text with env variables")
parser.add_argument("envfile",type=open)
parser.add_argument("infile",type=open)
parser.add_argument("outfile",type=open,nargs='?')
args = parser.parse_args()


def export(file_name,values,new_file_name="standart output"):

    t=""
    try:
        content=file_name.read()
        print("I've read content")
        t = string.Template(content).substitute(values)
        if new_file_name == "standart output":
           print(t)
        else:
            with open(new_file_name.name,"w+") as f:
                f.write(t)
        print("I've exported lines")
    except Exception:
        print("Unknown error")

def parser():
    values = Properties()
    try:
        values.load(args.envfile)
    except Exception:
        print("Occurred exception")
    if args.outfile:
        export(args.infile,values,args.outfile)
    else:
        export(file_name=args.infile,values=values)
    print("Success!")
    


if __name__=="__main__":
    if len(sys.argv) >= 2:
        parser()
    else:
        print("Call {} -h".format(argv[0]))

