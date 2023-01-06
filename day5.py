# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 16:29:23 2023

@author: daisy
"""

input_file = "C:/Users/daisy/OneDrive/Documents/advent_of_code/input_day5.txt"

with open(input_file) as f:
    stacks = []
    
    for line in f:
        if line.startswith('['):
            line = line.strip('\n')
            i = 1
            stack = 0
            while i <= len(line):
                try:
                    stacks[stack]+= line[i]
                except IndexError:
                    stacks.append(line[i])
                i +=4
                stack += 1    
        
stacks = [i.strip() for i in stacks]


            
with open(input_file) as f:
    moves = [[int(i) for i in line.strip('move ').strip('\n').replace('from', 'to').split(' to ')] 
             for line in f if line.startswith('move')]

def make_move(l, initial):
    number = l[0] 
    start = l[1] - 1
    dest = l[2] - 1
    new = initial.copy()
    i = 1
    while i <= number:
        new[dest] = new[start][0] + new[dest]
        new[start] = new[start][1:]
        i += 1
    return new

new = make_move(moves[0], stacks)  
for i in moves[1:]:
    new = make_move(i, new)   
    
top_of_stacks = [i[0] for i in new]

def make_move2(l, initial):
    number = l[0] 
    start = l[1] - 1
    dest = l[2] - 1
    new = initial.copy()
    new[dest] = new[start][:number] + new[dest]
    new[start] = new[start][number:]
     
    return new

new = make_move2(moves[0], stacks)  
for i in moves[1:]:
    new = make_move2(i, new)   
    
top_of_stacks_2 = [i[0] for i in new]
