import numpy as np
import scipy.linalg
def gaussElimin(a,b,numerDeSumas,numeroDeProductos):
    n = len(b)

    # Elimination Phase
    for k in range(0,n-1):
        for i in range(k+1,n):
            if a[i,k] != 0.0:
                lam = a [i,k]/a[k,k]
                a[i,k+1:n] = a[i,k+1:n] - lam*a[k,k+1:n]
                b[i] = b[i] - lam*b[k]
                numeroDeSumas =+1
                numeroDeProductos =+2

    # Back substitution
    for k in range(n-1,-1,-1):
        b[k] = (b[k] - np.dot(a[k,k+1:n],b[k+1:n]))/a[k,k]
        numerDeSumas=+1
    return b,numeroDeSumas,numeroDeProductos

def vandermode(v):
    n = len(v)
    a = np.zeros((n,n))
    for j in range(n):
        a[:,j] = v**(n-j-1)
    return a


v = np.array([1.0, 1.2, 1.4, 1.6, 1.8, 2.0])
bnormal = np.array([0.0, 1.0, 0.0, 1.0, 0.0, 1.0])
print ("\n vector orignial \n",v)
balterada = vandermode(bnormal)
a = vandermode(v)
print ("\n vector modificado\n",a)

errorpermitido = 10**(-16)
numeroDeSumasGauss = 0
numeroDeProductosGauss =0 

aOrig = a.copy() # Save original matrix
bOrig = bnormal.copy() # and the constant vector

x,numeroDeSumas,numeroDeProductos = gaussElimin(a,bnormal,numeroDeSumasGauss,numeroDeProductosGauss)
det = np.prod(np.diagonal(a))

print(" Resolución por método de reduccion de gauss")
print("x =\n ",x)
print("\ndet =",det)
print("\nError Calculado: [a]{x} - b =\n",np.dot(aOrig,x) - bOrig)
print("\nCantidad de sumas realizadas: {x}",numeroDeSumas)
print("\nCantidad de multiplicación: {x} ",numeroDeProductos)


y = scipy.linalg.solve(a,bnormal)
print("\n utilizando linalg.solve: ", y)
print("\nError calculado: [a]{x} - b = \n",np.dot(aOrig,y)-bOrig)