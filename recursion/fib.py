#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: fib.py
# Created at: 03/17/19, 14:44:40
# Created by: Kunal Gursahani
# Last Modified: 03/17/19, 23:43:53 
# ------
# Description: 
# 
# 
###


def fib(n):
    if n <= 1:
        f = n
    else:
        f = fib(n - 1) + fib(n - 2)
    return f


print(fib(20))


def fib_memo(n, memo):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    else:
        f = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
        memo[n] = f
    return memo[n]
    # else:
    #     return 0

# print(fib(90))
##
# T(n) = T(n - 1) + T(n - 2) + O(1)
#       >= F(n) ~~ 2^n 
#
# T(n) >= 2 * T(n - 2)
#        = 2^(n/2)
# 
# 
# 
#  #