#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: By 空道
# Created on 10:19 2015/3/6
from unicorn import *
import struct
# return a fake handle value
def mallocHook(eh, address, argv, size, userData):
    print("call mallocHook")
    allocSize = argv[0]
    ###设置一个函数静态变量方便累加
    if ( not hasattr(mallocHook,'base')  ):
            mallocHook.base = 0x00600000
    ##查找申请空间的地址
    while(eh.is_memory_mapped(mallocHook.base)):
        mallocHook.base += 0x1000
    addr = eh.map_memory(mallocHook.base, allocSize);
    ##方便下一次基地址获取;
    mallocHook.base +=  (allocSize + 0x1000 - 1) & ~(0x1000 - 1)
    return addr

def memsetHook(eh, address, argv, size, userData):
    print("memsetHook")
    print(argv)
    addr = argv[0]
    chrch = struct.pack("B", argv[1] & 0xff)
    bufsize = argv[2]
    eh.mu.mem_write(addr, chrch * bufsize)
    print("memset addr: 0x%x" % addr)
    return addr
def strcmpHook(eh, address, argv, size, userData):
    print("strcmpHook")
    if eh.is_memory_mapped(argv[0]) and eh.is_memory_mapped(argv[1]):
        str1 = eh.getEmuString(argv[0])
        str2 = eh.getEmuString(argv[1])
        if str1 == str2:
            return 0
    return -1;
def strlenHook(eh, address, argv, size, userData):
    print("strlenHook addr:0x%x" % argv[0])
    if eh.is_memory_mapped(argv[0]):
        str1 = eh.getEmuString(argv[0])
        return len(str1)
    else:
        return 0;
##随便打印一下 printf 的第一个参数;
def printfHook(eh, address, argv, size, userData):
    print("printfHook:%s" % eh.getEmuString(argv[0]))
    print(argv)
    
exp_apiHooks = {}
exp_apiHooks['malloc'] = mallocHook
exp_apiHooks['memset'] = memsetHook
exp_apiHooks['strcmp'] = strcmpHook
exp_apiHooks['strlen'] = strlenHook
exp_apiHooks['printf'] = printfHook
