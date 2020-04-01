#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 21:05:31 2020

@author: Ramirez Aguilar Jose Oswaldo, Sanchez Avila Gustavo Angel

"""


#Primos generadores 

""" 
    def gprimo(10)
        pass
        
    a = gprimo(10)
    z = [e for e in a]
    print(z)
    #[2,3,5,7]
    
"""

def Primo(N):
    if N < 2:
        return False
    for i in range(2,N):
        if N % i == 0:
            return False
    return True

def gPrimo(LMT):
    N = 0
    while N <= LMT:
        if Primo(N):
            yield N
        N = N + 1

b = gPrimo(10)
z = [a for a in b]
print(z)
print('')

#Bada Boom!! 

"""
    def genBadaBoom(10)
    z = [e for e in a]
    print(z)
    
"""