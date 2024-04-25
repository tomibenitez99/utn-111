from os import system

def sumar_numeros(un_numero, otro_numero):
    suma = un_numero + otro_numero
    return suma

bandera_seguir = True
bandera_numeros_ingresados = False

while bandera_seguir:
    opcion = int(input("1. Ingresar datos\n2. Sumar\n3. Restar\n4. Multiplicar\n5. Dividir\n6. Salir\nElija una opción: "))

    match opcion:
        case 1:
            numero_1 = int(input("Ingrese el primer número: "))
            numero_2 = int(input("Ingrese el segundo numero: "))
            bandera_numeros_ingresados = True
        case 2:
            if bandera_numeros_ingresados == False:
                print("Primero debe ingresar los numeros")
            else:
                resultado = sumar_numeros(numero_1, numero_2)
                print(f"El resultado de la suma es: {resultado}")
        case 3:
            print("Estoy restando")
        case 4:
            print("Estoy multiplicando")
        case 5:
            print("Estoy dividiendo")
        case 6:
            seguir = input("¿Seguro que quiere salir?")
            if seguir == "si":
                bandera_seguir = False

system("pause")
system("cls")