# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 11:26:05 2017

@author: Administrator
"""

import requests
import json
import config
import time
from globalMap import globalMap
class baseHttp:
    __params={}
    __headers={}
    __body=""
    __string=""
    __timeOut=config.httpTimeOut
    __log=""
    OPTIONS=("options","head","get","post","put","delete","trace","connect","patch")
    def __init__(self,url,options):
        self.__log=globalMap().get("log")
        self.url=url
        self.options=options
    def addParam(self,key,value):
        self.__params[key]=value
    def getParam(self,key):
        return self.__params[key]
    def addHeader(self,key,value):
        self.__headers[key]=value
    def getHeader(self,key):
        return self.__headers[key]
    def addBody(self,data):
        self.__body=json.dumps(data)
    def getBody(self):
        return self.__body
    def addTimeOut(self,timeOut):
        self.__timeOut=timeOut
    def getTimeOut(self):
        return self.__timeOut
    def executer(self):
        if self.options.lower() in baseHttp.OPTIONS:
            self.__string="requests."+self.options.lower()+"(\""+self.url+"\""
            self.__string=",timeout="+str(self.__timeOut)
            if len(self.__headers)>0:
                self.__string=",headers="+str(self.__headers)
            if len(self.__params)>0:
                self.__string=",params="+str(self.__params)
            if len(self.__body)>0:
                self.__string=",data="+self.__body
        self.__string+=")"
        try:
            startTime=time.time()
            r=eval(self.__string)
            self.__log.info(self.url+"  "+str(time.time()-startTime)+"  "+str(r.status_code))
            return r
        except requests.Timeout:
            self.__log.error(self.url+"  "+str(time.time()-startTime)+"  timeout")
        except:
            self.__log.error("other ERROR!")