# -*- coding: utf-8 -*-
"""
Congruential Number Generator
Created on Wed Mar  4 13:03:42 2020

@author: magomez
"""
import matplotlib.pyplot as plt
import numpy as np

def take_in_pairs(arr):
    needs_additional_element = len(arr) % 2 == 1
    remainder = None
    pass

def take_in_triplets(arr):
    pass

x_0 = 5003
x = np.array(x_0)
a = 9973
c = 9929
m = 9277

N_MAX = 10
x_nm1 = x_0
u = np.array(float(x_0)/m)

for i in range(1,N_MAX):
    random_number = (a* x_nm1 + c) % m
    x = np.append(x,random_number)
    x_nm1 = random_number
    u = np.append(u,float(random_number)/m)
    
print(x)
print(u)

heads = u <= 0.5 
tails = u > 0.5

print("Heads: {}, Tails: {}".format(sum(heads), sum(tails)))

plt.hist(u, bins=2)
plt.show()

ordinate = np.arange(0,N_MAX)

plt.scatter(ordinate, u)
plt.show()

n = 2
iterations = int((len(u) - len(u) % n)/n)

n_plet = []

for i in range(iterations):
    n_plet.append([u[n*i] <= 0.5, u[n*i +1] < 0.5])

categories = [[x,y] for x in vals for y in vals]

print(categories)



print(bool_results)
