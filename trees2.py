#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 19:42:29 2020

@author: hjchung
"""

import os
import pandas as pd

inputFilename = os.path.join('trees')
df = pd.read_csv(inputFilename, header=None)

positiony11 = 0
positiony13 = 0
positiony15 = 0
positiony17 = 0
positiony21 = 0

treecount11 = 0
treecount13 = 0
treecount15 = 0
treecount17 = 0
treecount21 = 0

for i in range(df.size):
    rowstr = df.iloc[i][0] * 73
    if rowstr[positiony11] == '#':
        treecount11 += 1
    positiony11 += 1
    if rowstr[positiony13] == '#':
        treecount13 += 1
    positiony13 += 3
    if rowstr[positiony15] == '#':
        treecount15 += 1
    positiony15 += 5
    if rowstr[positiony17] == '#':
        treecount17 += 1
    positiony17 += 7
    if i % 2 == 0:
        if rowstr[positiony21] == '#':
            treecount21 += 1
        positiony21 += 1

print(treecount11, treecount13, treecount15, treecount17, treecount21)
print(treecount11 * treecount13 * treecount15 * treecount17 * treecount21)


    
# import the trees file of 323 rows
# lengthen each row by duplicating 31 times
# replace each . with 0 and each # with 1
# count hits on path down


