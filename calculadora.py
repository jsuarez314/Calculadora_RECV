import numpy as np

def minimo(a,b,c):
    res=c
    if(a<=b and a<=c):
        res=a
    elif(b<=c):
        res=b
    return res