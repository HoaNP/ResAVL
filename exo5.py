#!/usr/bin/python3

import socket,re

motif_acces = re.compile(rb'^ACCESS:\s+([0-9a-zA-Z._\-+]+)@[A-Za-z.]+$')

masque_acces = '' # filtre les clients, ici aucun n'est filtre
numero_port_serveur = 6688 # identique à celui du client

ma_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # ou AF_INET6

# Permet de ne pas attendre pour réutiliser le numéro de port
ma_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

# Accroche le numéro de port à la socket
ma_socket.bind((masque_acces, numero_port_serveur))

# Configure la file d'attente
ma_socket.listen(socket.SOMAXCONN)

# L'accept renvoie une nouvelle socket
(nouvelle_connexion, tsap_depuis) = ma_socket.accept()
print ("Nouvelle connexion depuis ", tsap_depuis)
while 1:
    ligne = nouvelle_connexion.recv(1000) # au plus 1000
    if not ligne :
        break
    resultat = motif_acces.search(ligne)
    if resultat:
        print (b'Acces de :'+resultat.group(1))

nouvelle_connexion.close()
ma_socket.close()
