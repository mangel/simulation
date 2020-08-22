#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 02:47:06 2020

@author: mangel
"""
import numpy as np
import matplotlib.pyplot as plt

N=10000
REALVALUE = 0.7468241328

x = np.linspace(0,1,N)
y = np.exp(-x*x)

plt.plot(x,y)
plt.show()

plt.plot(x,y)
plt.fill_between(x,y)
plt.show()

# Monte Carlo Integration
x = np.random.uniform(low=0, high=1, size=[N, 1])
y = np.random.uniform(low=0, high=1, size=[N, 1])

inside_bool = y <= np.exp(-x**2)

x_in = x[inside_bool]
y_in = y[inside_bool]

approx = float(np.sum(inside_bool))/N

print("RealValue: {}, Approximation:{}".format(REALVALUE, approx))

plt.scatter(x, y)
plt.scatter(x_in, y_in, color='r')
plt.show()

