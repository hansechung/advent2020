#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 19:42:29 2020

@author: hjchung
"""

import os

inputFilename = os.path.join('customdata')

inputFile = open(inputFilename, 'r')
inputLines = inputFile.read()

inputLines = inputLines.replace('\n\n', '__')
inputLines = inputLines[:-1]

inputLines = inputLines.replace('\n', ',')
inputLines = inputLines.replace('__', '\n')
inputLines = inputLines.split('\n')

inputList = [line.split(',') for line in inputLines]

replynum = []
for replies in inputList:
    replyset = set()
    for item in replies:
        replyset.update(set(item))
    replynum.append(len(replyset))

print(sum(replynum))

allreplynum = []
for replies in inputList:
    allreplyset = set()
    allreplyset.update(replies[0])
    for item in replies:
        allreplyset = allreplyset.intersection(item)
    allreplynum.append(len(allreplyset))

print(sum(allreplynum))



        

