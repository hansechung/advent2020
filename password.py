#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 19:42:29 2020

@author: hjchung
"""

import os
import re
import numpy as np
import pandas as pd
import operator

from operator import xor

inputFilename = os.path.join('password')
df = pd.read_csv(inputFilename, sep='\s+', header=None)

countera = 0
counterb = 0

for i in range(len(df)):
        prule = df.iloc[i][0].split('-')
        pchar = df.iloc[i][1][:-1]
        pword = df.iloc[i][2]
        
        pmin = int(prule[0])
        pmax = int(prule[1])
        
        pcount = len(re.findall(pchar, pword))
        
        if pcount >= pmin and pcount <= pmax:
            countera = countera + 1
            
        if xor(pword[pmin-1] == pchar, pword[pmax-1] == pchar):
            counterb = counterb + 1

print(countera, counterb)


    
# for each item in df
# read count
# read letter
# read password



