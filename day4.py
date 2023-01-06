# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 15:21:09 2023

@author: daisy
"""

input_file = "C:/Users/daisy/OneDrive/Documents/advent_of_code/input_day4.txt"

with open(input_file) as f:
      pairs = [[[int(j) for j in i.split('-')] 
                for i in line.strip('\n').split(',')] 
               for line in f]
    
# pairs = []
# with open(input_file) as f:
#     for line in f:
#         line = line.strip('\n').split(',')
#         line = [i.split('-') for i in line]    
#         line = [[int(i) for i in j] for j in line]        
#         pairs.append(line)
        
        
number_within = 0

for i in pairs:
    elf1 = i[0]
    elf2 = i[1]
    if (elf1[0] >= elf2[0]) and (elf1[1] <= elf2[1]):
        number_within += 1
        continue
    elif (elf2[0] >= elf1[0]) and (elf2[1] <= elf1[1]):
        number_within += 1
   
#had to look at someone elses code to realise I imported the numbers as strings.

number_overlap = 0

for i in pairs:
    elf1 = i[0]
    elf2 = i[1]
    if (elf1[0] >= elf2[0]) and (elf1[0] <= elf2[1]):
        number_overlap += 1
        continue
    elif (elf1[1] >= elf2[0]) and (elf1[1] <= elf2[1]):
        number_overlap += 1
        continue
    elif (elf2[0] >= elf1[0]) and (elf2[0] <= elf1[1]):
        number_overlap += 1
        continue
    elif (elf2[1] >= elf1[0]) and (elf2[1] <= elf1[1]):
        number_overlap += 1
        