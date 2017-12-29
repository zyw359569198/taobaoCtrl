# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 10:51:17 2017

@author: Administrator
"""

import logging
#执行次数
threadExecTimes=1
threadExecSleep=0
#thread
threadCount=100
#0 threading 1 processing
threadType=1
#logging
logFilePath='log/taobaoCtl.log'
logLevelToFile=logging.INFO
logLevelToConsole=logging.INFO
logFormatter='%(asctime)s [%(processName)s][%(threadName)s][%(filename)s:%(lineno)s][%(levelname)s]%(message)s'
#日志达到10m时分割日志
logMaxBytes=1024*1024*10
#最多保留50份日志文件
logBackCount=50
#httpClient
httpTimeOut=1000