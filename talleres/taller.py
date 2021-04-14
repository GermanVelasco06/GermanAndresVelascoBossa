#taller

import scipy.interpolate as spi
import numpy as np
import random
import sympy as sp
import matplotlib.pyplot as plt

def f(a):

    x = sp.symbols('x')

    y = len(a)


    f = a[0]*x**0+ a[1]*x**1 + a[2]*x**2 + a[3]*x**3

    return f

def grafica(arr,arr1):

    plt.plot(arr, arr1,'r--')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title("Grafica")
    plt.show()

def evalPoli(polinomio, x):
    r = polinomio[0]
    n = len(polinomio)
    for i in range (1, n):
        r = polinomio[i] *x+ r    

    return r


x = np.array([0,1,2])

y = np.array([10.5,15.33,5.789])

dydx = np.array([1,(y[1]-y[0])/(x[1]-x[0]),(y[2]-y[1])/(x[2]-x[1])])

a = spi.CubicSpline(x,y,bc_type=((1,dydx[0]),(1,dydx[2])))
b = spi.CubicHermiteSpline(x,y,dydx)

polinomio = np.array([a.c[3,0],a.c[2,0],a.c[1,0],a.c[0,0]])
polinomio2 = np.array([b.c[3,0],b.c[2,0],b.c[1,0],b.c[0,0]])

funcion = f(polinomio)
funcion2 = f(polinomio2)

arreglo = np.zeros(50)
arr1 = np.linspace(0,2,50)
arr3 = np.array([0,1,2])

print("\nfuncion hallada con el método de spline cubico: {}\n".format(funcion))
print("\nfuncion hallda con el método de hermite: {} \n".format(funcion2))

print("\nSpline cubico\n")
print(evalPoli(polinomio,0))
print(evalPoli(polinomio,1))
print(evalPoli(polinomio,2))

print("\nHermite\n")
print(evalPoli(polinomio2,0))
print(evalPoli(polinomio2,1))
print(evalPoli(polinomio2,2))

print("\nDiferencia\n")
print(abs(evalPoli(polinomio,0)-evalPoli(polinomio2,0)))
print(abs(evalPoli(polinomio,1)-evalPoli(polinomio2,1)))
print(abs(evalPoli(polinomio,2)-evalPoli(polinomio2,2)))

print ("\nError spline cubico\n")
print(abs(evalPoli(polinomio,0)-10.5))
print(abs(evalPoli(polinomio,1)-15.33))
print(abs(evalPoli(polinomio,2)-5.789))

print ("\nError Hermite\n")
print(abs(evalPoli(polinomio2,0)-10.5))
print(abs(evalPoli(polinomio2,1)-15.33))
print(abs(evalPoli(polinomio2,2)-5.789))

grafica(arr1, a(arr1))
grafica(arr1,b(arr1))

print("\nspline cubico\n")
print(a.c)

print("\nHermite\n")
print(b.c)
