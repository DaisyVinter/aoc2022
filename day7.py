# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 17:09:57 2023

@author: daisy
"""
import string

input_file = "C:/Users/daisy/OneDrive/Documents/advent_of_code/input_day7.txt"

folder_dict = {}

with open(input_file) as f:
    for line in f:
        if line.startswith('$ cd '):
            folder = line.strip('\n')[5:]
            if folder != '..':
                folder_dict[folder] = []
        elif line.startswith('dir'):
            folder_dict[folder].append(line.strip('\n')[4:])
        elif line[0] in string.digits:
            folder_dict[folder].append(line.strip('\n').rstrip(string.ascii_letters + string.punctuation).rstrip())
            

sizes = {}

for key in folder_dict.keys():
    folder = folder_dict[key]
    sizes[key] = 0

    
folder = folder_dict['qsmg']
sizes['/'] = 0

def sum_files(folder, folder_dict):
    size = 0
    for i in folder:
        if i.isnumeric():
            print(i)
            size += int(i)
        else:
            sum_files(folder_dict[i], folder_dict)
    return size

size = sum_files(folder, folder_dict)

