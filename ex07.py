#!/usr/bin/python3
import sys, re

re_debut_titre = re.compile(r'<title>(.*)$', re.I)
re_fin_titre = re.compile(r'^(.*)</title>', re.I)
titre = ""
try:
    fichier = open("page.html", "r")
except Exception as e:
    print(e.args)
    sys.exit(1)
while 1:
    ligne = fichier.readline()  # .rstrip('\n')

    if not ligne:
        break
    ligne = ligne.rstrip('\n')
    resultat = re_debut_titre.search(ligne)
    if resultat:
        ligne = resultat.group(1)
        while 1:
            resultat = re_fin_titre.search(ligne)
            if resultat:
                titre += resultat.group(1)
                break
            titre += ligne
            ligne = fichier.readline().rstrip('\n')
            if not ligne:
                break
        break
print(titre)
