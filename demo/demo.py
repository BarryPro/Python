# -*- coding:utf-8 -*-

from pexpect import pxssh
import optparse #处理我们命令行参数的模块
from threading import * #多线程 高并发

maxConnections = 5 #执行的最大线程为5个
connection = BoundedSemaphore()
Found = False
Failes = 0
def connect(host,user,password,ports,release):
    global Found
    global Failes
    # try:
    #     s = pxssh.pxssh()
