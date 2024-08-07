'''
3. Crear una función que reciba como parámetro un valor
numérico. En caso de que ese valor recibido como
parámetro sea múltiplo de 3, se debe retornar el resultado
de su cubo (para calcular el cubo de dicho valor, utilizar otra
función). De no se múltiplo de 3, retornar el valor -1.
'''
def cubo(valor):
    return valor ** 3

def multiploDeTres(valor):
    if valor % 3 == 0:
        return cubo(valor)
    else:
        return -1
    
valores = [2,3, 4, 6, 7, 9, 10]
for valor in valores:
    resultado = multiploDeTres(valor)
    print(resultado)



