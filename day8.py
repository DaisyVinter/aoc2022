# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 17:10:23 2023

@author: daisy
"""

import numpy as np

test_array = np.array([[3,0,3,7,3],
                        [2,5,5,1,2],
                        [6,5,3,3,2],
                        [3,3,5,4,9]])

input_file = "C:/Users/daisy/OneDrive/Documents/advent_of_code/input_day8.txt"


with open(input_file) as f:
    tree_grid = np.array([[int(x) for x in line.strip('\n')] for line in f])

        
def total_visible(array):
    total_visible = 0
    outside_trees =  array.shape[0]*2 + array.shape[1]*2 - 4
    total_visible += outside_trees
    for i in range(1, array.shape[0]-1):
        for j in range(1, array.shape[1]-1):
            if ((array[i, j] > array[i, :j].max()) or 
                (array[i, j] > array[i, j+1:].max()) or
                (array[i, j] > array[:i, j].max()) or
                (array[i, j] > array[i+1: ,j].max())):
                    total_visible += 1
    return total_visible

# print(total_visible(test_array))
        
print(total_visible(tree_grid))
        
def get_distance(start_position, direction):
    for n, tree in enumerate(direction, 1):
        if tree >= start_position:
            return n
            break
    return n

def get_scenic_score(array, i, j):
    tree = array[i, j]
    d1 = get_distance(tree, array[i, j-1::-1])
    d2 = get_distance(tree, array[i, j+1:])
    d3 = get_distance(tree, array[i+1:, j])
    d4 = get_distance(tree, array[i-1::-1, j])
    score = d1*d2*d3*d4
    return score
    
def get_all_scores(array):
    scores = []
    for n, i in enumerate(array):
        if n == 0 or n == array.shape[0]-1:
            continue
        else:
            for m, j in enumerate(array[n]):
                if m == 0 or m == array.shape[1]-1:
                    continue
                else:
                    score = get_scenic_score(array, n, m)
                    scores.append(score)
    return scores

print(max(get_all_scores(tree_grid)))       
        
    