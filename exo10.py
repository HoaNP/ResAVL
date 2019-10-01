#!/usr/bin/python3

import re,sys

separateurs = re.compile(r"[ ,:;?!\.-]+")

try:
    entree = open("exo10.py","r")
except Exception as e:
    print(e.args)
    sys.exit(1)

dico_occurences = {}
while 1:
    ligne = entree.readline()
    if not ligne:
        break
    ligne = ligne.rstrip('\n')
    liste_mots = separateurs.split(ligne)
    for un_mot in liste_mots:
        if un_mot in dico_occurences:
            dico_occurences[un_mot] +=1 
        else:
            dico_occurences[un_mot] = 1
print(dico_occurences)
entree.close()
