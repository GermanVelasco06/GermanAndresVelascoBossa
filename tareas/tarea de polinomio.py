respuesta = "si"

print ( " Digite el grado de su polinomio ")
gradoDelPolinomio =int ( input())
coeficientes = [0 for i in range (gradoDelPolinomio+1)]
exponentes = [0 for i in range (gradoDelPolinomio+1)]
i = 0
contador = 0



def resolverPolinomio (grado,coeficientes,x,contador):
    resultado = 0
    resultado = int(coeficientes[grado])
    i = grado
    
    while i>0 : 
        resultado = resultado *x + int(coeficientes[i-1])
        contador +=1
        i-=1
    print ("multiplicaciones: ", contador)
    return resultado
    

    



for i in range (0,gradoDelPolinomio +1):
    print (" escriba el coeficiente para el termino de x elevado a ", i)
    coeficientes [i] = input()

    

print ( " Digite el valor de x ")
x = int(input())
print("El resultado es: " , resolverPolinomio(gradoDelPolinomio,coeficientes,x,contador))

