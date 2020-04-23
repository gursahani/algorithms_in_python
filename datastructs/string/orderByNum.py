#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: orderByNum.py
# Created at: 07-19-2019 00:46
# Created by: Kunal Gursahani
# Last Modified: 07/19/19, 03:13:44 
# ------
# Description: 
# Your task is to sort a given string.
# Each word in the string will contain a single number.
# This number is the position the word should have in the result.
# Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).
# If the input string is empty, return an empty string. 
# The words in the input String will only contain valid consecutive numbers.
# Examples
# "is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
# "4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
# ""  -->  ""
###

def order(sentence):
    output = ""
    m = {}
    sentence = sentence.split(' ')
    for i in range(len(sentence)):
        for j in range(1, len(sentence)+1):
            if str(j) in sentence[i]:
                m[j] = sentence[i]
                # output += sentence[j] + " "
    for i in range(1, len(m)+1):
        output += m[i] + " "
        print(m[i])
    return output


print(order("is2 Thi1s T4est 3a"))