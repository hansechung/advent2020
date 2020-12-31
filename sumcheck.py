#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 09:10:40 2020

@author: hjchung
"""


import numpy as np
import os

inputFilename = os.path.join('input1')
inputData = np.genfromtxt(inputFilename, dtype='i8')


def find_pair(inData):
    inputLength = len(inData)
    
    for i in range(inputLength-1):
        for j in range(inputLength-1):
            if inputData[i] + inputData[j] == 2020:
                return inputData[i] * inputData[j]
            elif i == inputLength - 1 and j == inputLength - 1:
                return "Not Found"

print(find_pair(inputData))

def find_triple(inData):
    inputLength = len(inData)
    
    for i in range(inputLength-1):
        for j in range(inputLength-1):
            for k in range(inputLength -1):
                if inputData[i] + inputData[j] + inputData[k] == 2020:
                    return inputData[i] * inputData[j] * inputData[k]
                elif i + j + k == (3* inputLength) - 3:
                    return "Not Found"

print(find_triple(inputData))
    
# read in list of numbers as numpy array
# get length of list

# create list of N^2 - N + 1 pairs

# for i in (0 to N^2-N), run through pairs and check_sum
# if check_sum = MATCHSUM then return pairs else next i


