
# Interpolacion de Lagrange
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

def lagrange (xi,fi):
    n = len(xi)
    x = sym.Symbol('x')
    polinomio = 0

    for i in range(0,n,1):
        
        # Termino de Lagrange
        numerador = 1
        denominador = 1
        for j  in range(0,n,1):

            if (j!=i):

                numerador = numerador*(x-xi[j])

                denominador = denominador*(xi[i]-xi[j])

        terminoLi = numerador/denominador

        polinomio = polinomio + terminoLi*fi[i]
    

    # simplifica el polinomio
    polisimple = polinomio.expand()

    # para evaluación numérica
    px = sym.lambdify(x,polisimple)

    # Puntos para la gráfica
    muestras = 101
    a = np.min(xi)
    b = np.max(xi)
    pxi = np.linspace(a,b,muestras)
    pfi = px(pxi)

    # SALIDA
    print('\n    valores de fi: ',fi)
    print('\nPolinomio de Lagrange antes de simplificar')
    print(polinomio)
    print('\nPolinomio de Lagrange: ')
    print(polisimple)

    
    puntos = np.array([1,2,2.5,3,3.5,4,5])
    
    cantidad = len(puntos)

    resultados = np.arange(cantidad, dtype= float)

    for i in range (0,cantidad):
        resultados[i] = float(polisimple.evalf(subs={x:puntos[i]}))

    for i in range (0,cantidad):

        print("\n En el punto {0:.2f}".format(puntos[i]) )
        print(" la funcion toma un valor de : {0:.56f}".format(resultados[i]))

    # Gráfica
    plt.plot(puntos,resultados,'o', label = 'Puntos')
    plt.plot(pxi,pfi, label = 'Polinomio')
    plt.legend()
    plt.xlabel('xi')
    plt.ylabel('fi')
    plt.title('Interpolación Lagrange')
    plt.show()

    return resultados

def diferenciasDivididas(xi,fi,a):
    # Tabla de Diferencias Divididas Avanzadas
    titulo = ['i   ','xi  ','fi  ']
    n = len(xi)
    ki = np.arange(0,n,1)
    tabla = np.concatenate(([ki],[xi],[fi]),axis=0)
    tabla = np.transpose(tabla)

    # diferencias divididas vacia
    dfinita = np.zeros(shape=(n,n),dtype=float)
    tabla = np.concatenate((tabla,dfinita), axis=1)

    # Calcula tabla, inicia en columna 3
    [n,m] = np.shape(tabla)
    diagonal = n-1
    j = 3
    while (j < m):
        # Añade título para cada columna
        titulo.append('F['+str(j-2)+']')

        # cada fila de columna
        i = 0
        paso = j-2 # inicia en 1
        while (i < diagonal):
            denominador = (xi[i+paso]-xi[i])
            numerador = tabla[i+1,j-1]-tabla[i,j-1]
            tabla[i,j] = numerador/denominador
            i = i+1
        diagonal = diagonal - 1
        j = j+1

    # POLINOMIO con diferencias Divididas
    # caso: puntos equidistantes en eje x
    dDividida = tabla[0,3:]
    n = len(dfinita)

    # expresión del polinomio con Sympy
    x = sym.Symbol('x')
    polinomio = fi[0]
    for j in range(1,n,1):
        factor = dDividida[j-1]
        termino = 1
        for k in range(0,j,1):
            termino = termino*(x-xi[k])
        polinomio = polinomio + termino*factor

    # simplifica multiplicando entre (x-xi)
    polisimple = polinomio.expand()

    # polinomio para evaluacion numérica
    px = sym.lambdify(x,polisimple)

    # Puntos para la gráfica
    muestras = 101
    a = np.min(xi)
    b = np.max(xi)
    pxi = np.linspace(a,b,muestras)
    pfi = px(pxi)

    # SALIDA
    np.set_printoptions(precision = 4)
    #print('Tabla Diferencia Dividida')
    #print([titulo])
    #print(tabla)
    #print('dDividida: ')
    #print(dDividida)
    print('polinomio simplificado: ' )
    print(polisimple)


    puntos = np.array([1,2,2,5,3,3.5,4,5])

    cantidad = len(puntos)

    resultados = np.arange(cantidad, dtype= float)

    for i in range (0,cantidad):
        resultados[i] = float(polisimple.evalf(subs={x:puntos[i]}))

    for i in range (0,cantidad):

        print("\n En el punto {0:.2f}".format(puntos[i]) )
        print(" la funcion toma un valor de : {0:.56f}".format(resultados[i]))

    # Gráfica
    plt.plot(puntos,resultados,'o', label = 'Puntos')
    ##for i in range(0,n,1):
    ##    plt.axvline(xi[i],ls='--', color='yellow')
    plt.plot(puntos,resultados, label = 'Polinomio')
    plt.legend()
    plt.xlabel('xi')
    plt.ylabel('fi')
    plt.title('Diferencias Divididas - Newton')
    plt.show()

    return resultados

print("\n  CASO DE ESTUDIANTES\n")

puntos = np.array([1,2,2.5,3,3.5,4,5])
n = len(puntos)
xi = np.array([1,2,3,4,5])
fi = np.array([35,83,153,193,215])
#fi = np.array([35,48,70,40,22])

cantidad = len(xi)

resultadoslagrange = np.zeros(n)
resultadosDivididas = np.zeros(n)

diferencia = np.zeros(n)
erroresLagrange = np.zeros(cantidad)
erroresDivididas = np.zeros(cantidad)

resultadoslagrange = lagrange(xi,fi)
resultadosDivididas = lagrange(xi,fi)

sumalagrange = resultadoslagrange[2]
sumadiferencias = resultadosDivididas[2]

for i in range ( 0 , n):
    diferencia[i] = abs(resultadoslagrange[i]-resultadosDivididas[i])

i = 0

while i< cantidad :
    if i<3 :
        erroresLagrange[i] = (fi[i] - resultadoslagrange[i])/fi[i] *100
        erroresDivididas[i] = (fi[i] - resultadosDivididas[i])/fi[i] *100
        i = i+1
    else :
        erroresLagrange[i] = (fi[i] - resultadoslagrange[i+1])/fi[i] *100
        erroresDivididas[i] = (fi[i] - resultadosDivididas[i+1])/fi[i] *100
        i = i+1


print("\nLa diferencia entre ambos métodos de interpolación es:\n")
print(diferencia)

print ( "\n El error relativo dado con el método de Lagrange en los puntos \n", xi ,"\n es :\n", erroresLagrange)

print ( "\n El error relativo dado con el método de Diferencias divididas de Newton en los puntos \n", xi ,"\n es :\n", erroresDivididas)

print ("\n Valor de estudiantes que sacaron 55 o menos \n", sumalagrange , "\n por lagrange\n", "\n y \n", sumadiferencias , "\n por diferencias divididas \n")
