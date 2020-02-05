# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 12:21:56 2020

@author: alvar
"""

def vigenere(message, key):
    encripted = ''
    index = 0
    
    for cha in message:
        if key[index].islower():
            key_cha = ord(key[index]) -97
        else:
            key_cha = ord(key[index]) -65
            
        if (ord(cha) >=65 and ord(cha) <=90):
            encripted += chr((((ord(cha) - 65) + key_cha) % 26) + 65)
            index = (index+1) % len(key)
            
        elif (ord(cha) >=97 and ord(cha) <= 122):
            encripted += chr((((ord(cha) - 97) + key_cha) %26) + 97)
            index = (index +1) % len(key)
            
        else:
            encripted += cha
            
    print(f"Plain text: {message}")
    print("Cipher text:", encripted)
            
            
message = input("What message would you like to encrypt? ")
key = input("The key to encript the message: ")
print("")

vigenere(message, key)