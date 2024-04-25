def sumar_positivos(lista: list) -> int: #recibo una lista de tipo LIST y me devuelve un entero o un flotante
    retorno = -2
    if type(lista) is list and len(lista) > 0: #si el tipo de dato de lo que yo estoy recibiendo (lista) es de tipo LIST y si el largo de la lista es mayor a 0 (o sea que la lista tiene algo dentro)
        retorno = -1
        for i in range(len(lista)):
            if lista[i] > 0:
                retorno += lista[i]
        return retorno

lista = [50, -20, 60]

suma = sumar_positivos(lista)
if suma == -2:
    print("El valor ingresado no es una lista")
elif suma == -1:
    print("La lista está vacía")
else:
    print(suma)


lista = [2, 5, 3, -6, 24, -6, -1]

###########CALCULOS##############
suma = 0

for i in range(len(lista)):
    if lista[i] > 0: #si el número es positivo
        suma = suma + lista[i] #sumame los números de la lista

print(suma)

#################################
###########MÁXIMO################
bandera_max = True
for i in range(len(lista)):
    if bandera_max == True or lista[i] > maximo_numero:
        maximo_numero = lista[i]
        bandera_max = False #hay que bajar la bandera para que no se cumpla siempre el IF

print(f"El máximo es: {maximo_numero}")

#############BANDERAS############

bandera_negativo = False
for i in range(len(lista)):
    if lista[i] < 0:
        bandera_negativo = True
        break

if bandera_negativo == True:
    print("Por lo menos hay un número negativo")
else:
    print("No hay ningún número negativo")

#########BUSCAR Y REEMPLAZAR##########
numero_buscado = 3
reemplazo = 1000

for i in range(len(lista)):
    if lista[i] == numero_buscado:
        lista[i] = reemplazo
        break #rompo en el caso de que quiera reemplazar solamente el primer caso que aplica (si hay dos 3, reemplazaría solo el primero que encuentro en la lista)

for i in range(len(lista)):
    print(lista[i])