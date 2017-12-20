# -*- coding: utf-8 -*-
import psutil

pid = psutil.pids()
for k, i in enumerate(pid):
    try:
        proc = psutil.Process(i)
        print k, i, "%.2f%%" % (proc.memory_percent()), "%", proc.name(), proc.exe()

    except psutil.AccessDenied:
        print "psutil.AccessDenied"
