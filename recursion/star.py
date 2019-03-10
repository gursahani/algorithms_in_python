#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: star.py
# Created at: 03/09/19, 20:38:23
# Created by: Kunal Gursahani
# Last Modified: 03/09/19, 21:37:13 
# ------
# Description: 
# 
# 
###



import turtle


ted = turtle.Turtle()


def move():
    ted.forward(300)
    ted.left(135)


def draw_star(i):
    if i == 0:
        ted.pu()
    else:
        move()
        draw_star(i - 1)

ted.getscreen().bgcolor("cyan")
ted.color("blue")

def make_stars(i):
    if i == 0:
        ted.pu()
    else:
        ted.pd()
        draw_star(8)
        ted.left(90)
        ted.forward(100)
        make_stars(i - 1)

ted.speed(0)
make_stars(4)
input()