import numpy as np

def multiplica(a,b):
    """
    Entrega el producto de a y b
    """
    return a*b

def factorial(a):
    value = 1
    for i in range(1,a+1):
        value = value * i
    return("El factorial es:",value)

def divide(a,b):
    if (b==0):
        return "El denominador no puede ser igual a 0"
    else:
        return a/b

def tangente(a):
	return np.tan(a)
