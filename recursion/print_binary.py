#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: print_binary.py
# Created at: 03/10/19, 17:46:26
# Created by: Kunal Gursahani
# Last Modified: 03/10/19, 18:06:49 
# ------
# Description: 
# 
# 
###



def print_helper(num,pre):
    if num == 0:
        print (pre)
    else:
        print_helper(num - 1, pre + "0")
        print_helper(num - 1, pre + "1")

def print_binary(num):
    print_helper(num,"")




print_binary(4)