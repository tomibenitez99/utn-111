def determinar_par(numero):    
    if numero % 2 == 0:
        mensaje = "El número es par"
    else:
        mensaje = "El número es impar"

    return mensaje

numero = int(input("Ingrese un número: "))

resultado = determinar_par(numero)
print(resultado)