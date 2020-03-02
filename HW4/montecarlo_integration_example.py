#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 01:33:22 2020

@author: mangel
"""
import numpy as np
import matplotlib.pyplot as plt

N = 1000000

x = np.random.uniform(low=-1, high=1, size=[N, 1])
y = np.random.uniform(low=-1, high=1, size=[N, 1])

inside_bool = x**2+ y**2 < 1

approx_pi = 4 * np.sum(inside_bool)/N

print("Pi: {}, Approximation {}".format(np.pi, approx_pi))

x_in = x[inside_bool]
y_in = y[inside_bool]

plt.figure(figsize=[5,5])
plt.scatter(x, y, s=1)
plt.scatter(x_in, y_in, color='r', s=1)
plt.show()