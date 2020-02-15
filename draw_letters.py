# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 22:41:43 2020

@author: alvar
"""
def print_rangoli2(size):
    pattern = [f'{chr(96+size-i)}' for i in range(size)]
    width = (size + size-1) * 2 -1
    
    print("\n".join(["-".join(pattern[0:i+1]).center(width,'-') if i==0 else "-".join(pattern[0:i+1] + pattern[i-size-1::-1]).center(width,'-')
                     for i in list(range(size)) + list(range(size-2,-1,-1))]))
    
size = int(input("Tell me a number: "))        
print_rangoli2(size) 