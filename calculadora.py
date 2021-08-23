import numpy as np

def cubo(a):
	return a**3


def fibonacci(a):

	serie =  0
	s = 0
	f0 ,f1  = 0,1  #primeros dos terminos
	lista  =  []

	#verificar que sea mayor  a  0
	if a == 0:

		print("El  número debe ser mayor a 0")

	#verificar que no sea un numero decinal
	elif a / a != 1:
		print("utilice numero entero")

	elif a == 1:
		print(f0)

	else:
		while serie < a:  
			lista.append(f0)
			s=  f0  + f1
			f0  = f1
			f1 = s
			serie =  serie + 1 
			
	return lista 



def raiz(a):
  if a<0:
    print('El número no puede ser negativo')
  else:
    return np.sqrt(a)

def sen(a):
    return np.sin(a)


def coseno(a):
  return np.cos(a)

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
