'''
4. Modifique el ejercicio anterior para que, en caso de
que una de las listas tenga más elementos que la otra, se
sumen dichos elementos al final de la nueva lista.
'''

def auxCombinarListasDistintoTamanio(listaGrande, listaChica):
    resultado = []
    for i in range(len(listaChica)):
        resultado.append(listaGrande[i])
        resultado.append(listaChica[i])
    for i in range(len(listaChica), len(listaGrande)):
        resultado.append(listaGrande[i])
    return resultado

def combinarListasDistintoTamanio(lista1, lista2):
    
    if len(lista1) > len(lista2):
        resultado = auxCombinarListasDistintoTamanio(lista1, lista2)
    else:
        resultado = auxCombinarListasDistintoTamanio(lista2, lista1)
    
    return resultado

# Listas de ejemplo
lista2 = ["mi", "es", "Perez", "Cardenas", "Smart"]
lista1 = ["Hola", "nombre", "Juan"]


# Imprimir el resultado
print(combinarListasDistintoTamanio(lista1, lista2))   
