# coding: utf-8
import time

import paramiko
import re

# 设置主机列表
from supervisor.RedisClient import redis_cli

host = {'ip': '47.105.104.233', 'port': 22, 'username': 'root', 'password': '1q2w3e4r!@#'}


def get_client():
    ssh = paramiko.SSHClient()
    # 设置为接受不在known_hosts 列表的主机可以进行ssh连接
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=host['ip'], port=host['port'], username=host['username'], password=host['password'])
    return ssh


def handle(client):
    stdin, stdout, stderr = client.exec_command('cat /proc/meminfo')
    str_out = stdout.read().decode()
    str_err = stderr.read().decode()
    if str_err != "":
        print(str_err)
    total_mem = re.search('\d+', re.search("MemTotal:.*?\n", str_out).group()).group()
    if not redis_cli.exist_key('mem:total'):
        redis_cli.set_key('mem:total', total_mem)
    free_mem = re.search('\d+', re.search('MemFree:.*?\n', str_out).group()).group()
    buffer_mem = re.search('\d+', re.search('Buffers:.*?\n', str_out).group()).group()
    cached_mem = re.search('\d+', re.search('Cached:.*?\n', str_out).group()).group()
    mem_used = float(total_mem) - float(free_mem) - float(buffer_mem) - float(cached_mem)
    redis_cli.lpush('mem:used', mem_used)
    use = round(float(mem_used) / float(total_mem), 2)
    print('当前内存使用率为: {:.2%}'.format(use))
    return


def draw():
    pass


def monitor():
    client = get_client()
    i = 0
    while i < 10:
        time.sleep(10)
        start = time.time()
        handle(client)
        i += 1
        end = time.time()
        cost = (end - start)
        print('i=%s, cost=%s' % (str(i), str(cost)))
        results = redis_cli.lrange('mem:free', 0, 10)
        result = [int(data) for data in results]
        print(result)
    client.close()


if __name__ == '__main__':
    monitor()
