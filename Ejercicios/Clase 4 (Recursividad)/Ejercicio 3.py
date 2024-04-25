def sumar_digitos(numero: int) -> int:
    #si el número es menor que 10, va a tener un solo dígito, por lo tanto el resultado es número
    if numero < 10:
        resultado = numero

    #la suma de los dígitos la hago con el módulo de 10 para ir "corriendo" de lugar
    else:
        resultado = (numero % 10) + int(sumar_digitos(numero/10))

    return resultado

numero = 763
resultado = sumar_digitos(numero)
print(resultado)