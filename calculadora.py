import numpy as np

def maximo(a,b,c):
    n = [a,b,c]
    mayor = n[0]
    for i in n:
        if i > mayor:
            mayor = i
    return mayor


