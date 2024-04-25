mi_lista = [-1] * 5 #valor ilógico -1

bandera_salida = True

while bandera_salida == True:
    index = int(input("Ingrese la posición: "))
    while index < 1 or index > len(mi_lista):
        index = int(input("Reingrese la posición: "))    
    numero = int(input("Ingrese un número: "))

    mi_lista[index - 1] = numero


    seguir = input("Continúa? si/no: ")
    if seguir == "no":
        break

for i in range(len(mi_lista)):
    if mi_lista[i] != -1:
        print(f"{i+1} -- {mi_lista[i]}")