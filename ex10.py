#!/usr/bin/python3

import re, sys

seperator = re.compile(r"[ ,:;?\.-]+")
try:
    entree = open("ex10.py", "r")
except Exception as e:
    print(e.args)
    sys.exit(1)

while (1):
    line = entree.readline()
    if not line:
        break;

    line = line.rstrip('\n')
    line_word = seperator.split(line)
    print(line_word)

entree.close()


