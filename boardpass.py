#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 19:42:29 2020

@author: hjchung
"""

import os
import re
import csv
#import numpy as np
#import pandas as pd

inputFilename = os.path.join('boardpasslist')

inputFile = open(inputFilename, 'r')
inputLines = inputFile.read()

inputLines = inputLines.split('\n')
inputLines = inputLines[:-1]


inputList = [[line[:7],line[7:]] for line in inputLines]

seatID = []

def findrow128(rowstring):
    
    rowlist = [0, 0, 0, 0, 0, 0, 0]
    
    if rowstring[0] == 'B':
        rowlist[0] = 64
    if rowstring[1] == 'B':
        rowlist[1] = 32
    if rowstring[2] == 'B':
        rowlist[2] = 16
    if rowstring[3] == 'B':
        rowlist[3] = 8
    if rowstring[4] == 'B':
        rowlist[4] = 4
    if rowstring[5] == 'B':
        rowlist[5] = 2
    if rowstring[6] == 'B':
        rowlist[6] = 1
    
    return sum(rowlist)

    
def findcol8(colstring):
    
    collist = [0, 0, 0]
    
    if colstring[0] == 'R':
        collist[0] = 4
    if colstring[1] == 'R':
        collist[1] = 2
    if colstring[2] == 'R':
        collist[2] = 1
    
    return sum(collist)
    

for i in range(len(inputList)):
    seatID.append(8 * findrow128(inputList[i][0]) + findcol8(inputList[i][1]))
    
seatID.sort()
myseat = min(seatID)


for j in range(1,len(seatID)):
    if seatID[j] != seatID[j-1]+1:
        myseat = seatID[j-1]+1

print(max(seatID))
print(myseat)


    
    
        

