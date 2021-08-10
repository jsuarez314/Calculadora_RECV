import numpy as np

def raiz(a):
  if a<0:
    print('El número no puede ser negativo')
    return None
  else:
    return np.sqrt(a)
