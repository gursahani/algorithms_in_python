#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: print_decimal.py
# Created at: 03/10/19, 18:12:03
# Created by: Kunal Gursahani
# Last Modified: 03/10/19, 18:23:50 
# ------
# Description: 
# 
# 
###


def print_helper(num,prefix):
    if num == 0:
        print(prefix)
    else:
        for i in range(0,10):
            print_helper(num - 1, prefix + str(i))




def print_decimal(num):
     print_helper(num,"")           




print_decimal(3)
