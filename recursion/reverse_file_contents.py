#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: reverse_file_contents.py
# Created at: 03/09/19, 13:24:16
# Created by: Kunal Gursahani
# Last Modified: 03/09/19, 13:59:11 
# ------
# Description: 
# Program to reverse file contents 
# recursively
# 
###



def reverse_contents(fileObj):
    line = fileObj.readline()
    if line:
        reverse_contents(fileObj)
        print(line)
        
fileObj = open("file.txt","r")    
reverse_contents(fileObj)


