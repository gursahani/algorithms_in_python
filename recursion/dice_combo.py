#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: dice_combo.py
# Created at: 03/10/19, 20:19:51
# Created by: Kunal Gursahani
# Last Modified: 03/12/19, 01:40:41 
# ------
# Description: 
# 
# 
###


def dice_roll(num,subvector):
    if num == 0:
        print(subvector)
    else:
        for i in range(1,6):
            # choose
            subvector.append(i)
            dice_roll(num - 1, subvector)
            del subvector[-1]


l = [1,2,3]
# print(l[:-1])
print(dice_roll(3,[]))


sofar = ""




# s = "kunal"
# print(s[:2] + s[2+1:])
# s = s[:2] + "n" + s[3:]
# print(s)
# print(s[:-1])
# chosen = ""
# c = ""

def remove_at(i, s):
    return s[:i] + s[i+1:]

#
## 
# 
# void recPermute(string s) {
    # recPermuteHelper("",s);
#}

##
# #void recPermuteHelper( string rest, string soFar) {
#     if (rest == "") {
#         cout << soFar << endl;
#     } else {
#         for (int i = 0; i < (int)rest.size(); i++) {
#             string remaining = rest.substr(0, i)
#                     + rest.substr(i+1);
#             recPermuteHelper(remaining,soFar + rest[i]);
#         }
#     }
# }
# 
# 
ch = []
def permutations(s,chosen, se):
    global ch
    # print("s is ", s)
    if s == "":
        if chosen not in se:
            se.add(chosen)
            ch.append(chosen)
    else:
        for i in range(0,len(s)):
            r = remove_at(i,s)
            permutations(r,chosen+s[i],se)
            

permutations("aabc","",set())
print(ch)
    

# print(sofar)