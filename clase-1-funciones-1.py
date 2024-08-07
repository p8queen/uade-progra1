'''
1. Crear una función que retorne una lista que tenga los
valores pares que se encuentran dentro de un rango dado
(dicho rango se recibe como parámetro de la función:
desde/hasta).
'''
def paresEnRango(desde, hasta):
    resultado = []
    for i in range(desde, hasta):
        if i % 2 == 0:
            resultado.append(i)
    return resultado


resultado = paresEnRango(1, 10)
print(resultado)