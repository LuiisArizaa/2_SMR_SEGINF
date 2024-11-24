#Luis Ariza Truan
#22 de Noviembre de 2024
#Algorítmo para ordenar una lista de mayor a menor

def ordenar_descendente(lista): 
    # Obtener el tamaño de la lista
    n = len(lista)
    
    # Utilizo un for in range para recorrer la lista desde el principio
    for i in range(n):
        # Indicador de si hubo algún intercambio en esta iteración
        intercambio = False
        
        # Comparar elementos adyacentes, hasta el penúltimo elemento no ordenado
        for j in range(n - i - 1):
            # Si el elemento de la izquierda es menor que el de la derecha
            if lista[j] < lista[j + 1]:
                # Intercambiar los elementos
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambio = True
        
        # Si no hubo intercambios, la lista ya está ordenada
        if not intercambio:
            # Si no hubo intercambio, la lista ya está ordenada, salimos del bucle
            return lista
    
    # Retornar la lista ordenada
    return lista

# Prueba con diferentes listas
lista1 = [3, 1, 4, 1, 5, 9]
lista2 = [10, 2, 8, 5, 3, 7, 6]
lista3 = [1, 2, 3, 4, 5]

# Llamamos a la función y mostramos los resultados
print("Lista 1 ordenada:", ordenar_descendente(lista1))
print("Lista 2 ordenada:", ordenar_descendente(lista2))
print("Lista 3 ordenada:", ordenar_descendente(lista3))
