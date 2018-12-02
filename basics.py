#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 20:08:51 2018

@author: hema
"""

a = 2
b= 5
print(a+b)

type(a)
c= 3.5
type(c)
d= 'hello'
type(d)
e= [1,2,3]
type(e)
f= (1,2,3)
type(f)

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

list1 = [1,3,5,7]
dir(list1)
list1.append(9)

list2 = [11,13,15]
list1.extend(list2)
list2.clear()
list2.append(-1)
list2.insert(1,-3)
list2.remove(-7)
list2.reverse()
list2.sort(reverse = True)
list2.pop()

list1.pop(4)
list2.extend([1,3,5,])
a = 1
type(a)
a= 1,

list3 = list2.copy()
list4 = list2
list1.extend(list2)
list1.count(3)

weekday_list.sort()

# tuple
tuple = (5,10,15,20,15)
(dir(tuple))
tuple.count(15)
tuple.count(3)

tuple.index(20)
tuple.index(3)



# dictionary
dic1= {1:'mon',2:'tue',6:'sat'}
type(dic1)
dir(dic1)
dic1.items()
dic1.keys()
dic1.values()
dic1[3]='wed'
# to add an element if it is not present in the dict already
# if the element being inserted is already present then it wont insert
dic1.setdefault(4,'thu')
dic1.setdefault(4,'Fri')
dic1[4]= 'Fri'
dic1[4]= 'Thu'
dic1.get(3)
dic1.pop(2)
dic1.popitem()

help(dic1.update)

dic1[2]='Sun'
dic1[4]='Tue'

dic2= {1:'mon',2:'tue',3:'wed',4:'thu',5:'fri'}

dic1.update(dic2)
help(dic1.fromkeys)
dic3 = dict()
type(dic3)
dic4 = dict.fromkeys(dic2, 'hema')
set = {1,2,3,4}
dic3 = dict.fromkeys(set, 'hema')




