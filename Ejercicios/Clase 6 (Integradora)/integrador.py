from package_funciones import funciones


lista_numeros = [0]*10

for i in range(len(lista_numeros)):
    
    lista_numeros[i] = get_int("Ingrese un número: ",-1000, 1000)
    if lista_numeros[i] < -1000 or lista_numeros[i] > 1000:
        lista_numeros[i] = int(input("ERROR. Reingrese un número entre -1000 y 1000: "))

for i in range(len(lista_numeros)):
    print(lista_numeros[i])