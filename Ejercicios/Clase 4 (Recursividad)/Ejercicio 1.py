def sumar_naturales(numero: int) -> int:
    if numero == 0:
        resultado = 0
    else:
        resultado = numero + sumar_naturales(numero - 1)

    return resultado

numero = 5
suma = sumar_naturales(numero)
print(suma)