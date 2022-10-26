#!/usr/bin/env python
# coding: utf-8
"""
Programa para generar polinomios

La primer función genera polinomios de números enteros menores 
que abs(n) <= N, con m < M elementos, encapsulados en blanco, 
corchetes circulares, corchetes cuadrados o llaves, según el 
nivel "l" < L de profunidad asignado.
"""

import numpy as np


p = lambda N,M: np.random.randint(low = -N, high = N+1, size = M , dtype=int) 

def noDuplicados(N,M): #Quita duplicados y ceros
    lX = 0; lnX = 1
    while lX != lnX:
        X = p(N,M)
        cX  = [e for e in p(N,M) if e !=0] # Quita los ceros...
        nX = list(dict.fromkeys(cX))       # Quita repetidos
        lX = len(X); lnX = len(nX)        
    return nX              

def terminales(x):
    c = '  ()[]{}' 
    return  c[2*x], c[2*x+1] 
    
def P(N,M,l,z):
    #M = M if M > 3 else 3 # no menos de tres elementos por polinomio
    r1, r2 = '', '' #terminales(l)
    X = noDuplicados(N,M) # ni ceros
    s = r1
    for x in X:
        r = ' + ' if x >= 0 else ' - '
        s += r + str(abs(x)) 
    s += r2  
    
    s = s[2:] if z == 0 and '+' in s[0:2] else s  # z == 0, quita el "+" de inicio
    
    return s


tf = lambda : np.random.choice([True, False])
op = lambda : np.random.randint(low = -10, high = 9, size = 10 , dtype=int)[0]

def c():
    aux = op()
    if aux == 1: return ' + '
    s = ' + ' if aux > 0 else ' - ' 
    return  s + str(abs(aux))
    
def Ps(N,M, N0, N1, N2, N3):
    s = ''
    for n0 in range(N0):
        #if not tf(): break 
        s += P(N,M,0,0) if n0 == 0 else P(N,M,0,1)
        for n1 in range(N1):
            if not tf(): break
            s += c() + '(' + P(N,M,0,0)
            for n2 in range(N2):
                if not tf(): break
                s += c() + '[' + P(N,M,0,0)
                for n3 in range(N3):
                    if not tf(): break
                    s += c() +'{' + P(N,M,0,0)
                    s += '}' 
                s += ']'
            s += ')'
    return s


if __name__ == "__main__":
    N = 9; M = 3
    N0 = 3
    N1 = 2
    N2 = 3
    N3 = 3
    print(Ps(N,M, N0, N1, N2, N3))


# In[ ]:





# In[ ]:




