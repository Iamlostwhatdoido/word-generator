# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 22:12:27 2022

@author: Jolan
"""

import numpy as np


def load(filename,encoding='utf-8',errors='ignore'):
    with open(filename) as f:
        dictio = f.read()

    dictio = dictio.lower()+" "
    alphabet    = ""

    for c in dictio.lower():
        if c in alphabet:
            pass
        else:
            alphabet += c
    
    alphabet = "".join(sorted(alphabet))
    
    keys = np.array(["  "])
    for e in alphabet:
        for f in alphabet:
            if e+f in keys or f==" ":
                pass
            else:
                keys = np.append(keys,[e+f])
    
    L = len(alphabet)
    
    table = np.zeros((L**2,L))
    
    table[0][alphabet.index(dictio[0])] +=1
    table[np.where(keys==' '+dictio[0])[0][0]][alphabet.index(dictio[1])] +=1
    
    for i in range(len(dictio)-2):
        duo = dictio[i]+dictio[i+1] 
        if duo[-1]==" ":
            table[0][alphabet.index(dictio[i+2])]+=1
        else :
            table[np.where(keys==duo)[0][0]][alphabet.index(dictio[i+2])]+=1
            
    return alphabet, keys, table


def next_char(duo, lingo):
     i = np.where(lingo[1]==duo)[0][0]
     s=0
     for e in lingo[2][i]:
         s+=e
     r = np.random.randint(0,s)
     s=0
     for j in range(len(lingo[2][i])):
         s+=lingo[2][i][j]
         if s>r:
             return lingo[0][j]
     return " "


def new_word(lingo):
    n=0
    out=""
    while len(out)<5 and n<400:
        out = ""+next_char("  ",lingo)
        out+= next_char(" "+out[-1],lingo)
        while out[-1]!=" " and len(out)<50:
            out+=next_char(out[-2]+out[-1],lingo)
        n+=1
    if n==400:
        return out+" !"
    return out

def words(n,lingo):
    for i in range(n):
        print(new_word(lingo))

lingo = load("Word generators/dharan.txt")


words(10,lingo)

