import math
import sympy as sp
from math import factorial
print ("Valor esperado de raiz de 0,088")
print(round(pow(0.088, 1/2),8))
x = sp.symbols('x')
f = x**(1/2)
n = 12
valor = 0.088
a = 0.05


def primero (f, n, a):
    resultado = 0
    for i in range (0, n+1):
        derivada = f.diff(x,i)

        resultado +=(sp.N(f,subs = {x: a})*(valor-a)**i)/(factorial(i))
    return resultado


print ("Valor calculado por polinomio de Taylor de raiz de 0,088")
print (round(primero (f,n,a),8))

print ("Valor esperado de e elevado a 2,5")
esperado = math.exp(2.5)
print ( esperado )
errorPermitido = 10**-7
y = sp.symbols('y')
e = sp.symbols('e')
formula = e**y
valor = 2.5
a = 0


def segundo (f,valor, a,errorPermitido):
    j = 0
    resultado = 0
    while ( abs(resultado-esperado)>errorPermitido):
        derivada = f.diff(y,j)
        resultado +=(sp.N(f,subs = {y: a, e : math.exp(1)})*(valor-a)**j)/(factorial(j))
        j = j + 1
    return resultado

print ("Valor calculado por polinomio de taylor de e elevado a la 2,5")
print ( segundo (formula,valor,a,errorPermitido))
    


