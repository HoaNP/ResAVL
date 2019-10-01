#!/usr/bin/python3

import sys

try:
    entrée = open("exo1.py","r")
    sortie = open("exo1.py_copie","w")
except Exception as e:
    print(e.args)
    sys.exit(1)

while 1:
    ligne = entrée.readline()
    if not ligne:
        break
    sortie.write(ligne)
    entrée.readline()

entrée.close()
sortie.close()
