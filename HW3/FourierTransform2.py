#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

"""
    Takes a SymPy Function f on (0, P) and returns the values of the Fourier
    series of the function f(x) at the point x.
"""
def FourierTrigonometricSeries(f, P, x, n):
    a_0 = 2/P * integrate.quad(f, 0, P)[0]
    acum = 0
    l_ak = lambda a: f(a) * np.cos(a*2*np.pi*k/P)
    l_bk = lambda a: f(a) * np.sin(a*2*np.pi*k/P)
    for k in range(1, n+1):
        a_k = 2/P * integrate.quad(l_ak, 0, P, x)[0]
        b_k = 2/P * integrate.quad(l_bk, 0, P, x)[0]
        acum = a_k + b_k        
    return a_0 + acum

N = 6
f = lambda x: 1-x
P = 1

dom = np.linspace(-2*P, 2*P, N)

y = FourierTrigonometricSeries(f, P, dom, N)

plt.plot(dom,y)
plt.show()
