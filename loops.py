#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 21:47:08 2018

@author: hema
"""

input_number = int(input("enter a number: "))
type(input_number)
if(input_number < 10):
    print("input number is < 10")
elif(input_number == 10):
    print("number is 10")
else:
    print("input number is > 10")
    
    
# while loop

i=0
while(i <= 10):
    print(i)
    i+=2
    
    
for i in range(0,11):
    if(i%2 == 0):
        print(i)
    else:
        pass

    
for i in range(0,11):
    if(i%2 == 0):
        print(i)

tuple1 = ('mon','tue','wed')
for i in tuple1:
    print(i)
    
tuple2 = ('jan','feb','mar')
for i in tuple2:
    print(i,end=',')
    
a = 10
for i in a:
    print(i)
    
 
alphabets = 'abcde'
for i in alphabets:
    print(i.upper() ,end=',')
    
    
    
    
    
    
    