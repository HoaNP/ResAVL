#!/usr/bin/python3

import sys, subprocess

résultat = subprocess.run('ls *.py', shell=True, stdout=subprocess.PIPE)
liste_fichiers_ls = résultat.stdout

liste_fichiers = liste_fichiers_ls.splitlines()

for nom_fichier in liste_fichiers:
    try:
        entrée = open(nom_fichier,'r')
    except Exception as e:
        print(e.args)
        continue

    ligne = entrée.readline()
    if not ligne:
        continue
    print(nom_fichier,' ', ligne, end='')
    entrée.close()
