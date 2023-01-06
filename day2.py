# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 13:09:50 2022

@author: daisy
"""

input = "C:/Users/daisy/OneDrive/Documents/advent_of_code/input_day2.txt"

with open(input) as file:
    dict_of_plays = {}
    n = 1
    for line in file:
        line = line.strip('\n')
        line = line.split(' ')
        dict_of_plays[n] = tuple(line)
        n += 1
        

def get_scores(d):
    total_score = 0
    for i in d:
        if d[i][0] == 'A':
            if d[i][1] == 'X':
                total_score += 3
            if d[i][1] == 'Y':
                total_score += 6
        if d[i][0] == 'B':
            if d[i][1] == 'Y':
                total_score += 3
            if d[i][1] == 'Z':
                total_score += 6   
        if d[i][0] == 'C':
            if d[i][1] == 'Z':
                total_score += 3
            if d[i][1] == 'X':
                total_score += 6
        if d[i][1] == 'X':
            total_score += 1
        if d[i][1] == 'Y':
            total_score += 2
        if d[i][1] == 'Z':
            total_score += 3
    
    return total_score            

##second method

score = get_scores(dict_of_plays)

score_dict = {('A', 'X'): 4, 
              ('A', 'Y'): 8, 
              ('A', 'Z'): 3,
              ('B', 'X'): 1,
              ('B', 'Y'): 5,
              ('B', 'Z'): 9,
              ('C', 'X'): 7,
              ('C', 'Y'): 2,
              ('C', 'Z'): 6}

score2 = 0
for i in dict_of_plays:
    score2 += score_dict[dict_of_plays[i]]
    
##second question
## rock = A, paper = B, scissors = C

lose = {'A': 'C', 'B': 'A', 'C': 'B'}
win = {'A': 'B', 'B': 'C', 'C':'A'}

def get_scores_2(d):
    total_score = 0
    for i in d:
        if d[i][1] == 'X':
            you_play = lose[d[i][0]]
        if d[i][1] == 'Y':
            total_score += 3
            you_play = d[i][0]
        if d[i][1] == 'Z':
            total_score += 6
            you_play = win[d[i][0]]
        if you_play == 'A':
            total_score += 1
        if you_play == 'B':
            total_score += 2
        if you_play == 'C':
            total_score += 3
    return total_score
            
score3 = get_scores_2(dict_of_plays)
