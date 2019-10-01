#!/usr/bin/python3

import re,sys

try:
    entree = open("exo12.py","rb")
    sortie = open("exo12.py_inverse","bw")
except Exception as e:
    print(e.args)
    sys.exit(1)

while 1:
    caractere = entree.read(1)
    if not caractere:
        break
    # rep_binaire = bin(caractere[0])[2:]
    rep_binaire = "{0:0{1}b}".format(caractere[0],8)
    rep_inverse = rep_binaire[:3]+rep_binaire[4]+rep_binaire[3]+rep_binaire[5:]
    print(rep_binaire,'->',rep_inverse)
    caractere_inverse = bytes([int(rep_inverse,2)])
    sortie.write(caractere_inverse)
entree.close()
sortie.close()
