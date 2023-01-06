# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 15:31:06 2023

@author: daisy
"""

input_file = "C:/Users/daisy/OneDrive/Documents/advent_of_code/input_day6.txt"

with open(input_file) as f:
    comm = ''
    for line in f:
        comm += line.strip('\n')

def find_marker(comm) :
    end = 4
    start = 0 
    while end < len(comm):
        if len(set(comm[start:end])) == 4:
            return end
            break
        else:
            end += 1
            start += 1
    
marker = find_marker(comm)

def find_messagemarker(comm) :
    end = 14
    start = 0 
    while end < len(comm):
        if len(set(comm[start:end])) == 14:
            return end
            break
        else:
            end += 1
            start += 1
    
messagemarker = find_messagemarker(comm)