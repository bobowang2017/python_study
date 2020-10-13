# -*- coding:UTF-8 -*-
'''
文件可将SSH服务端打开的某个端口的数据流量导向到指定的另一台服务器的端口上
例如：打开命令行输入以下代码：
rforward.py 192.168.209.121 -p 8080 -r 192.168.209.122:80 --user root --password
输入ssh密码后，控制台打印如下：
----------------------------控制台内容开始----------------------------------------
D:\Workspaces\python27\py_hacker\com\lyz\chapter2>rforward.py 192.168.209.121 -p 8080 -r 192.168.209.122:80 --user root --password
Enter SSH password:
Connecting to ssh host 192.168.209.121 ...
D:\Program Files\Python27\lib\site-packages\paramiko\client.py:779: UserWarning: Unknown ssh-rsa host key for 192.168.209.121: 3bc514e5b8ad5377141030149ea79649
  key.get_name(), hostname, hexlify(key.get_fingerprint()),
Now forwarding remote port 8080 to 192.168.209.122:80 ...
----------------------------控制台内容结束----------------------------------------
说明程序已经启动成功。
rforward.py 192.168.209.121 -p 8080 -r 192.168.209.122:80 --user root --password的作用是：
将访问192.168.209.121:8080的数据流量通过SSH隧道导向到192.168.209.122:80上，也就是说，打开浏览器访问http://192.168.209.121:8080会通过SSH隧道导向到http://192.168.209.122:80上。
这样，只要我们能够访问http://192.168.209.121:8080，不能直接访问http://192.168.209.122:80，通过这种方式，我们也能够访问http://192.168.209.122:80了
Created on 2017年12月19日
@author: liuyazhuang
'''

import getpass
import os
import socket
import select
import sys
import threading
from optparse import OptionParser

import paramiko


def handler(chan, host, port):
    sock = socket.socket()
    try:
        sock.connect((host, port))
    except Exception as e:
        print('Forwarding request to %s:%d failed: %r' % (host, port, e))
        return
    print('Connected!  Tunnel open %r -> %r -> %r' % (chan.origin_addr, chan.getpeername(), (host, port)))
    while True:
        r, w, x = select.select([sock, chan], [], [])
        if sock in r:
            data = sock.recv(1024)
            if len(data) == 0:
                break
            chan.send(data)
        if chan in r:
            data = chan.recv(1024)
            if len(data) == 0:
                break
            sock.send(data)
    chan.close()
    sock.close()


def reverse_forward_tunnel(server_port, remote_host, remote_port, transport):
    transport.request_port_forward('', server_port)
    while True:
        chan = transport.accept(1000)
        if chan is None:
            continue
        thr = threading.Thread(target=handler, args=(chan, remote_host, remote_port))
        thr.setDaemon(True)
        thr.start()


def main():
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.WarningPolicy())
    try:
        client.connect(hostname="10.175.1.155", port=22, username="root", password="start123@@")
    except Exception as e:
        print('*** Failed to connect to %s:%d: %r' % ("10.175.1.155", 22, e))
        sys.exit(1)
    print('*** Success to connect to %s:%d' % ("10.175.1.155", 22))
    try:
        reverse_forward_tunnel(6666, "10.176.139.10", 22, client.get_transport())
    except KeyboardInterrupt:
        print('C-c: Port forwarding stopped.')
        sys.exit(0)


if __name__ == '__main__':
    main()
