'''
2. Crear una función que elimine los elementos de una lista
que tengan un determinado valor. 
'''
def eliminarElemento(lista, valor):
    while valor in lista:
        lista.remove(valor)
    return lista


lista = [1, 2, 3, 4, 2, 6, 7, 2, 9, 10]
valor = 2
resultado = eliminarElemento(lista, valor)

print(resultado)


