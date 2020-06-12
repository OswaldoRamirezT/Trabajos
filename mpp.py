# -*- coding: utf-8 -*-
"""
Created on June 09 18:38:46 2020

@author: Ramirez Aguilar Jose Oswaldo y Sanchez Avila Gustavo
"""
"""
# Programación  Lógica

# Modus ponendo ponens

"el modo que, al afirmar, afirma"

P → Q. P ∴ Q


Se puede encadenar usando algunas variables

P → Q. 
Q → S. 
S → T. P ∴ T

Ejercicio 
Defina una funcion que resuelva con verdadero o falso segun corresponada

Laura esta en Queretaro
Alena esta en Paris
Claudia esta en San Francisco
Queretaro esta en Mexico
Paris esta en Francia
San Francisco esta en EUA
Mexico esta en America
Francia esta en Europa
EUA esta en America

def esta(E1,E2):
	pass


print(esta("Alena","Europa"))
# true

print(esta("Laura","America"))
# true

print(esta("Laura","Europa"))
# false

Base = [
	["Laura","Queretaro"],
	["EUA","America"]
]

"""
Base = [
	["Laura","Queretaro"],
    ["Alena","Paris"],
    ["Claudia","San Francisco"],
    ["Queretaro","Mexico"],
    ["Paris","Francia"],
    ["San Francisco","EUA"],
    ["Mexico","America"],
    ["Francia","Europa"],
	["EUA","America"]
]

def ubicacion(X,Y):
	if not X:
		return []
	if len(X):
		if Y == X[0][0]:
			return X[0][1]
		else:
			return ubicacion(X[1:],Y)


def sEncuentra (E1,E2):
	R = ubicacion(Base,E1)
	L = ubicacion(Base, R)
	if L == E2 or R == E2:
		return True
	S = ubicacion(Base, L)
	if S == E2:
		return True
	else:
		return False
    
print(sEncuentra("Alena","Europa"))# true


print(sEncuentra("Laura","America"))# true


print(sEncuentra("Laura","Europa")) # false
