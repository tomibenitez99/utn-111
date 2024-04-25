def calcular_promedio(lista: list) -> float:
    promedio = -1
    if type(lista) is list and len(lista) > 0:
        promedio = 0
        for i in range(len(lista)):
            if lista[i] > 0:
                promedio += lista[i]
        return promedio
    
lista = [10, 5, 7]

promedio = calcular_promedio(lista)
if promedio == -1:
    print("El valor ingresado no es una lista")
elif promedio == 0:
    print("La lista está vacía")
else:
    print(promedio)