def paridad_numero() -> int:
    numero = input("Ingrese un número entero: ")
    numero = int(numero)

    if numero%2 == 0:
        mensaje = f"El número {numero} es par"
    else:
        mensaje = f"El número {numero} es impar"

    return mensaje

numero_ingresado = paridad_numero()
print(numero_ingresado)