# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 22:09:09 2017

@author: Allen

Recursividad python
"""
def suma_elementos_vectores(vector,dimension):
    if(dimension < 0):
        return 0
    else:
        return suma_elementos_vectores(vector,dimension - 1) + vector[dimension]

def fibonacci(n):
	if(n==1 or n == 2):
		return 1
	else:
		suma = fibonacci(n-2) + fibonacci(n-1)
		return suma

def imp_fibonacci(n):
	for i in range(1,n):
		print(fibonacci(i))

def factorial(n):
	if( n == 0 ):
		return 1
	else:
		return n*factorial(n-1)

    
vector = [1,2,3]
resultado = suma_elementos_vectores(vector,len(vector)-1)
print("resultado suma: \t",resultado)

imp_fibonacci(7)

print("factorial:", factorial(4))