#!/usr/bin/python3

import os, socket, sys

list_service = [('smtp.unilim.fr',25),('imap.unilim.fr',995)]

for a_service in list_service:
	(server_name, server_port) = a_service
	server_add = socket.gethostbyname(server_name)
	my_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	try:
		my_socket.connect((server_add,server_port))
	except Exception as e:
		print("Connection problem", e.args)
		continue
	line = my_socket.recv(1024)
	if line:
		print("Banniere: ", line)
	my_socket.close()
