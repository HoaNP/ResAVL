#!/usr/bin/python3
import re
#re_decompose_url = re.compile(r'([^:]+)://([a-zA-Z0-9 \ . \ -]+)(?::( \ d+))?/(.*)$')
re_decompose_url_avec_port = re.compile(r'([^:]+)://([a-zA-Z0-9\.\-]+):(\ d+)/(.*)$')
re_decompose_url_sans_port = re.compile(r'([^:]+)://([a-zA-Z0-9\.\-]+)/(.*)$')
url1 = "http://mon-adresse:789/mon_rep/ma_ressource"
url2 = "http://mon-adresse/mon_rep/ma_ressource"
resultat = re_decompose_url_avec_port.search(url1)
if resultat:
    print ("avec port",resultat.groups())
resultat = re_decompose_url_sans_port.search(url1)
if resultat :
    print ("sans port",resultat.groups())