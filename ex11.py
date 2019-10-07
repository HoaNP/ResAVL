#!/usr/bin/python3
import sys
nom_fichier = 'xxd.txt'
try:
	f = open(nom_fichier,'rb')
except Exception as e:
	print(e.args)
	sys.exit(1)
décalage = 0

ligne = b''
while 1:
	if len(ligne) == 0:
		print('{0:0{1}x}'.format(décalage,4),': ',end='')
	car = f.read(1)
	if not car:
		break
	if (ord(car)<128) and (ord(car)>31):
		ligne += car
	else:
		ligne += b'.'
	print('{0:0{1}X} '.format(ord(car),2),end='')
	if len(ligne) == 16:
		print(' ',str(ligne,encoding='UTF-8'))
		ligne = b''
	décalage += 1

if len(ligne):
	print(''*(16-len(ligne)),end='')
	print(' ', str(ligne,encoding='UTF-8'))
f.close()