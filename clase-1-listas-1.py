'''
3. Crear un programa que combine dos listas en un
recorrido sucesivo de sus índices en una tercera. Si las
listas tienen diferentes longitudes, se debe notificar en
pantalla que el proceso no se puede realizar.
Ejemplo:
Lista1 = ["Hola","nombre", "Juan"]
Lista2 = ["mi","es", "Perez"]
Resultado esperado: ["Hola", "mi", "nombre", "es", "Juan", "Perez"]
'''

def combinar(list1, list2):
    if len(list1) != len(list2):
        return "Las listas tienen diferentes tamaños"
    else:
        resultado = []
        for i in range(len(list1)):
            resultado.append(list1[i])
            resultado.append(list2[i])
        return resultado


# Listas de ejemplo
lista1 = ["Hola", "nombre", "Juan"]
lista2 = ["mi", "es", "Perez"]

# Llamada a la función
resultado = combinar(lista1, lista2)
print(resultado)