#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: cantur.py
# Created at: 03/09/19, 22:45:27
# Created by: Kunal Gursahani
# Last Modified: 03/10/19, 01:13:14 
# ------
# Description: 
# 
# Draw the cantor set recursively
###


#import turtle library
import turtle

#initialize turtle
ted = turtle.Turtle()

#create function to 
#draw line between two points

def draw_line(turtle,x1,y1,x2,y2):
    turtle.penup()
    turtle.goto(x1,y1)
    turtle.pendown()
    turtle.goto(x2,y2)


#if there is only one level then draw one line
#else draw 1/3 line and after space draw 1/3 line again
#left line starts at x,y and line 2 starts at x+2x/3,y

def cantor(size,turtle,x,y,level):
    if level == 1:
        draw_line(turtle,x,y,x+size,y)
    else:
        draw_line(turtle,x,y,x+size,y)
        
        cantor(size/3,turtle,x,y - 20,level - 1)
        cantor(size/3,turtle,x+2*size/3,y - 20,level - 1)
        
cantor(200,ted,0,0,5)


input()
