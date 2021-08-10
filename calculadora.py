import numpy as np

# Juan Sebastián Rodríguez Páez
def factorial(a):
    value = 1
    for i in range(1,a+1):
        value = value * i
    return("El factorial es:",value)
