#!/usr/bin/python3

import sys

try:
    desc_fichier = open("exo1.py","r")
except Exception as e:
    print(e.args)
    sys.exit(1)

compteur_lignes = 0

while 1:
    ligne = desc_fichier.readline()
    if not ligne:
        break
    compteur_lignes += 1

print('Nombre de lignes : ',compteur_lignes)
desc_fichier.close()
