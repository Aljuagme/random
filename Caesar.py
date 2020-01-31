# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 23:42:09 2020

@author: alvar
"""

def encript(sentence, key):
    
    encripted_sentence = ""   
    for cha in sentence:
        if ord(cha) >=65 and ord(cha)<= 90:
            encripted_sentence += chr((((ord(cha) -65) + key) %26) + 65)
        elif ord(cha) >= 97 and ord(cha)<=122:
            encripted_sentence += chr((((ord(cha) -97) + key) %26) + 97)
        else:
            encripted_sentence += cha
            
    return encripted_sentence

sentence = input("Tell me the sentence you want to encript: ")
try:
    key = int(input("Tell me the key: "))
except:
    print("The key must be an integer!")
else:
    caesar = encript(sentence, key)
    print("The encripted sentence is: ", caesar)         
            
        