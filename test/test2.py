# -*- coding: utf-8 -*-
from sshtunnel import SSHTunnelForwarder
import paramiko

with SSHTunnelForwarder(
        ('10.175.1.155', 22),
        ssh_username="root",
        ssh_password="start123@@",
        remote_bind_address=('10.176.139.10', 22),
        local_bind_address=('0.0.0.0', 10022)
) as server:
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect('127.0.0.1', 10022, username="root", password="Cmplat2019")
    stdin, stdout, stderr = client.exec_command("curl http://127.0.0.1:6666/hello")
    res, err = stdout.read(), stderr.read()
    result = res if res else err
    res = result.decode()
    res = result.decode("utf-8")
    res = result.decode(encoding="utf-8")
    print(res)
    client.close()

print('FINISH!')
