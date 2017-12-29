# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 15:24:22 2017

@author: Administrator
"""

from selenium import webdriver
import os
import time

def browse():
    browser=webdriver.Chrome()
    
if __name__=="__main__":
    test.testPlanWithNoJoin(browse,1).run()
    str=raw_input(unicode("停止测试，杀掉所有的测试进程：","utf-8").encode("gb2312"))
    if str.count>0:
        os.system("taskkill /F /IM chrome.exe")
        os.system("taskkill /F /IM chromedriver.exe")