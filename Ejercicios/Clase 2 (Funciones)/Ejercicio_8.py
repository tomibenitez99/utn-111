def calcular_potencia(base: int, exponente: int):
    resultado = base ** exponente
    return resultado

base = int(input("Ingrese un número para la base: "))
exponente = int(input("Ingrese otro número para el exponente: "))
potencia = calcular_potencia(base, exponente)
print(f"La potencia de {base} a la {exponente} es: {potencia}")