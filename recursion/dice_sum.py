#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: dice_sum.py
# Created at: 03/12/19, 01:10:20
# Created by: Kunal Gursahani
# Last Modified: 03/12/19, 01:10:38 
# ------
# Description: 
# 
# 
###
count = 0
def dice_roll(num,subvector,sumSoFar, desiredSum):
    global count  
    count += 1
    if num == 0:
        # if sumSoFar == desiredSum:
            print(subvector)

    else:
        for i in range(1,7):
            if sumSoFar + i +1*(num - 1) <= desiredSum and\
               sumSoFar + i +6*(num - 1) >= desiredSum:
                subvector.append(i)
                dice_roll(num - 1, subvector,sumSoFar + i, desiredSum)
                del subvector[-1]


l = [1,2,3]
# print(l[:-1])
# dice_roll(4,[],0,9)
# print(count)