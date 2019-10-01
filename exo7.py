#!/usr/bin/python3

import socket

numero_port_serveur = 80 # identique à celui du client
adresse_serveur = socket.gethostbyname('www.unilim.fr')
ma_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # ou AF_INET6
ma_socket.connect((adresse_serveur,numero_port_serveur))
requete = b"""GET / HTTP/1.0
Host: www.unilim.fr

"""
ma_socket.sendall(requete)
while 1:
    ligne = ma_socket.recv(1000)
    if not ligne:
        break
    print(ligne)
ma_socket.close()
