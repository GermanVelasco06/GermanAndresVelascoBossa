import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

# Grafica de campo direccional
def f(x,y):
    return np.exp(-x**2)*x

n=20
x = np.linspace(-10,10,n)
y = np.linspace(-10,10,n)
X,Y = np.meshgrid(x,y)

u = 1
v=f(X,Y)
u2,v2 = u/np.sqrt(u**2+v**2),v/np.sqrt(u**2+v**2)
fig= plt.figure(figsize=(10,6))

plt.quiver(X,Y,u2,v2,color = 'k')
plt.grid(True)
plt.title("Campos direccionales de la ecuación diferencial")
plt.show()

#Resolver ecuación diferencial
x,e = sp.symbols('x e')
y = sp.Function('y')(x)
dydx = y.diff(x)
expr = sp.Eq(dydx,sp.exp(-x**2)*x)
solucion = sp.dsolve(expr)
print(solucion)
