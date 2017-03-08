#!/usr/bin/env python
# encoding: utf-8

import socket
port = 8008
host = 'localhost'
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto('aaabbb', (host,port))

