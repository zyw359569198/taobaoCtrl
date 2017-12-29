# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 13:48:55 2017

@author: Administrator
"""

import config
import time
from globalMap import globalMap
from multiprocessing import Manager
class resultCount:
    __threadCount=Manager().Value('c',0)
    __totalCount=Manager().Value('i',0)
    __successCount=Manager().Value('j',0)
    __totalSuccessTime=Manager().Value('k',0)
    __startExecTime=Manager().Value('l',0)
    __costTime=Manager().Value('m',0)
    __totalCostTime=Manager().Value('n',0)
    __resultCountName=Manager().Value('str','')
    __startDictTime=Manager().dict()
    __log=""
    def __init__(self,resultCountName):
        self.__totalCount.value=config.threadCount*config.threadExecTimes
        self.__threadCount.value=config.threadCount
        self.__resultCountName.value=resultCountName
        self.__startExecTime=time.time()
        self.__log=globalMap().get("log")
    def startRecord(self,index,lock):
        lock.acquire()
        try:
            self.__startDictTime[index]=time.time()
        finally:
            lock.release()
    def endRecord(self,index,lock):
        lock.acquire()
        try:
            self.__costTime.value=time.time()-self.__startDictTime.get(index)
            self.__totalSuccessTime.value=self.__totalSuccessTime.value+self.__costTime.value
            self.__successCount.value+=1
        finally:
            lock.release()
    def totalCostTime(self):
        self.__totalCostTime.value=time.time()-self.__startExecTime.value
        self.__log.info("totalCostTime :"+str(self.__totalCostTime.value)+" s")
        return self.__totalCostTime.value
    def avgCostTime(self):
        avgTime=self.__totalSuccessTime.value/self.__successCount.value
        self.__log.info("avgCostTime :"+str(avgTime)+" s")
        return avgTime
    def totalCount(self):
        self.__log.info("totalCount :"+str(self.__totalCount.value))
        return self.__totalCount.value
    def threadCount(self):
        self.__log.info("threadCount :"+str(self.__threadCount.value))
        return self.__threadCount.value
    def successCount(self):
        self.__log.info("successCount :"+str(self.__successCount.value))
        return self.__successCount.value
