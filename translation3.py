"""
Author: Novanator 2012
Program: Translation3
"""
import random
from btree import Node
from btree import BinTree

file = open ("list.txt", "r")
contents = file.read ()
words = contents.split ()

random.shuffle(words)

tree=BinTree()
for i in words:
    tree.put(i)
    
l=[]
for x in words:
    if tree.exists(x[::-1]) and x not in l:
        l.append(x)
        
l2=[]

for x in l:
    if x not in l2:
        l2.append(x)
        l2.append(x[::-1])
        
for i in range (0,len(l2),2):
    print(l2[i],l2[i+1])
    

