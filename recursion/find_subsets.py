#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: find_subsets.py
# Created at: 03/18/19, 17:08:13
# Created by: Kunal Gursahani
# Last Modified: 03/18/19, 20:59:49 
# ------
# Description: 
# 
# 
###

def subsets(v):
    finalset = []
    find_subsets(v,[],finalset)
    return finalset

    
def find_subsets(v,chosen,finalset):
    
    if len(v) == 0:
        finalset.append(chosen[:])
        
    else:
            first = v[0]
            v.pop(0)
            chosen.append(first)
            find_subsets(v,chosen,finalset)
            # s.insert(i,choose)
            chosen.pop()
            find_subsets(v,chosen,finalset)
            v.insert(0,first)
    


print(subsets([1,2,3]))

