#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 19:42:29 2020

@author: hjchung
"""

import os
import re

inputFilename = os.path.join('bagdata')

inputFile = open(inputFilename, 'r')
inputLines = inputFile.read()

inputLines = inputLines.replace(' bags contain ', ',')
inputLines = inputLines.replace(' bag, ', ',')
inputLines = inputLines.replace(' bags, ', ',')
inputLines = inputLines.replace(' bag.', '.')
inputLines = inputLines.replace(' bags.', '.')
inputLines = inputLines.replace('no other', '0 other')
inputLines = inputLines.replace('.\n', '\n')
inputLines = inputLines[:-1]

inputRE = re.compile(r',\d ')

nextLines = inputRE.sub(',', inputLines)
nextLines = nextLines.split('\n')
nextList = [line.split(',') for line in nextLines]

prevLines = inputLines
prevLines = prevLines.split('\n')
prevList = [line.split(',') for line in prevLines]


allcolors = [nextList[x][0] for x in range(len(nextLines))]

startcolor = 'shiny gold'

listofSets = [set([startcolor])]
listLength = [1]
flag = 1
counter = 0

def next_set(color, ruleList):
    
    inSet = set()
    
    for rule in ruleList:
        if color in rule[1:]:
            inSet.add(rule[0])
            ruleList.remove(rule)
    return inSet


        
while flag == 1 and counter <= len(allcolors):
    
    nextSet = set()
    
    for color in listofSets[counter]:
        nextSet.update(next_set(color, nextList))
    if len(nextSet) == 0:
        flag = 0
    else:
        listofSets.append(nextSet)
        listLength.append(len(nextSet))
        counter += 1

print(sum(listLength)-1)


    
        
        








    
    
        

