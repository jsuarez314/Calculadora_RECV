import numpy as np

def producto_punto(a,b):
	#Tarea de Jose Alejandro Cubillos Muñoz
	#Código: 201313719
	
	#Pasamos a np.arrays por si alguien mete arrays no np
	a_n=np.array(a);
	b_n=np.array(b);
	if len(a_n)!=len(b_n) and a_n.ndim==1 and b_n.ndim==1:
		print("Por favor meta vectores del mismo tamaño");
		resp=0;
	elif len(a_n[0,:])!=len(b_n[:,0]) and a_n.ndim==2 and b_n.ndim==2:
		print("Asegurese que el número de columnas de la primera matriz...");
		print("... sea igual al número de filas de la segunda matriz");
		resp=0;
	else:
		resp=a_n.dot(b_n);
	#fin if 
	return resp;
#fin función

