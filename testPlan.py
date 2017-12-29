# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 14:23:37 2017

@author: Administrator
"""

import threading
from multiprocessing import Process,Lock
import config
import logger
import httpClient
import resultCount
import time
from globalMap import globalMap
class myThread(threading.Thread):
    def __init__(self,fn,index,threadExecTimes,lock):
        threading.Thread.__init__(self,name=("Thread-"+str(index)))
        self.fn=fn
        self.index=index
        self.lock=lock
        self.threadExecTimes=threadExecTimes
    def run(self):
        for i in xrange(self.threadExecTimes):
            result.startRecord(self.index,self.lock)
            log.info("exec function:"+self.fn.func_name)
            self.fn(self.index)
            result.endRecord(self.index,self.lock)
            time.sleep(config.threadExecSleep)
            

class myProcess(Process):
    def __init__(self,fn,index,threadExecTimes,lock):
        Process.__init__(self,name=("Process-"+str(index)))
        self.fn=fn
        self.index=index
        self.lock=lock
        self.threadExecTimes=threadExecTimes
    def run(self):
        for i in xrange(self.threadExecTimes):
            result.startRecord(self.index,self.lock)
            log.info("exec function:"+self.fn.func_name)
            self.fn(self.index)
            result.endRecord(self.index,self.lock)
            time.sleep(config.threadExecSleep)
            
            
class testPlan:
    __threads=[]
    __child=""
    def __init__(self,fn):
        self.fn=fn
        self.count=config.threadCount
    def run(self):
        
        if config.threadType==1:
            lock=Lock()
            for index in xrange(self.count):
                log.info("Start Process :"+str(self.count))
                self.__threads.append(myProcess(self.fn,index,config.threadExecTimes,lock))
                self.__threads[index].daemon=True
                self.__threads[index].start()
            for index in xrange(self.count):
                self.__threads[index].join()
        else:
            lock=threading.Lock()
            for index in xrange(self.count):
                log.info("Start Thread :"+str(self.count))
                self.__threads.append(myThread(self.fn,index,config.threadExecTimes,lock))
                self.__threads[index].setDaemon(True)
                self.__threads[index].start()
            for index in xrange(self.count):
                self.__threads[index].join()
        
        result.threadCount()
        result.totalCount()
        result.successCount()
        result.totalCostTime()
        result.avgCostTime()

def testHttpToken(index):
    h=httpClient.baseHttp("http:/***","post")
    h.addHeader("Content-Type","application/json")
    h.addHeader("Accept","application/json")
    h.addBody("{\"auth\":\"test\"}")
    r=h.executer()
    return r
if __name__=='__main__':
    globalMap().set_map("log",logger.logger())
    globalMap().set_Map("result",resultCount.resultCount("test"))
    log=globalMap().get("log")
    result=globalMap().get("result")
    testPlan(testHttpToken).run()
