#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: sierpinski.py
# Created at: 03/10/19, 01:19:27
# Created by: Kunal Gursahani
# Last Modified: 03/10/19, 04:09:55 
# ------
# Description: 
# 
# 
###


import turtle

ted = turtle.Turtle()

def draw_line(turtle,x1,y1,x2,y2):
    # turtle.penup()
    turtle.goto(x1,y1)
    # turtle.pendown()
    turtle.goto(x2,y2)



def draw_triangle(turtle,size,n):
    
    if n == 0:
        turtle.forward(size)
        turtle.left(120)
        turtle.forward(size)
        turtle.left(120)
        turtle.forward(size)
        turtle.left(120)
    else:
        draw_triangle(turtle,size/2,n - 1)
        turtle.forward(size/2)
        draw_triangle(turtle,size/2,n - 1)
        turtle.left(120)
        turtle.forward(size/2)
        turtle.right(120)
        draw_triangle(turtle,size/2,n - 1)
        turtle.right(120)
        
        turtle.forward(size/2)
        turtle.left(120)
        
    

    

# def draw(turtle,size,x1,y1,x2,y2):
#     draw_triangle(turtle,size,x1,y1,x2,y2)
#     draw_triangle(turtle,size/2,x1+size,y1,x2/2,y2-size)
#     draw_triangle(turtle,size/4,x1 + 2*size,y1,x2/4,y2 - 2* size)

draw_triangle(ted,300,3)
# draw_triangle(ted,100,100,0,50,0)
input()