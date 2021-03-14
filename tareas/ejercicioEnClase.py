import sympy
import math

maxintervalo = 4
minintervalo = 0

x = (maxintervalo+minintervalo)/2
errorpermitido = 10**-5
resultado = math.exp(x)*(x)-math.pi
iteraciones = 0

while abs(resultado-math.pi)>errorpermitido:
    if (math.exp(x)*x>math.pi):
        maxintervalo= x
    else: 
        minintervalo= x
    x = (maxintervalo+minintervalo)/2
    resultado = math.exp(x)*x 
    iteraciones +=1
    print ("f(", x , ") = ", resultado - math.pi , " En la iteracion: ", iteraciones)

print (" numero de iteraciones totales : ", iteraciones , " error generado en la ultima iteracion: ", abs(resultado - math.pi), " y la raiz encontrada es : ", x)
