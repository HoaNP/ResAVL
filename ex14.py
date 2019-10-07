#!/usr/bin/python3

import sys
base64 = [chr(x) for x in range(ord('A'),ord('A')+26)] + [chr(x) for x in range(ord('a'),ord('a')+26)]+ [chr(x) for x in range(ord('0'),ord('0')+10)]+ ['+', '/']
def binaire(c):
    rep_binaire = bin(ord(c))[2:]
    rep_binaire = '0'*(8-len(rep_binaire))+rep_binaire
    return rep_binaire
try:
    entree = open("exo12.py","rb")
    sortie = open("td1_exo12.py.base64","w")
except Exception as e:
    print (e.args)
    sys.exit(1)
while True:
    car1 = entree.read(1)
    if not car1:
        break
    rep_binaire = binaire(car1)
    sortie.write(base64[int('00'+rep_binaire[:6],2)])
    bits_restants = rep_binaire[6:]
    car2 = entree.read(1)
    if not car2:
        sortie.write(base64[int('00'+bits_restants+'0000',2)])
        sortie.write('==')
        break
    rep_binaire = bits_restants + binaire(car2)
    sortie.write(base64[int('00'+rep_binaire[:6],2)])
    bits_restants = rep_binaire[6:]
    car3 = entree.read(1)
    if not car3:
        sortie.write(base64[int('00'+bits_restants+'00',2)])
        sortie.write('=')
        break
    rep_binaire = bits_restants + binaire(car3)
    sortie.write(base64[int('00'+rep_binaire[:6],2)])
    sortie.write(base64[int('00'+rep_binaire[6:],2)])
    entree.close()
    sortie.close()