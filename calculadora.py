import numpy as np

def fibonacci(a):

	serie =  0
	s = 0
	f0 ,f1  = 0,1  #primeros dos terminos

	

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
			print(f0)
			s=  f0  + f1
			f0  = f1
			f1 = s
			serie =  serie + 1 

 
