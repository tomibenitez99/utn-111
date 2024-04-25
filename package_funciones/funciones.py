def get_int(mensaje: str, minimo: int, maximo: int) -> int:
    numero = input(mensaje)
    numero = int(numero)
    while numero < minimo or numero > maximo:
        numero = input(f"Error. {mensaje}")
        numero = int(numero)

    return numero

def es_par(numero: int) -> bool:
    if numero % 2 == 0:
        return True
    else:
        return False