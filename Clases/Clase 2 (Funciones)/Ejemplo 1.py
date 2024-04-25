import random

# def sumar_1():

#     un_numero = input("Ingrese un numero: ")
#     un_numero = int(un_numero)
#     otro_numero = input("Ingrese otro numero: ")
#     otro_numero = int(otro_numero)

#     suma = un_numero + otro_numero

#     print(f"La suma es: {suma}")

############ Otra manera de definir ###########

def sumar_2(un_numero, otro_numero):
    suma = un_numero + otro_numero
    print(f"La suma es: {suma}")

# un_numero = random.randint(1,100) ### SI QUIERO QUE EL NUMERO A SUMARSE SEA RANDOM
# otro_numero = random.randint(500,700)

un_numero = int(input("Ingrese un número: "))
otro_numero = int(input("Ingrese otro número: "))

sumar_2(un_numero, otro_numero) #Llamo a la función

############ otro ejemplo ############

def sumar_3():
    un_numero = input("Ingrese un numero: ")
    un_numero = int(un_numero)
    otro_numero = input("Ingrese otro numero: ")
    otro_numero = int(otro_numero)

    suma = un_numero + otro_numero

    return suma

resultado = sumar_3()
print(f"La suma es: {resultado}")


############ otro ejemplo mas ###############

def sumar_4(un_numero, otro_numero): #INDEPENDIENTE Y REUTILIZABLE
    suma = un_numero + otro_numero

    return suma

resultado = sumar_4(8,99) # RECIBE PARAMETROS Y RETORNA RESULTADO
print(f"La suma es: {resultado}")

###################################################

primer_numero = int(input("Ingrese un número: "))
segundo_numero = int(input("Ingrese otro número: "))

resultado = sumar_4(primer_numero, segundo_numero) # Recibe de parametro los dos numeros ingresados por input
print(f"El resultado de la suma es: {resultado}")