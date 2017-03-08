#!/usr/bin/env python
# encoding: utf-8

import socket
class TcpClient:

    host = "127.0.0.1"
    port = 8008
    bufsiz = 1024
    addr = (host, port)

    def __init__(self):
        self.client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(self.addr)
        while True:
            data = input(">")
            if not data:
                break
            self.client.send(data.encode('utf8'))
            print 'send to %s: %s' % (self.host, data)
            if data == "quit":
                break
            data=self.client.recv(self.bufsiz)
            if not data:
                break
            print 'recv form %s: %s' % (self.host, data.decode('utf8'))

if __name__ == "__main__":
    client = TcpClient()
