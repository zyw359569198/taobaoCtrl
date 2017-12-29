# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 10:47:42 2017

@author: Administrator
"""

import logging
import config
import os
import cloghandler
import platform
class logger(logging.Logger):
    def __init__(self):
        logging.Logger.__init__(self,config.logFilePath)
        logging.Logger.propagate=0
        #日志格式
        fmtHandler=logging.Formatter(config.logFormatter)
        #输出到终端
        consoleHd=logging.StreamHandler()
        consoleHd.setLevel(config.logLevelToConsole)
        consoleHd.setFormatter(fmtHandler)
        self.addHandler(consoleHd)
        #日志文件
        if os.path.exists(os.path.dirname(config.logFilePath)):
            pass
        else:
            os.makedirs(os.path.dirname(config.logFilePath))
        if config.threadType==1 and str(platform.system())!="Windows":
            #多进程
            rotateHandler=cloghandler.ConcurrentRotatingFileHandler(config.logFilePath,'a',config.logMaxBytes,config.logBackCount)
            rotateHandler.setFormatter(fmtHandler)
            rotateHandler.setLevel(config.logLevelToFile)
            self.addHandler(rotateHandler)
        else:
            #线程
            fileHd=logging.FileHandler(config.logFilePath)
            fileHd.setLevel(config.logLevelToFile)
            fileHd.setFormatter(fmtHandler)
            self.addHandler(fileHd)
            
            
            
            
            
            
            
            