#!/usr/bin/env python
# encoding: utf-8

import socket
import time

host = ''
port = 8008
bufsiz = 1024
addr = (host, port)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(addr)
sock.listen(5)
stop_chat = False
while True:
    print "waiting..."
    tcp_client, addr = sock.accept()
    print "connect from ",  addr
    while True:
        try:
            data = tcp_client.recv(bufsiz)
        except:
            tcp_client.close()
            break
        if not data:
            break
        TIMEFORMAT = "%Y-%m-%d %X"
        stime = time.strftime(TIMEFORMAT, time.localtime())
        res = "%s: %s" % (addr[0], data.encode('utf8'))
        tcp_client.send(res.encode('utf8'))
        print stime, ':', data.encode('utf8')
        stop_chat = (data == u"quit")
        if stop_chat:
            break


tcp_client.close()
sock.close()

