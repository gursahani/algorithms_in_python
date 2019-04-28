#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: house_burglar.py
# Created at: 03/18/19, 01:35:07
# Created by: Kunal Gursahani
# Last Modified: 03/18/19, 16:23:04 
# ------
# Description: 
# 
# 
###


        
import sys
# import math

def getSum(nums,i,sum):
    if i == len(nums):
        return sum
    else:
        sum = getSum(nums,i+1,sum+nums[i])
        return sum


def findMax(nums):
    maxNum = -float('inf')
    for i in range(0,len(nums)):
        if maxNum < nums[i]:
            maxNum = nums[i]
    # print(maxNum)
    return maxNum

def findMaxRec(nums,i,maxNum):
    if i == len(nums):
        return maxNum
    else:
        if maxNum < nums[i]:
            maxNum = nums[i]
        return findMaxRec(nums,i+1,maxNum)


def max_theft(nums):
    max_dollar, maxSum = 0,0
    for i in range(0,len(nums)):
        if max_dollar < nums[i]:
            max_dollar = nums[i]
            i += 1
            maxSum += max_dollar
    
    return maxSum

def max_theft_rec(nums,i,max_sum,max_dollar):
    if i >= len(nums):
        return max_sum
    else:
        if max_dollar < nums[i]:
            
            max_dollar = nums[i]
            # print(max_dollar)
            i += 1
            
            max_sum += max_dollar
        
        return max_theft_rec(nums,i+1,max_sum,max_dollar)


# print(max_theft( [6, 1, 2, 7]))
# print(max_theft_rec([6, 1, 2, 7],0,0,0))

# def max_theft_dp(nums,n,cache,i,max_sum,max_dollar):
#     if max_sum in cache:
#         return cache[n]
#     if i >= len(nums):
#         return max_sum
#     else:
#         if max_dollar < nums[i]:
#             max_dollar = nums[i]
#             i += 1
#             max_sum += max_dollar
#         cache[n] = max_theft_dp(nums,n,cache,i+1,max_sum,max_dollar)
#         return cache[n]



# print(max_theft_dp([6, 1, 2, 7,9],4,{},0,0,0))

# print(findMax([4,2,3,1,9]))

# print(findMaxRec([4,2,3,1,9],0,-float('inf')))
    


        
# print(getSum([4,2,3,1,9],0,0))




def rob(houses):
    even_sum = 0
    odd_sum = 0

    for i in range(len(houses)):
        if i%2 == 0:
            even_sum += houses[i]
            print(even_sum+houses[i],odd_sum)
        else:
            odd_sum += houses[i]
            print(even_sum,odd_sum+houses[i])
    return max(odd_sum,even_sum)


print(rob([6,4,3,7,8,9,2,2,2,4]))
        