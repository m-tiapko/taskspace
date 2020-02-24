#!/usr/bin/env python3
import string
import sys


values={'USER':'Eliot',
'PASSWORD':'6edP@55word',
'USERINFO':'Eliot Alderson, La - scientist, 30 y.o'}


def export():
    file_name = sys.argv[1]
    new_file_name = "upt_" + file_name
    try:
        with open(file_name,"r") as f:
            content = f.read()
        print("I've read content")
        t = string.Template(content).substitute(values)
        with open(new_file_name,"w+") as f:
            f.write(str(t)+'\n')
        print("I've exported lines")
    except Exception:
        print("Unknown error")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        export()
        print("Success!")
        