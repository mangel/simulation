# -*- coding: utf-8 -*-
"""
Congruential Number Generator
Created on Wed Mar  4 13:03:42 2020

@author: mangel
"""
import matplotlib.pyplot as plt
import numpy as np

class NumberGenerator:
    def __init__(self, seed, a, c, m):
        self.seed = seed
        self.a = a
        self.c = c
        self.m = m
        self.x_n_m1 = seed
    
    def nextRandom(self):
        next_number = (self.a*self.x_n_m1 + self.c) % self.m
        self.x_n_m1 = next_number
        return float(next_number)/m

class ResultsCounter:
    @staticmethod
    def get_results(arr, possible_outcomes):
        results=[]
        for po in possible_outcomes:
            results.append([po, arr.count(po)])
        return results

x_0 = 5003
a = 9973
c = 9929
m = 9277

ng = NumberGenerator(x_0, a, c, m)

N_MAX = 10000
POSSIBLE_RESULTS = [True, False]

numbers = []

for i in range(N_MAX):
    numbers.append(ng.nextRandom())

# transform into a boolean array
numbers = np.array(numbers)

# Less than 0.5 means heads otherwise the result is tails.
tossed_coins = list(numbers <= 0.5)

#Histogram Data
d1_hist = ResultsCounter.get_results(tossed_coins, POSSIBLE_RESULTS)
#print(d1_hist)

# group in pairs
pairs = []
PAIRS_POSSIBLE_RESULTS = [[x,y] for x in POSSIBLE_RESULTS for y in POSSIBLE_RESULTS]

iterations = (len(tossed_coins) - len(tossed_coins) % 2)/2
iterations = int(iterations)

for n in range(iterations):
    factor = 2*n
    pairs.append([tossed_coins[factor], tossed_coins[factor + 1]])

#print(pairs)
d2_hist = ResultsCounter.get_results(pairs, PAIRS_POSSIBLE_RESULTS)
#print(d2_hist)

# group in triplets
triplets = []
TRIPLETS_POSSIBLE_RESULTS = [[x,y, z] for x in POSSIBLE_RESULTS for y in POSSIBLE_RESULTS for z in POSSIBLE_RESULTS]

iterations = (len(tossed_coins) - len(tossed_coins) % 3)/3
iterations = int(iterations)

for n in range(iterations):
    factor = 3*n
    triplets.append([tossed_coins[factor], tossed_coins[factor + 1], tossed_coins[factor + 2]])

#print(TRIPLETS_POSSIBLE_RESULTS)
d3_hist = ResultsCounter.get_results(triplets, TRIPLETS_POSSIBLE_RESULTS)
#print(d3_hist)

#Streak
item_looking_for = True # which is heads
streaks_hist=dict()
streak=0
for item in tossed_coins:
    if item == item_looking_for:
        streak = streak + 1
    else:
        if streak >= 1:
            if streak in streaks_hist.keys():
                streaks_hist[streak] = streaks_hist[streak] + 1
            else:
                streaks_hist[streak] = 1
        streak = 0

# If there is a last result must be counted
if streak >= 1:
    if streak in streaks_hist.keys():
        streaks_hist[streak] = streaks_hist[streak] + 1
    else:
        streaks_hist[streak] = 1
    streak = 0

#sort the results
keys = sorted(streaks_hist.keys())
sorted_streaks_hist = dict()
for k in keys:
    sorted_streaks_hist[k] = streaks_hist[k]
    
#print(tossed_coins)            
print(streaks_hist)
print(sorted_streaks_hist)
