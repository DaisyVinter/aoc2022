# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 14:33:16 2022

@author: daisy
"""

input = "C:/Users/daisy/OneDrive/Documents/advent_of_code/input_day1.txt"

import numpy as np

with open(input) as file:
    calories = [[]]
    n = 0
    for line in file:
        line = line.strip('\n')
        if line != '':
            line = int(line)
            calories[n].append(line)
        else:
            calories.append([])
            n += 1
            
## numpy solution to q1

#sums = []
#for elf in calories:
    #total_cals = np.sum(elf)
    #sums.append(total_cals)
    
sums = [np.sum(elf) for elf in calories]
            
maximum = np.max(sums)

## maximum is 71506

## numpy solution to q2

sorted_sums = np.sort(sums)
top3 = np.sum(sorted_sums[-3:])

#top3 is 209603