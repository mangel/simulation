#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 00:04:59 2020

@author: mangel
"""
class SuperK:
    def __init__(self, number):
        self.X = number
    
    def __decompose(self, number):
      n = 1
      digits = []
      while number != 0:
        digit = number % 10**n
        digits.append(int(digit/10**(n-1)))
        number = number - digit
        n = n + 1
      return digits
  
    def __compose(self, digits):
      result = 0
      for i, d in enumerate(digits):
        result = result + d*(10**i)
      return result
    
    # Choose number of iterations
    def K1(self):
        self.Y = int(self.X / 10**9)
        self.next_step = self.K2
        
    # Choose random step    
    def K2(self):
        self.Z = int(self.X / 10**8) % 10
        step = 3 + self.Z
        if step == 3:
            self.next_step = self.K3
        elif step == 4:
            self.next_step = self.K4
        elif step == 5:
            self.next_step = self.K5
        elif step == 6:
            self.next_step = self.K6
        elif step == 7:
            self.next_step = self.K7
        elif step == 8:
            self.next_step = self.K8
        elif step == 9:
            self.next_step = self.K9
        elif step == 10:
            self.next_step = self.K10
        elif step == 11:
            self.next_step = self.K11
        elif step == 12:
            self.next_step = self.K12
        elif step == 13:
            self.next_step = self.K13
            
    # Ensure >= 5x10**9    
    def K3(self):
        if self.X < 5000000000:
            self.X = self.X + 5000000000
        self.next_step = self.K4
    
    # Middle square    
    def K4(self):
        self.X = int(self.X**2 / 10**5) % 10**10
        self.next_step = self.K5
    
    # Multiply
    def K5(self):
        self.X = int(1001001001 * self.X) % 10**10
        self.next_step = self.K6
    
    # Pseudo-complement
    def K6(self):
        if self.X < 100000000:
            self.X = self.X + 9814055677
        else:
            self.X = 10**10 - self.X
        self.next_step = self.K7
    
    # Interchange Halves
    def K7(self):
        self.X = 10**5 * (self.X % 10**5) + int(self.X/10**5)
        self.next_step = self.K8
    
    # Multiply    
    def K8(self):
        self.K5()
        self.next_step = self.K9
    
    # Decrease digits    
    def K9(self):
        digits = self.__decompose(self.X)
        for i,d in enumerate(digits):
            if d !=0:
                d = d -1
            digits[i] = d
        self.X = self.__compose(digits)
        self.next_step = self.K10
    
    # 99999 Modify
    def K10(self):
        if self.X < 10**5:
            self.X = self.X**2 + 99999
        else:
            self.X = self.X - 99999
        self.next_step = self.K11
    
    # Normalize    
    def K11(self):
        if self.X < 10**9:
            self.X = 10 * self.X
            self.next_step = self.K11
        else:
            self.next_step = self.K12
    
    # Modified Middle square
    def K12(self):
        self.X = int(self.X*(self.X - 1 ) / 10**5) % 10**10
        self.next_step = self.K13
    
    # Repeat?    
    def K13(self):
        if self.Y > 0:
            self.Y = self.Y - 1
            self.next_step = self.K2
        else:
            self.next_step = None
    
    def nextRandom(self):
        self.next_step = self.K1
        while True:
            self.next_step()
            if self.next_step == None:
               break
        return self.X

X = 6065038420

sk = SuperK(X)

r = sk.nextRandom()

print(r)