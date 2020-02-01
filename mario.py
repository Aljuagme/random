# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 17:38:25 2020

@author: alvar

"""



def mario_less(n):
    for i in range(n):
        print((-i+n-1)*" " + (i+1)*"#")
try:
    n = int(input("How tall do you want the structure to be? "))
except ValueError:
    print("The input must be a number")   
else:
    mario_less(n)


def mario_more(m):
    for i in range(m):
        print((-i+m-1)*" " + (i+1)*"#", end="  ")
        print((-m+i)*" " + (i+1)*"#")
try:
    m= int(input("How tall do you want the double-structure to be?: "))
except ValueError:
    print("The input must be a number")
else:
       mario_more(m)