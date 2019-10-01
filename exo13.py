#!/usr/bin/python3

graine = 5
octet_courant = 8
a = 6364136223846793005
m = 2**64
b = 1442695040888963407
xn = (a*graine+b) % m

def gcl():
    global xn,octet_courant
    if (octet_courant == 8):
        xn = (a*xn+b)%m
        octet_courant= 0
    rep_hexa_gcl = "{0:0{1}X}".format(xn,16)
    rep_hexa_valeur = rep_hexa_gcl[octet_courant*2:octet_courant*2+2]
    octet_courant += 1
    print(rep_hexa_gcl," [",octet_courant,"] -> ",rep_hexa_valeur)
    return int(rep_hexa_valeur,16)

message = b"bonjour a tous"
chiffre = ''
for c in message:
    car_chiffre = gcl() ^ c
    chiffre += "{0:0{1}X}".format(car_chiffre,2)
print(chiffre)
xn = (a*graine+b) % m
octet_courant = 8
message = [int(chiffre[x:x+2],16) for x in range(0,len(chiffre),2)]
chiffre = b''
for c in message:
    car_chiffre = gcl() ^ c
    chiffre += bytes([car_chiffre])
print(chiffre)
