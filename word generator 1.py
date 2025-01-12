# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 22:12:27 2022

@author: Jolan
"""

import numpy as np

dictio      = "Fuer grissa ost drauka ulbrecken brennika dieser dominie dirtch owbens con dar tagenricht mosst verlaschendreck nich greschlechten bandakar talga vassternich reechani sentrosi vasi raug moss stroyza"

dictio = dictio.lower()+" "
alphabet    = ""

for c in dictio.lower():
    if c in alphabet:
        pass
    else:
        alphabet += c

alphabet = "".join(sorted(alphabet))




L = len(alphabet)

table = np.zeros((L,L))

table[0][alphabet.index(dictio[0])] +=1

for i in range(len(dictio)-1):
    table[alphabet.index(dictio[i])][alphabet.index(dictio[i+1])]+=1

print(alphabet)
print(table)


def next_char(c):
    i = alphabet.index(c)
    s=0
    for e in table[i]:
        s+=e
    r = np.random.randint(0,s)
    s=0
    for j in range(len(table[i])):
        s+=table[i][j]
        if s>r:
            return alphabet[j]
    return " "



out = ""+next_char(" ")
while out[-1]!=" " and len(out)<50:
    out+=next_char(out[-1])

print(out)







