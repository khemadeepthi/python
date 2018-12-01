#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 20:08:51 2018

@author: hema
"""

a = 2
b= 5
print(a+b)

name = 'hemadeepthi'
# add space b/w first and last names
print(name[0:name.find('a')+1],name[name.find('a')+1:len(name)])

# Define a list
weekday_list = ['Mon','Tue','Wed','Thu','Fri']
# Access an element from the list
weekday_list[2]

# Acess last 2 elements in the list
weekday_list[len(weekday_list)-2:len(weekday_list)]

# accessing last 2 elements using negative indexing
weekday_list[-2:len(weekday_list)]