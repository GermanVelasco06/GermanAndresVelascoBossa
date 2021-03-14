import numpy as np

matriz=np.array ([1,-2,2,-3,0],
        [3,4,-1,1,0],
        [2,-3,2,-1,0],
        [1,1,-3,-2,0])

tamaniofilas = 4
tamaniocolumnas = 4
vector = np.array(2,4,5,6)

def matrizaumentada(matriz,vector,tamaniocolumnas):
    numero = len(vector)-1
    for i in range (0, numero):
        matriz(i,tamaniocolumnas) = vector(i)
    
    return matriz

def ceros_debajo_de_la_diagonal (matriz,tamaniocolumnas,tamaniofilas):
    for i in range (0, tamaniocolumnas-1): 
        for j in range (tamaniofilas-1,1):
            if matriz[i][j] !=0:
                for k in range (0,tamaniocolumnas):
                    if matriz [i][j] <0 and matriz [1][j]>0 or matriz [i][j]>0 and matriz[1][j]<0 :
                        matriz[i][j+k] = (matriz[1][1]/matriz[i][j]*matriz[1,j+k])+matriz[i][j+k]
                    else:
                        matriz[i][j+k] = (matriz[1][1]/matriz[i][j]*matriz[1,j+k])-matriz[i][j+k]
    return matriz        

def ceros_arriba_de_la_diagonal (matriz,tamaniocolumnas,tamaniofilas):
    for i in range (0,tamaniofilas-1):
        for j in range (tamaniocolumnas-2,0):
            if matriz[i][j]!= 0 :
                for k in range (0,tamaniocolumnas):
                    if matriz [i][j] <0 and matriz [1][j]>0 or matriz [i][j]>0 and matriz[1][j]<0 :
                        matriz[i][j+k] = (matriz[1][1]/matriz[i][j]*matriz[1,j+k])+matriz[i][j+k]
                    else:
                        matriz[i][j+k] = (matriz[1][1]/matriz[i][j]*matriz[1,j+k])-matriz[i][j+k]
    return matriz

def resultado (matriz, tamaniocolumnas, tamaniofilas):
    for i in range (0,tamaniofilas-1):
        vector [i]= matriz[i][tamaniocolumnas]
    return vector


print("\n matriz: \n", matriz, "\n Vector: \n", vector)
matriz = matrizaumentada(matriz,vector,tamaniocolumnas)
print("\n matriz aumentada: \n", matriz)
matriz = ceros_debajo_de_la_diagonal(matriz,tamaniocolumnas,tamaniofilas)
print("\n matriz con 0 abajo de la diagonal principal: \n", matriz)
matriz = ceros_arriba_de_la_diagonal (matriz,tamaniocolumnas,tamaniofilas)
print ("\n matriz con 0 arriba y abajo de la diagonal principal: ", matriz)
print ("\n Respuest: \n", resultado(matriz,tamaniocolumnas,tamaniofilas))

