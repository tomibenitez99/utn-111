def calcular_potencia(base: int, exponente: int) -> int:
    if exponente == 0:
        resultado = 1
    else:
        resultado = base * calcular_potencia(base, exponente - 1)
    return resultado

base = 6
exponente = 3
potencia = calcular_potencia(base, exponente)
print(potencia)