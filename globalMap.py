# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 11:18:24 2017

@author: Administrator
"""

class globalMap:
    map={}
    
    def set_map(self,key,value):
        self.map[key]=value
        
    def set(self,**keys):
        try:
            for key_,value_ in keys.items():
                self.map[key_]=str(value_)
        except BaseException as msg:
            raise msg
            
    def del_map(self,key):
        try:
            del self.map[key]
            return self.map
        except KeyError:
            print 'error'
            
    def get(self,*args):
        try:
            dic={}
            for key in args:
                if len(args)==1:
                    dic=self.map[key]
                elif len(args)==1 and args[0]=='all':
                    dic=self.map
                else:
                    dic[key]=self.map[key]
            return dic
        except KeyError:
            return 'Null_'