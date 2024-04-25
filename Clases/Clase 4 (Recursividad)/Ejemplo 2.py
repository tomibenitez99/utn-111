numero = 5
factorial = 1

for i in range(1, numero + 1):
    factorial *= i #factorial = factorial * i

print(factorial)


def calcular_factorial(numero) -> int:
    if numero == 0:
        resultado = 1
    else:
        resultado = numero * calcular_factorial(numero - 1)

    return resultado

numero = 5
factorial = calcular_factorial(numero)

