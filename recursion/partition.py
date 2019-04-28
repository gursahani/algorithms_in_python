#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: partition.py
# Created at: 03/11/19, 19:38:37
# Created by: Kunal Gursahani
# Last Modified: 03/19/19, 01:39:14 
# ------
# Description: 
# 
# 
###

def remove_at(i, s):
    return s[:i] + s[i+1:]



global result
result = []
def permutation(st, output):
        global result
        if st == "":
            print(output)
        else:
            for i in range(0,len(st)):
                newstring = remove_at(i,st)
                # print("s is " + st)
                permutation(newstring,output + st[i])

# permutation("abc","")

# print(len(result))

def insert_char(string, index,ch):
    return string[:index] + 'ch' + string[index:]

result2 = []

# def find_partition(s,vec,k):
#     global result2
#     if k == len(s):
#         print (vec)
#     else:
        
        
vec = []
s = "1324"
ch  = ""
def find_partition(s,vec,ch):
    for i in range(len(s)):
            vec = []
            ch = s[i]
            # print(ch)
            vec.append(ch)
            rest = remove_at(i,s)
            # print("rest is ",rest)
            vec.append(rest)
            result2.append(vec)
            # print("result2 is ", result2)
            # vec.clear()    
            insert_char(s,i,ch)
            # print(s)

            
find_partition(s,vec,ch)        
print(result2)           
 # for (int i = index; i < instr.length(); i++)
    # {
    # 
    #            
def combine(instr,outstr, index):
    print(outstr)
    for i in range(index,len(instr)):
        outstr += instr[i]
        combine(instr, outstr, i + 1)
        outstr = remove_at(len(instr) - 1,outstr)
        

combine("abc","",0)
# find_partition("123",[],0)            

# str = "abcd"

def recursive_combinations(str,vec):
    global result2
    if str == "":
        # print(vec)
        result2.append(vec)
    else:
        for i in range(0,len(str)):
            ch = str[:i+1]
            
            vec.append(ch)
            newstring = str[i+1:]
            
            vec.append(newstring)
            result2.append(vec)
            vec =[]
            recursive_combinations(newstring,vec)


        # insert_char(str,0,ch)
        # for i in range(1,len(str)):
        #     ch = str[:i+1]
        #     # print(ch)
        #     vec.append(ch)
        #     # newstring = remove_at(i,str)
        #     newstring = str[i+1:]
        #     print("newstring is ", newstring)
        #     vec.append(newstring)
        #     result2.append(vec)
        #     vec =[]
        
        
            # recursive_combinations(newstring,vec)
            # vec.append(str)
            
            # print(str)


# recursive_combinations("jamesbond",[])
# print(result2)







s = "1234"
