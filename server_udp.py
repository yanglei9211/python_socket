#!/usr/bin/env python
# encoding: utf-8

import socket
port = 8008
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', port))
print "waiting..."
while True:
    data, addr = s.recvfrom(1024)
    print(data, addr)
