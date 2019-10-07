#!/usr/bin/python3

import re,sys

try:
    entree = open("xxd.txt","rb")
except Exception as e:
    print(e.args)
    sys.exit(1)

compteur=0
while 1:
    bloc = entree.read(16)
    if not bloc:
        break
    print("{0:0{1}X}: ".format(compteur,8),end='')
    representation_ansi = b' '
    t = 0;
    for un_octet in bloc:
        print("{0:0{1}X}".format(un_octet,2),end='')
        if (t):
            t = 0
            print(" ",end='')
        else:
            t = 1
        if (un_octet>31) and (un_octet < 128):
            representation_ansi += bytes([un_octet])
        else:
            representation_ansi += b'.'
    compteur += len(bloc) 
    print(representation_ansi.decode('utf8'))
    if compteur >= 64:
        break

entree.close()
