# Solución a Sistemas de Ecuaciones
# de la forma A.X=B
#http://blog.espol.edu.ec/analisisnumerico/3-5-2-numero-de-condicion/


import numpy as np
import random
import math

# INGRESO
A = np.array([[9,7,1.5],
              [4,38,11],
              [6,6.4,9]])
Adiferente = np.array([[9,7,1.5],
                    [4,38,11],
                    [6,6.9,9]])

B = np.array([[80],
              [75],
              [14]])

Bdiferente = np.array([[80],
                    [75],
                    [14],
                    [20],
                    [10],
                    [30],
                    [2],
                    [9],
                    [11],
                    [100],
                    [111],
                    [200],
                    [11],
                    [300],
                    [250],
                    [500],
                    [400],
                    [600],
                    [900],
                    [19]])

Bdispersa = np.zeros((1,20))

MatrizDispersa = np.zeros((20,20))
numerosDiferenteDe0 = np.zeros(20)

for i in range (20):
    numerosDiferenteDe0[i]=random.randint(0,20)
    Bdispersa[0,i]=random.randint(1,20)


for i in range (9):
    MatrizDispersa[random.randint(1,19)][random.randint(1,19)]=numerosDiferenteDe0[i]
        

        

numeroSumas=0
numeroProductos=0
numeroSumasD=0
numeroProductosD=0

# PROCEDIMIENTO
casicero = 1e-15 # Considerar como 0

# Evitar truncamiento en operaciones
A = np.array(A,dtype=float) 

# Matriz aumentada
def matrizAumentada (A,B):
    AB = np.concatenate((A,B),axis=1)
    AB0 = np.copy(AB)
    return AB0

# Pivoteo parcial por filas
def pivoteoParcial (AB):
    tamano = np.shape(AB)
    n = tamano[0]
    m = tamano[1]
    return n,m

# Para cada fila en AB
def ordenarPivoteo (n,AB):
    for i in range(0,n-1,1):
        # columna desde diagonal i en adelante
        columna = abs(AB[i:,i])
        dondemax = np.argmax(columna)
    
        # dondemax no está en diagonal
        if (dondemax !=0):
            # intercambia filas
            temporal = np.copy(AB[i,:])
            AB[i,:] = AB[dondemax+i,:]
            AB[dondemax+i,:] = temporal
    return AB

# eliminacion hacia adelante
def ceros_debajo_de_diagonal(AB,n,numeroSumas,numeroProductos):
    for i in range(0,n-1,1):
        pivote = AB[i,i]
        adelante = i + 1
        for k in range(adelante,n,1):
            factor = AB[k,i]/pivote
            AB[k,:] = AB[k,:] - AB[i,:]*factor
            numeroSumas= numeroSumas+1
            numeroProductos= numeroProductos+1
    return AB,numeroSumas,numeroProductos

# elimina hacia atras
def ceros_arriba_de_diagonal(AB,n,m,numeroSumas,numeroProductos):
    for i in range(n,0-1,-1):
        pivote = AB[i,i]
        atras = i-1 
        for k in range(atras,0-1,-1):
            factor = AB[k,i]/pivote
            AB[k,:] = AB[k,:] - AB[i,:]*factor
            numeroSumas= numeroSumas+1
            numeroProductos=numeroProductos+1
        # diagonal a unos
        AB[i,:] = AB[i,:]/AB[i,i]
        numeroProductos=numeroProductos+1
    X = np.copy(AB[:,m])
    X = np.transpose([X])
    return X,AB,numeroSumas,numeroProductos

def gauss_jordan(A,B,numerosumas,numeroproductos):

    AB=matrizAumentada(A,B)

    n,m = pivoteoParcial(AB)

    AB = ordenarPivoteo(n,AB)

    AB,numerosumas,numeroproductos = ceros_debajo_de_diagonal(AB,n,numerosumas,numeroproductos)

    x,AB,numerosumas,numeroproductos = ceros_arriba_de_diagonal(AB,n-1,m-1,numerosumas,numeroproductos)

    error = np.linalg.norm(np.dot(A,x)-B)

    return x,AB,error,numerosumas,numeroproductos

def remplazar_hacia_atras(AB,ultfila,ultcolumna,numeroSumas,numeroProductos):
    X = np.zeros(ultfila+1,dtype=float)
    for i in range(ultfila,0-1,-1):
        suma = 0
        for j in range(i+1,ultcolumna,1):
            suma = suma + AB[i,j]*X[j]
            numeroSumas=numeroSumas+1
            numeroProductos=numeroProductos+1
        b = AB[i,ultcolumna]
        X[i] = (b-suma)/AB[i,i]
        numeroSumas+1
        numeroProductos+1

    X = np.transpose([X])
    return X,numeroSumas,numeroProductos

def Gauss (A,B,numerosumas,numeroproductos):
    AB=matrizAumentada(A,B)

    n,m = pivoteoParcial(AB)

    AB = ordenarPivoteo(n,AB)

    AB,numerosumas,numeroproductos = ceros_debajo_de_diagonal(AB,n,numerosumas,numeroproductos)

    x,numerosumas,numeroproductos = remplazar_hacia_atras(AB,n-1,m-1,numerosumas,numeroproductos)

    error = np.linalg.norm(np.dot(A,x)-B)
    
    return x,AB,error,numerosumas,numeroproductos

def Cramer (A,B,numeroSumas,numeroProductos):
    AB = matrizAumentada
    D=np.linalg.det(A)
    n = len(B)
    numeroProductos=numeroProductos+n
    numeroSumas=numeroSumas+1
    if D != 0:

        n = len(B)
        vectorRespuestas=np.zeros(n)
        

        for i in range(n):
            Ai =A.copy()
            for j in range (n):
                Ai[j][i]=B[j]

            Di = np.linalg.det(Ai)
            vectorRespuestas[i]=Di/D
            numeroProductos=numeroProductos+1

        error = np.linalg.norm(np.dot(A,vectorRespuestas)-B)

        return vectorRespuestas,error,numeroSumas,numeroProductos

    else:
        print("\n no es posible usar Cramer \n")


# SALIDA
numeroSumas=0
numeroProductos=0
numeroSumasD=0
numeroProductosD=0

solucion,matriz,error,numeroSumas,numeroProductos=gauss_jordan(A,B,numeroSumas,numeroProductos)
solucionD,matrizD,errorD,numeroSumasD,numeroProductosD= gauss_jordan(Adiferente,B,numeroSumasD,numeroProductosD)
print("\n La solucion por Gauss-Jordan: \n",solucion,"\n Con un error de:\n",error )
print("\nDiferencia= ",(abs(solucion-solucionD)/abs(solucion))*100)
print("\nCond(A)= ", np.linalg.cond(A))
print("\nEs decir: la solución puede ser válida sólo para ", int(15-math.log( np.linalg.cond(A))), " dígitos luego de la coma.")
