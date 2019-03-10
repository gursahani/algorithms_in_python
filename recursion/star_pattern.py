#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: star_pattern.py
# Created at: 03/09/19, 21:37:34
# Created by: Kunal Gursahani
# Last Modified: 03/09/19, 21:51:14 
# ------
# Description: 
# 
# recursive star pattern
###


import turtle

ted = turtle.Turtle()



def star(t,size):
    if size <= 10:
        return
    else:
        for i in range(5):
            t.forward(size)
            star(t,size/3)
            t.left(216)


star(ted, 100)            
