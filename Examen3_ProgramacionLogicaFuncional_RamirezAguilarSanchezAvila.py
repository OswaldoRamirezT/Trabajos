#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 19:05:31 2020

@author: Ramirez Aguilar Jose Oswaldo, Sanchez Avila Gustavo Angel

"""


#Primos generadores 

""" 
Primos  <generadores>  30 pts

	Realice una generador que devuelva  de todos lo numeros primos
	existentes de 0 hasta n-1 que cumpla con el siguiente prototipo:
        
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
x = [a for a in b]
print(x)
print('')

#Bada Boom!! 

"""
Bada Boom!!! <generadores> 20 pts

    Defina un generador que reciba un numero entero positivo mayor a 0 N,
	dicho generador proporciona numero de 1 hasta N
	con las siguientes condiciones:
		1) si es multiplo de 3 coloque la cadena "Bada"
		2) si es multiplo de 5 coloque la cadena "Boom!!"
		3) si es multiplo de 3 y 5 coloque "Bada Boom!!"

    def genBadaBoom(10)
    pass
    a = genBadaBoom(10)
    z = [e for e in a]
    print(z)
    #[1,2,"Bada",4,"Boom","Bada",7,8,"Bada","Boom"]
    
"""

def genBadaBoom(N):
	n = 1
	while n <= N:
		Bada = n % 3 == 0
		Boom = n % 5 == 0
		if Bada and Boom :
			yield "BadaBom!" 
		elif Bada:
			yield "Bada"
		elif Boom:
			yield "Boom"
		else:
			yield n
		n = n + 1 
        
c = genBadaBoom(30)
y = [e for e in c]
print (y,'')
print ('')

#Comprension de listas

"""


Combinaciones Comprensin de listas 30pts

	Una tienda de ropa quiere saber cuantos conjuntos se pueden crear 
	a partir de un grupo de 5 camisas (roja,negra,azul,morada y cafe),      
	4 pantalones (negro, azul, cafe obscuro y crema) y uno de 4 accesorios
	posibles (cinturon, tirantes, lentes, fedora)
	
	1) Obtenga una lista con todos los conjuntos posibles e imprimala en pantalla
	2) imprima un mensaje donde mencione la cantidad de conjuntos posibles
	
"""

A = ['roja','negra','azul','morada', 'cafe'] 
B = ['negro', 'azul', 'cafe obscuro' , 'crema']
C = ['cinturon', 'tirantes', 'lentes', 'fedora']

D = [[a,b,c] for a in A for b in B for c in C]
print (D)
print("Total de conjuntos Posibles : ",len(D))
print('')

# Fedora ?!

"""
Fedora  Comprensin de listas   15 pts

	Del problema anterior imprima una lista que tenga todos los conjuntos
	que incluyen un sombrero fedora y tambien despliegue su longitud
    
"""

def contar(L):
	if not L:
		return []
	if 'fedora' in L[0]:
		return  [L[0]]+contar(L[1:])
	else: return contar(L[1:])
LS=contar(D)
print ("Conjuntos con sombrero Fedora: ",LS)
print ("Numero de conjuntos: " , len (LS))



"""
<Monads>   30 pts

--Lacrimosa - Durch Nacht und Flut --   

Die Suche endet jetzt und hier
Gestein kalt und nass
Granit in Deiner Brust
Der Stein der Dich zerdrückt
Der Fels der Dich umgibt
Aus dem gehauen Du doch bist

Despiertate te busco
Mi corazon abreté te libro
Elevate mi luz y prende mi llama
Si a ti, yo se, te encontrare

El fragmento anterior es un canción del duo lacrimosa

Usando Monads obtenga la letra 
que menos se repite por cada linea y obtenga la probabilidad de sacar dicha
letra.

Nota: Pueden ayudarse de funciones recursivas y compresiones de lista. 

"""


"""
<Monads>

--Hole in my soul apocalyptica--  20 pts

There's a hole in my heart, in my life, in my way
And it's filled with regret and all I did, to push you away
If there's still a place in your life, in your heart for me
I would do anything, so don't ask me to leave

I've got a hole in my soul where you use to be
You're the thorn in my heart and you're killing me
I wish I could go back and do it all differently
I wish that I'd treated you differently
'Cause now there's a hole in my soul where you use to be

El fragmento anterior es un canción del grupo apocalyptica

Usando Monads obtenga la letra 
que menos se repite de todo el fragmento y obtenga la probabilidad de sacar dicha
letra.

Nota: Pueden ayudarse de funciones recursivas y compresiones de lista. 

"""





