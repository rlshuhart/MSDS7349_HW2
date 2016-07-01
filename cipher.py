# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 20:36:56 2016

@author: Ryan Shuhart

MSDS 7349 Homework 2
"""

phrase = str(input("Enter sentence to encrypt: "))
shift = int(input("Enter shift value: "))
encodedPhrase = ""
for c in phrase:
    if c.islower() == True:
        encodedPhrase = encodedPhrase + chr(((ord(c)+shift)-97)%26 + 97)
    elif c.isupper() == True:
        encodedPhrase = encodedPhrase + chr(((ord(c)+shift)-65)%26 + 65)
    else:
        encodedPhrase = encodedPhrase + c
        
print(encodedPhrase)