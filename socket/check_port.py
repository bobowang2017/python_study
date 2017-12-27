# -*- coding: utf-8 -*-
import socket
import sys


def out_print(str):
    print('*'*40)
    print('*' + ' '*10 +str)
    print('*'*40)


def is_port_use(port):
    sk = socket.socket()
    try:
        if sk.connect_ex(('localhost', port)) != 0:
            out_print('port: ' + str(port) + 'is not used')
        else:
            out_print('port: ' + str(port) + ' is used')
    finally:
        sk.close()


if __name__ == '__main__':
    if len(sys.argv) < 2:
        out_print('input the port number!')
    else:
        is_port_use(int(sys.argv[1]))
