#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# GID = 7
# File: hw7.py
# Created at: 03/19/19, 12:59:17
# Created by: Kunal Gursahani
# Last Modified: 03/19/19, 18:14:15 
# ------
# Description: 
# find Valid words
# 
# ###


##
# Create table, if s[i:j] in dict,
#   table[i][j] = 1
#   k is the separator 
#   such that table[i][k] is 1
#   or table[k][j] = 1 
#   i.e. s[i:j] or s[k:j] is a valid word
# #
def createTable(string, dictionary):
    
    table = [[0]*len(string) for i in range(len(string))]

    for i in range(len(table)):
        for j in range(0, len(table)):
            if string[i] in dictionary:
                table[i][i] = 1
                if string[i:j] in dictionary:
                    table[i][j] = 1  
        
            for k in range(i+1,j):
                if table[i][k-1] == 1 and table[k][j] == 1:       
                    table[i][k] = 1  
    
    return table


vector = []

##
# 
# recursively check if col,row has 1, if so,
#   then append to vector to return s[col:row]
# #
def findValidWords(string, dictionary, table):
        for i in range(len(table)):
            for j in range(len(table)):
                if (table[i][j] == 1 and table[i+1][j] == 1) or (table[i][j] == 1 and table[i][j-1] == 1):
                    vector.append(string[i:j])
            findValidWords(string, dictionary, table)
        
        return vector
    
string = "redapples"
dictionary = ["red","app","apple","apples"]

table = createTable(string,dictionary)


findValidWords(string,dictionary,table)
