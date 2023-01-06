# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 13:51:09 2022

@author: daisy
"""

input_file = "C:/Users/daisy/OneDrive/Documents/advent_of_code/input_day3.txt"

backpacks= []
with open(input_file) as file:
    for line in file:
        line = line.strip('\n')
        backpacks.append(line)

common_items = []

for pack in backpacks:
    items_in_comp = int(len(pack)/2)
    for i in pack[:items_in_comp]:
        if i in pack[items_in_comp:]:
            common_items.append(i)
            break

priority_dict = {'a': 1,
                 'b': 2,
                 'c': 3,
                 'd': 4,
                 'e': 5,
                 'f': 6,
                 'g': 7,
                 'h': 8,
                 'i': 9,
                 'j': 10,
                 'k': 11,
                 'l': 12,
                 'm': 13,
                 'n': 14,
                 'o': 15,
                 'p': 16,
                 'q': 17,
                 'r': 18,
                 's': 19,
                 't': 20,
                 'u': 21,
                 'v': 22,
                 'w': 23,
                 'x': 24,
                 'y': 25,
                 'z': 26}

total_priority = 0

for i in common_items:
    if i.isupper():
        total_priority += 26
    total_priority += priority_dict[i.lower()]


# test = 'xhbvdgsdkjasdw'

# common_items = []

# for i in test[:int(len(test)/2)]:
#     if i in test[int(len(test)/2):]:
#         common_items.append(i)
#         break

in_threes = [[]]
with open(input_file) as file:
    n = 0
    for line in file:
        line = line.strip('\n')
        if len(in_threes[n]) < 3:
            in_threes[n].append(line)
        else:
            n += 1
            in_threes.append([])
            in_threes[n].append(line)

# test1 = ['vJrwpWtwJgWrhcsFMMfFFhFp',
# 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
# 'PmmdzqPrVvPwwTWBwg']

# for item in test1[0]:
#     if item in test1[1] and item in test1[2]:
#         print(item)
#         break

badges =[]
for three in in_threes:
    for item in three[0]:
        if item in three[1] and item in three[2]:
            badges.append(item)
            break
                    
badges_priority = 0

for i in badges:
    if i.isupper():
        badges_priority += 26
    badges_priority += priority_dict[i.lower()]