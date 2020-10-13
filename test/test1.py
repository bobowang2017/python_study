# -*- coding:utf-8 -*-
import paramiko  # 先安装pycrypto，再安装paramiko
# 创建SSH对象
ssh = paramiko.SSHClient()
# 允许连接不在~/.ssh/known_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接服务器
ssh.connect(hostname="10.175.1.155", port=22, username="root", password="start123@@")
# 执行命令，不要执行top之类的在不停的刷新的命令(可以执行多条命令，以分号来分隔多条命令)
stdin, stdout, stderr = ssh.exec_command("ls")
stdin.flush()
# 获取命令结果
res, err = stdout.read(), stderr.read()
result = res if res else err
res = result.decode()
res = result.decode("utf-8")
res = result.decode(encoding="utf-8")
print(res)
# 关闭服务器连接
ssh.close()
