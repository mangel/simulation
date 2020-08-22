#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 02:28:35 2020

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
    
    def heads_or_tails(self):
        result  = 'T'
        if float(self.x_n_m1)/m <= 0.5:
            result = 'H'
        return result

x_0 = 5003
a = 9973
c = 9929
m = 9277

ng = NumberGenerator(x_0, a, c, m)

N_MAX = 10000

numbers = [float(x_0)/m]
letters = [ng.heads_or_tails()]

for i in range(1, N_MAX):
    numbers.append(ng.nextRandom())
    letters.append(ng.heads_or_tails())

#Organize in Pairs
iterations = (len(letters) - len(letters) % 2)/2
iterations = int(iterations)

pairs = []
for n in range(iterations):
    factor = 2*n
    pairs.append(letters[factor] + letters[factor + 1])

#Organize in triplets
iterations = (len(letters) - len(letters) % 3)/3
iterations = int(iterations)

triplets = []
for n in range(iterations):
    factor = 3*n
    triplets.append(letters[factor] + letters[factor + 1] + letters[factor + 2])

#streaks
#Streak
item_looking_for = 'H' # which is heads
streaks = []
streak=0
for item in letters:
    if item == item_looking_for:
        streak = streak + 1
    else:
        if streak >= 1:
            streaks.append(item_looking_for*streak)
        streak = 0

# If there is a last result must be counted
if streak >= 1:
    streaks.append(item_looking_for*streak)
    streak = 0

#plot histograms
n, bins, patches = plt.hist(sorted(letters), bins=2)
plt.show()

print(n)

n, bins, patches = plt.hist(sorted(pairs), bins=4)
plt.show()

print(n)

n, bins, patches = plt.hist(sorted(triplets), bins=8)
plt.show()

print(n)

#Special manipulation to display the graph
streaks_hist  = []
for i in streaks:
    streaks_hist.append(str(len(i)))

n, bins, patches = plt.hist(sorted(streaks_hist), bins=len(set(streaks_hist)))
plt.show()

print(n)