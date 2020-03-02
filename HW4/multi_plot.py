#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 02:47:06 2020

@author: mangel
"""
import numpy as np
import matplotlib.pyplot as plt

# LOL
max_powers = 10**4
REALVALUE = 0.7468241328

approxs=[]
n=[]

for i in range(9000,max_powers+1):
    N = i
    
    x = np.linspace(0,1,N)
    y = np.exp(-x*x)
    
    # Monte Carlo Integration
    x = np.random.uniform(low=0, high=1, size=[N, 1])
    y = np.random.uniform(low=0, high=1, size=[N, 1])
    
    inside_bool = y <= np.exp(-x**2)
    
    x_in = x[inside_bool]
    y_in = y[inside_bool]
    
    approx = float(np.sum(inside_bool))/N
    
    print("RealValue: {}, Approximation:{}".format(REALVALUE, approx))
    approxs.append(approx)
    n.append(N)

plt.plot(n,approxs)
plt.axhline(y=REALVALUE, color='r', linestyle='-')
plt.show()

