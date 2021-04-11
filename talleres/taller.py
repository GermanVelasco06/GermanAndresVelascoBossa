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

a = spi.CubicHermiteSpline(x,y,dydx)

polinomio = np.array([a.c[0,0],a.c[1,0],a.c[2,0],a.c[3,0]])

funcion = f(polinomio)

arreglo = np.zeros(50)
arr1 = np.linspace(0,2,50)

grafica(arr1,a(arr1))
print (funcion)
