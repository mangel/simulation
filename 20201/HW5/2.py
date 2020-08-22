#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 05:07:19 2020

@author: mangel

Most of the code used and some parts of the explanations I took it from
https://tailcall.net/blog/cracking-randomness-lcgs/

I only rewritte some parts of the code to make it work on a OOP model and in the
end to learn.
"""
from functools import reduce
from math import gcd

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
        return next_number

class NumberGeneratorCracker:    
    def __init__(self, values):
        self.values = values
    
    # Simple modular equation after we know the multiplier and the modulus
    def get_unknown_increment(self, a, m):
        result = {"modulus": m, "multiplier":a, "increment": (self.values[1] - self.values[0]*a) % m}
        return result
    
    # We have linear equations with two unknowns (if you already have the increment and the modulus).
    def get_unknown_multiplier(self, m):
        self.a = (self.values[2] - self.values[1]) * self.modinv(self.values[1] - self.values[0], m) % m
        return self.get_unknown_increment(self.a, m)
    
    #We build a system of congruences(linear) to find the modulus.
    def get_unknown_modulus(self):
        # constructing a list that contains the difference of the results when i=j. (the diagonal).
        diffs = [s1 - s0 for s0, s1 in zip(self.values, self.values[1:])]
        #Computing the different
        zeroes = [t2*t0 - t1*t1 for t0, t1, t2 in zip(diffs, diffs[1:], diffs[2:])]
        #We perform with reduce and gcd, a serires of computations of the GCD.
        self.m = abs(reduce(gcd, zeroes))
        return self.get_unknown_multiplier(self.m)
    
    def crack(self):
        return self.get_unknown_modulus()
    
    def modinv(self, b, n):
        g, x, _ = self.egcd(b, n)
        if g == 1:
            return x % n
    
    # Euclid's Division algorithm
    def egcd(self, a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, x, y = self.egcd(b % a, a)
            return (g, y - (b // a) * x, x)

m=0
a=0
c=0

S = [137, 553, 990, 881, 646, 618, 323, 832, 897, 230, 181, 432, 44, 925, 525, 695, 367, 711, 974, 274]

cracker = NumberGeneratorCracker(S)

results = cracker.crack()
print(results)

ng = NumberGenerator(S[0], results["multiplier"], results["increment"], results["modulus"])

generated = [S[0]]
for i in range(len(S)-1):
    generated.append(ng.nextRandom())

print(generated)
print("Comparison result:{}".format(S==generated))