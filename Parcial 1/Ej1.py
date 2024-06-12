# Desarrollar una función recursiva que permita listar los elementos de vector/lista de
# manera inversa al que están cargados. Preferentemente la función solo debe tener un
# parámetro que es la lista de elementos.

def imprimir_inverso(lista):
    if not lista:  
        return  
    else:
        imprimir_inverso(lista[1:])  
        print(lista[0]) 

mi_lista = [1, 2, 3, 4, 5]
print("Lista original:")
print(mi_lista)
print("Lista en orden inverso:")
imprimir_inverso(mi_lista)