#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: word_break.py
# Created at: 03/18/19, 23:17:43
# Created by: Kunal Gursahani
# Last Modified: 03/19/19, 15:14:07 
# ------
# Description: 
# 
# 
###

f = open("myDictionary.txt","r")

dictionary = f.read().split("\n")
# dictionary = {}
# # j = ['a','b','c','d','e','f','g']
# for i in range(len(l)):
#     dictionary[i] = l[i]

# print(dictionary.items())



# print(len(dictionary))

def word_break(word):
    vector = []
    lookup = ""
    obj = []
    return helper(word,vector,dictionary,lookup,obj)


def helper(word,vector,dictionary,lookup,obj):
    if len(word) == 0:
        obj.append(vector[:])
        
    else:
        
        lookup += word[0]
        word = word[1:]
        if lookup in dictionary:
            vector.append(lookup)
        
        helper(word,vector,dictionary,lookup,obj)



print(word_break("newcomers"))



newword = "newcomers"
# ch = word[0] 
# word = word[1:]

# print(ch,"\n", word)
# newword = ch + word
# word = word[1:]
# print(word)
# # word = word[1:]
# print(len(word))


print("newword is " + newword)



# # word,vector,final_list = "",[],[]
# def find(word,newword,vector):
#     if len(newword) == 0:
#         if vector:
#             # print(vector)
#             # final_list.append(vector[:])
#     else:
#         # for i in range(len(n))
#         word += newword[0]
#         if word in dictionary:
#             vector.append(word)
#         newword = newword[1:]
#         find(word,newword,vector)
#         word = ""
#         vector.clear()
#         find(word,newword,vector)
 
# find(word,newword,vector)
# print(final_list)

# print(dictionary)


import copy
word,vector,lookup,final_list = "newcomers",[],"",[]
def create_table(dictionary,word,lookup,i):
    table = [[[0] for i in range(len(word)+1)]]
    
    if i == len(word):
        print(table)

    else:
        # for i in range(len(word)):
            lookup += word[i]
            nextword = word[i+1:]
            if lookup in dictionary:
                table[]
                
            


# print(create_table(dictionary,word,vector,lookup,0))




