'''
4. Escriba una función, que dada una lista con notas entre 0 y
10, retorne otra lista indicando su resultado por cada
posición; utilizando una función que al recibir una nota
retorne:
0: Ausente
Entre 1 y 3: Desaprobado
Entre 4 y 6: Aprobado
Entre 7 y 10: Promocionado
'''
def resultadoNota(nota):
    if nota == 0:
        return "Ausente"
    elif nota <= 3:
        return "Desaprobado"
    elif nota <= 6:
        return "Aprobado"
    else:
        return "Promocionado"
    
def listaResultadoNotas(notas):
    resultado = []
    for nota in notas:
        resultado.append(resultadoNota(nota))
    return resultado

notas = list(range(11))
resultado = listaResultadoNotas(notas)
print(resultado)
