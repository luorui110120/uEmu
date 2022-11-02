#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: By 空道
# Created on 10:19 2015/3/6
from unicorn import *

# return a fake handle value
def hook_590(eh, address, argv, size, userData):
    ###跳过这条指令,这里可以做任何处理,
    print("hook_590 addr: 0x%x"%address)
    eh.mu.reg_write(eh.getReg("PC"), address + size + 4)

exp_addrHooks = {}
##处理 590 地址的代码,可以选择跳过,也可以自己实现代码的逻辑;
exp_addrHooks['0x590'] = hook_590