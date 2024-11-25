#Luis Ariza Truan
#25 de Noviembre de 2024
#Alritmo para ordenar tabla de mayor a menor

L=[5,2,6,1,9] #He creado la lista y se guarda en variable llamada L

lis_ord = L.copy() #Aqui creo una copia de la lista L, que es con la que voy a hacer las comparaciones
seguir = True #En una variable llamada seguir guardo un True para que acceda al bucle

while seguir: #Hago un bucle while, ya que nose cuantas veces se va a repetir
    seguir = False

    for i in range(len(L) - 1): #Recorre con el valor i, la longitud de la lista entera, y se pone el -1, ya que si hay 5 valores tiene que hacer 4 comparaciones
        
        if L[i] <= L[i+1]: #Aqui pregunto que se el valor por ejemplo situado en la posición 1 es menor que el de la posición 2, si es así accede a hacer intercambio
            lis_ord[i], lis_ord[i+1] = lis_ord[i+1], lis_ord[i] #Entra a hacer el intercambio y esto lo que hace es si el que etsa en la posición 1 es menor que el que esta en la posición 2, el de la posición 2 se pone en la 1, y e de la posición 1 se pone en la 2
            seguir = True #Aquí indico que si se ha realizado un intercambio y es posible que la lista no esté entera ordenada, siga continuando el bucle

    L = lis_ord #Simplemente con esto es que actualizo los cambios realizados en la copia de la lista y se guardan en la lista original

#Una vez se ha ordenado la tabla entera se muestra con un print que he utilizado
print("La lista ordenada es: ", L) 

