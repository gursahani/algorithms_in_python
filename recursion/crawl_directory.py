#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: crawl_directory.py
# Created at: 03/09/19, 14:00:17
# Created by: Kunal Gursahani
# Last Modified: 03/09/19, 18:36:47 
# ------
# Description: 
# 
# 
###
import os
import pathlib


from pathlib import Path

print(Path.cwd())


def crawl(name):
    if Path(name).is_file():
        print(name)
    else:
        files = []
        for file in Path(name).iterdir():
            files.append(file)
        for f in files:
            if Path(f).is_dir():
                print(f)

            crawl(f)


# l = []
# p = Path('../')
# for x in p.iterdir():
#     l.append(x)
#
# print(l)
print(crawl('../'))
        



