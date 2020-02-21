#!/usr/bin/env python3

import sys


values={'USER':'Eliot',
'PASSWORD':'6edP@55word',
'USERINFO':'Eliot Alderson, La - scientist, 30 y.o'}


def export():
    export_lines=[]
    file_name = sys.argv[1]
    new_file_name = "upt_" + file_name
    try:
        with open(file_name,"r") as f:
            for i in f:
                export_lines += [i.format(**values)]
        print("I've read all lines")
        
        with open(new_file_name,"w") as f:
            for i in export_lines:
                f.write(i+'\n')
        print("I've exported lines")
    except Exception:
        print("Unknown error")




if __name__ == "__main__":
    if len(sys.argv) == 2:
        export()
        print("Success!")
        