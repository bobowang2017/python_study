# -*- coding: utf-8 -*-
import os

import sys


def out_print(str):
    print('*' * 40)
    print('*' + ' ' * 10 + str)
    print('*' * 40)


def kill_process_by_port(port_id):
    ret = os.popen("netstat -nao | findstr " + port_id)
    str_list = ret.read()
    print(str_list)
    if str_list == "":
        print('No process use port :' + port_id)
        return
    ret_list = str_list.split(' ')
    process_pid = ret_list[-1][:len(ret_list[-1]) - 2]
    print('Current process id is :' + process_pid)
    os.system("kill -9 " + process_pid)
    print('Kill process id :' + process_pid + 'successfully')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        out_print('input the port number!')
    else:
        kill_process_by_port(sys.argv[1])
