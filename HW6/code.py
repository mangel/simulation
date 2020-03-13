#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 22:55:26 2020

@author: mangel
"""
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
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
    
    def nextN(self, N):
        results = []
        for i in range(N):
            results.append(self.nextRandom())
        return results
        
    
    def heads_or_tails(self):
        result  = 'T'
        if float(self.x_n_m1)/m <= 0.5:
            result = 'H'
        return result

def load_data(path):
    data = []
    f = open(path, 'r')
    lines = f.readlines()
    for l in lines:
        data.append(float(l))
    return data

def compute_chi_squared(counts, expected, df):
    result = (counts-expected)**2/expected
    return np.sum(result)   

x_0 = 5003
a = 9973
c = 9929
m = 9277

ng = NumberGenerator(x_0, a, c, m)

mu = 0
sigma = 0.1

s = np.random.normal(mu, sigma, 100000)

PATH = 'Sequence.txt'

data = load_data(PATH)
#data = ng.nextN(100000)
#data = s

# It looks like it is uniform.
#plt.plot(data)
#plt.show()

# something strange happened between 0.25 and 0.4 there is an empty space.
#plt.hist(data, bins=10000)
#plt.show()

points = [x for x in data if 0.1 <= x <= 0.12]

# Ok if we choose a shorter interval we obtain some empty spaces.
#plt.hist(points, len(points))
#plt.show()

x = []
y = []
z = []

for i,d in enumerate(data[:9999]):
   x.append(data[i])
   y.append(data[i+1])
   z.append(data[i+2])
   
figure = plt.figure()
ax = Axes3D(figure)

ax.scatter(x, y,z)
plt.show()

# Chi squared

counts, bin_edges = np.histogram(data, bins=10)

plt.hist(data, bins=10)
plt.plot()

df = len(bin_edges) - 1

#because the values are uniformly distributed
expected_values = np.ones(len(counts))*(100000/10)

chi_squared_computed = compute_chi_squared(counts, expected_values, df)